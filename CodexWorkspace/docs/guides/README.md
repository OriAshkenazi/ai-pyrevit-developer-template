# Guides (Start Here)

This folder is the beginner-friendly entry point for civil engineers who are new to coding.

## Start Here (No Coding Required)
1. Install pyRevit (see `environment_setup.md`).
2. Add this repo as an extension (pyRevit Settings > Extensions > Add).
3. Restart Revit so the extension loads.
4. Create a plan in `../plans/` using `../plans/plan_template.md`.
5. Ask Codex: "Turn this plan into a step-by-step development plan and tasks."
6. Create a command folder: `<Tab>.tab/<Panel>.panel/<Button>.pushbutton/`.
7. Copy `../../scripts/new_command_template.py` to `script.py`.
8. Add `icon.png` to the pushbutton folder and test in Revit.

[Screenshot: pyRevit Settings > Extensions > Add]
[Screenshot: Folder selected in Extensions list]
[Screenshot: New tab shows up in Revit]

## Glossary (Plain Language)
- Extension: The folder you add in pyRevit Settings so your tools show up.
- Tab: A top-level toolbar name in Revit.
- Panel: A group of buttons inside a tab.
- Pushbutton: The clickable command button.
- script.py: The file that runs when the button is clicked.
- icon.png: The button image.

## Where To Go Next
- "First Command Walkthrough": `pyrevit/README.md`
- Common issues: `troubleshooting.md`
- How to ask Codex for help: `llm_prompting_guidelines.md`
