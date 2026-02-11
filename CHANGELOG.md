# Changelog

All notable template updates are documented in this file.

Format:
- Keep one `Unreleased` section for in-progress changes.
- Move completed changes into a dated version section.
- Keep entries scoped to template/workflow infrastructure.

## [Unreleased]

No unreleased changes yet.

## [v0.2.0] - 2026-02-11

### Added
- Tiered workflow structure with dedicated beginner and advanced documentation entrypoints.
- Advanced workspace overlays: `CodexWorkspace/workspace/prd.md`, `CodexWorkspace/workspace/tech_spec.md`, and `CodexWorkspace/workspace/status.md`.
- Advanced templates: `prd_template.md`, `tech_spec_template.md`, and `status_template.md`.
- Logging standards reference (`logging_and_debugging.md`) with beginner/advanced guidance.
- Optional advanced hook tooling: `.githooks/`, `tools/setup_advanced_hooks.ps1`, `tools/disable_advanced_hooks.ps1`.
- Template safeguard scripts and CI workflow:
  - `tools/check_example_scaffold.ps1`
  - `tools/check_stale_doc_paths.ps1`
  - `tools/check_status_schema.ps1`
  - `tools/check_status_updated.ps1`
  - `tools/check_temp_files_policy.ps1`
  - `.github/workflows/template-safeguards.yml`
- Temporary workspace policy docs: `tmp/README.md` and `tmp/logs/README.md`.

### Changed
- `AGENTS.md` promoted to canonical operating contract with decision log and strict temporary artifact policy.
- Root and CodexWorkspace navigation docs updated for tiered onboarding.
- Checklists updated for advanced AI/data safety and scaffold-preservation checks.
- Issue templates updated to current repository paths and wording.

### Fixed
- Legacy path references in docs/templates updated to current structure.
- Workspace `tasks/README.md` and `reviews/README.md` moved to repo-relative links.

## [v0.1.0] - 2026-02-02

### Baseline Summary (main before tiered updates)
- CodexWorkspace template structure with human guides, skills, references, prompts, scripts, and planning templates.
- Out-of-box pyRevit scaffold:
  - `ai-pyrevit-developer-template.extension/`
  - `HelloWorld.tab` validation button path.
- Baseline workspace flow with:
  - `development.md`
  - `plans/`, `tasks/`, `reviews/`
  - `backlog.md`
- Existing checklists and issue templates prior to the beginner/advanced tier split.
