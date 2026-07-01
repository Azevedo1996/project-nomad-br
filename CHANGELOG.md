# Changelog

Todas as mudanças relevantes do **Project N.O.M.A.D. Brasil** serão documentadas neste arquivo.

Este projeto segue uma organização simples de versões brasileiras usando o sufixo `-br`.

---

## [v0.1.0-br] - 2026-07-01

### Adicionado

- Criação da versão brasileira paralela do Project N.O.M.A.D.
- README principal em português brasileiro.
- Docker Compose brasileiro em `docker-compose.br.yml`.
- Documentação inicial em `docs/`.
- Catálogos brasileiros em `collections/br/`.
- Catálogo inicial de Wikipédia em português.
- Catálogo inicial de categorias Kiwix para conteúdo brasileiro.
- Catálogo inicial de mapas brasileiros.
- Validador local dos catálogos brasileiros.
- Workflow específico para validar catálogos brasileiros.
- Workflow consultivo para validação de URLs externas.
- Script para atualizar metadados Kiwix em português.
- Workflow manual para atualização de metadados Kiwix.
- Estrutura para geração de mapas PMTiles do Brasil.
- Scripts para geração de mapas PMTiles no Linux/WSL e PowerShell.
- Script para atualizar o catálogo de mapas brasileiros.
- Documentação de primeiros passos.
- Guia do usuário brasileiro.
- FAQ Brasil.
- Troubleshooting Brasil.
- Guia de contribuição.

### Alterado

- Organização inicial do README para focar na experiência brasileira.
- Separação dos catálogos brasileiros em `collections/br/` sem substituir diretamente os catálogos originais.
- Validação de URLs externas tratada como consultiva para não bloquear o desenvolvimento brasileiro por links legados do projeto original.

### Planejado

- Validar URLs reais da Wikipédia em português no Kiwix.
- Validar Wiktionary e Wikivoyage em português.
- Gerar primeiro mapa PMTiles de teste do Brasil ou Rio de Janeiro.
- Publicar mapas em GitHub Releases.
- Atualizar `collections/br/maps-br.json` com URLs reais.
- Iniciar futura tradução da interface para pt-BR.

---
