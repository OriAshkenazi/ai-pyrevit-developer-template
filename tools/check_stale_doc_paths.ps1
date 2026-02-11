$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot
try {
    $pattern = "CodexWorkspace/docs/"
    $excludePrefixes = @(
        "CodexWorkspace/workspace/plans/",
        "CodexWorkspace/workspace/tasks/",
        "CodexWorkspace/workspace/reviews/"
    )
    $excludeFiles = @(
        "tools/check_stale_doc_paths.ps1"
    )

    $violations = @()

    if (Get-Command rg -ErrorAction SilentlyContinue) {
        $rgExclude = @(
            "--glob", "!CodexWorkspace/workspace/plans/**",
            "--glob", "!CodexWorkspace/workspace/tasks/**",
            "--glob", "!CodexWorkspace/workspace/reviews/**",
            "--glob", "!tools/check_stale_doc_paths.ps1"
        )
        $result = & rg -n --hidden @rgExclude $pattern .
        if ($LASTEXITCODE -eq 0 -and $result) {
            $violations += $result
        }
    }
    else {
        $files = git ls-files
        foreach ($file in $files) {
            $normalized = $file -replace "\\", "/"
            if ($excludeFiles -contains $normalized) { continue }

            $skip = $false
            foreach ($prefix in $excludePrefixes) {
                if ($normalized.StartsWith($prefix)) {
                    $skip = $true
                    break
                }
            }
            if ($skip) { continue }

            $hits = Select-String -Path $file -SimpleMatch -Pattern $pattern -ErrorAction SilentlyContinue
            foreach ($hit in $hits) {
                $violations += ("{0}:{1}:{2}" -f $file, $hit.LineNumber, $hit.Line.Trim())
            }
        }
    }

    if ($violations.Count -gt 0) {
        Write-Error ("Stale path pattern found:`n" + ($violations -join "`n"))
        exit 1
    }

    Write-Host "Stale doc path check passed."
}
finally {
    Pop-Location
}
