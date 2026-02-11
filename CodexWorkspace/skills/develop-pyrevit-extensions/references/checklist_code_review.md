# Code Review Checklist (Revit + pyRevit)

- [ ] **Transactions**: explicit `Transaction` usage, narrow scope, rollback in `except`.
- [ ] **Error Handling**: validate inputs (elements, parameters, modifiability) before edits; emit helpful messages.
- [ ] **Performance**: minimize document scans, reuse collectors, and apply filters early.
- [ ] **Collections**: ensure .NET collections (`List[ElementId]`, etc.) are passed where the API expects them.
- [ ] **Memory**: drop temporary lists/dicts after use; avoid retaining Element references longer than needed.
- [ ] **UI/UX**: confirm no document edits outside transactions; add dialogs/progress feedback when work is lengthy.
- [ ] **Docs**: docstrings cover parameters, return types, exceptions, and usage within a transaction.
- [ ] **OOTB Scaffold**: confirm `ai-pyrevit-developer-template.extension` and HelloWorld script path are still present.

Advanced-only checks (AI/Data tasks):
- [ ] **Dataset Coverage**: report what percent of dataset was processed.
- [ ] **Sampling Disclosure**: if sampling/downsampling is used, it is explicit and justified.
- [ ] **No Silent Simplification**: verify no hidden downsampling/performance shortcuts were introduced.
- [ ] **Numeric Sanity**: key numbers are cross-checked and internally consistent.
- [ ] **Metric Direction**: state which metric direction is better/worse.

Return back: [`checklists_overview.md`](checklists_overview.md)
Return to root: [`README.md`](../../../../README.md)
