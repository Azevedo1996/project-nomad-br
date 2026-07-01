# Como contribuir com o Project N.O.M.A.D. Brasil

Obrigado pelo interesse em contribuir.

## Formas de contribuição

Você pode ajudar com:

- documentação em português;
- revisão de textos;
- testes em Windows, Linux e WSL2;
- validação de catálogos;
- geração de mapas `.pmtiles`;
- lista de conteúdos Kiwix em português;
- melhoria dos scripts;
- tradução futura da interface;
- tutoriais para usuários brasileiros.

## Antes de enviar alterações

Execute:

```bash
python scripts/validate-br-catalogs.py
```

Se mexeu em mapas:

```bash
python scripts/update-br-maps-catalog.py --dry-run --release-tag maps-br-v1
```

## Padrão de commits sugerido

Exemplos:

```text
Adiciona documentação de primeiros passos
Corrige catálogo brasileiro de mapas
Atualiza metadados Kiwix em português
Melhora script de geração PMTiles
```

## O que evitar

Evite commitar:

```text
arquivos .zim
arquivos .pmtiles
storage local
bancos de dados
logs grandes
senhas reais
chaves privadas
```

## Organização

Arquivos brasileiros ficam preferencialmente em:

```text
collections/br/
docs/
scripts/
maps/br/
```
