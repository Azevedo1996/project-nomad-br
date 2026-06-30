#!/usr/bin/env bash
set -e

echo "Atualizando imagens do Project N.O.M.A.D. Brasil..."
docker compose -f docker-compose.br.yml pull
docker compose -f docker-compose.br.yml up -d

echo "Atualização concluída."
