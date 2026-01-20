# Testing Strategy Quick Reference

- [ ] **Unit-like checks**: exercise pure-Python utilities or data transforms that do not touch the Revit API.
- [ ] **Integration runs**: validate behavior on a small seed model with known expectations; confirm clean document state.
- [ ] **Performance sampling**: capture timings on representative projects; compare to agreed budgets.
- [ ] **User validation**: confirm workflows with real-world users; ensure prompts, dialogs, and error messages are clear.
- [ ] **Edge cases**: cover empty selections, read-only documents, linked elements, and missing parameters.

