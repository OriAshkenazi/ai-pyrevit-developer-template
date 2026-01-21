# pyRevit Guides (Agent Only)

Imported reference notes for pyRevit development (from `pbs-handler` docs).

## What Is pyRevit
pyRevit lets you add custom buttons to Revit. Each button runs a `script.py` file in a specific folder structure.

## First Command Walkthrough (No Coding)
If you want a quick validation, use the scaffolded command in [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab).

1. Create a folder path like the Hello World scaffold: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton).
2. Copy [`CodexWorkspace/docs/agent/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/scripts/new_command_template.py) into that folder as `script.py`.
3. Restart Revit so the new button appears.
4. Click the button and confirm the placeholder message shows.
5. If it does not show, check [`CodexWorkspace/docs/human/troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/human/troubleshooting.md).

## Reference Notes
- Engine selection (IronPython vs CPython): [`cpython-ironpython-development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/pyrevit/cpython-ironpython-development.md)
- Element selection + parameter access patterns: [`elements-selection.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/pyrevit/elements-selection.md)
- Extension structure and deployment patterns: [`script-architecture.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/pyrevit/script-architecture.md)

Return back: [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
