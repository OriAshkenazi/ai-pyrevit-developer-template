# pyRevit Guides (Agent Only)

Imported reference notes for pyRevit development (from `pbs-handler` docs).

## What Is pyRevit
pyRevit lets you add custom buttons to Revit. Each button runs a `script.py` file in a specific folder structure.

## First Command Walkthrough (No Coding)
Use the human guide for the smoothest path (setup + first button copy/edit):
- [`../../human/README.md`](../../human/README.md)

Reference scaffold paths (for agents):
- Extension bundle: [`../../../../ai-pyrevit-developer-template.extension/`](../../../../ai-pyrevit-developer-template.extension/)
- Hello World pushbutton: [`../../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](../../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/)

If you're adding a new command, start from:
- [`../scripts/new_command_template.py`](../scripts/new_command_template.py)

## Reference Notes
- Engine selection (IronPython vs CPython): [`cpython-ironpython-development.md`](cpython-ironpython-development.md)
- Element selection + parameter access patterns: [`elements-selection.md`](elements-selection.md)
- Extension structure and deployment patterns: [`script-architecture.md`](script-architecture.md)

Return back: [`../README.md`](../README.md)
Return to root: [`../../../../README.md`](../../../../README.md)
