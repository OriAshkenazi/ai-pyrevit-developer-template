$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    $pattern = "CodexWorkspace/docs/"
    $exclude = @(
        "--glob", "!CodexWorkspace/workspace/plans/**",
        "--glob", "!CodexWorkspace/workspace/tasks/**",
        "--glob", "!CodexWorkspace/workspace/reviews/**",
        "--glob", "!tools/check_stale_doc_paths.ps1"
    )

    $result = & rg -n --hidden @exclude $pattern .
    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0) {
        Write-Error ("Stale path pattern found:`n" + ($result -join "`n"))
        exit 1
    }

    Write-Host "Stale doc path check passed."
}
finally {
    Pop-Location
}
