# Correção do workflow Validate Collection URLs

Este ajuste corrige o workflow `.github/workflows/validate-collection-urls.yml` para validar URLs de catálogos sem baixar arquivos grandes.

## Problema identificado

O workflow falhou ao validar uma URL de arquivo `.zim` grande:

```text
https://download.kiwix.org/zim/devdocs/devdocs_en_bash_2026-01.zim
Process completed with exit code 63
```

O código `63` do `curl` normalmente está relacionado a limite de tamanho ao tentar acessar um arquivo grande. Como os catálogos do NOMAD possuem arquivos `.zim` e futuramente `.pmtiles`, a validação não deve tentar baixar o conteúdo completo.

## O que mudou

O workflow novo:

1. Extrai URLs de todos os JSON em `collections/`.
2. Ignora `url: null`.
3. Tenta validar com `HEAD` primeiro.
4. Se `HEAD` falhar, tenta `GET` com `Range: 0-0`.
5. Trata `curl exit code 63` como aviso, não como erro fatal.
6. Continua falhando se a URL estiver realmente inválida ou indisponível.

## Como aplicar

Copie o arquivo do pacote para:

```text
.github/workflows/validate-collection-urls.yml
```

Depois rode:

```bash
git add .github/workflows/validate-collection-urls.yml docs/correcao-workflow-validacao-urls.md
git commit -m "Corrige workflow de validacao de URLs para arquivos grandes"
git push
```
