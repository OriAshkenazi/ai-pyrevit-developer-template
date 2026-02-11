# Advanced Hooks (Opt-In)

These hooks are optional and intended for advanced mode only.

Enable:

```powershell
powershell -ExecutionPolicy Bypass -File tools/setup_advanced_hooks.ps1
```

Disable:

```powershell
powershell -ExecutionPolicy Bypass -File tools/disable_advanced_hooks.ps1
```

## Hooks
- `pre-commit`
  - `tools/check_temp_files_policy.ps1`
  - `tools/check_status_schema.ps1`
  - `tools/check_status_updated.ps1`
  - `tools/check_example_scaffold.ps1`
- `pre-push`
  - `tools/check_status_schema.ps1`
  - `tools/check_example_scaffold.ps1`
  - `tools/check_stale_doc_paths.ps1`

These hooks should never be required for beginner onboarding.
