# Plan Template (Plain Language)

Copy this file to [`CodexWorkspace/workspace/plans/`](../../../../workspace/plans/) and name it `<feature>_plan.md`.

## Goal (One Sentence)
- Describe the outcome you want.

## Stakeholders Or Roles
- Example: "Project managers reviewing takeoff data."

## Inputs (What You Select)
- Example: "Rooms from the current view."

## Outputs (What You Expect)
- Example: "A schedule or updated parameters."

## Steps (Simple Actions)
1.
2.
3.

## Technical Notes
- Data sources, constraints, or API limitations that matter.

## Questions Or Unknowns
- Anything you are not sure about.

## Risks Or Limitations
- Example: "May not work in linked models."

## Tests (How You Will Check It)
- Example: "Run in a sample model and verify the output."

## Prompt For gpt-5.2 (Planning)
Use [`planning_phase_prompt.txt`](../prompts/planning_phase_prompt.txt) and provide this plan as input.

Save the output as [`CodexWorkspace/workspace/development.md`](../../../../workspace/development.md).

Return back: [`templates_overview.md`](../../references/templates_overview.md)
Return to root: [`README.md`](../../../../../README.md)
