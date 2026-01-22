# Codex Workspace

This workspace is a curated knowledge base for pyRevit development (docs, prompts, and planning artifacts).

## Start Here
- Setup + first button walkthrough (no coding): [`docs/human/README.md`](docs/human/README.md).
- Agent workflow, checklists, and references (advanced): [`docs/agent/README.md`](docs/agent/README.md).
- Project planning artifacts: [`workspace/README.md`](workspace/README.md).

## Directory Tour
- [`docs`](docs/README.md) - navigation for static docs (human + agent).
- [`docs/human`](docs/human) - setup and troubleshooting.
- [`docs/agent`](docs/agent) - agent-only guidance (workflow, prompting, pyRevit guides, checklists, templates).
- [`workspace`](workspace) - plans, development.md, tasks, reviews, backlog.
- [`prompts`](prompts) - prompt snippets for gpt-5.2 and gpt-5.2-codex.
- [`docs/agent/scripts`](docs/agent/scripts) - pyRevit-ready templates and harnesses.

## Notes
- Current docs and templates are aligned with Autodesk Revit 2023 APIs; adjust as needed for other versions and avoid legacy `Document.New*` patterns.
- Keep transactions explicit (`Transaction.Start()` / `Commit()`), and roll back inside `except` blocks.
- Use [`docs/agent/pyrevit/revit_version_documentation/`](docs/agent/pyrevit/revit_version_documentation/) for version-specific guidance.

Return back: [`../README.md`](../README.md)
Return to root: [`../README.md`](../README.md)
