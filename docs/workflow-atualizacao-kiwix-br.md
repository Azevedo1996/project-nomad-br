# Workflow para atualizar metadados Kiwix em português

Este documento descreve o workflow:

```text
.github/workflows/update-br-kiwix-metadata.yml
```

## Objetivo

Executar pelo GitHub Actions o script:

```text
scripts/update-br-kiwix-metadata.py
```

O workflow consulta os índices públicos do Kiwix/Wikimedia e tenta atualizar os catálogos brasileiros com:

- URL real dos arquivos `.zim`;
- versão no formato `AAAA-MM`;
- tamanho aproximado em MB;
- nome do arquivo de origem.

## Como executar no GitHub

1. Entre no repositório.
2. Acesse a aba **Actions**.
3. Selecione **Update Brazilian Kiwix Metadata**.
4. Clique em **Run workflow**.
5. Escolha o modo:

```text
dry-run
apply
```

## Modos

### dry-run

Executa a busca e gera relatório, mas não altera os catálogos.

Use primeiro para conferir o resultado.

### apply

Executa a busca, aplica alterações nos catálogos e faz commit automático se houver mudança.

Arquivos que podem ser alterados:

```text
collections/br/wikipedia-br.json
collections/br/kiwix-categories-br.json
docs/relatorio-kiwix-br.md
```

## Segurança

O workflow usa:

```yaml
permissions:
  contents: write
```

Isso permite que o GitHub Actions faça commit no próprio repositório quando executado em modo `apply`.

## Recomendação de uso

1. Execute primeiro em `dry-run`.
2. Confira o relatório gerado no resumo da Action.
3. Se estiver tudo certo, execute em `apply`.
4. Verifique se o commit automático foi criado.
5. Confira se o workflow **Validate Brazilian Catalogs** ficou verde.
