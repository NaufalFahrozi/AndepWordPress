$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $PSScriptRoot
$MariaDump = Join-Path $Root 'bin\mariadb\bin\mariadb-dump.exe'
$Php = Join-Path $Root 'bin\php\php.exe'
$Wp = Join-Path $Root 'bin\wp-cli.phar'
$Public = Join-Path $Root 'public'
$Backup = Join-Path $Root 'backup'

New-Item -ItemType Directory -Force -Path $Backup | Out-Null

# Check database port
$client = New-Object System.Net.Sockets.TcpClient
try {
    $client.Connect('127.0.0.1', 3307)
    $client.Close()
} catch {
    Write-Host 'Database belum menyala. Jalankan MULAI.bat dulu.'
    exit 1
}

$sql = Join-Path $Backup 'database.sql'
if (Test-Path $sql) { Remove-Item $sql -Force }
Write-Host 'Membuat backup database...'
$cmd = '"' + $MariaDump + '" --no-defaults -u root --port=3307 --databases studio_karya_nusa --routines --events --triggers --single-transaction > "' + $sql + '"'
cmd /c $cmd
if (-not (Test-Path $sql)) {
    Write-Host 'ERROR: Backup database gagal.'
    exit 1
}

$wxr = Join-Path $Backup 'studio-karya-nusa-wxr.xml'
if (Test-Path $wxr) { Remove-Item $wxr -Force }
Write-Host 'Membuat export WXR...'
& $Php $Wp --path=$Public export --dir=$Backup --filename_format='studio-karya-nusa-wxr.xml' --skip_comments

Write-Host ''
Write-Host 'Backup selesai:'
Write-Host "  $sql"
Write-Host "  $wxr"

