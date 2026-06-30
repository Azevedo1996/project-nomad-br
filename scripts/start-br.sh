#!/usr/bin/env bash
set -e

echo "Iniciando Project N.O.M.A.D. Brasil..."
docker compose -f docker-compose.br.yml up -d

echo ""
echo "Acesse: http://localhost:8082"
echo "Logs:   http://localhost:9998"
