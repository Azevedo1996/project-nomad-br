# Atualização automática dos catálogos Kiwix brasileiros

Este documento explica como atualizar os metadados dos catálogos brasileiros usando o script:

```text
scripts/update-kiwix-br-catalogs.py
```

## Objetivo

O script consulta os índices públicos do Kiwix e tenta encontrar os arquivos `.zim` mais recentes em português, preenchendo automaticamente:

```text
url
version
size_mb
validation_required=false
```

## Arquivos atualizados

O script atua sobre:

```text
collections/br/wikipedia-br.json
collections/br/kiwix-categories-br.json
```

## Como testar sem alterar arquivos

No Windows:

```cmd
cd C:\docker\project-nomad-br
python scripts\update-kiwix-br-catalogs.py --dry-run --verbose
```

No Linux/WSL:

```bash
cd project-nomad-br
python3 scripts/update-kiwix-br-catalogs.py --dry-run --verbose
```

## Como atualizar de verdade

```cmd
python scripts\update-kiwix-br-catalogs.py --verbose
```

Depois valide:

```cmd
python scripts\validate-br-catalogs.py
```

Confira as alterações:

```cmd
git diff collections\br
```

Faça commit:

```cmd
git add collections\br scripts\update-kiwix-br-catalogs.py docs\atualizar-catalogos-kiwix.md
git commit -m "Adiciona atualizador de metadados Kiwix brasileiros"
git push
```

## Como funciona

Os recursos brasileiros possuem campos auxiliares como:

```json
"candidate_filename_pattern": "wikipedia_pt_all_nopic_AAAA-MM.zim",
"source_directory": "download.kiwix.org/zim/wikipedia/"
```

O script transforma `AAAA-MM` em uma busca por versão no formato `YYYY-MM`, consulta o índice HTML do Kiwix e seleciona a versão mais recente encontrada.

## Observação importante

Este script precisa de internet durante a execução.

Se a biblioteca Kiwix mudar o padrão de nomes, talvez seja necessário ajustar os campos `candidate_filename_pattern` nos catálogos brasileiros.
