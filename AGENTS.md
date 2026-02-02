# Codex Agent Guide (Repository Root)

This repo includes a curated knowledge base under [`CodexWorkspace/`](CodexWorkspace/) that Codex should use as the **default reference** for pyRevit work (pair with the matching versioned Revit skill).

## Start Here
- Primary entrypoint: [`CodexWorkspace/README.md`](CodexWorkspace/README.md)
- Human docs index: [`CodexWorkspace/human/README.md`](CodexWorkspace/human/README.md)
- Skill references index: [`CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md)
- Agent docs index: [`CodexWorkspace/skills/develop-pyrevit-extensions/references/agent_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/agent_overview.md)
- Checklists: [`CodexWorkspace/skills/develop-pyrevit-extensions/references/checklists_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/checklists_overview.md)
- Prompt snippets: [`CodexWorkspace/skills/develop-pyrevit-extensions/assets/prompts/`](CodexWorkspace/skills/develop-pyrevit-extensions/assets/prompts/)
- Script templates/harnesses: [`CodexWorkspace/skills/develop-pyrevit-extensions/scripts/`](CodexWorkspace/skills/develop-pyrevit-extensions/scripts/)
- Planning templates: [`CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/`](CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/)
- Planning workspace (project-specific): [`CodexWorkspace/workspace/`](CodexWorkspace/workspace/)

## How To Use [`CodexWorkspace`](CodexWorkspace/)
1. **Before coding**: open the relevant doc(s) from [`CodexWorkspace/skills/develop-pyrevit-extensions/references/`](CodexWorkspace/skills/develop-pyrevit-extensions/references/) and the matching versioned skill (e.g., [`CodexWorkspace/skills/pyrevit-revit-2023/`](CodexWorkspace/skills/pyrevit-revit-2023/), [`CodexWorkspace/skills/pyrevit-revit-2024/`](CodexWorkspace/skills/pyrevit-revit-2024/), [`CodexWorkspace/skills/pyrevit-revit-2025/`](CodexWorkspace/skills/pyrevit-revit-2025/)).
2. **When planning**: copy templates from [`CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/`](CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/) into [`CodexWorkspace/workspace/`](CodexWorkspace/workspace/) and edit only the workspace copies.
3. **When creating a new pyRevit command**: start from [`CodexWorkspace/skills/develop-pyrevit-extensions/scripts/new_command_template.py`](CodexWorkspace/skills/develop-pyrevit-extensions/scripts/new_command_template.py) and adapt it to the target tool folder.
4. **When reviewing or debugging**: use the checklists in [`CodexWorkspace/skills/develop-pyrevit-extensions/references/checklists_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/checklists_overview.md) and the prompt snippets in [`CodexWorkspace/skills/develop-pyrevit-extensions/assets/prompts/`](CodexWorkspace/skills/develop-pyrevit-extensions/assets/prompts/) to standardize analysis and outcomes.
5. **When unsure about patterns**: prefer the matching versioned Revit skill (e.g., [`CodexWorkspace/skills/pyrevit-revit-2023/`](CodexWorkspace/skills/pyrevit-revit-2023/), [`CodexWorkspace/skills/pyrevit-revit-2024/`](CodexWorkspace/skills/pyrevit-revit-2024/), [`CodexWorkspace/skills/pyrevit-revit-2025/`](CodexWorkspace/skills/pyrevit-revit-2025/)) over ad-hoc API usage.

## Repo Layout Notes (pyRevit Extensions)
- Commands typically live under a pushbutton folder (example: [`ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)).
- Keep transactions explicit (`Start/Commit`, `RollBack` on exceptions).
- Convert Python iterables to .NET collections at Revit API boundaries when required (e.g., `List[ElementId]`).

## Git Workflow
- **Branch naming**: use `<prefix>/<short-topic>` (e.g., `docs/codexworkspace-nav`, `fix/copy-level-remap`).
- **Prefix guide**: `agent/` setup, `docs/` documentation-only, `feat/` new behavior, `fix/` bug fix, `refactor/` structure-only, `test/` tests only, `chore/` maintenance.
- **Commits**: keep commits small + scoped; prefer one logical change per commit; message format `type: summary` (e.g., `docs: add dev workflow guide`).
- **Hygiene**: run `git status -sb` before/after changes; avoid mixing unrelated edits; avoid destructive commands (e.g., `git reset --hard`) unless explicitly requested.
- **Naming**: use `snake_case` for reusable modules; for standalone helper scripts prefer lower-kebab where practical (pyRevit command entrypoints stay as `script.py`).
- **Docs**: prefer lower `snake_case.md` filenames (exceptions: [`README.md`](README.md), [`AGENTS.md`](AGENTS.md)); when moving docs, prefer `git mv` + updating references over file-based "Moved to ..." stubs.

Return back: [`README.md`](README.md)
Return to root: [`README.md`](README.md)
