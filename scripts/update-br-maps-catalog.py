#!/usr/bin/env python3
"""
Atualizador do catálogo de mapas brasileiros do Project N.O.M.A.D. Brasil.

Lê arquivos .pmtiles gerados em maps/br/output/ e atualiza:
- collections/br/maps-br.json

O script NÃO faz upload para GitHub Releases. O script apenas prepara o catálogo com URLs esperadas.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MAPS_CATALOG = ROOT / "collections" / "br" / "maps-br.json"
OUTPUT_DIR = ROOT / "maps" / "br" / "output"
DEFAULT_REPO = "Azevedo1996/project-nomad-br"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def size_mb(path: Path) -> int:
    return max(1, round(path.stat().st_size / (1024 * 1024)))


def has_pmtiles_cli() -> bool:
    try:
        subprocess.run(["pmtiles", "--help"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        return True
    except FileNotFoundError:
        return False


def verify_pmtiles(path: Path) -> bool:
    if not has_pmtiles_cli():
        return False
    result = subprocess.run(["pmtiles", "verify", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0


def iter_resources(data: dict[str, Any]):
    for collection in data.get("collections", []):
        for resource in collection.get("resources", []):
            yield resource


def update_catalog(data: dict[str, Any], base_url: str, verify: bool) -> tuple[list[str], list[str]]:
    changes: list[str] = []
    warnings: list[str] = []
    resources_by_id = {resource.get("id"): resource for resource in iter_resources(data)}

    if not OUTPUT_DIR.exists():
        warnings.append(f"Diretório de saída não encontrado: {OUTPUT_DIR}")
        return changes, warnings

    pmtiles_files = sorted(OUTPUT_DIR.glob("*.pmtiles"))
    if not pmtiles_files:
        warnings.append(f"Nenhum arquivo .pmtiles encontrado em {OUTPUT_DIR}")
        return changes, warnings

    for file_path in pmtiles_files:
        region_id = file_path.stem
        resource = resources_by_id.get(region_id)
        if resource is None:
            warnings.append(f"Arquivo sem recurso correspondente no catálogo: {file_path.name}")
            continue

        if verify:
            ok = verify_pmtiles(file_path)
            if not ok:
                warnings.append(f"Não foi possível validar com pmtiles verify: {file_path.name}")

        url = f"{base_url.rstrip('/')}/{file_path.name}"
        mb = size_mb(file_path)
        before = (resource.get("url"), resource.get("size_mb"), resource.get("status"))

        resource["url"] = url
        resource["size_mb"] = mb
        resource["status"] = "available"
        resource["source_filename"] = file_path.name
        resource["release_asset_name"] = file_path.name

        after = (resource.get("url"), resource.get("size_mb"), resource.get("status"))
        if before != after:
            changes.append(f"{region_id}: {file_path.name} -> {mb} MB")

    return changes, warnings


def make_release_commands(tag: str, title: str) -> str:
    return """# Publicação dos mapas brasileiros em GitHub Releases

## Criar release e enviar arquivos PMTiles

Requer GitHub CLI autenticado:

```bash
gh auth login
```

Criar release:

```bash
gh release create {tag} maps/br/output/*.pmtiles --title "{title}" --notes "Mapas PMTiles brasileiros para Project N.O.M.A.D. Brasil"
```

Se a release já existir, enviar/atualizar assets:

```bash
gh release upload {tag} maps/br/output/*.pmtiles --clobber
```

Depois de publicar, atualize o catálogo:

```bash
python scripts/update-br-maps-catalog.py --apply --release-tag {tag}
```
""".format(tag=tag, title=title)


def main() -> int:
    parser = argparse.ArgumentParser(description="Atualiza collections/br/maps-br.json com arquivos PMTiles gerados.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Mostra alterações sem salvar.")
    group.add_argument("--apply", action="store_true", help="Aplica alterações no catálogo.")
    parser.add_argument("--release-tag", default="maps-br-v1", help="Tag da release GitHub. Padrão: maps-br-v1")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="Repositório GitHub owner/repo.")
    parser.add_argument("--base-url", default=None, help="URL base manual para os assets.")
    parser.add_argument("--verify", action="store_true", help="Executa pmtiles verify nos arquivos, se pmtiles CLI existir.")
    parser.add_argument("--write-release-doc", default="docs/publicacao-mapas-br-release.md", help="Caminho do doc com comandos de release.")
    args = parser.parse_args()

    data = load_json(MAPS_CATALOG)
    base_url = args.base_url or f"https://github.com/{args.repo}/releases/download/{args.release_tag}"
    changes, warnings = update_catalog(data, base_url=base_url, verify=args.verify)

    print("Atualizador de catálogo de mapas brasileiros")
    print(f"Catálogo: {MAPS_CATALOG}")
    print(f"Diretório PMTiles: {OUTPUT_DIR}")
    print(f"Base URL: {base_url}")
    print("")

    if changes:
        print("Alterações:")
        for change in changes:
            print(f"- {change}")
    else:
        print("Nenhuma alteração detectada.")

    if warnings:
        print("\nAvisos:")
        for warning in warnings:
            print(f"- {warning}")

    release_doc = ROOT / args.write_release_doc
    release_doc.parent.mkdir(parents=True, exist_ok=True)
    release_doc.write_text(make_release_commands(args.release_tag, "Mapas Brasil PMTiles v1"), encoding="utf-8")
    print(f"Documento de publicação gerado/atualizado: {release_doc}")

    if args.dry_run:
        print("Modo dry-run: catálogo não foi alterado.")
        return 0

    save_json(MAPS_CATALOG, data)
    print("Catálogo atualizado com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
