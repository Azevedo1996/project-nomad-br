# Instalação do Project N.O.M.A.D. Brasil

Este guia instala o Project N.O.M.A.D. Brasil usando Docker Compose.

## Requisitos

- Docker instalado
- Docker Compose instalado
- Acesso ao terminal
- Permissão administrativa/root no host

## Instalação no Linux

Crie os diretórios persistentes:

```bash
sudo mkdir -p /opt/project-nomad-br/storage
sudo mkdir -p /opt/project-nomad-br/mysql
sudo mkdir -p /opt/project-nomad-br/redis
```

Clone o repositório:

```bash
git clone https://github.com/Azevedo1996/project-nomad-br.git
cd project-nomad-br
```

Suba os containers:

```bash
docker compose -f docker-compose.br.yml up -d
```

Acesse:

```text
http://IP_DO_SERVIDOR:8082
```

## Instalação no Windows

No Windows, o uso recomendado é via Docker Desktop com WSL2.

Clone o projeto:

```powershell
git clone https://github.com/Azevedo1996/project-nomad-br.git
cd project-nomad-br
```

Suba o ambiente:

```powershell
docker compose -f docker-compose.br.yml up -d
```

Acesse:

```text
http://localhost:8082
```

## Comandos úteis

Ver containers:

```bash
docker ps
```

Ver logs:

```bash
docker compose -f docker-compose.br.yml logs -f
```

Parar:

```bash
docker compose -f docker-compose.br.yml down
```

Atualizar imagens:

```bash
docker compose -f docker-compose.br.yml pull
docker compose -f docker-compose.br.yml up -d
```
