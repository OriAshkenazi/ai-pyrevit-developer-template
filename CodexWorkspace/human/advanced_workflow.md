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
