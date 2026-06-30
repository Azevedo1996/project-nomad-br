Write-Host "Atualizando imagens do Project N.O.M.A.D. Brasil..." -ForegroundColor Cyan

docker compose -f docker-compose.br.yml pull
docker compose -f docker-compose.br.yml up -d

Write-Host "Atualização concluída." -ForegroundColor Green
