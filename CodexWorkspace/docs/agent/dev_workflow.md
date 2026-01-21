# Dev Workflow (This Repo)

For the AI-orchestrated workflow and prompt usage, see [`CodexWorkspace/docs/agent/ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/ai_orchestrated_dev_methodology.md).

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
- If you change a tool's behavior, update the relevant [`CodexWorkspace/docs/agent/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent) pages and any tool-specific docs near the code.
- Keep [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md) (and checklist indexes) up to date when adding/moving docs.
- When moving/renaming docs, prefer `git mv` + updating references over file-based "Moved to ..." stubs.
- Keep project-specific planning artifacts in [`CodexWorkspace/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace) and static guidance in [`CodexWorkspace/docs/agent/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent) plus [`CodexWorkspace/docs/human/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/human). Agent-only assets live in [`CodexWorkspace/docs/agent/checklists/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/checklists), [`CodexWorkspace/docs/agent/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/templates), [`CodexWorkspace/docs/agent/pyrevit/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/pyrevit), and [`CodexWorkspace/docs/agent/scripts/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/scripts).

## Naming Conventions
- **Python modules**: `snake_case.py` for reusable libraries/utilities.
- **Standalone helper scripts**: prefer lower-kebab names where practical.
- **pyRevit command entrypoints**: keep `script.py` inside the pushbutton folder (example: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton)).
- **Docs**: prefer lower `snake_case.md` filenames (exceptions: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md), [`AGENTS.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/AGENTS.md)).

## Validation
- If tests exist, run them (start with the smallest relevant subset, then broader runs).
- For script-only changes without tests, at least run a quick syntax check on edited Python files (e.g., `python -m py_compile ...`).

Return back: [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
