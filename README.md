# Project N.O.M.A.D. Brasil

> Servidor offline de conhecimento, mapas, educação e IA local adaptado para usuários brasileiros.

O **Project N.O.M.A.D. Brasil** é uma adaptação brasileira e comunitária do **Project N.O.M.A.D.**, com foco em facilitar o uso da plataforma por pessoas brasileiras, priorizando documentação em português, conteúdos offline em português, mapas do Brasil e IA local respondendo em português brasileiro.

Este repositório mantém uma base paralela ao projeto original, preservando os créditos e a licença, mas adicionando uma camada brasileira de documentação, catálogos, scripts e automações.

---

## Objetivo

O objetivo do Project N.O.M.A.D. Brasil é permitir que usuários brasileiros consigam montar um servidor local/offline com:

- biblioteca de conhecimento em português;
- Wikipédia e outros conteúdos offline via Kiwix;
- mapas offline do Brasil em formato PMTiles;
- educação offline;
- IA local orientada ao português brasileiro;
- documentação simples e prática;
- scripts e workflows para manter catálogos brasileiros.

---

## Status do projeto

Este projeto está em desenvolvimento ativo.

### Já iniciado

- Código base importado para repositório brasileiro;
- README principal em português;
- Docker Compose brasileiro;
- documentação inicial para usuários;
- catálogos brasileiros em `collections/br/`;
- validador dos catálogos brasileiros;
- workflow específico para validar catálogos brasileiros;
- workflow consultivo para validação de URLs externas;
- scripts para atualizar metadados Kiwix em português;
- estrutura inicial para geração de mapas PMTiles do Brasil;
- script para atualizar catálogo de mapas brasileiros.

### Em andamento

- validação dos arquivos ZIM em português;
- preenchimento automático de URLs reais do Kiwix;
- geração e publicação dos primeiros mapas `.pmtiles` brasileiros;
- melhoria do catálogo brasileiro;
- preparação para futura tradução da interface.

---

## Instalação rápida

Clone o repositório:

```bash
git clone https://github.com/Azevedo1996/project-nomad-br.git
cd project-nomad-br
```

Suba o ambiente brasileiro:

```bash
docker compose -f docker-compose.br.yml up -d
```

Acesse o painel:

```text
http://localhost:8082
```

Em outro dispositivo na rede local:

```text
http://IP_DO_SERVIDOR:8082
```

Logs via Dozzle:

```text
http://localhost:9998
```

---

## Docker Compose brasileiro

O arquivo principal para esta adaptação é:

```text
docker-compose.br.yml
```

Portas padrão:

```text
8082 - Painel principal do N.O.M.A.D. Brasil
9998 - Visualizador de logs Dozzle
```

Comandos úteis:

```bash
docker compose -f docker-compose.br.yml up -d
docker compose -f docker-compose.br.yml logs -f
docker compose -f docker-compose.br.yml down
```

---

## Documentação

A documentação brasileira está em:

```text
docs/
```

Guias principais:

- [Primeiros passos](docs/primeiros-passos.md)
- [Guia do usuário brasileiro](docs/guia-usuario-brasil.md)
- [FAQ Brasil](docs/faq-brasil.md)
- [Troubleshooting Brasil](docs/troubleshooting-brasil.md)
- [Como contribuir](docs/contribuindo-brasil.md)
- [Catálogos brasileiros](docs/catalogos-brasil.md)
- [Atualização de metadados Kiwix](docs/atualizacao-metadados-kiwix.md)
- [Geração de mapas PMTiles do Brasil](docs/geracao-mapas-pmtiles-brasil.md)
- [Atualização do catálogo de mapas](docs/atualizacao-catalogo-mapas-br.md)

---

## Catálogos brasileiros

Os catálogos brasileiros ficam em:

```text
collections/br/
```

Arquivos principais:

```text
collections/br/wikipedia-br.json
collections/br/kiwix-categories-br.json
collections/br/maps-br.json
collections/br/catalog-index.json
```

Esses arquivos organizam as opções brasileiras de:

- Wikipédia em português;
- conteúdos Kiwix em português;
- mapas PMTiles do Brasil;
- categorias de conhecimento prioritárias para usuários brasileiros.

---

## Validação dos catálogos

Execute localmente:

```bash
python scripts/validate-br-catalogs.py
```

No Windows:

```cmd
python scriptsalidate-br-catalogs.py
```

O workflow correspondente no GitHub Actions é:

```text
Validate Brazilian Catalogs
```

---

## Atualização dos metadados Kiwix

Para buscar automaticamente arquivos ZIM em português:

```bash
python scripts/update-br-kiwix-metadata.py --dry-run --report docs/relatorio-kiwix-br.md
```

Para aplicar alterações:

```bash
python scripts/update-br-kiwix-metadata.py --apply --report docs/relatorio-kiwix-br.md
```

Também existe um workflow manual:

```text
Update Brazilian Kiwix Metadata
```

---

## Mapas do Brasil

A estrutura de mapas fica em:

```text
maps/br/
```

Mapas planejados:

```text
Brasil
Região Sudeste
Região Sul
Região Nordeste
Região Norte
Região Centro-Oeste
Rio de Janeiro
São Paulo
Minas Gerais
Espírito Santo
```

Gerar mapa de teste:

```bash
./scripts/generate-br-pmtiles.sh https://build.protomaps.com/AAAAmmdd.pmtiles rio-de-janeiro
```

No PowerShell:

```powershell
.\scripts\generate-br-pmtiles.ps1 -SourcePmtiles "https://build.protomaps.com/AAAAmmdd.pmtiles" -Region "rio-de-janeiro"
```

Atualizar catálogo de mapas depois de gerar os arquivos:

```bash
python scripts/update-br-maps-catalog.py --apply --release-tag maps-br-v1
```

> Não faça commit de arquivos `.pmtiles`. Publique arquivos grandes em GitHub Releases ou outro storage.

---

## Estrutura brasileira adicionada

```text
collections/br/
docs/
scripts/
maps/br/
.github/workflows/
docker-compose.br.yml
```

---

## Roadmap

### Fase 1 — Base brasileira

- [x] Criar repositório brasileiro;
- [x] Importar código base;
- [x] Criar README brasileiro;
- [x] Criar Docker Compose brasileiro;
- [x] Criar documentação brasileira inicial;
- [x] Criar catálogos brasileiros iniciais;
- [x] Criar validador dos catálogos brasileiros.

### Fase 2 — Conteúdo em português

- [x] Criar script de atualização de metadados Kiwix;
- [x] Criar workflow de atualização Kiwix;
- [ ] Validar arquivos reais da Wikipédia em português;
- [ ] Validar Wiktionary e Wikivoyage em português;
- [ ] Criar catálogo brasileiro pronto para uso no painel.

### Fase 3 — Mapas do Brasil

- [x] Criar estrutura de mapas PMTiles;
- [x] Criar script de geração de mapas;
- [x] Criar script de atualização do catálogo de mapas;
- [ ] Gerar primeiro mapa de teste;
- [ ] Publicar mapa em GitHub Releases;
- [ ] Atualizar `collections/br/maps-br.json` com URLs reais.

### Fase 4 — Experiência brasileira completa

- [ ] Melhorar documentação de usuário final;
- [ ] Criar instalador simplificado;
- [ ] Criar imagem Docker brasileira;
- [ ] Iniciar tradução da interface para pt-BR;
- [ ] Adicionar seletor de idioma futuramente.

---

## Requisitos recomendados

Uso básico:

```text
CPU: 4 núcleos
RAM: 8 GB
Disco: 100 GB ou mais
Docker instalado
Docker Compose instalado
```

Uso com IA local:

```text
CPU: 8 núcleos ou mais
RAM: 16 GB ou mais
Disco: 250 GB ou mais
GPU: recomendada para modelos maiores
```

Biblioteca grande e mapas:

```text
Disco: 500 GB ou mais
SSD recomendado
```

---

## Segurança

Alguns containers usam acesso ao Docker socket:

```text
/var/run/docker.sock
```

Esse acesso é sensível e deve ser usado com cuidado.

Recomendações:

- não exponha o painel diretamente na internet;
- use apenas em rede local ou VPN;
- proteja o host com firewall;
- faça backup periódico;
- use senhas fortes;
- revise arquivos antes de publicar.

---

## Backup

Diretório sugerido:

```text
/opt/project-nomad-br
```

Itens importantes:

```text
/opt/project-nomad-br/storage
/opt/project-nomad-br/mysql
/opt/project-nomad-br/redis
```

---

## Como contribuir

Contribuições são bem-vindas.

Você pode ajudar com:

- documentação em português;
- testes no Brasil;
- lista de conteúdos Kiwix em português;
- mapas PMTiles do Brasil;
- scripts;
- workflows;
- tradução futura da interface;
- tutoriais para usuários iniciantes.

Leia:

```text
docs/contribuindo-brasil.md
```

---

## Créditos

Este projeto é baseado no Project N.O.M.A.D. original, criado e mantido pela Crosstalk Solutions.

Repositório original:

```text
https://github.com/Crosstalk-Solutions/project-nomad
```

Site oficial:

```text
https://www.projectnomad.us/
```

---

## Aviso importante

Este repositório é uma adaptação brasileira independente e comunitária.

Este projeto não substitui o projeto original e não representa oficialmente a Crosstalk Solutions.

O objetivo é criar uma experiência mais acessível para usuários brasileiros, mantendo os devidos créditos ao projeto original.

---

## Licença

Este projeto mantém a licença Apache-2.0 do projeto original.

Consulte:

```text
LICENSE
```

---

## Autor da adaptação brasileira

Mantido por:

```text
Leonardo Azevedo
GitHub: https://github.com/Azevedo1996
```
