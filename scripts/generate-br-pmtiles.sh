#!/usr/bin/env bash
set -euo pipefail

# Gera mapas PMTiles brasileiros a partir de um PMTiles global/regional.
# Requer pmtiles CLI instalado: https://docs.protomaps.com/pmtiles/cli
# Uso:
#   ./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles brasil
#   ./scripts/generate-br-pmtiles.sh ./planet.pmtiles sudeste
#   ./scripts/generate-br-pmtiles.sh ./planet.pmtiles all

SOURCE_PMtiles="${1:-}"
REGION="${2:-all}"
MAXZOOM="${MAXZOOM:-}"
THREADS="${DOWNLOAD_THREADS:-4}"

if [ -z "$SOURCE_PMtiles" ]; then
  echo "Uso: $0 <SOURCE_PMtiles_URL_ou_arquivo> [region|all]"
  exit 1
fi

if ! command -v pmtiles >/dev/null 2>&1; then
  echo "Erro: pmtiles CLI não encontrado no PATH."
  echo "Instale conforme documentação: https://docs.protomaps.com/pmtiles/cli"
  exit 1
fi

mkdir -p maps/br/output

run_extract() {
  local id="$1"
  local bbox="$2"
  local output="maps/br/output/${id}.pmtiles"

  echo "Gerando ${output} usando bbox ${bbox}..."

  if [ -n "$MAXZOOM" ]; then
    pmtiles extract "$SOURCE_PMtiles" "$output" --bbox="$bbox" --maxzoom="$MAXZOOM" --download-threads="$THREADS"
  else
    pmtiles extract "$SOURCE_PMtiles" "$output" --bbox="$bbox" --download-threads="$THREADS"
  fi

  pmtiles verify "$output"
  pmtiles show "$output" --metadata > "${output}.metadata.json" || true
  ls -lh "$output"
}

# id|bbox
REGIONS=$(python3 - <<'PY'
import json
from pathlib import Path
regions = json.loads(Path('maps/br/regions.json').read_text(encoding='utf-8'))['regions']
for r in regions:
    print(f"{r['id']}|{r['bbox']}")
PY
)

while IFS='|' read -r id bbox; do
  [ -z "$id" ] && continue
  if [ "$REGION" = "all" ] || [ "$REGION" = "$id" ]; then
    run_extract "$id" "$bbox"
  fi
done <<< "$REGIONS"

echo "Concluído. Arquivos gerados em maps/br/output/."
