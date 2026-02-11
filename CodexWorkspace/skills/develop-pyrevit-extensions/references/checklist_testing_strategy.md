# Testing Strategy Quick Reference

## New User Walkthrough (Template)
- [ ] Clone the repo and open `README.md`.
- [ ] Add `ai-pyrevit-developer-template.extension` in pyRevit Settings > Extensions > Add.
- [ ] Restart/Re-load Revit and confirm the extension loads.
- [ ] Click HelloWorld and verify output behavior.

## Beginner Validation
- [ ] Unit-like checks for pure Python helpers where applicable.
- [ ] Integration run on safe sample model.
- [ ] Edge cases: empty selection, read-only state, missing parameters.
- [ ] Basic logging captured (outcome + error context) when failures occur.

## Advanced Validation
- [ ] `status.md` schema remains complete after meaningful updates.
- [ ] Advanced logs are persisted under `tmp/logs/`.
- [ ] Hook setup/disable scripts are verified.
- [ ] Template safeguard scripts pass locally.

## AI/Data Validation (Advanced)
- [ ] Dataset coverage percent is logged.
- [ ] Sampling/downsampling is explicitly stated.
- [ ] Numeric sanity checks are documented.
- [ ] Metric direction assumptions are stated and validated.

Return back: [`checklists_overview.md`](checklists_overview.md)
Return to root: [`README.md`](../../../../README.md)
