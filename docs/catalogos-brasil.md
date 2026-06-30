# Como usar os catálogos brasileiros

## Opção segura

Mantenha os arquivos brasileiros separados em:

```text
collections/br/
```

Isso evita quebrar o funcionamento original do NOMAD.

## Teste manual

Para testar um catálogo brasileiro no lugar do catálogo oficial:

1. Faça backup do arquivo original:

```bash
cp collections/wikipedia.json collections/wikipedia.original.json
cp collections/maps.json collections/maps.original.json
cp collections/kiwix-categories.json collections/kiwix-categories.original.json
```

2. Copie o catálogo brasileiro desejado:

```bash
cp collections/br/wikipedia-br.json collections/wikipedia.json
cp collections/br/maps-br.json collections/maps.json
cp collections/br/kiwix-categories-br.json collections/kiwix-categories.json
```

3. Rebuild/redeploy conforme estratégia do projeto.

## Observação

Algumas URLs são placeholders planejados e precisam ser validadas antes de uso automático.
