# pyrevit_structure

pyRevit commands live under `<Tab>.tab/<Panel>.panel/<Button>.pushbutton/`.

Notes:
- Keep transactions explicit (`Start`/`Commit`, `RollBack` on exceptions).
- Convert Python iterables to .NET collections at Revit API boundaries when required.
