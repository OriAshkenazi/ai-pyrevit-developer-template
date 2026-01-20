# Troubleshooting Cheatsheet

- Split long-running transactions; keep commits short to avoid blocking the UI.
- Ensure API calls receive the correct .NET collection types.
- Add defensive checks for missing parameters, null elements, or unmodifiable states.
- Watch for memory usage in long sessions and release large lists or dictionaries.
- Replace legacy creation patterns (`Document.New*`, old analytical APIs) with their Revit 2023 counterparts.
- When seeking LLM assistance, provide the exception message, relevant code block, transaction state, and performance constraints.

