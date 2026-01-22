# Start Here (No Coding Required)

This guide gets the template loaded in Revit, verifies it works (Hello World), and helps you create your first simple button by copying an example.

## Quick Setup Check (Hello World)
1. Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
2. Get this repo onto your machine (choose one option):
   - Download ZIP:
     - Open https://github.com/OriAshkenazi/ai-pyrevit-developer-template.
     - Click **Code** > **Download ZIP**.
     - Open the downloaded zip and choose **Extract All...**.
     - Pick a folder you control (example: `C:/revit-extensions/ai-pyrevit-developer-template`) and extract.
   - Use Git (optional):
     - Open PowerShell.
     - Move to the folder where you want the repo (example: `cd C:/revit-extensions`).
     - Run:
       ```
       git clone https://github.com/OriAshkenazi/ai-pyrevit-developer-template.git
       ```
3. Confirm the folder you extracted/cloned contains:
   - `ai-pyrevit-developer-template.extension` (this is what pyRevit loads)
   - `CodexWorkspace` (docs + planning workspace)
4. Add the extension to pyRevit:
   - Open Revit.
   - Go to the `pyRevit` tab -> `Settings`.
   - Under `Extensions`, click **Add** and select:
     - `ai-pyrevit-developer-template.extension`

   Common wrong choices (don't select these):
   - The parent repo folder (it contains `CodexWorkspace`)
   - `CodexWorkspace`
   - `HelloWorld.tab`
5. Reload pyRevit (or restart Revit):
   - If you see a `Reload` button in the `pyRevit` tab, use it.
   - Otherwise, restart Revit so the extension loads.
6. Confirm the Hello World tab loads:
   - Extension bundle: [`../../../ai-pyrevit-developer-template.extension/`](../../../ai-pyrevit-developer-template.extension/)
   - Tab: [`../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/`](../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/)
   - Panel: [`../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/`](../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/)
   - Button: [`../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/)
   - Script: [`../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](../../../ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)
7. Click the Hello World button and confirm the alert appears.
8. If the tab or button does not show up, check [`troubleshooting.md`](troubleshooting.md).

## Build Tools With Codex (AI) (Primary Workflow)
This repo is designed for AI-assisted pyRevit development. You write a short plan, a planning model turns it into tasks, and Codex (the coding agent) implements those tasks by editing files in this repo.

Model choice (important):
- Planning + task writing: use `gpt-5.2` (or "GPT-5.2") in your chat tool.
- Implementation: use Codex with `gpt-5.2-codex` (the model that can edit files and run commands).

1. Write a plan:
   - Copy [`../agent/templates/plan_template.md`](../agent/templates/plan_template.md) to [`../../workspace/plans/`](../../workspace/plans/) and name it `<feature>_plan.md`.
   - Fill it in using plain language (goal, inputs, outputs, steps).
2. Planning phase (model: `gpt-5.2`):
   - Open [`../../prompts/planning_phase_prompt.txt`](../../prompts/planning_phase_prompt.txt) and paste it into your chat.
   - Include the contents of your plan file (`CodexWorkspace/workspace/plans/<feature>_plan.md`).
   - Save the output as [`../../workspace/development.md`](../../workspace/development.md).
3. Generate tasks (model: `gpt-5.2`):
   - Open [`../../prompts/seed_code_tasks_prompt.txt`](../../prompts/seed_code_tasks_prompt.txt) and run it with your plan + `development.md`.
   - Save the output under [`../../workspace/tasks/`](../../workspace/tasks/) (example: `first_feature_tasks.md`).
4. Implement with Codex (model: `gpt-5.2-codex`):
   - Open Codex in this repo (the coding agent that can edit files and run commands).
   - Tell it to implement the next task file, for example: `Implement CodexWorkspace/workspace/tasks/first_feature_tasks.md`.
5. Validate in Revit:
   - Reload pyRevit (or restart Revit) and test the button in a safe model copy.

## Optional: Make Your First Button (Manual Copy + Edit)
You'll copy the existing Hello World button folder, rename it, and change the message.

1. Copy this folder:
   - `ai-pyrevit-developer-template.extension/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton`
2. Paste it next to the original, and rename the copied folder to something like:
   - `MyFirstTool.pushbutton`
3. Open the copied `script.py` and change the text inside the `forms.alert(...)` call.
4. Reload pyRevit (or restart Revit).
5. Click your new button and confirm the new message appears.

If it doesn't show up, it's almost always one of these:
- The folder name must end with `.pushbutton`
- The file must be named exactly `script.py` and sit directly inside the `.pushbutton` folder
- Avoid extra nesting (no `MyFirstTool.pushbutton/something/script.py`)

## Required pyRevit Folder Structure (Simple Rule)
pyRevit shows buttons based on folder names:

- `<Tab>.tab/`
  - `<Panel>.panel/`
    - `<Button>.pushbutton/`
      - `script.py`

## Glossary (Quick Definitions)
- **Extension**: a folder that ends with `.extension` (this is what you add in pyRevit Settings).
- **Tab / Panel / Button**: how your tools show up on the Revit ribbon (a button lives inside a `.pushbutton` folder).
- **`script.py`**: the file that runs when you click the button.
- **Reload**: refreshes pyRevit without a full Revit restart (if available in your pyRevit version).

## Where To Go Next
- Troubleshooting: [`troubleshooting.md`](troubleshooting.md)
- Environment setup notes (advanced): [`environment_setup.md`](environment_setup.md)
- Agent workflow index (advanced): [`../agent/README.md`](../agent/README.md)

Return back: [`../README.md`](../README.md)
Return to root: [`../../../README.md`](../../../README.md)
