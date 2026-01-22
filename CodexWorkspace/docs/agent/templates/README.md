# Templates

Static templates used by the planning workflow. Copy these into [`../../workspace/`](../../workspace/) and edit only the workspace copies. Plans in [`../../workspace/plans/`](../../workspace/plans/) are treated as product docs and technical notes during implementation.

## Available Templates
- [`plan_template.md`](plan_template.md) - plain-language plan input for gpt-5.2.
- [`development_template.md`](development_template.md) - scaffold for the development plan output.
- [`backlog_template.md`](backlog_template.md) - scaffold for the backlog.

## How To Use
1. Copy [`plan_template.md`](plan_template.md) to [`../../workspace/plans/`](../../workspace/plans/) and name it `<feature>_plan.md` (include product context and technical notes).
2. Use gpt-5.2 with [`../../prompts/planning_phase_prompt.txt`](../../prompts/planning_phase_prompt.txt) to generate [`../../workspace/development.md`](../../workspace/development.md).
3. Use the backlog prompt to update [`../../workspace/backlog.md`](../../workspace/backlog.md).

Return back: [`../README.md`](../README.md)
Return to root: [`../../../../README.md`](../../../../README.md)
