# Mapas do Brasil no Project N.O.M.A.D. Brasil

O objetivo desta etapa é utilizar mapas offline do Brasil no ambiente NOMAD.

## Formato

O formato planejado é:

```text
.pmtiles
```

## Mapas planejados

```text
brasil.pmtiles
sudeste.pmtiles
sul.pmtiles
nordeste.pmtiles
norte.pmtiles
centro-oeste.pmtiles
rio-de-janeiro.pmtiles
sao-paulo.pmtiles
minas-gerais.pmtiles
espirito-santo.pmtiles
```

## Fonte de dados

A fonte preferencial será OpenStreetMap.

## Estratégia inicial

1. Gerar ou obter um arquivo `.pmtiles` do Brasil.
2. Publicar o arquivo em Releases do GitHub.
3. Importar pelo NOMAD como mapa customizado.
4. Testar navegação offline.
5. Documentar o processo para usuários brasileiros.

## Observação

Arquivos `.pmtiles` podem ser grandes. É recomendado usar GitHub Releases ou outro armazenamento externo para publicar mapas.
