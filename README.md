# Project N.O.M.A.D. Brasil

> Servidor offline de conhecimento, mapas, educação e IA local adaptado para usuários brasileiros.

O **Project N.O.M.A.D. Brasil** é uma adaptação brasileira e comunitária do projeto open source **Project N.O.M.A.D.**, com foco em tornar a solução mais acessível para pessoas brasileiras por meio de documentação em português, conteúdo offline em português brasileiro, mapas do Brasil e uso de IA local orientada ao idioma português.

Este repositório mantém uma base paralela ao projeto original, com o objetivo de facilitar instalação, uso, documentação, testes e futuras customizações para o público brasileiro.

---

## Sumário

- [Objetivo](#objetivo)
- [O que é o Project N.O.M.A.D.](#o-que-é-o-project-nomad)
- [Por que uma versão brasileira?](#por-que-uma-versão-brasileira)
- [Status do projeto](#status-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Instalação rápida](#instalação-rápida)
- [Docker Compose brasileiro](#docker-compose-brasileiro)
- [Acessos padrão](#acessos-padrão)
- [Conteúdos recomendados para o Brasil](#conteúdos-recomendados-para-o-brasil)
- [Mapas do Brasil](#mapas-do-brasil)
- [IA local em português](#ia-local-em-português)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Roadmap](#roadmap)
- [Requisitos recomendados](#requisitos-recomendados)
- [Segurança](#segurança)
- [Backup](#backup)
- [Como contribuir](#como-contribuir)
- [Créditos](#créditos)
- [Licença](#licença)

---

## Objetivo

O objetivo do **Project N.O.M.A.D. Brasil** é criar uma versão brasileira paralela do Project N.O.M.A.D., mantendo os créditos e a compatibilidade com o projeto original, mas adicionando uma camada voltada ao Brasil.

A proposta inicial é:

- Facilitar a instalação para usuários brasileiros;
- Documentar tudo em português brasileiro;
- Incentivar o uso de conteúdos offline em português;
- Adicionar documentação para mapas offline do Brasil;
- Orientar o uso de IA local respondendo em português;
- Criar uma base para futura tradução da interface principal;
- Disponibilizar um ambiente pronto para laboratórios, estudo, preparação emergencial e uso offline.

---

## O que é o Project N.O.M.A.D.

**N.O.M.A.D.** significa:

```text
Node for Offline Media, Archives, and Data
```

O Project N.O.M.A.D. é uma plataforma offline-first que permite rodar, em um servidor local, ferramentas de conhecimento, mapas, educação, IA e utilidades técnicas.

A ideia principal é simples:

```text
Baixe o conteúdo enquanto há internet.
Depois use tudo localmente, mesmo sem conexão.
```

Com isso, é possível criar um servidor local com:

- Enciclopédias offline;
- Biblioteca de documentos;
- Mapas offline;
- Cursos e materiais educacionais;
- IA local;
- Ferramentas técnicas;
- Notas locais;
- Base de conhecimento pesquisável.

---

## Por que uma versão brasileira?

O projeto original é excelente, mas grande parte da experiência inicial está em inglês e algumas coleções de mapas/conteúdos são mais direcionadas a outros países.

Para muitos usuários brasileiros, isso cria barreiras como:

- Interface e documentação em inglês;
- Dificuldade para encontrar conteúdos em português;
- Ausência de catálogo brasileiro inicial;
- Falta de mapas prontos do Brasil;
- Falta de instruções específicas para ambiente Windows/Linux usado no Brasil;
- Dificuldade para configurar IA local respondendo em português.

O **Project N.O.M.A.D. Brasil** tenta resolver essas barreiras de forma comunitária.

---

## Status do projeto

Este projeto está em fase inicial.

A primeira etapa consiste em:

- Importar o código base do Project N.O.M.A.D.;
- Criar documentação brasileira;
- Criar Docker Compose adaptado;
- Documentar o uso de conteúdos em português;
- Documentar mapas do Brasil;
- Preparar a base para futuras traduções da interface.

A interface principal ainda pode estar em inglês durante a fase inicial.

---

## Funcionalidades

### Biblioteca offline

Por meio do Kiwix, o ambiente pode disponibilizar conteúdos offline em formato `.zim`, como:

- Wikipédia em português;
- Wiktionary em português;
- Wikivoyage em português;
- Livros de domínio público;
- Referências técnicas;
- Materiais educacionais;
- Documentações locais;
- Guias de primeiros socorros;
- Manuais e apostilas.

---

### IA local em português

Com Ollama e modelos locais, o usuário pode utilizar uma IA executando no próprio servidor, sem depender de serviços em nuvem.

Uso esperado:

- Perguntas e respostas em português;
- Apoio a estudos;
- Explicações técnicas;
- Análise de documentos;
- Ajuda com Linux, redes, Docker e infraestrutura;
- Consulta a materiais locais quando integrada à base de conhecimento.

---

### Mapas offline do Brasil

O projeto pretende documentar e disponibilizar mapas offline em formato `.pmtiles`, derivados de dados abertos do OpenStreetMap.

Mapas planejados:

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

---

### Educação offline

A versão brasileira pretende orientar o uso de conteúdos educacionais em português, incluindo materiais compatíveis com Kolibri e conteúdos educacionais brasileiros quando disponíveis.

Exemplos de foco:

- Matemática;
- Ciências;
- Língua Portuguesa;
- Ensino Fundamental;
- Ensino Médio;
- BNCC;
- Cursos técnicos;
- Conteúdos livres em português.

---

### Ferramentas técnicas

O ecossistema do Project N.O.M.A.D. pode incluir ferramentas úteis como:

- Kiwix;
- Ollama;
- Qdrant;
- Kolibri;
- CyberChef;
- FlatNotes;
- OpenWebUI;
- Mapas offline;
- Visualização de logs;
- Gerenciamento de apps e containers.

---

## Instalação rápida

> Recomendado para usuários que já possuem Docker e Docker Compose instalados.

Clone este repositório:

```bash
git clone https://github.com/Azevedo1996/project-nomad-br.git
cd project-nomad-br
```

Suba o ambiente brasileiro usando o compose adaptado:

```bash
docker compose -f docker-compose.br.yml up -d
```

Acesse no navegador:

```text
http://localhost:8082
```

Caso esteja acessando de outro computador na rede, use o IP do servidor:

```text
http://IP_DO_SERVIDOR:8082
```

---

## Docker Compose brasileiro

Este projeto pode incluir um arquivo específico para o ambiente brasileiro:

```text
docker-compose.br.yml
```

Esse compose usa portas ajustadas para evitar conflitos comuns em servidores que já possuem outros containers em execução.

Portas padrão sugeridas:

```text
8082 - Painel principal do N.O.M.A.D. Brasil
9998 - Visualizador de logs Dozzle
```

Para subir:

```bash
docker compose -f docker-compose.br.yml up -d
```

Para parar:

```bash
docker compose -f docker-compose.br.yml down
```

Para ver logs:

```bash
docker compose -f docker-compose.br.yml logs -f
```

---

## Acessos padrão

Após subir o ambiente:

```text
Painel principal: http://localhost:8082
Logs Dozzle:      http://localhost:9998
```

Em outro dispositivo na mesma rede:

```text
Painel principal: http://IP_DO_SERVIDOR:8082
Logs Dozzle:      http://IP_DO_SERVIDOR:9998
```

---

## Conteúdos recomendados para o Brasil

### Kiwix / ZIM

Conteúdos recomendados:

```text
Wikipédia em português
Wiktionary em português
Wikivoyage em português
Livros em português
Materiais educacionais em português
Documentações técnicas
Guias de primeiros socorros
```

Tipos comuns de arquivos ZIM:

```text
mini  - versão reduzida
nopic - versão sem imagens
maxi  - versão mais completa
all   - conteúdo amplo
```

Estratégia sugerida:

- Para pouco espaço em disco, começar por versões `mini` ou `nopic`;
- Para servidores com bastante armazenamento, usar versões completas;
- Manter conteúdos essenciais em português como prioridade;
- Adicionar documentos próprios em PDF, Markdown ou texto quando necessário.

---

## Mapas do Brasil

O projeto pretende trabalhar com mapas offline no formato:

```text
.pmtiles
```

Esses arquivos podem ser usados para navegação offline dentro do ambiente N.O.M.A.D.

Fonte preferencial dos dados:

```text
OpenStreetMap
```

Lista inicial desejada:

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

Objetivo futuro:

- Gerar arquivos `.pmtiles` brasileiros;
- Publicar os arquivos em Releases do GitHub;
- Documentar importação no N.O.M.A.D.;
- Criar catálogo brasileiro de mapas.

---

## IA local em português

Prompt recomendado para uso em português:

```text
Você é um assistente local offline para usuários brasileiros.
Responda sempre em português brasileiro.
Explique termos técnicos de forma simples.
Quando citar comandos, mantenha os comandos no idioma original.
Quando não souber uma resposta, diga claramente que não sabe.
Se usar documentos da base local, informe que a resposta foi baseada no conteúdo disponível localmente.
```

Uso recomendado:

- Estudos;
- Infraestrutura;
- Linux;
- Docker;
- Redes;
- Programação;
- Resumo de documentos;
- Apoio educacional;
- Consulta a base local.

---

## Estrutura do projeto

Estrutura inicial planejada:

```text
project-nomad-br/
├── admin/
├── collections/
├── install/
├── docs/
│   ├── instalacao-brasil.md
│   ├── conteudos-brasil.md
│   ├── mapas-brasil.md
│   └── ia-portugues.md
├── scripts/
│   ├── start-br.ps1
│   ├── stop-br.ps1
│   └── update-br.ps1
├── docker-compose.br.yml
├── README.md
├── LICENSE
└── FAQ.md
```

---

## Roadmap

### Fase 1 — Base brasileira

- [x] Criar repositório brasileiro;
- [x] Importar código base;
- [x] Criar README brasileiro;
- [ ] Criar Docker Compose brasileiro;
- [ ] Criar documentação de instalação em pt-BR;
- [ ] Criar documentação de conteúdos brasileiros;
- [ ] Criar documentação de mapas do Brasil;
- [ ] Criar documentação de IA em português.

### Fase 2 — Conteúdo brasileiro

- [ ] Documentar importação da Wikipédia em português;
- [ ] Documentar importação de arquivos ZIM;
- [ ] Documentar integração com Kolibri em português;
- [ ] Documentar modelos de IA recomendados para português;
- [ ] Criar lista de conteúdos brasileiros recomendados.

### Fase 3 — Mapas do Brasil

- [ ] Gerar ou obter `brasil.pmtiles`;
- [ ] Gerar mapas regionais;
- [ ] Testar importação no N.O.M.A.D.;
- [ ] Publicar mapas em releases do GitHub;
- [ ] Documentar uso offline dos mapas.

### Fase 4 — Tradução da interface

- [ ] Mapear textos da interface original;
- [ ] Implementar estrutura de internacionalização;
- [ ] Criar tradução `pt-BR`;
- [ ] Adicionar seletor de idioma;
- [ ] Gerar imagem Docker brasileira;
- [ ] Publicar versão inicial traduzida.

---

## Requisitos recomendados

### Uso básico

```text
CPU: 4 núcleos
RAM: 8 GB
Disco: 100 GB ou mais
Docker instalado
Docker Compose instalado
```

### Uso com IA local

```text
CPU: 8 núcleos ou mais
RAM: 16 GB ou mais
Disco: 250 GB ou mais
GPU: recomendada, mas não obrigatória
```

### Biblioteca grande e mapas offline

```text
Disco: 500 GB ou mais
SSD recomendado
```

---

## Segurança

Este projeto utiliza containers Docker e alguns serviços podem precisar de acesso ao Docker socket:

```text
/var/run/docker.sock
```

Esse acesso é poderoso e deve ser usado com cuidado.

Recomendações:

- Não exponha o painel diretamente à internet;
- Use apenas em rede confiável;
- Prefira acesso via LAN ou VPN;
- Proteja o servidor com firewall;
- Faça backup periódico do diretório de dados;
- Use senhas fortes;
- Evite portas abertas desnecessárias.

---

## Backup

Diretório sugerido para dados persistentes:

```text
/opt/project-nomad-br
```

Itens importantes:

```text
/opt/project-nomad-br/storage
/opt/project-nomad-br/mysql
/opt/project-nomad-br/redis
```

Recomenda-se fazer backup regular desses diretórios.

---

## Como contribuir

Contribuições são bem-vindas.

Você pode ajudar com:

- Tradução da interface;
- Documentação em português;
- Testes no Brasil;
- Mapas regionais;
- Lista de conteúdos brasileiros;
- Scripts de instalação;
- Correções;
- Sugestões de modelos de IA;
- Guias para usuários iniciantes.

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

Consulte o arquivo:

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

---

## Nome do projeto

```text
Project N.O.M.A.D. Brasil
```

Servidor offline de conhecimento, mapas, educação e IA local para usuários brasileiros.
