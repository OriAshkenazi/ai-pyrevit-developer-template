# Prompt Snippets

Use these as copy/paste starters to keep output consistent with Revit 2023 patterns in `CodexWorkspace/docs/reference/`.
Each prompt file indicates which model to use (gpt-5.2 for planning/review, gpt-5.2-codex for implementation).

## Workflow Prompts (Dual-Model Methodology)
- `planning_phase_prompt.txt` - create `CodexWorkspace/docs/workspace/development.md` with architecture and milestones (gpt-5.2).
- `seed_code_tasks_prompt.txt` - generate initial Code-Tasks for the first feature (gpt-5.2).
- `review_ask_task_prompt.txt` - generate a review Ask-Task after a task batch (gpt-5.2).
- `iteration_task_adjust_prompt.txt` - adjust subsequent tasks when conflicts appear (gpt-5.2).
- `iteration_summary_tasks_prompt.txt` - generate remediation Code-Tasks from analysis output (gpt-5.2).
- `backlog_code_task_prompt.txt` - document non-urgent tasks in CodexWorkspace/docs/workspace/backlog.md (gpt-5.2).
- `next_feature_ask_task_prompt.txt` - recommend the next feature based on repo state (gpt-5.2).

## Utility Prompts
- `generate_code.txt` - ask for implementation with explicit API choices and transactions (gpt-5.2-codex).
- `review_optimize.txt` - quick technical review with performance and correctness focus (gpt-5.2).
- `document_command.txt` - docstrings and user-facing documentation for a pyRevit command (gpt-5.2-codex).
