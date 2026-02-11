# Tasks: Tiered Meta-Workflow Upgrade (2026-02-11)

Plan source: `CodexWorkspace/workspace/plans/tiered_meta_workflow_upgrade_plan.md`

## Task Format
- Size target: <= 3 hours, <= ~100 LoC of net changes per task where practical.
- Each task must include docs updates when behavior changes.
- All paths are repo-relative.

## Route A: Tiered Onboarding and Navigation

### Task TMW-001: Create root changelog scaffold
- Depends on: none
- Files: `CHANGELOG.md`
- Work:
  - Add changelog structure with `Unreleased` and first version section format.
  - Add contributor instructions for adding entries.
- Validation:
  - `Test-Path CHANGELOG.md`
  - `rg -n \"^## \\[Unreleased\\]\" CHANGELOG.md`
- Done when:
  - `CHANGELOG.md` exists and documents update policy.

### Task TMW-002: Update root README for tiered entrypoints
- Depends on: TMW-001
- Files: `README.md`
- Work:
  - Add Beginner/Advanced navigation links.
  - Link to `CHANGELOG.md`.
  - Reinforce template-only positioning.
- Validation:
  - `rg -n \"beginner|advanced|CHANGELOG\" README.md -i`
- Done when:
  - Root README exposes tiered workflow and updates log.

### Task TMW-003: Update human index for tier selector
- Depends on: none
- Files: `CodexWorkspace/human/README.md`
- Work:
  - Add clear split between Beginner and Advanced paths.
  - Link to new guide pages.
- Validation:
  - `rg -n \"beginner_quickstart|advanced_workflow\" CodexWorkspace/human/README.md`
- Done when:
  - Human index routes users to the correct tier.

### Task TMW-004: Create Beginner quickstart guide
- Depends on: TMW-003
- Files: `CodexWorkspace/human/beginner_quickstart.md`
- Work:
  - Document no-hook path for first-time users.
  - Include minimal steps to run OOTB HelloWorld.
- Validation:
  - `Test-Path CodexWorkspace/human/beginner_quickstart.md`
  - `rg -n \"no hooks|required\" CodexWorkspace/human/beginner_quickstart.md -i`
- Done when:
  - Beginner workflow is self-contained and non-blocking.

### Task TMW-005: Create Advanced workflow guide
- Depends on: TMW-003
- Files: `CodexWorkspace/human/advanced_workflow.md`
- Work:
  - Document opt-in advanced controls, hooks, stricter checks.
  - Include setup and disable commands for advanced mode.
- Validation:
  - `Test-Path CodexWorkspace/human/advanced_workflow.md`
  - `rg -n \"setup_advanced_hooks|disable_advanced_hooks|opt-in\" CodexWorkspace/human/advanced_workflow.md -i`
- Done when:
  - Advanced mode is clearly documented and optional.

### Task TMW-006: Add cross-links between root/workspace/human entrypoints
- Depends on: TMW-002, TMW-003, TMW-004, TMW-005
- Files: `CodexWorkspace/README.md`, `CodexWorkspace/workspace/README.md`, `CodexWorkspace/human/README.md`
- Work:
  - Add consistent links to tier docs and changelog from entrypoint docs.
- Validation:
  - `rg -n \"beginner_quickstart|advanced_workflow|CHANGELOG\" CodexWorkspace/README.md CodexWorkspace/workspace/README.md CodexWorkspace/human/README.md`
- Done when:
  - Entrypoint docs provide consistent navigation.

## Route B: AGENTS Contract, Decision Log, and Policies

### Task TMW-007: Add template-only operating contract in AGENTS
- Depends on: none
- Files: `AGENTS.md`
- Work:
  - Add explicit template-only scope statement.
  - Clarify that this repo is methodology/template infrastructure.
- Validation:
  - `rg -n \"template|meta|not a project-specific add-on\" AGENTS.md -i`
- Done when:
  - AGENTS establishes scope unambiguously.

### Task TMW-008: Add Decision Log section in AGENTS
- Depends on: TMW-007
- Files: `AGENTS.md`
- Work:
  - Add `Decision Log` section and initial entries.
  - Include update rules for recording major corrections.
- Validation:
  - `rg -n \"Decision Log\" AGENTS.md`
- Done when:
  - AGENTS contains maintained decision-memory structure.

### Task TMW-009: Add strict temp-files policy in AGENTS
- Depends on: TMW-007
- Files: `AGENTS.md`
- Work:
  - Define `tmp/` as the only temp artifact location.
  - Define `tmp/logs/` for persisted logs.
- Validation:
  - `rg -n \"tmp/|tmp/logs\" AGENTS.md`
- Done when:
  - Temp artifact constraints are explicit in AGENTS.

### Task TMW-010: Add advanced mode rules in AGENTS
- Depends on: TMW-007, TMW-008, TMW-009
- Files: `AGENTS.md`
- Work:
  - Add advanced-only rules: status update cadence, hook opt-in behavior.
  - Add non-removal rule for OOTB scaffold paths.
- Validation:
  - `rg -n \"status|hooks|opt-in|non-removal|ai-pyrevit-developer-template.extension\" AGENTS.md -i`
- Done when:
  - AGENTS captures advanced mode obligations and scaffold guardrails.

## Route C: Advanced Workspace Artifacts and Templates

### Task TMW-011: Add PRD template
- Depends on: none
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/prd_template.md`
- Work:
  - Add sections: problem, goals, user stories, roadmap, metrics, non-goals.
- Validation:
  - `Test-Path CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/prd_template.md`
- Done when:
  - PRD template is available for advanced mode.

### Task TMW-012: Add Tech Spec template
- Depends on: none
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/tech_spec_template.md`
- Work:
  - Add architecture, modules, APIs/interfaces, failure modes, validation strategy.
- Validation:
  - `Test-Path CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/tech_spec_template.md`
- Done when:
  - Tech spec template is available for advanced mode.

### Task TMW-013: Add Status template with schema contract
- Depends on: none
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/status_template.md`
- Work:
  - Add required fixed sections:
    - `Scope`, `Folder Map`, `Completed`, `In Progress`, `Pending`, `Known Bugs`, `Open Risks`, `Next Actions`, `Last Updated`.
- Validation:
  - `rg -n \"^## Scope|^## Folder Map|^## Completed|^## In Progress|^## Pending|^## Known Bugs|^## Open Risks|^## Next Actions|^## Last Updated\" CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/status_template.md`
- Done when:
  - Status schema is explicit and machine-checkable.

### Task TMW-014: Create workspace PRD artifact
- Depends on: TMW-011
- Files: `CodexWorkspace/workspace/prd.md`
- Work:
  - Add starter artifact copied/adapted from template with guidance text.
- Validation:
  - `Test-Path CodexWorkspace/workspace/prd.md`
- Done when:
  - Advanced workspace PRD artifact exists.

### Task TMW-015: Create workspace Tech Spec artifact
- Depends on: TMW-012
- Files: `CodexWorkspace/workspace/tech_spec.md`
- Work:
  - Add starter artifact copied/adapted from template with guidance text.
- Validation:
  - `Test-Path CodexWorkspace/workspace/tech_spec.md`
- Done when:
  - Advanced workspace Tech Spec artifact exists.

### Task TMW-016: Create workspace Status artifact
- Depends on: TMW-013
- Files: `CodexWorkspace/workspace/status.md`
- Work:
  - Add starter artifact following required status schema.
- Validation:
  - `rg -n \"^## Scope|^## Folder Map|^## Completed|^## In Progress|^## Pending|^## Known Bugs|^## Open Risks|^## Next Actions|^## Last Updated\" CodexWorkspace/workspace/status.md`
- Done when:
  - Advanced workspace Status artifact exists and matches schema.

### Task TMW-017: Update workspace README with beginner/advanced overlays
- Depends on: TMW-014, TMW-015, TMW-016
- Files: `CodexWorkspace/workspace/README.md`
- Work:
  - Document baseline artifacts vs advanced overlays.
  - Add links to new workspace artifacts.
- Validation:
  - `rg -n \"prd\\.md|tech_spec\\.md|status\\.md|beginner|advanced\" CodexWorkspace/workspace/README.md -i`
- Done when:
  - Workspace README describes both tiers and artifact responsibilities.

### Task TMW-018: Update template index docs
- Depends on: TMW-011, TMW-012, TMW-013
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/templates_overview.md`
- Work:
  - Add new templates to inventory and usage steps.
- Validation:
  - `rg -n \"prd_template|tech_spec_template|status_template\" CodexWorkspace/skills/develop-pyrevit-extensions/references/templates_overview.md`
- Done when:
  - Template index includes all advanced templates.

### Task TMW-019: Update docs index with new pages/artifacts
- Depends on: TMW-004, TMW-005, TMW-014, TMW-015, TMW-016, TMW-023
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`
- Work:
  - Add links to tier guides, status artifacts, logging reference.
- Validation:
  - `rg -n \"beginner_quickstart|advanced_workflow|prd\\.md|tech_spec\\.md|status\\.md|logging\" CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md -i`
- Done when:
  - Docs index is aligned with new architecture.

## Route D: Temp Policy and Logging Standards

### Task TMW-020: Update gitignore for strict temp policy
- Depends on: none
- Files: `.gitignore`
- Work:
  - Ignore `tmp/` outputs by default.
  - Add explicit allowlist exceptions for policy docs inside `tmp/`.
- Validation:
  - `rg -n \"tmp/|tmp/logs\" .gitignore`
- Done when:
  - Temp artifacts are ignored while policy docs can be tracked.

### Task TMW-021: Add tmp policy readme
- Depends on: TMW-020
- Files: `tmp/README.md`
- Work:
  - Document what belongs in `tmp/`, what must never be committed.
- Validation:
  - `Test-Path tmp/README.md`
- Done when:
  - Temp usage policy is discoverable in-repo.

### Task TMW-022: Add logs directory policy readme
- Depends on: TMW-020
- Files: `tmp/logs/README.md`
- Work:
  - Define log naming and retention guidance.
- Validation:
  - `Test-Path tmp/logs/README.md`
- Done when:
  - Log storage rules are defined.

### Task TMW-023: Add logging standards reference (tiered)
- Depends on: none
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/logging_and_debugging.md`
- Work:
  - Add beginner logging minimum and advanced structured logging standard.
  - Reference `tmp/logs/`.
- Validation:
  - `rg -n \"beginner|advanced|tmp/logs\" CodexWorkspace/skills/develop-pyrevit-extensions/references/logging_and_debugging.md -i`
- Done when:
  - Logging standard exists and is tier-specific.

### Task TMW-024: Link logging standards from advanced guide and indexes
- Depends on: TMW-005, TMW-023
- Files: `CodexWorkspace/human/advanced_workflow.md`, `CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`
- Work:
  - Add links and required usage notes for logging standard.
- Validation:
  - `rg -n \"logging_and_debugging\" CodexWorkspace/human/advanced_workflow.md CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`
- Done when:
  - Advanced workflow points to concrete logging standard.

### Task TMW-025: Add logging checks to testing strategy checklist
- Depends on: TMW-023
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md`
- Work:
  - Add beginner and advanced logging verification checklist items.
- Validation:
  - `rg -n \"log|logging|tmp/logs|beginner|advanced\" CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md -i`
- Done when:
  - Logging validation is part of testing checklist.

## Route E: Advanced AI/Data Safety Rules

### Task TMW-026: Add AI/data safety checks to code review checklist
- Depends on: none
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md`
- Work:
  - Add advanced-mode checklist items:
    - dataset coverage disclosure,
    - explicit sampling disclosure,
    - no silent downsampling,
    - numeric sanity checks,
    - metric direction validation.
- Validation:
  - `rg -n \"dataset|sampling|downsampling|numeric|metric\" CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md -i`
- Done when:
  - Advanced AI/data safety is codified in checklist.

### Task TMW-027: Add advanced AI/data safety section in advanced workflow doc
- Depends on: TMW-005, TMW-026
- Files: `CodexWorkspace/human/advanced_workflow.md`
- Work:
  - Add operational procedure for running AI/data tasks safely.
  - Link to checklist items and required evidence.
- Validation:
  - `rg -n \"dataset coverage|sampling|numeric sanity|metric direction\" CodexWorkspace/human/advanced_workflow.md -i`
- Done when:
  - Advanced workflow includes AI/data safety execution guidance.

### Task TMW-028: Add advanced-mode markers to avoid beginner confusion
- Depends on: TMW-026, TMW-027
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md`, `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md`
- Work:
  - Mark AI/data safety items as advanced-only where needed.
- Validation:
  - `rg -n \"advanced\" CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_testing_strategy.md -i`
- Done when:
  - Checklist intent is clear by tier.

## Route F: Advanced Hook Tooling (Opt-In)

### Task TMW-029: Add advanced hook setup script
- Depends on: none
- Files: `tools/setup_advanced_hooks.ps1`
- Work:
  - Set repo-local `core.hooksPath` to `.githooks`.
  - Print clear success/failure output.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/setup_advanced_hooks.ps1`
  - `git config --get core.hooksPath`
- Done when:
  - Setup script enables hooks explicitly.

### Task TMW-030: Add advanced hook disable script
- Depends on: TMW-029
- Files: `tools/disable_advanced_hooks.ps1`
- Work:
  - Unset repo-local hooks path or restore default.
  - Print clear success/failure output.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/disable_advanced_hooks.ps1`
  - `git config --get core.hooksPath`
- Done when:
  - Disable script cleanly turns off advanced hooks.

### Task TMW-031: Add hook documentation
- Depends on: TMW-029, TMW-030
- Files: `.githooks/README.md`
- Work:
  - Document hook purpose, scripts called, bypass guidance.
- Validation:
  - `Test-Path .githooks/README.md`
- Done when:
  - Hook behavior is documented for advanced users.

### Task TMW-032: Add temp-policy check script
- Depends on: TMW-020
- Files: `tools/check_temp_files_policy.ps1`
- Work:
  - Detect staged files that appear temporary and are outside `tmp/`.
  - Return non-zero on violations.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/check_temp_files_policy.ps1`
- Done when:
  - Script can block temp-file policy violations.

### Task TMW-033: Add status schema check script
- Depends on: TMW-013, TMW-016
- Files: `tools/check_status_schema.ps1`
- Work:
  - Validate required `status.md` headers exist.
  - Return non-zero if schema is incomplete.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/check_status_schema.ps1`
- Done when:
  - Status schema can be auto-validated.

### Task TMW-034: Add status-update enforcement script
- Depends on: TMW-016
- Files: `tools/check_status_updated.ps1`
- Work:
  - In advanced mode, fail if relevant code/docs changed without touching `CodexWorkspace/workspace/status.md`.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/check_status_updated.ps1`
- Done when:
  - Advanced mode can enforce status update cadence.

### Task TMW-035: Add pre-commit hook wrapper
- Depends on: TMW-032, TMW-033, TMW-034
- Files: `.githooks/pre-commit`
- Work:
  - Execute advanced checks and block on failures.
- Validation:
  - Run setup script and perform dry-run commit with intentional violation.
- Done when:
  - Pre-commit hook blocks violating commits in advanced mode.

### Task TMW-036: Add pre-push hook wrapper
- Depends on: TMW-032, TMW-033, TMW-034
- Files: `.githooks/pre-push`
- Work:
  - Re-run critical checks before push.
- Validation:
  - Dry-run push behavior after setup.
- Done when:
  - Pre-push check exists and documents blocking behavior.

## Route G: Scaffold Safeguards and CI

### Task TMW-037: Add OOTB scaffold check script
- Depends on: none
- Files: `tools/check_example_scaffold.ps1`
- Work:
  - Assert required paths exist:
    - `ai-pyrevit-developer-template.extension/`
    - `ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`
  - Return non-zero on missing paths.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/check_example_scaffold.ps1`
- Done when:
  - Script fails on scaffold removal and passes on intact scaffold.

### Task TMW-038: Add stale-path checker script
- Depends on: none
- Files: `tools/check_stale_doc_paths.ps1`
- Work:
  - Detect legacy path patterns such as `CodexWorkspace/docs/`.
  - Return non-zero when stale patterns are found.
- Validation:
  - `powershell -ExecutionPolicy Bypass -File tools/check_stale_doc_paths.ps1`
- Done when:
  - Stale path usage can be detected automatically.

### Task TMW-039: Add CI workflow for template safeguards
- Depends on: TMW-037, TMW-038
- Files: `.github/workflows/template-safeguards.yml`
- Work:
  - Run scaffold and stale-path checks on push/PR.
  - Keep workflow focused on template integrity.
- Validation:
  - `Test-Path .github/workflows/template-safeguards.yml`
- Done when:
  - PRs get automated guardrails for template-critical paths.

### Task TMW-040: Add scaffold-preservation item to code review checklist
- Depends on: TMW-037
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md`
- Work:
  - Add explicit item verifying OOTB example scaffold remains intact.
- Validation:
  - `rg -n \"scaffold|HelloWorld|ai-pyrevit-developer-template.extension\" CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_code_review.md -i`
- Done when:
  - Checklist enforces preservation of working example.

### Task TMW-041: Add temp-policy and hook notes to git hygiene checklist
- Depends on: TMW-020, TMW-029, TMW-030
- Files: `CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_git_hygiene.md`
- Work:
  - Add checklist items for `tmp/` policy and advanced hooks opt-in awareness.
- Validation:
  - `rg -n \"tmp/|hooks|opt-in\" CodexWorkspace/skills/develop-pyrevit-extensions/references/checklist_git_hygiene.md -i`
- Done when:
  - Git hygiene checklist reflects new workflow controls.

## Route H: Link Hygiene Cleanup

### Task TMW-042: Fix stale links in issue template config
- Depends on: none
- Files: `.github/ISSUE_TEMPLATE/config.yml`
- Work:
  - Replace old `CodexWorkspace/docs/...` URLs with current valid paths.
- Validation:
  - `rg -n \"CodexWorkspace/docs\" .github/ISSUE_TEMPLATE/config.yml`
- Done when:
  - Config links resolve to current repo structure.

### Task TMW-043: Fix stale paths in bug report template
- Depends on: none
- Files: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Work:
  - Update stale doc path references and options to current structure.
  - Fix any encoding artifacts that reduce readability.
- Validation:
  - `rg -n \"CodexWorkspace/docs\" .github/ISSUE_TEMPLATE/bug_report.yml`
- Done when:
  - Bug template path hints are accurate and readable.

### Task TMW-044: Fix stale paths in docs improvement template
- Depends on: none
- Files: `.github/ISSUE_TEMPLATE/docs_improvement.yml`
- Work:
  - Update placeholder examples to current path conventions.
- Validation:
  - `rg -n \"CodexWorkspace/docs\" .github/ISSUE_TEMPLATE/docs_improvement.yml`
- Done when:
  - Docs improvement template examples are correct.

### Task TMW-045: Fix stale paths in feature request template
- Depends on: none
- Files: `.github/ISSUE_TEMPLATE/feature_request.yml`
- Work:
  - Update target area labels to current folder structure.
- Validation:
  - `rg -n \"CodexWorkspace/docs\" .github/ISSUE_TEMPLATE/feature_request.yml`
- Done when:
  - Feature template paths match current repository.

### Task TMW-046: Normalize workspace task/review README links
- Depends on: none
- Files: `CodexWorkspace/workspace/tasks/README.md`, `CodexWorkspace/workspace/reviews/README.md`
- Work:
  - Replace absolute GitHub links with repo-relative links.
- Validation:
  - `rg -n \"https://github.com\" CodexWorkspace/workspace/tasks/README.md CodexWorkspace/workspace/reviews/README.md`
- Done when:
  - Workspace readmes use local relative navigation.

### Task TMW-047: Repo-wide stale-path cleanup pass
- Depends on: TMW-042, TMW-043, TMW-044, TMW-045, TMW-046
- Files: repo-wide docs/templates as needed
- Work:
  - Remove remaining stale path patterns and inconsistent references.
- Validation:
  - `rg -n \"CodexWorkspace/docs\" -S`
- Done when:
  - No stale `CodexWorkspace/docs` path references remain.

## Route I: Coverage Validation Documentation

### Task TMW-048: Create implementation coverage review artifact
- Depends on: TMW-001 through TMW-047 (planning dependency)
- Files: `CodexWorkspace/workspace/reviews/review_tiered_meta_workflow_coverage_20260211.md`
- Work:
  - Record feature-to-task and scenario-to-task coverage.
  - Identify any uncovered scope with remediation tasks.
- Validation:
  - `Test-Path CodexWorkspace/workspace/reviews/review_tiered_meta_workflow_coverage_20260211.md`
- Done when:
  - Coverage review document exists with explicit gap status.

### Task TMW-049: Add final validation command bundle
- Depends on: TMW-032, TMW-033, TMW-034, TMW-037, TMW-038, TMW-039
- Files: `CodexWorkspace/workspace/reviews/review_tiered_meta_workflow_coverage_20260211.md`
- Work:
  - Add runnable validation command list and expected outcomes.
- Validation:
  - Coverage review file contains executable command list.
- Done when:
  - Validation is reproducible for reviewers.

### Task TMW-050: Add closure checklist for PR readiness
- Depends on: TMW-048, TMW-049
- Files: `CodexWorkspace/workspace/reviews/review_tiered_meta_workflow_coverage_20260211.md`
- Work:
  - Add go/no-go checklist:
    - tier docs complete,
    - AGENTS contract complete,
    - temp policy active,
    - advanced artifacts complete,
    - hooks optional and working,
    - scaffold preserved.
- Validation:
  - Closure checklist present with pass/fail markers.
- Done when:
  - PR can be reviewed with a single closure artifact.

## Coverage Validation Matrix

### Planned Feature Coverage
| Plan Feature | Covered By Tasks | Coverage Status |
| --- | --- | --- |
| 1. Tiered onboarding and navigation | TMW-002, TMW-003, TMW-004, TMW-005, TMW-006 | Covered |
| 2. Canonical agent contract and decision memory | TMW-007, TMW-008, TMW-009, TMW-010 | Covered |
| 3. Strict temporary-files policy | TMW-009, TMW-020, TMW-021, TMW-022, TMW-032, TMW-041 | Covered |
| 4. Advanced workflow artifact layer | TMW-011, TMW-012, TMW-013, TMW-014, TMW-015, TMW-016, TMW-017, TMW-018 | Covered |
| 5. `Status.md` schema contract | TMW-013, TMW-016, TMW-033, TMW-034 | Covered |
| 6. Optional advanced hooks and setup scripts | TMW-029, TMW-030, TMW-031, TMW-035, TMW-036 | Covered |
| 7. Release/update communication | TMW-001, TMW-002, TMW-006 | Covered |
| 8. Logging standards by tier | TMW-023, TMW-024, TMW-025 | Covered |
| 9. Advanced AI/data-task safety rules | TMW-026, TMW-027, TMW-028 | Covered |
| 10. OOTB scaffold preservation safeguards | TMW-010, TMW-037, TMW-039, TMW-040 | Covered |
| 11. Documentation and link hygiene cleanup | TMW-019, TMW-042, TMW-043, TMW-044, TMW-045, TMW-046, TMW-047 | Covered |

### Validation Scenario Coverage
| Validation Scenario | Covered By Tasks | Coverage Status |
| --- | --- | --- |
| 1. Beginner flow works without hooks | TMW-004, TMW-006 | Covered |
| 2. Advanced flow enables checks after setup | TMW-005, TMW-029, TMW-035, TMW-036 | Covered |
| 3. Advanced flow disable works cleanly | TMW-030 | Covered |
| 4. `CHANGELOG.md` exists and is linked | TMW-001, TMW-002, TMW-006 | Covered |
| 5. PRD/TechSpec/Status files exist and are documented | TMW-011, TMW-012, TMW-013, TMW-014, TMW-015, TMW-016, TMW-017, TMW-018 | Covered |
| 6. `status.md` validates against schema | TMW-013, TMW-016, TMW-033 | Covered |
| 7. Temp artifacts outside `tmp/` are flagged | TMW-020, TMW-032, TMW-035 | Covered |
| 8. Logging requirements documented (`tmp/logs/`) | TMW-022, TMW-023, TMW-024, TMW-025 | Covered |
| 9. Advanced checklist contains AI/data safety | TMW-026, TMW-028 | Covered |
| 10. Scaffold check passes with intact paths | TMW-037, TMW-039 | Covered |
| 11. Scaffold check fails on missing OOTB paths | TMW-037, TMW-039 | Covered |
| 12. Manual smoke: extension loads and HelloWorld runs | TMW-004, TMW-040, TMW-050 | Covered |

Coverage result: all planned features and all validation scenarios are mapped to at least one concrete task.
