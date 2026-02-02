# Workspace (Planning Artifacts)

This folder holds project-specific planning artifacts that change per project. Plans are treated as product docs and technical notes during implementation.

Static guidance lives in [`../skills/develop-pyrevit-extensions/references/`](../skills/develop-pyrevit-extensions/references/) with versioned Revit skills under [`../skills/`](../skills/) (e.g., `pyrevit-revit-2023`, `pyrevit-revit-2024`, `pyrevit-revit-2025`). Agent-only assets include [`../skills/develop-pyrevit-extensions/references/checklists_overview.md`](../skills/develop-pyrevit-extensions/references/checklists_overview.md), [`../skills/develop-pyrevit-extensions/assets/templates/`](../skills/develop-pyrevit-extensions/assets/templates/), and [`../skills/develop-pyrevit-extensions/scripts/`](../skills/develop-pyrevit-extensions/scripts/).

## How To Use
1. Copy [`../skills/develop-pyrevit-extensions/assets/templates/plan_template.md`](../skills/develop-pyrevit-extensions/assets/templates/plan_template.md) to [`plans/`](plans/) and name it `<feature>_plan.md`.
2. Include product goals, inputs, outputs, constraints, and technical notes in the plan.
3. Use gpt-5.2 with [`../skills/develop-pyrevit-extensions/assets/prompts/planning_phase_prompt.txt`](../skills/develop-pyrevit-extensions/assets/prompts/planning_phase_prompt.txt) to generate [`development.md`](development.md).
4. Use gpt-5.2 with [`../skills/develop-pyrevit-extensions/assets/prompts/seed_code_tasks_prompt.txt`](../skills/develop-pyrevit-extensions/assets/prompts/seed_code_tasks_prompt.txt) to produce task batches.
5. Store task batches under [`tasks/`](tasks/) and reviews under [`reviews/`](reviews/).
6. Keep [`backlog.md`](backlog.md) updated using the backlog prompt.

## Files And Folders
- [`plans/`](plans/): product docs and technical notes (input to gpt-5.2).
- [`development.md`](development.md): canonical architecture and milestones for this project.
- [`backlog.md`](backlog.md): non-urgent work captured for later.
- [`tasks/`](tasks/): Code-Task batches (implementation tasks).
- [`reviews/`](reviews/): Ask-Task outputs and gap analysis.

Return back: [`../skills/develop-pyrevit-extensions/references/docs_overview.md`](../skills/develop-pyrevit-extensions/references/docs_overview.md)
Return to root: [`../../README.md`](../../README.md)
