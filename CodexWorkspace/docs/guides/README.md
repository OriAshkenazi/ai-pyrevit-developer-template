# Guides (Start Here)

This guide walks you through setup, validates your pyRevit installation with a scaffolded Hello World add-on, and then takes you through the full AI-orchestrated workflow.

## Quick Setup Check (Hello World)
1. Install pyRevit: [Install pyRevit](https://pyrevitlabs.notion.site/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d).
2. Get this repo onto your machine (choose one option):
   - Download ZIP: open the repo page at https://github.com/OriAshkenazi/ai-pyrevit-developer-template, click **Code** > **Download ZIP**, then extract it to a folder you control (example: `C:\revit-extensions\ai-pyrevit-developer-template`).
   - Use Git: open PowerShell in the folder where you want the repo, then run:
     ```
     git clone https://github.com/OriAshkenazi/ai-pyrevit-developer-template.git
     ```
3. Add the repo folder as an extension:
   - Open Revit.
   - Go to the pyRevit tab > Settings.
   - Under Extensions, click **Add** and select the repo folder (the folder that contains [`HelloWorld.tab`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab) and [`CodexWorkspace`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace)).
4. Restart Revit so the extension loads.
5. Confirm the Hello World tab loads:
   - Tab: [`HelloWorld.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab)
   - Panel: [`HelloWorld.tab/GettingStarted.panel/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel)
   - Button: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton)
   - Script: [`HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)
6. Click the Hello World button and confirm the alert appears.
7. If the tab or button does not show up, check [`troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/troubleshooting.md).

## Required pyRevit Folder Structure
pyRevit recognizes commands by folder naming. Your extension root is the repo folder. A command must live in a `.pushbutton` folder with a `script.py` inside it.

Use this structure:
- [`<Tab>.tab/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab)
  - [`<Panel>.panel/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel)
    - [`<Button>.pushbutton/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton)
      - [`script.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/HelloWorld.tab/GettingStarted.panel/HelloWorld.pushbutton/script.py)

You can rename the Hello World folders or create new ones, as long as you keep the `.tab/.panel/.pushbutton` suffixes and the `script.py` entrypoint.

## Development Workflow (Dual-Model Methodology)
1. Copy [`CodexWorkspace/docs/templates/plan_template.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/templates/plan_template.md) to [`CodexWorkspace/docs/workspace/plans/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace/plans) and name it `<feature>_plan.md`.
2. Use gpt-5.2 with [`CodexWorkspace/prompts/planning_phase_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/planning_phase_prompt.txt) to create [`CodexWorkspace/docs/workspace/development.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/development.md).
3. Use gpt-5.2 with [`CodexWorkspace/prompts/seed_code_tasks_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/seed_code_tasks_prompt.txt) to generate the first Code-Task batch.
4. Create your command folder using the required `.tab/.panel/.pushbutton` structure and start from [`CodexWorkspace/scripts/new_command_template.py`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/scripts/new_command_template.py).
5. Implement each Code-Task with gpt-5.2-codex and update docs in the same task.
6. Use gpt-5.2 with [`CodexWorkspace/prompts/review_ask_task_prompt.txt`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/prompts/review_ask_task_prompt.txt) to review the batch.
7. Capture non-urgent tasks in [`CodexWorkspace/docs/workspace/backlog.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/workspace/backlog.md).
8. Repeat using the iteration prompts as needed.

## Where To Go Next
- Full AI workflow: [`ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md)
- First command walkthrough: [`pyrevit/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/pyrevit/README.md)
- Troubleshooting: [`troubleshooting.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/troubleshooting.md)
- Prompting guidelines: [`llm_prompting_guidelines.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/llm_prompting_guidelines.md)

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
