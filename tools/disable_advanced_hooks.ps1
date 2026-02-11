$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    git rev-parse --is-inside-work-tree | Out-Null
    $current = git config --get core.hooksPath
    if ($LASTEXITCODE -eq 0 -and $current) {
        git config --local --unset core.hooksPath
        Write-Host "Advanced hooks disabled. core.hooksPath unset."
    }
    else {
        Write-Host "Advanced hooks already disabled."
    }
}
finally {
    Pop-Location
}
