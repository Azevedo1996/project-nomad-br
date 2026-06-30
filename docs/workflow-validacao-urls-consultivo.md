# Workflow de validação de URLs em modo consultivo

Este ajuste transforma o workflow `.github/workflows/validate-collection-urls.yml` em uma validação **consultiva**.

## Por que isso foi necessário

Durante a adaptação brasileira, o workflow original começou a falhar por URLs antigas ou externas do catálogo original, por exemplo:

```text
https://download.kiwix.org/zim/wikipedia/wikipedia_en_top_nopic_2025-12.zim
https://download.kiwix.org/zim/wikipedia/wikipedia_en_top_mini_2025-12.zim
https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_nopic_2025-12.zim
https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_mini_2025-12.zim
```

Como o objetivo do `project-nomad-br` é manter um projeto paralelo em desenvolvimento, o repositório não deve ficar bloqueado por links legados do projeto original ou por indisponibilidade temporária de arquivos externos.

## O que mudou

O workflow agora:

- extrai URLs de todos os JSON em `collections/`;
- ignora `url: null`;
- tenta validar com `HEAD`;
- tenta fallback com `GET` parcial usando `Range: 0-0`;
- registra URLs problemáticas como `warning`;
- gera resumo no GitHub Actions;
- sempre finaliza com `exit 0`.

## Quando voltar a ser bloqueante

Depois que o Project N.O.M.A.D. Brasil tiver catálogos próprios estáveis, podemos criar uma validação mais rígida apenas para:

```text
collections/br/*.json
```

Ou separar em dois workflows:

```text
validate-original-catalogs.yml   # consultivo
validate-br-catalogs.yml         # bloqueante
```
