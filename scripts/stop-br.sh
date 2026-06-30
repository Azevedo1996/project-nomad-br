#!/usr/bin/env bash
set -e

echo "Parando Project N.O.M.A.D. Brasil..."
docker compose -f docker-compose.br.yml down

echo "Serviços parados."
