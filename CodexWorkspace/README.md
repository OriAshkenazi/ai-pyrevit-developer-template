# Codex Workspace

This workspace is a curated knowledge base for pyRevit development with gpt-5.2 (planning/review) and gpt-5.2-codex (implementation).

## Start Here
- Use [`CodexWorkspace/docs/human/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/human/README.md) for setup, Hello World validation, and plan handoff (single usage guide).
- Use [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md) for agent workflow, checklists, and pyRevit references.
- Use [`CodexWorkspace/workspace/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/README.md) for project-specific planning artifacts.

## Directory Tour
- [`docs`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md) - navigation for static docs (human + agent).
- [`docs/agent`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent) - agent-only guidance (workflow, prompting, pyRevit guides, checklists, templates).
- [`docs/human`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/human) - setup and troubleshooting.
- [`workspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace) - plans, development.md, tasks, reviews, backlog.
- [`prompts`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/prompts) - prompt snippets for gpt-5.2 and gpt-5.2-codex.
- [`scripts`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/scripts) - pyRevit-ready templates and harnesses.

## Notes
- Target Autodesk Revit 2023 APIs and avoid legacy `Document.New*` patterns.
- Keep transactions explicit (`Transaction.Start()` / `Commit()`), and roll back inside `except` blocks.
- Use [`docs/agent/pyrevit/revit_version_documentation/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/pyrevit/revit_version_documentation) for version-specific guidance.

Return back: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
