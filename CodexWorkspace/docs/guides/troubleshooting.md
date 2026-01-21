# Troubleshooting Cheatsheet

## Extension Does Not Show Up
- Confirm the repo folder is added in pyRevit Settings > Extensions.
- Restart Revit after adding or changing folders.
- Make sure you did not rename or delete the extension folder.

## pyRevit Not Installed Or Not Loading
- Follow the steps in `environment_setup.md`.
- Make sure you launched Revit after installing pyRevit.

## Tab or Button Not Visible
- Check folder naming: `<Tab>.tab/<Panel>.panel/<Button>.pushbutton/`.
- Ensure a `script.py` file exists directly inside the pushbutton folder.
- Avoid extra nesting (the pushbutton folder should be the last level).

## Button Shows But Nothing Happens
- Open the pyRevit Output window (from the pyRevit tab) and look for errors.
- Copy the error text and the `script.py` contents when asking for help.

## Logging
- Use the pyRevit Output window to view error details.
- Copy the error text into your plan or gpt-5.2 request.

## Safe Testing Tips
- Test on a copy of a model, not your production file.
- Use Revit Undo if the command makes unintended changes.

## When Asking For Help (gpt-5.2 or gpt-5.2-codex)
- Include the error message and the file path of `script.py`.
- Describe what you clicked, what you expected, and what happened.
