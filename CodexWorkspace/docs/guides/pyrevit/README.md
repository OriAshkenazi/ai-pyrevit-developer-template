# PyRevit Guides

Imported reference notes for pyRevit development (from `pbs-handler` docs).

## What Is pyRevit
pyRevit lets you add custom buttons to Revit. Each button runs a `script.py` file in a specific folder structure.

## First Command Walkthrough (No Coding)
1. Create a folder path like: `MyTools.tab/MyPanel.panel/MyCommand.pushbutton/`.
2. Copy [`CodexWorkspace/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py) into that folder as `script.py`.
3. Restart Revit so the new button appears.
4. Click the button and confirm the placeholder message shows.
5. If it does not show, check [`../troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/troubleshooting.md).

- Engine selection (IronPython vs CPython): [`cpython-ironpython-development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/pyrevit/cpython-ironpython-development.md)
- Element selection + parameter access patterns: [`elements-selection.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/pyrevit/elements-selection.md)
- Extension structure and deployment patterns: [`script-architecture.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/pyrevit/script-architecture.md)

Return back: [`CodexWorkspace/docs/guides/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
