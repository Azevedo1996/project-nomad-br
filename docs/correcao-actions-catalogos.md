# Correção dos Catálogos Brasileiros para o GitHub Actions

Este pacote corrige os catálogos brasileiros para não quebrar o workflow `Validate Collection URLs`.

## Motivo

A primeira versão dos catálogos possuía URLs planejadas com placeholders como `YYYY-MM` e links de Releases ainda inexistentes. O workflow oficial valida URLs encontradas nos catálogos e falha quando encontra links inválidos, malformados ou ainda não publicados.

## Correção aplicada

- `url` ficou como `null` para recursos ainda não validados.
- Os nomes esperados dos arquivos foram movidos para campos auxiliares como `candidate_filename_pattern` e `planned_asset_name`.
- Os catálogos continuam documentando o plano brasileiro, mas não expõem URLs falsas ou pendentes para o validador automático.

## Próximo passo

Depois de validar URLs reais da biblioteca Kiwix e publicar mapas `.pmtiles`, preencher novamente `url`, `version` e `size_mb`.
