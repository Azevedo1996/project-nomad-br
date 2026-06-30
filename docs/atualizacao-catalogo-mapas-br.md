# Atualização do catálogo de mapas brasileiros

Este documento descreve o script:

```text
scripts/update-br-maps-catalog.py
```

## Objetivo

Depois que os arquivos `.pmtiles` forem gerados em:

```text
maps/br/output/
```

O script atualiza o catálogo:

```text
collections/br/maps-br.json
```

com:

- URL esperada do asset no GitHub Releases;
- tamanho em MB;
- status `available`;
- nome do arquivo de origem.

## Fluxo recomendado

### 1. Gerar um mapa de teste

Exemplo:

```bash
./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles rio-de-janeiro
```

O PMTiles CLI suporta o comando `extract` para criar um arquivo menor a partir de uma fonte local ou remota usando `--bbox` ou `--region`.

### 2. Simular atualização do catálogo

```bash
python scripts/update-br-maps-catalog.py --dry-run --release-tag maps-br-v1
```

### 3. Publicar o `.pmtiles` em GitHub Releases

```bash
gh release create maps-br-v1 maps/br/output/*.pmtiles --title "Mapas Brasil PMTiles v1" --notes "Mapas PMTiles brasileiros para Project N.O.M.A.D. Brasil"
```

Se a release já existir:

```bash
gh release upload maps-br-v1 maps/br/output/*.pmtiles --clobber
```

### 4. Aplicar atualização no catálogo

```bash
python scripts/update-br-maps-catalog.py --apply --release-tag maps-br-v1
```

### 5. Validar catálogo brasileiro

```bash
python scripts/validate-br-catalogs.py
```

### 6. Commitar

```bash
git add collections/br/maps-br.json docs/publicacao-mapas-br-release.md scripts/update-br-maps-catalog.py docs/atualizacao-catalogo-mapas-br.md
git commit -m "Adiciona atualizador do catalogo de mapas brasileiros"
git push
```

## Importante

Não faça commit dos arquivos `.pmtiles`. Esses arquivos podem ser grandes e devem ser publicados via GitHub Releases ou outro storage.
