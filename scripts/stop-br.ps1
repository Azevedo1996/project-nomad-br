Write-Host "Parando Project N.O.M.A.D. Brasil..." -ForegroundColor Yellow

docker compose -f docker-compose.br.yml down

Write-Host "Serviços parados." -ForegroundColor Green
