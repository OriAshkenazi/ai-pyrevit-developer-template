# Beginner Quickstart (No Hooks Required)

This workflow is for first-time users. It keeps setup minimal and avoids local hook automation.

## Goals
- Load the template extension in Revit.
- Run the out-of-box HelloWorld button successfully.
- Start a basic plan-to-tasks workflow using existing workspace artifacts.

## Steps
1. Install pyRevit:
   - [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)
2. Clone or download this repository.
3. In Revit, open `pyRevit -> Settings -> Extensions -> Add`.
4. Select:
   - `ai-pyrevit-developer-template.extension`
5. Reload pyRevit (or restart Revit).
6. Click the HelloWorld button:
   - Path: [`../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)

## Beginner Planning Flow
1. Create a plan in:
   - `CodexWorkspace/workspace/plans/<feature>_plan.md`
2. Generate/update:
   - `CodexWorkspace/workspace/development.md`
3. Track tasks in:
   - `CodexWorkspace/workspace/tasks/`
4. Track reviews in:
   - `CodexWorkspace/workspace/reviews/`
5. Track non-urgent items in:
   - `CodexWorkspace/workspace/backlog.md`

## Not Required In Beginner Mode
- Enabling `.githooks/`
- Advanced artifact layer (`prd.md`, `tech_spec.md`, `status.md`)
- Advanced status enforcement scripts

## When To Move To Advanced
- You want stricter local quality gates.
- You need persistent status tracking for frequent multi-step changes.
- You are working with high-risk AI/data tasks and need stronger controls.

Next: [`advanced_workflow.md`](advanced_workflow.md)

Return back: [`README.md`](README.md)
Return to root: [`../../README.md`](../../README.md)
