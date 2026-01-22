# AI pyRevit Developer Template

Template scaffold for pyRevit development with a curated CodexWorkspace and a Hello World add-on for validation.

## Start Here
- Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
- Using this in Revit (no coding): [`CodexWorkspace/docs/human/README.md`](CodexWorkspace/docs/human/README.md).
- Building tools (agent workflow + references): [`CodexWorkspace/docs/agent/README.md`](CodexWorkspace/docs/agent/README.md).
- Planning artifacts (plans, development.md, tasks, reviews, backlog): [`CodexWorkspace/workspace/README.md`](CodexWorkspace/workspace/README.md).

## What This Repo Contains
- pyRevit extension bundle (what you add in pyRevit Settings): [`ai-pyrevit-developer-template.extension/`](ai-pyrevit-developer-template.extension/).
- Hello World scaffold (inside the extension bundle): [`ai-pyrevit-developer-template.extension/HelloWorld.tab/`](ai-pyrevit-developer-template.extension/HelloWorld.tab/).
- Static docs (human + agent): [`CodexWorkspace/docs/`](CodexWorkspace/docs/).
- Prompt library for gpt-5.2 and gpt-5.2-codex: [`CodexWorkspace/prompts/`](CodexWorkspace/prompts/).
- Script templates and harnesses: [`CodexWorkspace/docs/agent/scripts/`](CodexWorkspace/docs/agent/scripts/).

## Notes
- Use [`CodexWorkspace/docs/agent/pyrevit/revit_version_documentation/`](CodexWorkspace/docs/agent/pyrevit/revit_version_documentation/) for Revit 2023 guidance.
- Keep the Hello World scaffold in this template; put project-specific `.tab` content in your own extension repo or rename the scaffold as needed.

## Contributing
- Contribute only to static template files: [`CodexWorkspace/docs/human/`](CodexWorkspace/docs/human/), [`CodexWorkspace/docs/agent/`](CodexWorkspace/docs/agent/), [`CodexWorkspace/prompts/`](CodexWorkspace/prompts/), [`CodexWorkspace/docs/agent/scripts/`](CodexWorkspace/docs/agent/scripts/), and the Hello World scaffold.
- Keep project-specific planning artifacts in [`CodexWorkspace/workspace/`](CodexWorkspace/workspace/) out of template contributions.
- Do not propose or include plans for a specific add-on.
- Keep additional `.tab` folders out of the template and project code in your extension repo.
- When updating static docs, also update [`CodexWorkspace/docs/README.md`](CodexWorkspace/docs/README.md) and any relevant indexes.
- Follow the repo conventions in [`AGENTS.md`](AGENTS.md).
- Use GitHub Discussions for questions and ideas: [`Discussions`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/discussions).

Return back: [`CodexWorkspace/README.md`](CodexWorkspace/README.md)
Return to root: [`README.md`](README.md)
