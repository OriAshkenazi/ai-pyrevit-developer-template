# Codex Agent Guide (Repository Root)

This repo includes a curated knowledge base under [`CodexWorkspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace) that Codex should use as the **default reference** for Revit 2023 + pyRevit work.

## Start Here
- Primary entrypoint: [`CodexWorkspace/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/README.md)
- Docs index: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
- Checklists: [`CodexWorkspace/docs/checklists/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/checklists)
- Prompt snippets: [`CodexWorkspace/prompts/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/prompts)
- Script templates/harnesses: [`CodexWorkspace/scripts/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/scripts)
- Planning templates: [`CodexWorkspace/docs/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/templates)
- Planning workspace (project-specific): [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace)

## How To Use [`CodexWorkspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace)
1. **Before coding**: open the relevant doc(s) from [`CodexWorkspace/docs/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs) (especially the Revit 2023 guideline reference and the checklists).
2. **When planning**: copy templates from [`CodexWorkspace/docs/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/templates) into [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) and edit only the workspace copies.
3. **When creating a new pyRevit command**: start from [`CodexWorkspace/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py) and adapt it to the target tool folder.
4. **When reviewing or debugging**: use the checklists in [`CodexWorkspace/docs/checklists/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/checklists) and the prompt snippets in [`CodexWorkspace/prompts/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/prompts) to standardize analysis and outcomes.
5. **When unsure about patterns**: prefer the Revit 2023 guidance under [`CodexWorkspace/docs/reference/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/reference) over ad-hoc API usage.

## Repo Layout Notes (pyRevit Extensions)
- Commands typically live under a pushbutton folder (example: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)).
- Keep transactions explicit (`Start/Commit`, `RollBack` on exceptions).
- Convert Python iterables to .NET collections at Revit API boundaries when required (e.g., `List[ElementId]`).

## Git Workflow
- **Branch naming**: use `<prefix>/<short-topic>` (e.g., `docs/codexworkspace-nav`, `fix/copy-level-remap`).
- **Prefix guide**: `agent/` setup, `docs/` documentation-only, `feat/` new behavior, `fix/` bug fix, `refactor/` structure-only, `test/` tests only, `chore/` maintenance.
- **Commits**: keep commits small + scoped; prefer one logical change per commit; message format `type: summary` (e.g., `docs: add dev workflow guide`).
- **Hygiene**: run `git status -sb` before/after changes; avoid mixing unrelated edits; avoid destructive commands (e.g., `git reset --hard`) unless explicitly requested.
- **Naming**: use `snake_case` for reusable modules; for standalone helper scripts prefer lower-kebab where practical (pyRevit command entrypoints stay as `script.py`).
- **Docs**: prefer lower `snake_case.md` filenames (exceptions: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md), [`AGENTS.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/AGENTS.md)); when moving docs, prefer `git mv` + updating references over file-based “Moved to …” stubs.

Return back: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
