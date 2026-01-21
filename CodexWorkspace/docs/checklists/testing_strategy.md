# Testing Strategy Quick Reference

## New User Walkthrough (Template)
- [ ] Clone the repo and open the README.
- [ ] Add the repo folder in pyRevit Settings > Extensions > Add.
- [ ] Restart Revit and confirm the extension loads.
- [ ] Create a plan using `CodexWorkspace/docs/templates/plan_template.md` and store it in `CodexWorkspace/docs/workspace/plans/`.
- [ ] Create a sample button using the template script and confirm it runs.

- [ ] **Unit-like checks**: exercise pure-Python utilities or data transforms that do not touch the Revit API.
- [ ] **Integration runs**: validate behavior on a small seed model with known expectations; confirm clean document state.
- [ ] **Performance sampling**: capture timings on representative projects; compare to agreed budgets.
- [ ] **User validation**: confirm workflows with real-world users; ensure prompts, dialogs, and error messages are clear.
- [ ] **Edge cases**: cover empty selections, read-only documents, linked elements, and missing parameters.
