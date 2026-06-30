# Geração de mapas PMTiles do Brasil

Este documento descreve a primeira estrutura para gerar mapas offline brasileiros no Project N.O.M.A.D. Brasil.

## Base técnica

O PMTiles CLI suporta o comando `extract` para criar um arquivo menor a partir de um arquivo PMTiles maior usando `--bbox=MIN_LON,MIN_LAT,MAX_LON,MAX_LAT` ou `--region=REGION.geojson`. A documentação oficial também mostra que a fonte pode ser um arquivo local ou uma URL remota. citeturn23search93

O guia do Protomaps mostra o fluxo recomendado: instalar o CLI, escolher um build diário em `maps.protomaps.com/builds`/`build.protomaps.com`, inspecionar com `pmtiles show` e extrair uma área com `pmtiles extract`. citeturn23search94

A Geofabrik disponibiliza dados OpenStreetMap para o Brasil e informa que o arquivo `brazil-latest.osm.pbf` existe para uso com ferramentas como Osmium, Osmosis, imposm, osm2pgsql e outras; a página também lista sub-regiões brasileiras como Centro-Oeste, Nordeste, Norte, Sudeste e Sul. citeturn23search99

## Arquivos adicionados

```text
maps/br/regions.json
maps/br/geojson/*.geojson
scripts/generate-br-pmtiles.sh
scripts/generate-br-pmtiles.ps1
docs/geracao-mapas-pmtiles-brasil.md
```

## Instalar o pmtiles CLI

Instale o binário `pmtiles` conforme a documentação oficial do Protomaps. O CLI é um binário único e possui comandos como `show`, `verify` e `extract`. citeturn23search93

## Gerar um mapa de teste

Exemplo com Rio de Janeiro:

```bash
./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles rio-de-janeiro
```

Exemplo no PowerShell:

```powershell
.\scripts\generate-br-pmtiles.ps1 -SourcePmtiles "https://build.protomaps.com/AAAAmmdd.pmtiles" -Region "rio-de-janeiro"
```

## Gerar todos os mapas planejados

```bash
./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles all
```

## Reduzir tamanho usando MAXZOOM

Para testes, limite o zoom:

```bash
MAXZOOM=10 ./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles rio-de-janeiro
```

## Não commitar arquivos gerados

Os arquivos finais em `.pmtiles` podem ficar muito grandes. O caminho correto é gerar localmente e publicar em Releases do GitHub:

```text
maps-br-v1
```

Depois preencher `collections/br/maps-br.json` com as URLs reais.

## Próxima etapa

Depois de gerar um primeiro `.pmtiles`, vamos criar um script para:

1. calcular tamanho do arquivo;
2. validar com `pmtiles verify`;
3. preencher `collections/br/maps-br.json` automaticamente;
4. preparar release no GitHub.
