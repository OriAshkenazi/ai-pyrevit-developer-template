$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    $statusPath = "CodexWorkspace/workspace/status.md"
    $staged = git diff --cached --name-only --diff-filter=ACMR
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Unable to read staged files."
        exit 1
    }

    if (-not $staged) {
        Write-Host "No staged files. Status update check passed."
        exit 0
    }

    $normalized = @($staged | ForEach-Object { $_ -replace "\\", "/" })
    if ($normalized -contains $statusPath) {
        Write-Host "Status update check passed (status.md is staged)."
        exit 0
    }

    $ignoredPrefixes = @(
        "CodexWorkspace/workspace/plans/",
        "CodexWorkspace/workspace/tasks/",
        "CodexWorkspace/workspace/reviews/",
        "tmp/"
    )
    $ignoredFiles = @(
        "CHANGELOG.md",
        "CodexWorkspace/workspace/status.md"
    )

    $meaningful = @()
    foreach ($file in $normalized) {
        if ($ignoredFiles -contains $file) { continue }
        $skip = $false
        foreach ($prefix in $ignoredPrefixes) {
            if ($file.StartsWith($prefix)) {
                $skip = $true
                break
            }
        }
        if (-not $skip) {
            $meaningful += $file
        }
    }

    if ($meaningful.Count -gt 0) {
        Write-Error ("Advanced mode requires status.md updates for meaningful staged changes.`nMissing staged file: $statusPath`nAffected staged paths:`n- " + ($meaningful -join "`n- "))
        exit 1
    }

    Write-Host "Status update check passed."
}
finally {
    Pop-Location
}
