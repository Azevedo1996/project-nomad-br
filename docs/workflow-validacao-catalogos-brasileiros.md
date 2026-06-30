# Workflow de validação dos catálogos brasileiros

Este documento descreve o workflow:

```text
.github/workflows/validate-br-catalogs.yml
```

## Objetivo

Este workflow valida somente os catálogos brasileiros do projeto:

```text
collections/br/*.json
```

Ele usa o script local:

```text
scripts/validate-br-catalogs.py
```

## Diferença entre os workflows

### Validate Collection URLs

Workflow herdado/adaptado do projeto original.

Função:

- varrer URLs de todos os catálogos;
- gerar relatório consultivo;
- não bloquear o desenvolvimento por URLs externas legadas.

### Validate Brazilian Catalogs

Workflow específico do Project N.O.M.A.D. Brasil.

Função:

- validar a estrutura dos catálogos brasileiros;
- detectar JSON inválido;
- detectar campos obrigatórios ausentes;
- detectar IDs duplicados;
- detectar placeholders e campos pendentes;
- bloquear erro estrutural real nos arquivos brasileiros.

## Como executar localmente

No Windows:

```cmd
cd C:\docker\project-nomad-br
python scripts\validate-br-catalogs.py
```

No Linux/WSL:

```bash
cd project-nomad-br
python3 scripts/validate-br-catalogs.py
```

## Resultado esperado nesta fase

Nesta fase inicial, o workflow pode passar com avisos, desde que não existam erros críticos.

Avisos esperados:

- `size_mb` ainda igual a `0`;
- mapas com status `planned`;
- URLs `null` para itens ainda não publicados;
- itens marcados como `validation_required`.

## Quando o workflow deve falhar

O workflow deve falhar se houver:

- JSON inválido;
- arquivo obrigatório ausente;
- campo obrigatório ausente;
- ID duplicado;
- `size_mb` inválido;
- estrutura incompatível com os catálogos do NOMAD.
