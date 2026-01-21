# AI pyRevit Developer Template

Template scaffold for pyRevit development with CodexWorkspace docs and workflow guidance. This repo is built for civil engineers who want clear, step-by-step instructions and minimal coding. `.tab` folders are intentionally excluded so you can add project-specific commands later.

## Start Here (Beginner)
1. Clone this repo.
2. Add the repo folder as a pyRevit extension (pyRevit Settings > Extensions > Add).
3. Restart Revit so the extension loads.
4. Create a plan in [`CodexWorkspace/docs/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans) (copy from [`CodexWorkspace/docs/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md)).
5. Follow [`CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md) to create [`CodexWorkspace/docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md) and tasks.
6. When ready, create a command folder and copy [`CodexWorkspace/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py) to `script.py`.
7. Choose a logo by adding `icon.png` to the pushbutton folder.
8. Test the command in Revit.

For a slower, visual walkthrough and definitions, start with [`CodexWorkspace/docs/guides/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/README.md).

## Notes
- Use [`CodexWorkspace/docs/reference/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/reference) for Revit 2023 guidance.
- Keep `.tab` content project-specific and out of the template.

## Contributing
- Contribute only to the static template files (prompts, guides, checklists, reference, templates, and scripts).
- Keep project-specific planning artifacts in [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) out of template contributions.
- Do not propose or include plans for a specific add-on.
- Keep `.tab` folders out of the template and project code in your extension repo.
- When updating static docs, also update [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md) and any relevant indexes.
- Follow the repo conventions in [`CodexWorkspace/docs/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs) and [`AGENTS.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/AGENTS.md).

Return back: [`CodexWorkspace/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
