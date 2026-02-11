# Git Hygiene Checklist

- [ ] **Branch Name** follows `<prefix>/<short-topic>`.
- [ ] **Scope** is single-purpose; unrelated changes are split.
- [ ] **Status Check** run before/after edits (`git status -sb`).
- [ ] **No Generated Artifacts** are committed (`__pycache__/`, `*.pyc`, runtime logs).
- [ ] **Temp Policy** respected: temporary artifacts remain under `tmp/` only.
- [ ] **Commit Message** uses `type: summary`.
- [ ] **Validation** run where applicable.
- [ ] **Docs Updated** when behavior/workflow changes.
- [ ] **Docs Naming** follows lower `snake_case.md` (except `README.md`, `AGENTS.md`).

Advanced-only checks:
- [ ] **Hooks Awareness**: if advanced mode is enabled, local hook checks pass before push.
- [ ] **Status Tracking**: advanced workflow commits include meaningful `status.md` updates.

Return back: [`checklists_overview.md`](checklists_overview.md)
Return to root: [`README.md`](../../../../README.md)
