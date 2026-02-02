# LLM Prompting Guidelines

For the full workflow, use [`agent_ai_orchestrated_dev_methodology.md`](agent_ai_orchestrated_dev_methodology.md).

Store planning artifacts in [`CodexWorkspace/workspace/`](../../../workspace/) and keep static templates in [`assets/templates/`](../assets/templates/).

## Model Selection
- gpt-5.2: planning, task generation, reviews, backlog, and next-feature analysis.
- gpt-5.2-codex: implementation and documentation updates.

## Plain-Language Prompts
- "Explain the folder and file structure required for this command."
- "Write a numbered plan with explicit inputs, outputs, and checks."
- "Show how to test safely and what to capture if a step fails."
- "Summarize the expected data flow in plain language."

## Technical Prompts
1. Specify the exact Revit APIs to use (e.g., `FilteredElementCollector`, `ViewSheet.Duplicate`).
2. Declare inputs and outputs, including types and expected containers.
3. State error-handling expectations: validate element existence, modifiability, and parameter presence; describe rollback behavior.
4. Ask for validation hooks such as preconditions and postconditions for each step.
5. When reviewing code, share the full context (imports, surrounding functions, usage patterns) plus performance and UI considerations.
6. Request docstrings that include parameter types, exceptions, and a transaction-scoped usage example.

Return back: [`agent_overview.md`](agent_overview.md)
Return to root: [`README.md`](../../../../README.md)
