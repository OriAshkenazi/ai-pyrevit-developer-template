# Templates

Static templates used by the planning workflow. Copy these into [`CodexWorkspace/workspace/`](../../../workspace/) and edit only the workspace copies. Plans in [`CodexWorkspace/workspace/plans/`](../../../workspace/plans/) are treated as product docs and technical notes during implementation.

## Available Templates
- [`plan_template.md`](../assets/templates/plan_template.md) - plain-language plan input for gpt-5.2.
- [`development_template.md`](../assets/templates/development_template.md) - scaffold for the development plan output.
- [`backlog_template.md`](../assets/templates/backlog_template.md) - scaffold for the backlog.
- [`prd_template.md`](../assets/templates/prd_template.md) - advanced product requirements template.
- [`tech_spec_template.md`](../assets/templates/tech_spec_template.md) - advanced technical specification template.
- [`status_template.md`](../assets/templates/status_template.md) - advanced status tracking template with required schema.

## How To Use
1. Copy [`plan_template.md`](../assets/templates/plan_template.md) to [`CodexWorkspace/workspace/plans/`](../../../workspace/plans/) and name it `<feature>_plan.md` (include product context and technical notes).
2. Use gpt-5.2 with [`planning_phase_prompt.txt`](../assets/prompts/planning_phase_prompt.txt) to generate [`CodexWorkspace/workspace/development.md`](../../../workspace/development.md).
3. Use the backlog prompt to update [`CodexWorkspace/workspace/backlog.md`](../../../workspace/backlog.md).
4. Advanced mode only: copy advanced overlays to:
   - [`CodexWorkspace/workspace/prd.md`](../../../workspace/prd.md)
   - [`CodexWorkspace/workspace/tech_spec.md`](../../../workspace/tech_spec.md)
   - [`CodexWorkspace/workspace/status.md`](../../../workspace/status.md)

Return back: [`docs_overview.md`](docs_overview.md)
Return to root: [`README.md`](../../../../README.md)
