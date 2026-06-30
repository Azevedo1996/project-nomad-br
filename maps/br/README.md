# Mapas Brasileiros em PMTiles

Esta pasta contém a estrutura inicial para gerar mapas offline brasileiros para o Project N.O.M.A.D. Brasil.

## Estrutura

```text
maps/br/regions.json
maps/br/geojson/
maps/br/output/
```

## Estratégia

A forma mais compatível com o NOMAD é gerar arquivos `.pmtiles` derivados de um basemap Protomaps/OSM.

Nesta fase, os recortes usam `bbox` aproximado para testes. Para publicação pública, o ideal é substituir os polígonos por GeoJSON oficiais/administrativos por estado/região.

## Exemplos

Linux/WSL:

```bash
./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles rio-de-janeiro
```

Windows PowerShell:

```powershell
.\scripts\generate-br-pmtiles.ps1 -SourcePmtiles "https://build.protomaps.com/AAAAmmdd.pmtiles" -Region "rio-de-janeiro"
```

## Observação

Arquivos `.pmtiles` podem ser grandes. Não faça commit dos arquivos gerados em `maps/br/output/`. Publique em GitHub Releases ou armazenamento externo.
