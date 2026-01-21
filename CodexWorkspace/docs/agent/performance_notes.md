# Performance Notes

- Batch related edits inside a single `Transaction` when possible; use `TransactionGroup` for staged commits.
- Filter early when using `FilteredElementCollector` to reduce unnecessary iteration.
- Cache lookups such as Level or Type mappings instead of re-running document queries.
- Release large Python or .NET collections once they are no longer required to avoid memory pressure.
- Treat `ElementId` values as opaque tokens; do not rely on a specific integer range.

Return back: [`CodexWorkspace/docs/agent/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/agent/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
