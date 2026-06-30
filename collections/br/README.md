# Catálogos Brasileiros

Esta pasta contém os catálogos iniciais do **Project N.O.M.A.D. Brasil**.

## Arquivos

```text
collections/br/wikipedia-br.json
collections/br/kiwix-categories-br.json
collections/br/maps-br.json
collections/br/catalog-index.json
```

## Importante

Estes catálogos são a primeira versão brasileira e ainda não substituem automaticamente os catálogos oficiais do Project N.O.M.A.D.

Antes de usar em produção:

1. Validar URLs de arquivos `.zim` na biblioteca Kiwix.
2. Gerar/publicar arquivos `.pmtiles` dos mapas do Brasil.
3. Testar importação no Command Center.
4. Só então substituir ou integrar com os arquivos oficiais em `collections/`.

## Próxima etapa

A próxima etapa será criar scripts para:

- validar URLs de ZIM;
- baixar metadados da biblioteca Kiwix;
- gerar mapas `.pmtiles` do Brasil;
- atualizar `size_mb` e `version` automaticamente.
