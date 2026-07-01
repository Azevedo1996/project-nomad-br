# Guia do usuário brasileiro

Este guia explica como usar o Project N.O.M.A.D. Brasil no dia a dia.

## O que é o Project N.O.M.A.D. Brasil?

O Project N.O.M.A.D. Brasil é uma adaptação brasileira do Project N.O.M.A.D. com foco em:

- conteúdo offline em português;
- mapas do Brasil;
- educação offline;
- IA local em português;
- documentação simples para usuários brasileiros.

## Como acessar

Depois que o ambiente estiver rodando, acesse:

```text
http://localhost:8082
```

Ou, pela rede local:

```text
http://IP_DO_SERVIDOR:8082
```

## Biblioteca offline

A biblioteca offline é a parte usada para guardar conteúdo como:

- Wikipédia;
- dicionários;
- guias;
- livros;
- documentos técnicos;
- materiais próprios.

A prioridade do projeto brasileiro é usar conteúdos em português.

## Mapas offline

Os mapas brasileiros serão disponibilizados em formato `.pmtiles`.

Mapas planejados:

```text
Brasil
Sudeste
Sul
Nordeste
Norte
Centro-Oeste
Rio de Janeiro
São Paulo
Minas Gerais
Espírito Santo
```

## IA local

A IA local deve ser usada preferencialmente em português brasileiro.

Prompt recomendado:

```text
Você é um assistente local offline para usuários brasileiros.
Responda sempre em português brasileiro.
Explique termos técnicos de forma simples.
Quando citar comandos, mantenha os comandos no idioma original.
Quando não souber uma resposta, diga claramente que não sabe.
```

## Educação

A área educacional deve priorizar conteúdos em português e materiais compatíveis com uso offline.

Sugestões:

- matemática;
- ciências;
- português;
- cursos técnicos;
- apostilas;
- materiais próprios.

## Boas práticas

- Não exponha o painel diretamente na internet.
- Use em rede local ou VPN.
- Faça backup do diretório `/opt/project-nomad-br`.
- Comece com conteúdos pequenos antes de baixar arquivos grandes.
- Monitore espaço em disco.
- Prefira SSD para melhor desempenho.

## Backup recomendado

Diretórios importantes:

```text
/opt/project-nomad-br/storage
/opt/project-nomad-br/mysql
/opt/project-nomad-br/redis
```

## Atualização

Para atualizar imagens Docker:

```bash
docker compose -f docker-compose.br.yml pull
docker compose -f docker-compose.br.yml up -d
```
