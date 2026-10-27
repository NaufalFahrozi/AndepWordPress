$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $PSScriptRoot
$Bin = Join-Path $Root 'bin'
$PhpDir = Join-Path $Bin 'php'
$Php = Join-Path $PhpDir 'php.exe'
$PhpIni = Join-Path $PhpDir 'php.ini'
$MariaDir = Join-Path $Bin 'mariadb'
$Maria = Join-Path $MariaDir 'bin\mariadbd.exe'
$MariaClient = Join-Path $MariaDir 'bin\mariadb.exe'
$MariaInstall = Join-Path $MariaDir 'bin\mariadb-install-db.exe'
$Data = Join-Path $Root 'data\mariadb'
$Public = Join-Path $Root 'public'
$Router = Join-Path $Root 'router.php'
$Logs = Join-Path $Root 'logs'
$Runtime = Join-Path $Root 'runtime'
$BackupSql = Join-Path $Root 'backup\database.sql'

New-Item -ItemType Directory -Force -Path $Logs, $Runtime | Out-Null

function Test-Port([int]$Port) {
    try {
        $client = New-Object System.Net.Sockets.TcpClient
        $async = $client.BeginConnect('127.0.0.1', $Port, $null, $null)
        $ok = $async.AsyncWaitHandle.WaitOne(600)
        if ($ok -and $client.Connected) {
            $client.Close()
            return $true
        }
        $client.Close()
        return $false
    } catch {
        return $false
    }
}

function Wait-Port([int]$Port, [int]$Seconds) {
    $deadline = (Get-Date).AddSeconds($Seconds)
    while ((Get-Date) -lt $deadline) {
        if (Test-Port $Port) { return $true }
        Start-Sleep -Milliseconds 500
    }
    return $false
}

if (-not (Test-Path $Php)) {
    Write-Host "ERROR: PHP tidak ditemukan di $Php"
    exit 1
}
if (-not (Test-Path $Maria)) {
    Write-Host "ERROR: MariaDB tidak ditemukan di $Maria"
    exit 1
}

# 1. Database
if (-not (Test-Port 3307)) {
    if (-not (Test-Path (Join-Path $Data 'ibdata1'))) {
        Write-Host 'Menyiapkan database pertama kali...'
        New-Item -ItemType Directory -Force -Path $Data | Out-Null
        & $MariaInstall --datadir="$Data" --port=3307 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host 'ERROR: Gagal menyiapkan database.'
            exit 1
        }
    }

    Write-Host 'Menyalakan database...'
    $mariaArgs = @(
        '--no-defaults',
        "--basedir=`"$MariaDir`"",
        "--datadir=`"$Data`"",
        '--port=3307',
        '--bind-address=127.0.0.1',
        '--skip-name-resolve',
        '--console'
    )
    $mariaProc = Start-Process -FilePath $Maria -ArgumentList $mariaArgs `
        -RedirectStandardOutput (Join-Path $Logs 'mariadb.out.log') `
        -RedirectStandardError (Join-Path $Logs 'mariadb.err.log') `
        -WindowStyle Hidden -PassThru
    $mariaProc.Id | Set-Content (Join-Path $Runtime 'mariadb.pid')

    if (-not (Wait-Port 3307 60)) {
        Write-Host 'ERROR: Database gagal menyala. Lihat logs\mariadb.err.log.'
        exit 1
    }

    $checkCmd = '"' + $MariaClient + '" --no-defaults -u root --port=3307 -N -B -e "SHOW DATABASES LIKE ''studio_karya_nusa'';" 2>nul'
    $dbExists = cmd /c $checkCmd
    if (-not $dbExists) {
        if (Test-Path $BackupSql) {
            Write-Host 'Mengimpor database dari backup...'
            $cmd = '"' + $MariaClient + '" --no-defaults -u root --port=3307 < "' + $BackupSql + '"'
            cmd /c $cmd
        } else {
            Write-Host 'ERROR: Database belum ada dan backup\database.sql tidak ditemukan.'
            exit 1
        }
    }
} else {
    Write-Host 'Database sudah berjalan di port 3307.'
}

# 2. Web server
if (-not (Test-Port 8080)) {
    Write-Host 'Menyalakan website...'
    $phpArgs = @(
        '-c', "`"$PhpIni`"",
        '-S', '127.0.0.1:8080',
        '-t', "`"$Public`"",
        "`"$Router`""
    )
    $phpProc = Start-Process -FilePath $Php -ArgumentList $phpArgs -WorkingDirectory $Root `
        -RedirectStandardOutput (Join-Path $Logs 'php.out.log') `
        -RedirectStandardError (Join-Path $Logs 'php.err.log') `
        -WindowStyle Hidden -PassThru
    $phpProc.Id | Set-Content (Join-Path $Runtime 'php.pid')

    if (-not (Wait-Port 8080 30)) {
        Write-Host 'ERROR: Website gagal menyala. Lihat logs\php.err.log.'
        exit 1
    }
} else {
    Write-Host 'Website sudah berjalan di port 8080.'
}

Write-Host ''
Write-Host 'Studio Karya Nusa siap dibuka di http://localhost:8080'
Write-Host 'Admin: http://localhost:8080/wp-admin'
Write-Host 'Username: admin   Password: StudioKaryaNusa2026!'
Write-Host 'Untuk mematikan website: klik MATIKAN.bat'
Start-Process 'http://localhost:8080'
