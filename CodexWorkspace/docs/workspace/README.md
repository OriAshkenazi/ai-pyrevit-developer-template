# Workspace (Planning Artifacts)

This folder holds user- or gpt-5.2-generated planning artifacts that change per project.
Static guidance lives in `CodexWorkspace/docs/guides/`, `reference/`, `checklists/`, and `templates/`.

## How To Use
1. Copy `../templates/plan_template.md` to `plans/<feature>_plan.md` and fill it in.
2. Use gpt-5.2 with `CodexWorkspace/prompts/planning_phase_prompt.txt` to generate `CodexWorkspace/docs/workspace/development.md`.
3. Use gpt-5.2 with `CodexWorkspace/prompts/seed_code_tasks_prompt.txt` to produce task batches.
4. Store task batches under `tasks/` and reviews under `reviews/`.
5. Keep `CodexWorkspace/docs/workspace/backlog.md` updated using the backlog prompt.

## Files And Folders
- `plans/`: plain-language plans (input to gpt-5.2).
- `development.md`: canonical architecture and milestones for this project.
- `backlog.md`: non-urgent work captured for later.
- `tasks/`: Code-Task batches (implementation tasks).
- `reviews/`: Ask-Task outputs and gap analysis.
