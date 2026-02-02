# Git Hygiene Checklist

- [ ] **Branch name** follows `<prefix>/<short-topic>` (e.g., `docs/...`, `fix/...`).
- [ ] **Scope** is single-purpose; unrelated changes are split into separate commits.
- [ ] **Status** checked before/after work (`git status -sb`).
- [ ] **No generated artifacts** are committed (e.g., `__pycache__/`, `*.pyc`).
- [ ] **Commit message** uses `type: summary` and describes the change succinctly.
- [ ] **Validation** run where applicable (tests if present; otherwise at least `python -m py_compile` for edited Python files).
- [ ] **Docs** updated when behavior/workflow changes (and indexes updated if docs moved/added).
- [ ] **Docs naming** follows lower `snake_case.md` (exceptions: [`README.md`](../../../../README.md), [`AGENTS.md`](../../../../AGENTS.md)); avoid file-based "Moved to ..." stubs.

Return back: [`checklists_overview.md`](checklists_overview.md)
Return to root: [`README.md`](../../../../README.md)
