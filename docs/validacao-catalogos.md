# Validação dos Catálogos Brasileiros

Este documento explica como validar os catálogos brasileiros do Project N.O.M.A.D. Brasil.

## Arquivo criado

```text
scripts/validate-br-catalogs.py
```

## O que o script valida

O script verifica:

- se os arquivos JSON existem;
- se os arquivos JSON são válidos;
- se os campos obrigatórios existem;
- se há IDs duplicados;
- se `size_mb` é inteiro;
- se URLs começam com `http://` ou `https://`;
- se ainda existem placeholders como `YYYY-MM`;
- se mapas ainda estão marcados como `planned`.

## Como executar no Windows

Na raiz do projeto:

```cmd
cd C:\docker\project-nomad-br
python scripts\validate-br-catalogs.py
```

## Como executar no Linux/WSL

```bash
cd project-nomad-br
python3 scripts/validate-br-catalogs.py
```

## Resultado esperado nesta fase

Nesta fase inicial, o ideal é:

```text
Erros críticos: 0
Avisos: vários
```

Os avisos são esperados porque ainda temos:

- URLs com `YYYY-MM` para validar no Kiwix;
- `size_mb` igual a `0` até buscar os tamanhos reais;
- mapas `.pmtiles` com status `planned` até serem gerados e publicados.

## Próxima etapa

Depois desta validação estrutural, a próxima etapa será criar um atualizador de metadados para:

- consultar a biblioteca Kiwix;
- encontrar os arquivos `.zim` mais recentes em português;
- preencher automaticamente `version`, `url` e `size_mb`;
- gerar uma versão pronta para uso automático no NOMAD.
