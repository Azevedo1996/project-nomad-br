#!/usr/bin/env python3
"""
Atualizador de metadados Kiwix para o Project N.O.M.A.D. Brasil.

Objetivo:
- consultar índices públicos do Kiwix;
- encontrar arquivos .zim recentes em português;
- atualizar os catálogos brasileiros em collections/br/;
- preencher url, version e size_mb quando houver correspondência.

Uso:
  python scripts/update-kiwix-br-catalogs.py

Opções:
  --dry-run      apenas mostra o que seria alterado
  --verbose      mostra mais detalhes

Observação:
Este script precisa de internet para consultar download.kiwix.org.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BR_DIR = ROOT / "collections" / "br"

CATALOG_FILES = [
    BR_DIR / "wikipedia-br.json",
    BR_DIR / "kiwix-categories-br.json",
]

INDEX_URLS = {
    "wikipedia": "https://download.kiwix.org/zim/wikipedia/",
    "wiktionary": "https://download.kiwix.org/zim/wiktionary/",
    "wikivoyage": "https://download.kiwix.org/zim/wikivoyage/",
}

# Mapeia candidate_filename_pattern do catálogo para regex real.
# O catálogo usa AAAA-MM para evitar URLs falsas nos workflows.
PATTERN_TOKEN = "AAAA-MM"
DATE_RE = r"(?P<version>\d{4}-\d{2})"


@dataclass
class ZimCandidate:
    filename: str
    url: str
    version: str
    size_mb: int | None = None


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attrs_dict = dict(attrs)
        href = attrs_dict.get("href")
        if href:
            self.links.append(href)


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "project-nomad-br-catalog-updater/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def head_size_mb(url: str) -> int | None:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "project-nomad-br-catalog-updater/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            length = resp.headers.get("Content-Length")
            if not length:
                return None
            return max(1, round(int(length) / (1024 * 1024)))
    except Exception:
        return None


def build_regex(candidate_pattern: str) -> re.Pattern[str]:
    escaped = re.escape(candidate_pattern)
    escaped = escaped.replace(re.escape(PATTERN_TOKEN), DATE_RE)
    return re.compile(rf"^{escaped}$")


def find_latest_zim(source_directory: str, candidate_pattern: str, verbose: bool = False) -> ZimCandidate | None:
    # source_directory pode vir como download.kiwix.org/zim/wikipedia/
    normalized = source_directory.strip()
    if normalized.startswith("https://") or normalized.startswith("http://"):
        base_url = normalized
    else:
        base_url = "https://" + normalized
    if not base_url.endswith("/"):
        base_url += "/"

    if verbose:
        print(f"Consultando índice: {base_url}")

    try:
        html = fetch_text(base_url)
    except urllib.error.URLError as exc:
        print(f"[AVISO] Falha ao consultar {base_url}: {exc}")
        return None

    parser = LinkParser()
    parser.feed(html)

    regex = build_regex(candidate_pattern)
    matches: list[ZimCandidate] = []

    for href in parser.links:
        filename = href.split("/")[-1]
        match = regex.match(filename)
        if not match:
            continue
        version = match.group("version")
        matches.append(ZimCandidate(filename=filename, url=base_url + filename, version=version))

    if not matches:
        if verbose:
            print(f"Nenhum arquivo encontrado para padrão: {candidate_pattern}")
        return None

    # Ordena por versão YYYY-MM.
    matches.sort(key=lambda item: item.version, reverse=True)
    latest = matches[0]
    latest.size_mb = head_size_mb(latest.url)

    if verbose:
        print(f"Encontrado: {latest.filename} | versão={latest.version} | size_mb={latest.size_mb}")

    return latest


def walk_items(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_items(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_items(child)


def update_catalog(path: Path, dry_run: bool, verbose: bool) -> int:
    if not path.exists():
        print(f"[ERRO] Arquivo não encontrado: {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    changes = 0

    for item in walk_items(data):
        candidate_pattern = item.get("candidate_filename_pattern")
        source_directory = item.get("source_directory")
        validation_required = item.get("validation_required")

        if not candidate_pattern or not source_directory or not validation_required:
            continue

        item_id = item.get("id", "sem-id")
        title = item.get("title") or item.get("name") or item_id

        print(f"Validando recurso: {title} ({item_id})")
        latest = find_latest_zim(source_directory, candidate_pattern, verbose=verbose)

        if not latest:
            print(f"  [PENDENTE] Nenhum ZIM compatível encontrado para {candidate_pattern}")
            continue

        old_url = item.get("url")
        old_version = item.get("version")
        old_size = item.get("size_mb")

        item["url"] = latest.url
        item["version"] = latest.version
        if latest.size_mb is not None:
            item["size_mb"] = latest.size_mb
        item["validation_required"] = False
        item["validated_by"] = "scripts/update-kiwix-br-catalogs.py"

        if old_url != item.get("url") or old_version != item.get("version") or old_size != item.get("size_mb"):
            changes += 1
            print(f"  [OK] {latest.filename}")
            print(f"       url: {latest.url}")
            print(f"       version: {latest.version}")
            print(f"       size_mb: {item.get('size_mb')}")

    if changes and not dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[ALTERADO] {path} ({changes} recurso(s))")
    elif changes and dry_run:
        print(f"[DRY-RUN] {path} teria {changes} alteração(ões)")
    else:
        print(f"[SEM ALTERAÇÕES] {path}")

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Atualiza metadados dos catálogos Kiwix brasileiros.")
    parser.add_argument("--dry-run", action="store_true", help="Mostra alterações sem gravar arquivos")
    parser.add_argument("--verbose", action="store_true", help="Mostra detalhes adicionais")
    args = parser.parse_args()

    print("Atualizador Kiwix - Project N.O.M.A.D. Brasil")
    print(f"Raiz do projeto: {ROOT}")
    print(f"Modo dry-run: {args.dry_run}")
    print("")

    total_changes = 0
    for catalog in CATALOG_FILES:
        total_changes += update_catalog(catalog, dry_run=args.dry_run, verbose=args.verbose)
        print("")

    print(f"Total de recursos alterados: {total_changes}")

    if total_changes:
        print("")
        print("Próximos comandos sugeridos:")
        print("  python scripts/validate-br-catalogs.py")
        print("  git diff collections/br")
        print("  git add collections/br scripts/update-kiwix-br-catalogs.py docs/atualizar-catalogos-kiwix.md")
        print('  git commit -m "Atualiza metadados Kiwix dos catalogos brasileiros"')
        print("  git push")

    return 0


if __name__ == "__main__":
    sys.exit(main())
