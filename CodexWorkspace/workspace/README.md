# Workspace (Planning Artifacts)

This folder holds project-specific planning artifacts that change per project. Plans are treated as product docs and technical notes during implementation.

Static guidance lives in [`CodexWorkspace/docs/agent/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent) and [`CodexWorkspace/docs/human/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/human). Agent-only assets include [`CodexWorkspace/docs/agent/checklists/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/checklists), [`CodexWorkspace/docs/agent/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/templates), [`CodexWorkspace/docs/agent/scripts/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/scripts), and [`CodexWorkspace/docs/agent/pyrevit/revit_version_documentation/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/agent/pyrevit/revit_version_documentation).

## How To Use
1. Copy [`CodexWorkspace/docs/agent/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/plan_template.md) to [`plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/plans) and name it `<feature>_plan.md`.
2. Include product goals, inputs, outputs, constraints, and technical notes in the plan.
3. Use gpt-5.2 with [`CodexWorkspace/prompts/planning_phase_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/planning_phase_prompt.txt) to generate [`CodexWorkspace/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/development.md).
4. Use gpt-5.2 with [`CodexWorkspace/prompts/seed_code_tasks_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/seed_code_tasks_prompt.txt) to produce task batches.
5. Store task batches under [`tasks/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/tasks) and reviews under [`reviews/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/reviews).
6. Keep [`CodexWorkspace/workspace/backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/backlog.md) updated using the backlog prompt.

## Files And Folders
- [`plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/plans): product docs and technical notes (input to gpt-5.2).
- [`development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/development.md): canonical architecture and milestones for this project.
- [`backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/backlog.md): non-urgent work captured for later.
- [`tasks/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/tasks): Code-Task batches (implementation tasks).
- [`reviews/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/reviews): Ask-Task outputs and gap analysis.

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
