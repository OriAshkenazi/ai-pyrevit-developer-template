$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    git rev-parse --is-inside-work-tree | Out-Null
    git config --local core.hooksPath .githooks
    $hookPath = git config --get core.hooksPath
    Write-Host "Advanced hooks enabled. core.hooksPath=$hookPath"
}
finally {
    Pop-Location
}
