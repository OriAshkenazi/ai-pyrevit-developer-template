# AI-Orchestrated Development Methodology (pyRevit)

This is the single canonical usage guide for this template. Use it to minimize cognitive load while building pyRevit extensions with a dual-model workflow.

## Model Roles
- gpt-5.2: planning, task generation, review, backlog, and next-feature analysis.
- gpt-5.2-codex: implementation of code changes and documentation updates.

## Static vs Workspace Files
- Static guidance lives in `CodexWorkspace/docs/guides/`, `reference/`, `checklists/`, and `templates/`.
- Project-specific planning artifacts live in `CodexWorkspace/docs/workspace/`.

## Core Artifacts
- `CodexWorkspace/docs/workspace/development.md`: canonical architecture, milestones, and constraints.
- Code-Tasks: implementation tasks for gpt-5.2-codex.
- Ask-Tasks: review/analysis tasks for gpt-5.2.
- `CodexWorkspace/docs/workspace/backlog.md`: non-urgent work captured for later.
- `CodexWorkspace/docs/workspace/plans/`: plain-language plans that seed the workflow.

## Quick Start
1. Copy `CodexWorkspace/docs/templates/plan_template.md` to `CodexWorkspace/docs/workspace/plans/<feature>_plan.md` and fill it in.
2. Run the Planning prompt with gpt-5.2 to create `CodexWorkspace/docs/workspace/development.md`.
3. Run the Seed Code-Tasks prompt with gpt-5.2 to generate the first task batch.
4. Execute each Code-Task with gpt-5.2-codex (code and docs in the same task).
5. Run the Review Ask-Task prompt with gpt-5.2 after the batch merges.
6. Use Iteration prompts if gaps or conflicts appear.
7. Capture non-urgent tasks using the Backlog prompt into `CodexWorkspace/docs/workspace/backlog.md`.
8. Run the Next Feature prompt when the current feature is complete.

## Phase Map
| Phase | Trigger | Model | Prompt File | Expected Output |
| --- | --- | --- | --- | --- |
| Planning | New repo or new feature | gpt-5.2 | `CodexWorkspace/prompts/planning_phase_prompt.txt` | `CodexWorkspace/docs/workspace/development.md` |
| Seeding | Plan accepted | Manual | (none) | Repo structure seeded |
| First Step Implementation | Start first feature | gpt-5.2 | `CodexWorkspace/prompts/seed_code_tasks_prompt.txt` | Code-Tasks batch |
| Review | Task batch merged | gpt-5.2 | `CodexWorkspace/prompts/review_ask_task_prompt.txt` | Gap report + remediation |
| Iteration I | In-flight conflicts | gpt-5.2 | `CodexWorkspace/prompts/iteration_task_adjust_prompt.txt` | Adjusted tasks |
| Iteration II | Post-batch gaps | gpt-5.2 | `CodexWorkspace/prompts/iteration_summary_tasks_prompt.txt` | Additional Code-Tasks |
| Backlog | Non-urgent tasks found | gpt-5.2 | `CodexWorkspace/prompts/backlog_code_task_prompt.txt` | `CodexWorkspace/docs/workspace/backlog.md` updated |
| Next Feature | Roadmap advance | gpt-5.2 | `CodexWorkspace/prompts/next_feature_ask_task_prompt.txt` | Next feature recommendation |
| Implementation | Start next feature | gpt-5.2 | `CodexWorkspace/prompts/iteration_summary_tasks_prompt.txt` | New Code-Tasks batch |

## Code-Task Rules (Implementation)
- Scope limit: 3 hours max, roughly 100 LoC.
- Must include explicit file paths and responsibilities.
- Must include documentation updates as first-class requirements.
- Must include validation commands.
- Must follow Revit 2023 patterns (explicit transactions, .NET collections at API boundaries).

## Ask-Task Rules (Review)
- Technical findings only (no code generation).
- Include file and line references.
- Prioritize recommendations by severity.
- Validate completeness against `CodexWorkspace/docs/workspace/development.md`.

## Prompt Library
All prompts are stored in `CodexWorkspace/prompts/`. Use the model indicated in each prompt file and keep the output format unchanged.

## Documentation Hygiene
- Update README and relevant docs in the same task that changes behavior.
- Keep docstrings current for new or edited functions.
- Keep `CodexWorkspace/docs/README.md` and `CodexWorkspace/prompts/README.md` up to date.

## Validation and Checklists
- Review work against `CodexWorkspace/docs/checklists/` before merging.
- Use Revit 2023 guidance in `CodexWorkspace/docs/reference/` for API decisions.

## Git Cadence (Short)
- Open a PR after the first Code-Task of a feature.
- Keep pushing follow-up tasks to the same PR.
- Do not merge until the Review Ask-Task passes and backlog items are captured.
