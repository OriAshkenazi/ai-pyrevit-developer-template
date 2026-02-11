$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    $required = @(
        "ai-pyrevit-developer-template.extension",
        "ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py"
    )

    $missing = @()
    foreach ($path in $required) {
        if (-not (Test-Path $path)) {
            $missing += $path
        }
    }

    if ($missing.Count -gt 0) {
        Write-Error ("Missing required OOTB scaffold paths:`n- " + ($missing -join "`n- "))
        exit 1
    }

    Write-Host "OOTB scaffold check passed."
}
finally {
    Pop-Location
}
