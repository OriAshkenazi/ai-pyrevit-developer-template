$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    $staged = git diff --cached --name-only --diff-filter=ACMR
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Unable to read staged files."
        exit 1
    }

    if (-not $staged) {
        Write-Host "No staged files. Temp policy check passed."
        exit 0
    }

    $violations = @()
    foreach ($item in $staged) {
        $path = $item -replace "\\", "/"
        if ($path -like "tmp/*") { continue }

        if ($path -match '(^|/)(tmp|temp|scratch|debug|playground|sandbox)(/|_|-|\.)') {
            $violations += $item
            continue
        }

        if ($path -match '\.(tmp|log|bak)$') {
            $violations += $item
            continue
        }
    }

    if ($violations.Count -gt 0) {
        Write-Error ("Temp file policy violation. Move temporary artifacts under tmp/:`n- " + ($violations -join "`n- "))
        exit 1
    }

    Write-Host "Temp file policy check passed."
}
finally {
    Pop-Location
}
