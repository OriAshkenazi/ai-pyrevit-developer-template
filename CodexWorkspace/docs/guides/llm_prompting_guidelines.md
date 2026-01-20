# LLM Prompting Guidelines

1. Specify the exact Revit APIs to use (e.g., `FilteredElementCollector`, `ViewSheet.Duplicate`).
2. Declare inputs and outputs, including types and expected containers.
3. State error-handling expectations: validate element existence, modifiability, and parameter presence; describe rollback behavior.
4. Ask for validation hooks such as preconditions and postconditions for each step.
5. When reviewing code, share the full context (imports, surrounding functions, usage patterns) plus performance and UI considerations.
6. Request docstrings that include parameter types, exceptions, and a transaction-scoped usage example.

