# LLM Prompting Guidelines

For the full workflow, use [`CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/ai_orchestrated_dev_methodology.md).
Store planning artifacts in [`CodexWorkspace/docs/workspace/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/workspace) and keep static templates in [`CodexWorkspace/docs/templates/`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/tree/main/CodexWorkspace/docs/templates).

## Model Selection
- gpt-5.2: planning, task generation, reviews, backlog, and next-feature analysis.
- gpt-5.2-codex: implementation and documentation updates.

## Plain-Language Prompts
- "Explain this in plain language and list the steps."
- "I do not code. What folders and files should I create?"
- "Write a plan I can follow with numbered steps."
- "Show me how to test safely and what to do if it fails."

## Technical Prompts
1. Specify the exact Revit APIs to use (e.g., `FilteredElementCollector`, `ViewSheet.Duplicate`).
2. Declare inputs and outputs, including types and expected containers.
3. State error-handling expectations: validate element existence, modifiability, and parameter presence; describe rollback behavior.
4. Ask for validation hooks such as preconditions and postconditions for each step.
5. When reviewing code, share the full context (imports, surrounding functions, usage patterns) plus performance and UI considerations.
6. Request docstrings that include parameter types, exceptions, and a transaction-scoped usage example.

Return back: [`CodexWorkspace/docs/guides/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
