# Templates

Static templates used by the planning workflow. Copy these into [`CodexWorkspace/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace) and edit only the workspace copies. Plans in [`CodexWorkspace/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/plans) are treated as product docs and technical notes during implementation.

## Available Templates
- [`plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/plan_template.md) - plain-language plan input for gpt-5.2.
- [`development_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/development_template.md) - scaffold for the development plan output.
- [`backlog_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/backlog_template.md) - scaffold for the backlog.

## How To Use
1. Copy [`plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/plan_template.md) to [`CodexWorkspace/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/plans) and name it `<feature>_plan.md` (include product context and technical notes).
2. Use gpt-5.2 with [`CodexWorkspace/prompts/planning_phase_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/planning_phase_prompt.txt) to generate [`CodexWorkspace/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/development.md).
3. Use the backlog prompt to update [`CodexWorkspace/workspace/backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/backlog.md).

Return back: [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
