$ErrorActionPreference = 'SilentlyContinue'

$Root = Split-Path -Parent $PSScriptRoot
$MariaAdmin = Join-Path $Root 'bin\mariadb\bin\mariadb-admin.exe'
$Runtime = Join-Path $Root 'runtime'

Write-Host 'Mematikan website...'

$phpPidFile = Join-Path $Runtime 'php.pid'
if (Test-Path $phpPidFile) {
    $phpId = (Get-Content $phpPidFile).Trim()
    if ($phpId) { Stop-Process -Id $phpId -Force }
    Remove-Item $phpPidFile -Force
}

if (Test-Path $MariaAdmin) {
    & $MariaAdmin --no-defaults --protocol=tcp -h 127.0.0.1 -P 3307 -u root shutdown 2>$null | Out-Null
}
Start-Sleep -Seconds 2

$mariaPidFile = Join-Path $Runtime 'mariadb.pid'
if (Test-Path $mariaPidFile) {
    $mariaId = (Get-Content $mariaPidFile).Trim()
    if ($mariaId) { Stop-Process -Id $mariaId -Force }
    Remove-Item $mariaPidFile -Force
}

# Fallback: stop processes that belong to this folder
$mine = Get-CimInstance Win32_Process | Where-Object {
    $_.CommandLine -and $_.CommandLine -like "*$Root*" -and ($_.Name -eq 'mariadbd.exe' -or $_.Name -eq 'php.exe')
}
foreach ($p in $mine) {
    Stop-Process -Id $p.ProcessId -Force
}

Write-Host 'Website sudah dimatikan.'
