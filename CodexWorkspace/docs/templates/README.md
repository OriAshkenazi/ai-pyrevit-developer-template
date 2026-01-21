# Templates

Static templates used by the planning workflow. Copy these into [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) and edit there.

## Available Templates
- [`plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md) - plain-language plan input for gpt-5.2.
- [`development_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/development_template.md) - scaffold for the development plan output.
- [`backlog_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/backlog_template.md) - scaffold for the backlog.

## How To Use
1. Copy [`plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md) to [`CodexWorkspace/docs/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans) and name it `<feature>_plan.md`.
2. Use gpt-5.2 with [`CodexWorkspace/prompts/planning_phase_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/planning_phase_prompt.txt) to generate [`CodexWorkspace/docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md).
3. Use the backlog prompt to update [`CodexWorkspace/docs/workspace/backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/backlog.md).

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
