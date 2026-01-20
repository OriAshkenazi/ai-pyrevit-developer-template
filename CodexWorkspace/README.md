# Codex Workspace

This workspace is a curated knowledge base so Codex sessions can start quickly on Revit 2023 automation tasks.

## Quick Start
- Prefer the script engine already used by the command you are editing; avoid changing `#! python` / `#! python3` unless required.
- Target Autodesk Revit 2023 APIs and avoid legacy `Document.New*` patterns.
- Keep transactions explicit (`Transaction.Start()` / `Commit()`), and roll back inside `except` blocks.
- Convert Python iterables to .NET collections (`List[ElementId]`) at API boundaries.

## Directory Tour
- `docs` &mdash; documentation index (start at `docs/README.md`).
- `docs/checklists` &mdash; ready-to-use review and testing checklists.
- `prompts` &mdash; curated prompt snippets for generating, reviewing, and documenting code with Codex or GPT.
- `scripts` &mdash; pyRevit-ready templates that follow the guidelines.

## Suggested Workflow
1. Read the relevant checklist before authoring or reviewing a tool.
2. Start from the script template in `scripts/new_command_template.py`.
3. Use the prompt snippets to guide Codex conversations about implementation or documentation.
4. Use the docs index (`docs/README.md`) to jump to guides/reference quickly.

## References
- Primary source: `docs/reference/revit_2023_development_guidelines_with_llm_integration.md`.
- Autodesk Revit 2023 API docs (lookup specifics when prompted).
