# ai-pyrevit-developer-template

Template scaffold for pyRevit development with CodexWorkspace docs and workflow guidance. This repo is built for civil engineers who want clear, step-by-step instructions and minimal coding. `.tab` folders are intentionally excluded so you can add project-specific commands later.

## Start Here (Beginner)
1. Clone this repo.
2. Add the repo folder as a pyRevit extension (pyRevit Settings > Extensions > Add).
3. Restart Revit so the extension loads.
4. Create a plan in `CodexWorkspace/docs/plans/` (start from `plan_template.md`).
5. Ask Codex to turn that plan into a full development plan and tasks.
6. When ready, create a command folder and copy `CodexWorkspace/scripts/new_command_template.py` to `script.py`.
7. Choose a logo by adding `icon.png` to the pushbutton folder.
8. Test the command in Revit.

For a slower, visual walkthrough and definitions, start with `CodexWorkspace/docs/guides/README.md`.

## Notes
- Use `CodexWorkspace/docs/reference/` for Revit 2023 guidance.
- Keep `.tab` content project-specific and out of the template.

## Contributing
- Contribute only to the template itself (prompts, best-practices, Revit version guidance).
- Do not propose or include plans for a specific add-on.
- Keep `.tab` folders out of the template and project code in your extension repo.
- Follow the repo conventions in `CodexWorkspace/docs/` and `AGENTS.md`.
