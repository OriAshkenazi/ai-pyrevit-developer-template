# Troubleshooting Cheatsheet

## Extension Does Not Show Up
- In Revit: `pyRevit` tab -> `Settings` -> `Extensions`: confirm `ai-pyrevit-developer-template.extension` is added.
- Reload pyRevit (if you see a `Reload` button) or restart Revit after changing extension folders.
- Make sure you did not rename or delete the `ai-pyrevit-developer-template.extension` folder.

## pyRevit Not Installed Or Not Loading
- Follow the steps in [`environment_setup.md`](environment_setup.md).
- Make sure you launched Revit after installing pyRevit.

## Tab Or Button Not Visible
- Compare your folder naming to the Hello World scaffold: [`../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/).
- Ensure a `script.py` file exists directly inside the `.pushbutton` folder.
- Avoid extra nesting (the `.pushbutton` folder should be the last level).

## Button Shows But Nothing Happens
- Open the pyRevit Output window (from the `pyRevit` tab) and look for errors.
- Copy the error text and the `script.py` contents when asking for help.

## Safe Testing Tips
- Test on a copy of a model, not your production file.
- Use Revit Undo if the command makes unintended changes.

## When Asking For Help
- Include the error message and the file path of `script.py`.
- Describe what you clicked, what you expected, and what happened.

Return back: [`README.md`](README.md)
Return to root: [`../../../README.md`](../../../README.md)
