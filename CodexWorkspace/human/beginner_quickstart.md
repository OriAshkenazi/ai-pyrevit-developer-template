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

## Seed Prompt Template (Beginner)
Use this as the first message to the agent. Replace placeholders before sending.

Placeholder definitions:
- `<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>`:
  - A plain-language description of what you want built.
  - Include: user goal, expected behavior, key inputs/outputs, and constraints.
  - Example: `Create a pyRevit button that selects all walls in the active view and shows a summary dialog with count and type breakdown.`
- `<FEATURE_SLUG>`:
  - A short kebab-case identifier used for workspace filenames.
  - Use lowercase letters, numbers, and hyphens only.
  - Example: `select-walls-summary`

```text
Use the Beginner workflow for this repository.

Plain-English feature request:
<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>

Feature slug:
<FEATURE_SLUG>

Start in planning mode first:
1. Restate the request as implementation scope, assumptions, non-goals, and acceptance criteria.
2. Ask me focused clarification questions.
3. Do not implement code until I answer the questions.

After clarifications, use the Beginner workspace flow:
- CodexWorkspace/workspace/plans/<FEATURE_SLUG>_plan.md
- CodexWorkspace/workspace/development.md
- CodexWorkspace/workspace/tasks/<FEATURE_SLUG>_tasks.md
- CodexWorkspace/workspace/reviews/<FEATURE_SLUG>_review.md
- CodexWorkspace/workspace/backlog.md (if needed)

Then implement a fully working pyRevit button:
- ai-pyrevit-developer-template.extension/<Tab>.tab/<Panel>.panel/<Command>.pushbutton/script.py
- ai-pyrevit-developer-template.extension/<Tab>.tab/<Panel>.panel/<Command>.pushbutton/icon.png (if needed)

Constraints:
- Preserve:
  - ai-pyrevit-developer-template.extension/
  - ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py
- Keep temporary outputs under tmp/ and persisted logs under tmp/logs/.
- In Beginner mode, do not require:
  - CodexWorkspace/workspace/prd.md
  - CodexWorkspace/workspace/tech_spec.md
  - CodexWorkspace/workspace/status.md

Git handling is the agent's responsibility:
1. Create and manage branches without asking me.
2. Make atomic, single-purpose commits throughout the work.
3. Do not pause to ask for git-operation approval.
4. Keep work reversible via clean commit history (small, scoped commits).
5. Push progress when meaningful milestones are complete.
6. At completion, provide branch name, commit list, and PR link/status.
7. Do not wait for user input for git flow decisions. Execute branching, committing, pushing, and PR lifecycle autonomously.

Finish with:
- validation results
- changed files
- open risks
- next actions
```

### How To Use This Template
1. Copy the template into your first message to the agent.
2. Write `<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>` with concrete behavior and constraints.
3. Choose `<FEATURE_SLUG>` in kebab-case (for example: `select-walls-summary`).
4. Answer planning questions first; implementation starts after clarifications.

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
