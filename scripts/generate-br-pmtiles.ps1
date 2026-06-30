param(
    [Parameter(Mandatory=$true)]
    [string]$SourcePmtiles,

    [string]$Region = "all",

    [string]$MaxZoom = "",

    [int]$DownloadThreads = 4
)

Write-Host "Gerador de PMTiles Brasil - Project N.O.M.A.D. Brasil" -ForegroundColor Cyan

if (-not (Get-Command pmtiles -ErrorAction SilentlyContinue)) {
    Write-Host "Erro: pmtiles CLI não encontrado no PATH." -ForegroundColor Red
    Write-Host "Instale conforme documentação: https://docs.protomaps.com/pmtiles/cli"
    exit 1
}

New-Item -ItemType Directory -Force -Path "maps/br/output" | Out-Null

$regions = Get-Content "maps/br/regions.json" -Raw | ConvertFrom-Json

foreach ($r in $regions.regions) {
    if ($Region -ne "all" -and $Region -ne $r.id) {
        continue
    }

    $output = "maps/br/output/$($r.id).pmtiles"
    Write-Host "Gerando $output usando bbox $($r.bbox)..." -ForegroundColor Green

    if ($MaxZoom -ne "") {
        pmtiles extract $SourcePmtiles $output --bbox=$($r.bbox) --maxzoom=$MaxZoom --download-threads=$DownloadThreads
    } else {
        pmtiles extract $SourcePmtiles $output --bbox=$($r.bbox) --download-threads=$DownloadThreads
    }

    pmtiles verify $output
    pmtiles show $output --metadata | Out-File "$output.metadata.json" -Encoding utf8
    Get-Item $output | Select-Object FullName, Length
}

Write-Host "Concluído. Arquivos gerados em maps/br/output/." -ForegroundColor Cyan
