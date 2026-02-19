# AI pyRevit Developer Template

AI-first pyRevit developer template with a CodexWorkspace plan-to-tasks workflow and a ready-to-load `.extension` bundle.

## Start Here
- Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
- Beginner workflow (no hooks required): [`CodexWorkspace/human/beginner_quickstart.md`](CodexWorkspace/human/beginner_quickstart.md).
- Advanced workflow (opt-in hooks and stricter checks): [`CodexWorkspace/human/advanced_workflow.md`](CodexWorkspace/human/advanced_workflow.md).
- Tier selector and full human docs index: [`CodexWorkspace/human/README.md`](CodexWorkspace/human/README.md).
- Agent workflow + references (advanced): [`CodexWorkspace/skills/develop-pyrevit-extensions/references/agent_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/agent_overview.md).
- Planning artifacts (plans, development.md, tasks, reviews, backlog, advanced overlays): [`CodexWorkspace/workspace/README.md`](CodexWorkspace/workspace/README.md).
- Update log: [`CHANGELOG.md`](CHANGELOG.md).

## What This Repo Contains
- pyRevit extension bundle (what you add in pyRevit Settings): [`ai-pyrevit-developer-template.extension/`](ai-pyrevit-developer-template.extension/).
- Hello World scaffold (inside the extension bundle): [`ai-pyrevit-developer-template.extension/HelloWorld.tab/`](ai-pyrevit-developer-template.extension/HelloWorld.tab/).
- Base skill package (workflow, prompts, templates, scripts): [`CodexWorkspace/skills/develop-pyrevit-extensions/`](CodexWorkspace/skills/develop-pyrevit-extensions/).
- Version-specific skills: [`CodexWorkspace/skills/pyrevit-revit-2023/`](CodexWorkspace/skills/pyrevit-revit-2023/), [`CodexWorkspace/skills/pyrevit-revit-2024/`](CodexWorkspace/skills/pyrevit-revit-2024/) (scaffold), [`CodexWorkspace/skills/pyrevit-revit-2025/`](CodexWorkspace/skills/pyrevit-revit-2025/) (scaffold).
- Icon-selection helper skill: [`CodexWorkspace/skills/select-svg-icon/`](CodexWorkspace/skills/select-svg-icon/) for SVG-only icon acquisition (`svgrepo` automated first, `svgfind` manual fallback) and vision-based icon-to-script matching.

## Notes
- Current references are aligned with Revit 2023; use the matching `CodexWorkspace/skills/pyrevit-revit-20xx/` skill and adjust as needed for other versions.
- This repository is a template/meta workflow repository, not a project-specific add-on implementation repo.
- Keep `ai-pyrevit-developer-template.extension/` and the HelloWorld scaffold path in this template; put project-specific `.tab` content in your own extension repo.

## Contributing
- Contribute only to static template files under [`CodexWorkspace/human/`](CodexWorkspace/human/) and [`CodexWorkspace/skills/`](CodexWorkspace/skills/) (including versioned `pyrevit-revit-20xx` skills), plus the Hello World scaffold.
- Call for contributions: add guidance for any Revit version by extending or adding `pyrevit-revit-20xx` skills.
- Keep project-specific planning artifacts in [`CodexWorkspace/workspace/`](CodexWorkspace/workspace/) out of template contributions.
- Do not propose or include plans for a specific add-on.
- Keep additional `.tab` folders out of the template and project code in your extension repo.
- When updating static docs, also update [`CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md`](CodexWorkspace/skills/develop-pyrevit-extensions/references/docs_overview.md) and any relevant indexes.
- Follow the repo conventions in [`AGENTS.md`](AGENTS.md).
- Record user-visible template changes in [`CHANGELOG.md`](CHANGELOG.md).
- Use GitHub Discussions for questions and ideas: [`Discussions`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/discussions).

Return back: [`CodexWorkspace/README.md`](CodexWorkspace/README.md)
Return to root: [`README.md`](README.md)
