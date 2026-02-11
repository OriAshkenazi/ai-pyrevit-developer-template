# Logging and Debugging Standards

Use tier-appropriate logging so troubleshooting is fast and reproducible.

## Log Storage
- Temporary/persisted logs belong under:
  - `tmp/logs/`
- Do not store logs outside `tmp/`.
- Do not commit runtime log outputs.

## Beginner Standard (Minimum)
- Record:
  - command/tool name,
  - pass/fail outcome,
  - key error message when failed.
- Keep logs short and human-readable.

## Advanced Standard (Strict)
- Record:
  - timestamp,
  - operation name,
  - key inputs/filters,
  - result summary,
  - error details and stack context (when failed),
  - validation checks executed.
- Keep logs persisted in `tmp/logs/` for review cycles.

## AI/Data Task Logging (Advanced)
- Include:
  - dataset coverage percentage,
  - whether sampling/downsampling was used,
  - explicit metric direction statement,
  - numeric sanity check outcomes.

## Quick Checks
- Verify logs path exists:
  - `tmp/logs/`
- Verify no logs are staged for commit:
  - `git status -sb`

Return back: [`docs_overview.md`](docs_overview.md)
Return to root: [`README.md`](../../../../README.md)
