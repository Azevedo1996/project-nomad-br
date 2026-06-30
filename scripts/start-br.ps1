Write-Host "Iniciando Project N.O.M.A.D. Brasil..." -ForegroundColor Green

docker compose -f docker-compose.br.yml up -d

Write-Host ""
Write-Host "Acesse o painel em:" -ForegroundColor Cyan
Write-Host "http://localhost:8082"
Write-Host ""
Write-Host "Logs em:" -ForegroundColor Cyan
Write-Host "http://localhost:9998"
