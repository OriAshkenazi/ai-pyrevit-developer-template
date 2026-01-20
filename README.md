# ai-pyrevit-developer-template

Minimal pyRevit extension template with CodexWorkspace docs. This repo ships without any `.tab` folders so the template stays clean.

## Quickstart
1. Clone this repo.
2. Add the repo folder as a pyRevit extension (pyRevit Settings > Extensions > Add).
3. Create a plan file in `CodexWorkspace/docs/plans/` (start from `plan_template.md`).
4. Ask Codex to expand the plan into a full development plan and tasks.
5. Scaffold a command: create `<Tab>.tab/<Panel>.panel/<Button>.pushbutton/` and copy `CodexWorkspace/scripts/new_command_template.py` to `script.py`.
6. Choose a logo by adding `icon.png` to the pushbutton folder.
7. Test the command in Revit.

## Notes
- Use `CodexWorkspace/docs/reference/` for Revit 2023 guidance.
- Keep `.tab` content project-specific and out of the template.

## Contributing
- Create a plan in `CodexWorkspace/docs/plans/` before starting work.
- Keep `.tab` folders out of the template and project code in your extension repo.
- Follow the repo conventions in `CodexWorkspace/docs/` and `AGENTS.md`.
