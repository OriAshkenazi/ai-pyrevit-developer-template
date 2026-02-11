# Workspace (Planning Artifacts)

This folder holds project-specific planning artifacts that change per project. Plans are treated as product docs and technical notes during implementation.

Static guidance lives in [`../skills/develop-pyrevit-extensions/references/`](../skills/develop-pyrevit-extensions/references/) with versioned Revit skills under [`../skills/`](../skills/) (e.g., `pyrevit-revit-2023`, `pyrevit-revit-2024`, `pyrevit-revit-2025`). Agent-only assets include [`../skills/develop-pyrevit-extensions/references/checklists_overview.md`](../skills/develop-pyrevit-extensions/references/checklists_overview.md), [`../skills/develop-pyrevit-extensions/assets/templates/`](../skills/develop-pyrevit-extensions/assets/templates/), and [`../skills/develop-pyrevit-extensions/scripts/`](../skills/develop-pyrevit-extensions/scripts/).

## Beginner Workflow (Default)
1. Copy [`../skills/develop-pyrevit-extensions/assets/templates/plan_template.md`](../skills/develop-pyrevit-extensions/assets/templates/plan_template.md) to [`plans/`](plans/) and name it `<feature>_plan.md`.
2. Include product goals, inputs, outputs, constraints, and technical notes in the plan.
3. Use gpt-5.2 with [`../skills/develop-pyrevit-extensions/assets/prompts/planning_phase_prompt.txt`](../skills/develop-pyrevit-extensions/assets/prompts/planning_phase_prompt.txt) to generate [`development.md`](development.md).
4. Use gpt-5.2 with [`../skills/develop-pyrevit-extensions/assets/prompts/seed_code_tasks_prompt.txt`](../skills/develop-pyrevit-extensions/assets/prompts/seed_code_tasks_prompt.txt) to produce task batches.
5. Store task batches under [`tasks/`](tasks/) and reviews under [`reviews/`](reviews/).
6. Keep [`backlog.md`](backlog.md) updated using the backlog prompt.

## Advanced Workflow Overlay (Opt-In)
In advanced mode, maintain these additional artifacts:
- [`prd.md`](prd.md)
- [`tech_spec.md`](tech_spec.md)
- [`status.md`](status.md)

`status.md` is required to include:
- `Scope`, `Folder Map`, `Completed`, `In Progress`, `Pending`, `Known Bugs`, `Open Risks`, `Next Actions`, `Last Updated`.

For mode-specific usage, see:
- [`../human/beginner_quickstart.md`](../human/beginner_quickstart.md)
- [`../human/advanced_workflow.md`](../human/advanced_workflow.md)
- [`../../CHANGELOG.md`](../../CHANGELOG.md)

## Files And Folders
- [`plans/`](plans/): product docs and technical notes (input to gpt-5.2).
- [`development.md`](development.md): canonical architecture and milestones for this project.
- [`backlog.md`](backlog.md): non-urgent work captured for later.
- [`tasks/`](tasks/): Code-Task batches (implementation tasks).
- [`reviews/`](reviews/): Ask-Task outputs and gap analysis.
- [`prd.md`](prd.md): advanced product requirement document (optional in beginner mode).
- [`tech_spec.md`](tech_spec.md): advanced technical specification (optional in beginner mode).
- [`status.md`](status.md): advanced status tracker with required schema (optional in beginner mode).

Return back: [`../skills/develop-pyrevit-extensions/references/docs_overview.md`](../skills/develop-pyrevit-extensions/references/docs_overview.md)
Return to root: [`../../README.md`](../../README.md)
