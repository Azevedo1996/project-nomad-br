# Primeiros passos - Project N.O.M.A.D. Brasil

Este guia é voltado para quem acabou de instalar o Project N.O.M.A.D. Brasil e quer entender o que fazer primeiro.

## 1. Subir o ambiente

Na pasta do projeto, execute:

```bash
docker compose -f docker-compose.br.yml up -d
```

No Windows PowerShell:

```powershell
docker compose -f docker-compose.br.yml up -d
```

## 2. Acessar o painel

No mesmo computador:

```text
http://localhost:8082
```

Em outro dispositivo na rede local:

```text
http://IP_DO_SERVIDOR:8082
```

## 3. Verificar containers

```bash
docker ps
```

Containers esperados na base brasileira:

```text
nomad_br_admin
nomad_br_mysql
nomad_br_redis
nomad_br_dozzle
nomad_br_updater
nomad_br_disk_collector
```

## 4. Acessar logs

Pelo Dozzle:

```text
http://localhost:9998
```

Ou via terminal:

```bash
docker compose -f docker-compose.br.yml logs -f
```

## 5. Primeira configuração recomendada

A ordem recomendada é:

1. Confirmar que o painel abriu.
2. Verificar armazenamento disponível.
3. Instalar/ativar Kiwix.
4. Baixar conteúdo em português.
5. Instalar/ativar mapas, se disponível.
6. Instalar/ativar IA local somente se o hardware suportar.
7. Testar acesso offline pela rede local.

## 6. Conteúdo recomendado para começar

Para um primeiro teste:

```text
Wikipédia em português compacta ou sem imagens
Wiktionary em português
Mapa de uma região pequena, como Rio de Janeiro, quando disponível
```

## 7. Teste offline

Depois de baixar algum conteúdo:

1. Desconecte temporariamente a internet do servidor.
2. Mantenha a rede local ligada.
3. Acesse o painel pelo navegador.
4. Tente abrir o conteúdo baixado.

Se o conteúdo abrir, o uso offline está funcionando.
