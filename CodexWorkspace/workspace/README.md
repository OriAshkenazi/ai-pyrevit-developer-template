# Workspace (Planning Artifacts)

This folder holds project-specific planning artifacts that change per project. Plans are treated as product docs and technical notes during implementation.

Static guidance lives in [`../docs/agent/`](../docs/agent/) and [`../docs/human/`](../docs/human/). Agent-only assets include [`../docs/agent/checklists/`](../docs/agent/checklists/), [`../docs/agent/templates/`](../docs/agent/templates/), [`../docs/agent/scripts/`](../docs/agent/scripts/), and [`../docs/agent/pyrevit/revit_version_documentation/`](../docs/agent/pyrevit/revit_version_documentation/).

## How To Use
1. Copy [`../docs/agent/templates/plan_template.md`](../docs/agent/templates/plan_template.md) to [`plans/`](plans/) and name it `<feature>_plan.md`.
2. Include product goals, inputs, outputs, constraints, and technical notes in the plan.
3. Use gpt-5.2 with [`../prompts/planning_phase_prompt.txt`](../prompts/planning_phase_prompt.txt) to generate [`development.md`](development.md).
4. Use gpt-5.2 with [`../prompts/seed_code_tasks_prompt.txt`](../prompts/seed_code_tasks_prompt.txt) to produce task batches.
5. Store task batches under [`tasks/`](tasks/) and reviews under [`reviews/`](reviews/).
6. Keep [`backlog.md`](backlog.md) updated using the backlog prompt.

## Files And Folders
- [`plans/`](plans/): product docs and technical notes (input to gpt-5.2).
- [`development.md`](development.md): canonical architecture and milestones for this project.
- [`backlog.md`](backlog.md): non-urgent work captured for later.
- [`tasks/`](tasks/): Code-Task batches (implementation tasks).
- [`reviews/`](reviews/): Ask-Task outputs and gap analysis.

Return back: [`../docs/README.md`](../docs/README.md)
Return to root: [`../../README.md`](../../README.md)
