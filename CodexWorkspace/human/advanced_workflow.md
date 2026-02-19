# Advanced Workflow (Opt-In Hooks and Strict Controls)

This workflow adds stricter checks and additional planning artifacts. It is optional and should not block beginner onboarding.

## Advanced Scope
- Keep template-first behavior.
- Enforce stronger local quality gates after explicit setup.
- Use richer planning/status artifacts for multi-step work.

## Enable Advanced Hooks (Opt-In)
Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools/setup_advanced_hooks.ps1
```

Disable advanced hooks:

```powershell
powershell -ExecutionPolicy Bypass -File tools/disable_advanced_hooks.ps1
```

## Advanced Artifact Layer
Maintain these files in addition to baseline workflow files:
- [`../workspace/prd.md`](../workspace/prd.md)
- [`../workspace/tech_spec.md`](../workspace/tech_spec.md)
- [`../workspace/status.md`](../workspace/status.md)

`status.md` required sections:
- `Scope`
- `Folder Map`
- `Completed`
- `In Progress`
- `Pending`
- `Known Bugs`
- `Open Risks`
- `Next Actions`
- `Last Updated`

Update `status.md` after each meaningful code/workflow change in advanced mode.

## Seed Prompt Template (Advanced)
Use this as the first message to the agent. Replace placeholders before sending.

Placeholder definitions:
- `<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>`:
  - A plain-language description of what you want built.
  - Include: user goal, expected behavior, key inputs/outputs, constraints, and quality expectations.
  - Example: `Create a pyRevit button that checks selected rooms for missing required parameters, writes a detailed log, and presents a pass/fail summary with next actions.`
- `<FEATURE_SLUG>`:
  - A short kebab-case identifier used for workspace filenames.
  - Use lowercase letters, numbers, and hyphens only.
  - Example: `room-parameter-audit`

```text
Use the Advanced workflow for this repository.

Plain-English feature request:
<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>

Feature slug:
<FEATURE_SLUG>

Start in planning mode first:
1. Restate the request as implementation scope, assumptions, non-goals, and acceptance criteria.
2. Ask me focused clarification questions.
3. Do not implement code until I answer the questions.

After clarifications, use the full Advanced artifact flow:
- CodexWorkspace/workspace/prd.md
- CodexWorkspace/workspace/tech_spec.md
- CodexWorkspace/workspace/status.md
- CodexWorkspace/workspace/plans/<FEATURE_SLUG>_plan.md
- CodexWorkspace/workspace/development.md
- CodexWorkspace/workspace/tasks/<FEATURE_SLUG>_tasks.md
- CodexWorkspace/workspace/reviews/<FEATURE_SLUG>_review.md
- CodexWorkspace/workspace/backlog.md (if needed)

Update CodexWorkspace/workspace/status.md after each meaningful change with:
- Scope
- Folder Map
- Completed
- In Progress
- Pending
- Known Bugs
- Open Risks
- Next Actions
- Last Updated

Then implement a fully working pyRevit button:
- ai-pyrevit-developer-template.extension/<Tab>.tab/<Panel>.panel/<Command>.pushbutton/script.py
- ai-pyrevit-developer-template.extension/<Tab>.tab/<Panel>.panel/<Command>.pushbutton/icon.png (if needed)

Constraints:
- Preserve:
  - ai-pyrevit-developer-template.extension/
  - ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py
- Keep temporary outputs under tmp/ and persisted logs under tmp/logs/.
- Apply advanced review/testing rigor before completion.

Git handling is the agent's responsibility:
1. Create and manage branches without asking me.
2. Make atomic, single-purpose commits throughout the work.
3. Do not pause to ask for git-operation approval.
4. Keep work reversible via clean commit history (small, scoped commits).
5. Push progress when meaningful milestones are complete.
6. At completion, provide branch name, commit list, and PR link/status.
7. Do not wait for user input for git flow decisions. Execute branching, committing, pushing, and PR lifecycle autonomously.

Finish with:
- validation results
- changed files
- open risks
- next actions
```

### How To Use This Template
1. Copy the template into your first message to the agent.
2. Write `<FEATURE_DESCRIPTION_IN_PLAIN_ENGLISH>` with concrete behavior, constraints, and quality expectations.
3. Choose `<FEATURE_SLUG>` in kebab-case (for example: `room-parameter-audit`).
4. Answer planning questions first; implementation starts after clarifications.

## Temporary Files and Logs
- Store scratch/test artifacts only under `tmp/`.
- Store persisted logs under `tmp/logs/`.
- Logging standard reference:
  - [`../skills/develop-pyrevit-extensions/references/logging_and_debugging.md`](../skills/develop-pyrevit-extensions/references/logging_and_debugging.md)

## AI/Data Safety (Advanced)
For AI/data-heavy tasks, require explicit evidence for:
- Dataset coverage (what percent of data was processed).
- Sampling disclosure (if any sampling is used, explain why).
- No silent downsampling.
- Numeric sanity checks before conclusions.
- Metric direction validation (state what better/worse means).

Review checklist:
- [`../skills/develop-pyrevit-extensions/references/checklist_code_review.md`](../skills/develop-pyrevit-extensions/references/checklist_code_review.md)

Testing checklist:
- [`../skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md`](../skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md)

## Template Asset Protection
Do not remove:
- `ai-pyrevit-developer-template.extension/`
- `ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`

Validation script:

```powershell
powershell -ExecutionPolicy Bypass -File tools/check_example_scaffold.ps1
```

Return back: [`README.md`](README.md)
Return to root: [`../../README.md`](../../README.md)
