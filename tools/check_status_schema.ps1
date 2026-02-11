$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$statusFile = Join-Path $repoRoot "CodexWorkspace/workspace/status.md"

if (-not (Test-Path $statusFile)) {
    Write-Error "Missing required advanced artifact: CodexWorkspace/workspace/status.md"
    exit 1
}

$content = Get-Content $statusFile -Raw
$requiredHeaders = @(
    "Scope",
    "Folder Map",
    "Completed",
    "In Progress",
    "Pending",
    "Known Bugs",
    "Open Risks",
    "Next Actions",
    "Last Updated"
)

$missing = @()
foreach ($header in $requiredHeaders) {
    if ($content -notmatch ("(?m)^##\s+" + [regex]::Escape($header) + "\b")) {
        $missing += $header
    }
}

if ($missing.Count -gt 0) {
    Write-Error ("status.md schema is incomplete. Missing headers:`n- " + ($missing -join "`n- "))
    exit 1
}

Write-Host "Status schema check passed."
