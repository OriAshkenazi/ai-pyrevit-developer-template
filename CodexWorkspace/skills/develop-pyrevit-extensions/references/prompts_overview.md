# Prompt Snippets

Use these as copy/paste starters to keep output consistent with target Revit version patterns in the versioned skills (e.g., [`pyrevit-revit-2023`](../../pyrevit-revit-2023/), [`pyrevit-revit-2024`](../../pyrevit-revit-2024/), [`pyrevit-revit-2025`](../../pyrevit-revit-2025/)).
Replace `{REVIT_VERSION}` placeholders in prompts with the target version.
Each prompt file indicates which model to use (gpt-5.2 for planning/review, gpt-5.2-codex for implementation).

## Workflow Prompts (Dual-Model Methodology)
- [`planning_phase_prompt.txt`](../assets/prompts/planning_phase_prompt.txt) - create [`CodexWorkspace/workspace/development.md`](../../../workspace/development.md) with architecture and milestones (gpt-5.2).
- [`seed_code_tasks_prompt.txt`](../assets/prompts/seed_code_tasks_prompt.txt) - generate initial Code-Tasks for the first feature (gpt-5.2).
- [`review_ask_task_prompt.txt`](../assets/prompts/review_ask_task_prompt.txt) - generate a review Ask-Task after a task batch (gpt-5.2).
- [`iteration_task_adjust_prompt.txt`](../assets/prompts/iteration_task_adjust_prompt.txt) - adjust subsequent tasks when conflicts appear (gpt-5.2).
- [`iteration_summary_tasks_prompt.txt`](../assets/prompts/iteration_summary_tasks_prompt.txt) - generate remediation Code-Tasks from analysis output (gpt-5.2).
- [`backlog_code_task_prompt.txt`](../assets/prompts/backlog_code_task_prompt.txt) - document non-urgent tasks in [`CodexWorkspace/workspace/backlog.md`](../../../workspace/backlog.md) (gpt-5.2).
- [`next_feature_ask_task_prompt.txt`](../assets/prompts/next_feature_ask_task_prompt.txt) - recommend the next feature based on repo state (gpt-5.2).

## Utility Prompts
- [`generate_code.txt`](../assets/prompts/generate_code.txt) - ask for implementation with explicit API choices and transactions (gpt-5.2-codex).
- [`review_optimize.txt`](../assets/prompts/review_optimize.txt) - quick technical review with performance and correctness focus (gpt-5.2).
- [`document_command.txt`](../assets/prompts/document_command.txt) - docstrings and user-facing documentation for a pyRevit command (gpt-5.2-codex).

Return back: [`docs_overview.md`](docs_overview.md)
Return to root: [`README.md`](../../../../README.md)
