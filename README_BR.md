\# Project N.O.M.A.D. Brasil



Versão brasileira paralela do Project N.O.M.A.D., com foco em usuários brasileiros, conteúdo em português, mapas do Brasil, educação offline e IA local em português.



\## Objetivo



O objetivo deste projeto é adaptar o Project N.O.M.A.D. para uso no Brasil, mantendo compatibilidade com a base original, mas adicionando documentação, configurações e coleções voltadas ao público brasileiro.



\## Funcionalidades planejadas



\- Interface e documentação em português brasileiro

\- Conteúdo offline em português

\- Wikipédia em português via Kiwix

\- Mapas offline do Brasil via PMTiles/OpenStreetMap

\- Educação com conteúdo em português/Brasil

\- IA local orientada a responder em português

\- Docker Compose adaptado para ambientes brasileiros

\- Scripts auxiliares para instalação e manutenção



\## Status do projeto



Este projeto está em fase inicial.



A primeira etapa usa a imagem oficial do Project N.O.M.A.D. e adiciona uma camada brasileira de configuração, documentação e conteúdo.



\## Como executar



Use o compose brasileiro:



```bash

docker compose -f docker-compose.br.yml up -d

