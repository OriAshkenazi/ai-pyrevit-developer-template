# Environment Setup Snapshot

If you are only *using* the buttons in Revit, you generally do not need to install Python separately—installing pyRevit is enough.

If you are *building* tools (editing `script.py` files), these notes help you avoid common setup issues:

- pyRevit supports **IronPython 2.7** and **CPython 3.x**. Use an explicit script header:
  - `#! python` for Revit/UI-first scripts (stable Revit API + pyRevit UX patterns)
  - `#! python3` when you need Python 3 features and external libraries (e.g., `openpyxl`, `pandas`)
- pyRevitLabs notes the CPython engine is under active development and may be unstable; prefer IronPython unless you need C-based packages (e.g., `numpy`, `scipy`).
- When mixing engines, keep **Revit API read/write + UI orchestration** in IronPython and offload heavy processing to CPython via a small file-based interface (e.g., JSON) documented in your tool.
- Target **Autodesk Revit 2023** APIs; avoid legacy `Document.New*` patterns.
- Treat ElementIds as opaque tokens (Revit 2023 moves toward 64-bit ids).
- Favor modern creation APIs (e.g., `Floor.Create`, `ViewSheet.Duplicate`) over removed `Document.New*` calls.

Return back: [`README.md`](README.md)
Return to root: [`../../../README.md`](../../../README.md)

