# Start Here

This guide covers setup, validates pyRevit with the Hello World scaffold, and defines the plan handoff to the agent.

## Quick Setup Check (Hello World)
1. Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
2. Get this repo onto your machine (choose one option):
   - Download ZIP:
     - Open https://github.com/OriAshkenazi/ai-pyrevit-developer-template.
     - Click **Code** > **Download ZIP**.
     - Open the downloaded zip and choose **Extract All...**.
     - Pick a folder you control (example: `C:/revit-extensions/ai-pyrevit-developer-template`) and extract.
     - Confirm the extracted folder contains [`HelloWorld.tab`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab) and [`CodexWorkspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace).
   - Use Git:
     - Open PowerShell (press the Windows key, type `PowerShell`, and open it).
     - Move to the folder where you want the repo (example: `cd C:/revit-extensions`).
     - Run:
       ```
       git clone https://github.com/OriAshkenazi/ai-pyrevit-developer-template.git
       ```
     - Confirm the new folder contains [`HelloWorld.tab`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab) and [`CodexWorkspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace).
3. Add the repo folder as an extension:
   - Open Revit.
   - Go to the pyRevit tab > Settings.
   - Under Extensions, click **Add** and select the repo folder.
4. Restart Revit so the extension loads.
5. Confirm the Hello World tab loads:
   - Tab: [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab)
   - Panel: [`HelloWorld.tab/GettingStarted.panel/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel)
   - Button: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton)
   - Script: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)
6. Click the Hello World button and confirm the alert appears.
7. If the tab or button does not show up, check [`troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/human/troubleshooting.md).

## Required pyRevit Folder Structure
pyRevit recognizes commands by folder naming. Your extension root is the repo folder. A command must live in a `.pushbutton` folder with a `script.py` inside it.

Use this structure:
- [`<Tab>.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab)
  - [`<Panel>.panel/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel)
    - [`<Button>.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton)
      - [`script.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)

The agent uses the same `.tab/.panel/.pushbutton` structure when adding commands; keep the suffixes and the `script.py` entrypoint.

## Workflow Handoff (Plan -> Agent)
1. Copy [`CodexWorkspace/docs/agent/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/templates/plan_template.md) to [`CodexWorkspace/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/workspace/plans) and name it `<feature>_plan.md`.
2. Capture product goals, inputs, outputs, constraints, and technical notes in the plan (plans are treated as product docs and technical docs).
3. Hand the plan to the agent. The agent uses gpt-5.2 to create [`CodexWorkspace/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/workspace/development.md) and tasks, then uses gpt-5.2-codex to implement the code.

## Where To Go Next
- Agent workflow index: [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md)
- Troubleshooting: [`troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/human/troubleshooting.md)

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
