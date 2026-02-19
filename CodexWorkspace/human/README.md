# Human Guides (Tier Selector)

Use this page to choose the workflow depth that matches your experience and risk tolerance.

## Beginner Tier (Default)
- Guide: [`beginner_quickstart.md`](beginner_quickstart.md)
- Characteristics:
  - No hooks required.
  - Minimal setup to load and run the template.
  - Focus on out-of-box validation and simple planning flow.
  - Includes a copy/paste seed prompt template for starting an agent run.

## Advanced Tier (Opt-In)
- Guide: [`advanced_workflow.md`](advanced_workflow.md)
- Characteristics:
  - Optional local hooks and stricter checks.
  - Additional planning artifacts (`prd.md`, `tech_spec.md`, `status.md`).
  - Stronger logging and AI/data safety controls.
  - Includes a copy/paste seed prompt template for starting an agent run.

## Seed Prompt Templates
- Beginner template: use `beginner_quickstart.md` section `Seed Prompt Template (Beginner)`.
- Advanced template: use `advanced_workflow.md` section `Seed Prompt Template (Advanced)`.
- Both templates:
  - Start with a plain-English feature description placeholder.
  - Force a planning/question phase before implementation.
  - Require autonomous git handling by the agent (branching, atomic commits, push/PR flow) without waiting for user input.

## Additional Guides
- Environment setup notes: [`environment_setup.md`](environment_setup.md)
- Troubleshooting: [`troubleshooting.md`](troubleshooting.md)

## Related Entry Points
- Root README: [`../../README.md`](../../README.md)
- Workspace overview: [`../workspace/README.md`](../workspace/README.md)
- Agent references: [`../skills/develop-pyrevit-extensions/references/agent_overview.md`](../skills/develop-pyrevit-extensions/references/agent_overview.md)
- Update log: [`../../CHANGELOG.md`](../../CHANGELOG.md)

Return back: [`../README.md`](../README.md)
Return to root: [`../../README.md`](../../README.md)
