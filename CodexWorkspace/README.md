# Codex Workspace

This workspace is a curated knowledge base so Codex sessions can start quickly on Revit 2023 automation tasks.

## Start Here (Beginner)
- Read [`docs/guides/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/README.md) for a step-by-step walkthrough.
- Read [`docs/guides/ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md) for the dual-model workflow.
- Verify the Hello World scaffold in [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab) to confirm pyRevit setup.
- Create a plan using [`docs/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md), then use the planning prompt to produce [`docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md).

## Quick Start
- Prefer the script engine already used by the command you are editing; avoid changing `#! python` / `#! python3` unless required.
- Target Autodesk Revit 2023 APIs and avoid legacy `Document.New*` patterns.
- Keep transactions explicit (`Transaction.Start()` / `Commit()`), and roll back inside `except` blocks.
- Convert Python iterables to .NET collections (`List[ElementId]`) at API boundaries.

## Directory Tour
- [`docs`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs) &mdash; documentation index (start at [`docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)).
- [`docs/checklists`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/checklists) &mdash; ready-to-use review and testing checklists.
- [`docs/templates`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/templates) &mdash; static templates for planning artifacts.
- [`docs/workspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) &mdash; project-specific plans, tasks, reviews, and backlog.
- [`prompts`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/prompts) &mdash; curated prompt snippets for generating, reviewing, and documenting code with Codex or GPT.
- [`scripts`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/scripts) &mdash; pyRevit-ready templates that follow the guidelines.

## Suggested Workflow
1. Read the relevant checklist before authoring or reviewing a tool.
2. Start from the script template in [`scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py).
3. Use the prompt snippets to guide Codex conversations about implementation or documentation.
4. Use the docs index ([`docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)) to jump to guides/reference quickly.

## References
- Primary source: [`docs/reference/revit_2023_development_guidelines_with_llm_integration.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/reference/revit_2023_development_guidelines_with_llm_integration.md).
- Autodesk Revit 2023 API docs (lookup specifics when prompted).

Return back: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
