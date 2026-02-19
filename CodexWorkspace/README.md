# Codex Workspace

This workspace is a curated knowledge base for pyRevit development, organized as skills plus project planning artifacts.

## Start Here
- Beginner quickstart (no hooks): [`human/beginner_quickstart.md`](human/beginner_quickstart.md).
- Advanced workflow (opt-in hooks): [`human/advanced_workflow.md`](human/advanced_workflow.md).
- Tier selector: [`human/README.md`](human/README.md).
- Agent workflow, checklists, and references (advanced): [`skills/develop-pyrevit-extensions/references/agent_overview.md`](skills/develop-pyrevit-extensions/references/agent_overview.md).
- Project planning artifacts: [`workspace/README.md`](workspace/README.md).
- Update log: [`../CHANGELOG.md`](../CHANGELOG.md).

## Directory Tour
- [`human/`](human/) - human-facing setup and troubleshooting.
- [`skills/develop-pyrevit-extensions/`](skills/develop-pyrevit-extensions/) - base pyRevit development skill (SKILL.md + resources).
- [`skills/pyrevit-revit-2023/`](skills/pyrevit-revit-2023/) - Revit 2023 version-specific guidance skill.
- [`skills/pyrevit-revit-2024/`](skills/pyrevit-revit-2024/) - Revit 2024 version-specific guidance skill (scaffold).
- [`skills/pyrevit-revit-2025/`](skills/pyrevit-revit-2025/) - Revit 2025 version-specific guidance skill (scaffold).
- [`skills/select-svg-icon/`](skills/select-svg-icon/) - SVG-only icon selection skill for pyRevit commands with automated `svgrepo` acquisition and manual `svgfind` fallback.
- [`skills/develop-pyrevit-extensions/references/`](skills/develop-pyrevit-extensions/references/) - agent references.
- [`skills/develop-pyrevit-extensions/assets/`](skills/develop-pyrevit-extensions/assets/) - prompts and templates.
- [`skills/develop-pyrevit-extensions/scripts/`](skills/develop-pyrevit-extensions/scripts/) - pyRevit-ready templates and harnesses.
- [`workspace`](workspace) - plans, development.md, tasks, reviews, backlog, plus advanced overlays (`prd.md`, `tech_spec.md`, `status.md`).

## Notes
- Base workflow is version-agnostic; versioned skills carry API specifics (2023 populated, 2024/2025 scaffolds).
- Advanced controls are opt-in. Beginner workflow stays non-blocking.
- Keep transactions explicit (`Transaction.Start()` / `Commit()`), and roll back inside `except` blocks.
- Use the matching `skills/pyrevit-revit-20xx/` skill for version-specific guidance.

## Call For Contributions
- Add guidance for any Revit version by extending or adding `pyrevit-revit-20xx` skills.

Return back: [`../README.md`](../README.md)
Return to root: [`../README.md`](../README.md)
