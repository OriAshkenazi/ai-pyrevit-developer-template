# Environment Setup Snapshot

- pyRevit supports **IronPython 2.7** and **CPython 3.x**. Use an explicit script header:
  - `#! python` for Revit/UI-first scripts (stable Revit API + pyRevit UX patterns)
  - `#! python3` when you need Python 3 features and external libraries (e.g., `openpyxl`, `pandas`)
- pyRevitLabs notes the CPython engine is under active development and may be unstable; prefer IronPython unless you need C-based packages (e.g., `numpy`, `scipy`). For CPython, ensure a 64-bit environment and use `PYTHONPATH` for additional module search paths.
- When mixing engines, keep **Revit API read/write + UI orchestration** in IronPython and offload heavy processing to CPython via a small file-based interface (e.g., JSON) documented in your tool.
- Target **Autodesk Revit 2023** APIs; remove or avoid 2019 compatibility shims.
- Keep a consistent CPython interpreter/version across the team when using CPython scripts to avoid behavioral drift.
- Treat ElementIds as opaque tokens (Revit 2023 moves toward 64-bit ids).
- Favor modern creation APIs (e.g., `Floor.Create`, `ViewSheet.Duplicate`) over removed `Document.New*` calls.
