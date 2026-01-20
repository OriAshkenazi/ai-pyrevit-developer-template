# Dev Workflow (This Repo)

## Git Strategy
- **Branch naming**: `<prefix>/<short-topic>`
  - `agent/` agent setup or automation
  - `docs/` documentation-only changes
  - `feat/` new behavior or features
  - `fix/` bug fixes
  - `refactor/` structural refactors without behavior changes
  - `test/` tests only
  - `chore/` tooling or maintenance
- **Commits**: keep commits small and scoped; prefer one logical change per commit.
- **Commit messages**: `type: summary` (e.g., `docs: update CodexWorkspace index`).

## Git Hygiene
- Run `git status -sb` before and after each change.
- Avoid mixing unrelated changes in a single commit.
- Avoid destructive commands (`git reset --hard`, `git checkout --`) unless explicitly requested.

## Documentation Hygiene
- If you change a tool's behavior, update the relevant `CodexWorkspace/docs/` pages and any tool-specific docs near the code.
- Keep `CodexWorkspace/docs/README.md` (and checklist indexes) up to date when adding/moving docs.
- When moving/renaming docs, prefer `git mv` + updating references over file-based "Moved to ..." stubs.

## Naming Conventions
- **Python modules**: `snake_case.py` for reusable libraries/utilities.
- **Standalone helper scripts**: prefer lower-kebab names where practical.
- **pyRevit command entrypoints**: keep the conventional `script.py` inside `*.pushbutton/` bundles.
- **Docs**: prefer lower `snake_case.md` filenames (exceptions: `README.md`, `AGENTS.md`).

## Validation
- If tests exist, run them (start with the smallest relevant subset, then broader runs).
- For script-only changes without tests, at least run a quick syntax check on edited Python files (e.g., `python -m py_compile ...`).
