# Codex Agent Guide (Repository Root)

This repository is a template/meta workflow repository for pyRevit development. It is not a project-specific add-on implementation repository.

## Start Here
- Primary entrypoint: [`CodexWorkspace/README.md`](CodexWorkspace/README.md)
- Beginner workflow (no hooks): [`CodexWorkspace/human/beginner_quickstart.md`](CodexWorkspace/human/beginner_quickstart.md)
- Advanced workflow (opt-in checks): [`CodexWorkspace/human/advanced_workflow.md`](CodexWorkspace/human/advanced_workflow.md)
- Human docs index: [`CodexWorkspace/human/README.md`](CodexWorkspace/human/README.md)
- Skill references index: [`CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md)
- Planning workspace (project-specific): [`CodexWorkspace/workspace/`](CodexWorkspace/workspace/)
- Release notes: [`CHANGELOG.md`](CHANGELOG.md)

## Operating Contract
- Keep this repo template-first. Do not add project-specific production add-on logic here.
- Preserve the out-of-box scaffold:
  - `ai-pyrevit-developer-template.extension/`
  - `ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`
- Keep code and docs clean:
  - Remove orphaned code after refactors.
  - Extract repeated logic into reusable functions/modules.
  - Update references/index docs when files move or behavior changes.
- Keep temporary artifacts under `tmp/` only:
  - Scratch code, one-off test outputs, and debug dumps must be created under `tmp/`.
  - Persisted logs must be created under `tmp/logs/`.
  - Do not commit temporary artifacts unless they are policy docs (`tmp/README.md`, `tmp/logs/README.md`).
- Seed-prompt workflow contract:
  - Start from a plain-English user description.
  - Run a planning/clarification phase before coding.
  - Map work through workspace artifacts to a fully working pyRevit button.
  - Use beginner or advanced artifact depth based on selected tier.

## Tier Rules
- Beginner mode:
  - No local hooks required.
  - Baseline workflow uses `development.md`, `tasks/`, `reviews/`, and `backlog.md`.
- Advanced mode (opt-in):
  - Enable hooks via `tools/setup_advanced_hooks.ps1`.
  - Maintain advanced overlays: `CodexWorkspace/workspace/prd.md`, `CodexWorkspace/workspace/tech_spec.md`, `CodexWorkspace/workspace/status.md`.
  - Update `CodexWorkspace/workspace/status.md` after meaningful code/workflow changes.
  - Use advanced checklist gates before commit/push.

## Git Workflow
- Branch naming: `<prefix>/<short-topic>` (for example: `docs/tiered-meta-workflow`, `fix/link-index`).
- Prefix guide:
  - `agent/` setup or automation
  - `docs/` documentation-only changes
  - `feat/` new behavior
  - `fix/` bug fixes
  - `refactor/` structural refactors
  - `test/` tests only
  - `chore/` maintenance
- Commits:
  - Keep commits scoped and single-purpose.
  - Use `type: summary` format.
- Hygiene:
  - Run `git status -sb` before and after changes.
  - Avoid destructive commands unless explicitly requested.
- Agent-owned git execution (when seed prompts request autonomous flow):
  - Handle branch creation/management without waiting for user input.
  - Make atomic, single-purpose, reversible commits.
  - Execute push and PR lifecycle steps autonomously.
  - Report branch, commit list, and PR/release status at handoff.

## Decision Log
Use this section to capture major corrections and persistent rules that must survive across sessions.

### 2026-02-11: Tiered Workflow
- Added two user tiers:
  - Beginner mode without mandatory hooks.
  - Advanced mode with opt-in hooks and stricter checks.
- Advanced controls must never block beginner onboarding by default.

### 2026-02-11: Template Asset Protection
- `ai-pyrevit-developer-template.extension` is a protected template asset and must remain present.
- The HelloWorld path is part of the out-of-box validation contract and must remain runnable.

### 2026-02-11: Temporary Artifact Policy
- `tmp/` is the only allowed location for temporary files.
- `tmp/logs/` is the standard persisted log path.

### 2026-02-11: Advanced Status Tracking
- Advanced-mode work requires consistent `status.md` updates using the required schema.

### 2026-02-19: Seed Prompt Standardization
- Human guides include copy/paste seed prompts for beginner and advanced tiers.
- Seed prompts require plain-English kickoff, planning questions before coding, and explicit workspace artifact flow.
- Seed prompts define agent-owned git handling with atomic commits and autonomous branch/PR operations.

Return back: [`README.md`](README.md)
Return to root: [`README.md`](README.md)
