# pyRevit Guides (Agent Only)

Imported reference notes for pyRevit development (from `pbs-handler` docs).

## What Is pyRevit
pyRevit lets you add custom buttons to Revit. Each button runs a `script.py` file in a specific folder structure.

## First Command Walkthrough (No Coding)
Use the human guide for the smoothest path (setup + first button copy/edit):
- [`CodexWorkspace/human/README.md`](../../../human/README.md)

Reference scaffold paths (for agents):
- Extension bundle: [`../../../../ai-pyrevit-developer-template.extension/`](../../../../ai-pyrevit-developer-template.extension/)
- Hello World pushbutton: [`../../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](../../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/)

If you're adding a new command, start from:
- [`../scripts/new_command_template.py`](../scripts/new_command_template.py)

## Reference Notes
- Extension structure and deployment patterns: [`pyrevit_script_architecture.md`](pyrevit_script_architecture.md)

## Versioned Guidance
Engine selection, element selection, and API rules live in the versioned skills.
- Revit 2023 guidance (engine selection, element selection, API rules): [`CodexWorkspace/skills/pyrevit-revit-2023/`](../../pyrevit-revit-2023/)
- Revit 2024 guidance (scaffold): [`CodexWorkspace/skills/pyrevit-revit-2024/`](../../pyrevit-revit-2024/)
- Revit 2025 guidance (scaffold): [`CodexWorkspace/skills/pyrevit-revit-2025/`](../../pyrevit-revit-2025/)

Return back: [`agent_overview.md`](agent_overview.md)
Return to root: [`../../../../README.md`](../../../../README.md)
