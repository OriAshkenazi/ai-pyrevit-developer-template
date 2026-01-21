# Code Review Checklist (Revit 2023 + pyRevit)

- [ ] **Transactions**: explicit `Transaction` usage, narrow scope, rollback in `except`.
- [ ] **Error Handling**: validate inputs (elements, parameters, modifiability) before edits; emit helpful messages.
- [ ] **Performance**: minimize document scans, reuse collectors, and apply filters early.
- [ ] **Collections**: ensure .NET collections (`List[ElementId]`, etc.) are passed where the API expects them.
- [ ] **Memory**: drop temporary lists/dicts after use; avoid retaining Element references longer than needed.
- [ ] **UI/UX**: confirm no document edits outside transactions; add dialogs/progress feedback when work is lengthy.
- [ ] **Docs**: docstrings cover parameters, return types, exceptions, and usage within a transaction.

Return back: [`CodexWorkspace/docs/agent/checklists/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/checklists/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
