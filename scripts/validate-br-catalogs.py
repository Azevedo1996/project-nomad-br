#!/usr/bin/env python3
"""
Validador dos catálogos brasileiros do Project N.O.M.A.D. Brasil.

Este script valida os arquivos em collections/br/ sem acessar a internet.
Ele verifica:
- JSON válido
- campos obrigatórios
- estrutura básica esperada
- placeholders como YYYY-MM
- resources sem size_mb real
- URLs planejadas de mapas ainda não publicadas

Uso:
  python scripts/validate-br-catalogs.py

Retorno:
  0 = validação concluída sem erros críticos
  1 = existem erros críticos
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "collections" / "br"

FILES = {
    "wikipedia": CATALOG_DIR / "wikipedia-br.json",
    "kiwix": CATALOG_DIR / "kiwix-categories-br.json",
    "maps": CATALOG_DIR / "maps-br.json",
    "index": CATALOG_DIR / "catalog-index.json",
}

errors: list[str] = []
warnings: list[str] = []
infos: list[str] = []


def load_json(path: Path) -> Any:
    if not path.exists():
        errors.append(f"Arquivo não encontrado: {path}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"JSON inválido em {path}: linha {exc.lineno}, coluna {exc.colno}: {exc.msg}")
        return None


def require(obj: dict[str, Any], key: str, context: str) -> None:
    if key not in obj:
        errors.append(f"Campo obrigatório ausente em {context}: {key}")


def check_url(url: Any, context: str) -> None:
    if url is None:
        return
    if not isinstance(url, str):
        errors.append(f"URL inválida em {context}: precisa ser string ou null")
        return
    if not (url.startswith("https://") or url.startswith("http://")):
        warnings.append(f"URL não começa com http/https em {context}: {url}")
    if "YYYY-MM" in url:
        warnings.append(f"Placeholder YYYY-MM encontrado em {context}: {url}")


def check_size(size: Any, context: str) -> None:
    if not isinstance(size, int):
        errors.append(f"size_mb inválido em {context}: precisa ser inteiro")
        return
    if size == 0:
        warnings.append(f"size_mb ainda não preenchido em {context}")
    if size < 0:
        errors.append(f"size_mb negativo em {context}")


def validate_wikipedia(data: dict[str, Any]) -> None:
    context = "wikipedia-br.json"
    require(data, "spec_version", context)
    require(data, "options", context)

    options = data.get("options", [])
    if not isinstance(options, list):
        errors.append("wikipedia-br.json: options precisa ser lista")
        return

    ids = set()
    for item in options:
        item_context = f"{context} option"
        if not isinstance(item, dict):
            errors.append(f"{item_context}: item precisa ser objeto")
            continue
        for key in ["id", "name", "description", "size_mb", "url", "version"]:
            require(item, key, item_context)
        item_id = item.get("id")
        if item_id in ids:
            errors.append(f"ID duplicado em {context}: {item_id}")
        ids.add(item_id)
        check_url(item.get("url"), f"{context}:{item_id}")
        check_size(item.get("size_mb"), f"{context}:{item_id}")


def iter_kiwix_resources(data: dict[str, Any]):
    for category in data.get("categories", []):
        category_slug = category.get("slug", "sem-slug")
        for tier in category.get("tiers", []):
            tier_slug = tier.get("slug", "sem-tier")
            for resource in tier.get("resources", []):
                yield category_slug, tier_slug, resource


def validate_kiwix(data: dict[str, Any]) -> None:
    context = "kiwix-categories-br.json"
    require(data, "spec_version", context)
    require(data, "categories", context)

    categories = data.get("categories", [])
    if not isinstance(categories, list):
        errors.append("kiwix-categories-br.json: categories precisa ser lista")
        return

    for category in categories:
        if not isinstance(category, dict):
            errors.append("Categoria Kiwix precisa ser objeto")
            continue
        for key in ["name", "slug", "icon", "description", "language", "tiers"]:
            require(category, key, f"{context}:category")
        tiers = category.get("tiers", [])
        if not isinstance(tiers, list):
            errors.append(f"tiers precisa ser lista em categoria {category.get('slug')}")
            continue
        for tier in tiers:
            for key in ["name", "slug", "description", "resources"]:
                require(tier, key, f"{context}:tier")
            resources = tier.get("resources", [])
            if not isinstance(resources, list):
                errors.append(f"resources precisa ser lista em tier {tier.get('slug')}")

    ids = set()
    for category_slug, tier_slug, resource in iter_kiwix_resources(data):
        ctx = f"{context}:{category_slug}:{tier_slug}"
        for key in ["id", "version", "title", "description", "url", "size_mb"]:
            require(resource, key, ctx)
        resource_id = resource.get("id")
        if resource_id in ids:
            errors.append(f"ID duplicado em {context}: {resource_id}")
        ids.add(resource_id)
        check_url(resource.get("url"), f"{ctx}:{resource_id}")
        check_size(resource.get("size_mb"), f"{ctx}:{resource_id}")


def validate_maps(data: dict[str, Any]) -> None:
    context = "maps-br.json"
    require(data, "spec_version", context)
    require(data, "collections", context)

    collections = data.get("collections", [])
    if not isinstance(collections, list):
        errors.append("maps-br.json: collections precisa ser lista")
        return

    ids = set()
    for collection in collections:
        if not isinstance(collection, dict):
            errors.append("Coleção de mapas precisa ser objeto")
            continue
        for key in ["name", "slug", "description", "icon", "language", "resources"]:
            require(collection, key, f"{context}:collection")
        for resource in collection.get("resources", []):
            ctx = f"{context}:{collection.get('slug')}"
            for key in ["id", "version", "title", "description", "url", "size_mb"]:
                require(resource, key, ctx)
            resource_id = resource.get("id")
            if resource_id in ids:
                errors.append(f"ID duplicado em {context}: {resource_id}")
            ids.add(resource_id)
            check_url(resource.get("url"), f"{ctx}:{resource_id}")
            check_size(resource.get("size_mb"), f"{ctx}:{resource_id}")
            if resource.get("status") == "planned":
                warnings.append(f"Mapa planejado ainda não publicado: {resource.get('title')} ({resource.get('url')})")


def validate_index(data: dict[str, Any]) -> None:
    context = "catalog-index.json"
    for key in ["project", "repository", "generated_at", "catalogs"]:
        require(data, key, context)
    catalogs = data.get("catalogs", [])
    if not isinstance(catalogs, list):
        errors.append("catalog-index.json: catalogs precisa ser lista")
        return
    for catalog in catalogs:
        for key in ["name", "file", "description"]:
            require(catalog, key, context)
        file_path = ROOT / catalog.get("file", "")
        if not file_path.exists():
            errors.append(f"Arquivo referenciado no índice não existe: {file_path}")


def main() -> int:
    print("Validador de Catálogos Brasileiros - Project N.O.M.A.D. Brasil")
    print(f"Raiz do projeto: {ROOT}")
    print(f"Diretório de catálogos: {CATALOG_DIR}")
    print("")

    data = {name: load_json(path) for name, path in FILES.items()}

    if isinstance(data.get("wikipedia"), dict):
        validate_wikipedia(data["wikipedia"])
    if isinstance(data.get("kiwix"), dict):
        validate_kiwix(data["kiwix"])
    if isinstance(data.get("maps"), dict):
        validate_maps(data["maps"])
    if isinstance(data.get("index"), dict):
        validate_index(data["index"])

    print("Resumo:")
    print(f"  Erros críticos: {len(errors)}")
    print(f"  Avisos:         {len(warnings)}")
    print(f"  Informações:    {len(infos)}")
    print("")

    if errors:
        print("ERROS:")
        for err in errors:
            print(f"  [ERRO] {err}")
        print("")

    if warnings:
        print("AVISOS:")
        for warn in warnings:
            print(f"  [AVISO] {warn}")
        print("")

    if not errors:
        print("Validação concluída sem erros críticos.")
        if warnings:
            print("Existem avisos esperados nesta fase inicial, principalmente placeholders e mapas planejados.")
        return 0

    print("Validação falhou com erros críticos.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
