# Changelog

All notable template updates are documented in this file.

Format:
- Keep one `Unreleased` section for in-progress changes.
- Move completed changes into a dated version section.
- Keep entries scoped to template/workflow infrastructure.

## [Unreleased]

No unreleased changes yet.

## [v0.2.1] - 2026-02-19

### Added
- New helper skill: `CodexWorkspace/skills/select-svg-icon/` for choosing pyRevit command icons with a vision-based semantic validation workflow.
- New icon review reference rubric: `CodexWorkspace/skills/select-svg-icon/references/icon_review_rubric.md`.
- New source acquisition protocols:
  - `CodexWorkspace/skills/select-svg-icon/references/svgrepo_automated_acquisition.md` (automated default path)
  - `CodexWorkspace/skills/select-svg-icon/references/svgfind_acquisition.md` (manual fallback path)
- New skill scripts:
  - `CodexWorkspace/skills/select-svg-icon/scripts/acquire_svgrepo_svg.py`
  - `CodexWorkspace/skills/select-svg-icon/scripts/render_svg_icon_png.py`
- Seed prompt templates for agent kickoff in:
  - `CodexWorkspace/human/beginner_quickstart.md`
  - `CodexWorkspace/human/advanced_workflow.md`

### Changed
- Navigation indexes now include the new icon-selection skill:
  - `README.md`
  - `CodexWorkspace/README.md`
  - `CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`
- Skill naming and metadata now use SVG-only naming (`select-svg-icon`) with no source-site name in the skill identifier.
- Human docs index now points to tiered seed prompt usage in `CodexWorkspace/human/README.md`.
- `AGENTS.md` now captures the seed-prompt workflow contract and agent-owned git execution requirements (atomic commits, autonomous branch/PR flow).

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
