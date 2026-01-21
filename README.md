# AI pyRevit Developer Template

Template scaffold for pyRevit development with CodexWorkspace docs and workflow guidance. A Hello World `.tab` scaffold is included to validate setup.

## Start Here (Beginner)
1. Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
2. Get this repo onto your machine (choose one option):
   - Download ZIP: open https://github.com/OriAshkenazi/ai-pyrevit-developer-template, click **Code** > **Download ZIP**, then extract it to a folder you control (example: `C:\revit-extensions\ai-pyrevit-developer-template`).
   - Use Git: open PowerShell in the folder where you want the repo, then run:
     ```
     git clone https://github.com/OriAshkenazi/ai-pyrevit-developer-template.git
     ```
3. Add the repo folder as a pyRevit extension:
   - Open Revit.
   - Go to the pyRevit tab > Settings.
   - Under Extensions, click **Add** and select the repo folder (the folder that contains [`HelloWorld.tab`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab) and [`CodexWorkspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace)).
4. Restart Revit so the extension loads.
5. Confirm the scaffolded Hello World tab appears (see [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab)) and click the button to verify setup.
6. Create a plan in [`CodexWorkspace/docs/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans) (copy from [`CodexWorkspace/docs/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md)).
7. Follow [`CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md) to create [`CodexWorkspace/docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md) and tasks.
8. When ready, create a command folder and copy [`CodexWorkspace/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py) to `script.py`.
9. Choose a logo by adding `icon.png` to the pushbutton folder.
10. Test the command in Revit.

For a slower, visual walkthrough and definitions, start with [`CodexWorkspace/docs/guides/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/README.md).

## Notes
- Use [`CodexWorkspace/docs/reference/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/reference) for Revit 2023 guidance.
- The template includes a Hello World scaffold under [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab); keep your project-specific `.tab` content in your own extension repo or rename the scaffold as needed.

## Contributing
- Contribute only to the static template files (prompts, guides, checklists, reference, templates, and scripts).
- Keep project-specific planning artifacts in [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) out of template contributions.
- Do not propose or include plans for a specific add-on.
- Keep additional `.tab` folders out of the template and project code in your extension repo.
- When updating static docs, also update [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md) and any relevant indexes.
- Follow the repo conventions in [`CodexWorkspace/docs/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs) and [`AGENTS.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/AGENTS.md).

Return back: [`CodexWorkspace/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
