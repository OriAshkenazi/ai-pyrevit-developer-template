# Workspace (Planning Artifacts)

This folder holds user- or gpt-5.2-generated planning artifacts that change per project.
Static guidance lives in [`CodexWorkspace/docs/guides/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/guides), [`CodexWorkspace/docs/reference/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/reference), [`CodexWorkspace/docs/checklists/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/checklists), and [`CodexWorkspace/docs/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/templates).

## How To Use
1. Copy [`../templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md) to [`plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans) and name it `<feature>_plan.md`.
2. Use gpt-5.2 with [`CodexWorkspace/prompts/planning_phase_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/planning_phase_prompt.txt) to generate [`CodexWorkspace/docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md).
3. Use gpt-5.2 with [`CodexWorkspace/prompts/seed_code_tasks_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/seed_code_tasks_prompt.txt) to produce task batches.
4. Store task batches under [`tasks/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/tasks) and reviews under [`reviews/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/reviews).
5. Keep [`CodexWorkspace/docs/workspace/backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/backlog.md) updated using the backlog prompt.

## Files And Folders
- [`plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans): plain-language plans (input to gpt-5.2).
- [`development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md): canonical architecture and milestones for this project.
- [`backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/backlog.md): non-urgent work captured for later.
- [`tasks/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/tasks): Code-Task batches (implementation tasks).
- [`reviews/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/reviews): Ask-Task outputs and gap analysis.

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
