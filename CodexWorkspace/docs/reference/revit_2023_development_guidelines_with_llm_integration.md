# Revit 2023 Development Guidelines with LLM Integration

## Environment Setup
- **Python Engine:** pyRevit supports **IronPython 2.7** (`#! python`) and **CPython 3.x** (`#! python3`). Pick the engine per script and keep it explicit in the file header.
- **Platform:** **Autodesk Revit 2023** (no 2019 compatibility in scope).
- **Framework:** **pyRevit 5.2**.
- **Required File Header:** Use `#! python` or `#! python3` at the top of each script (don’t omit it).

> Tip: Keep your team on the same default engine and CPython interpreter/version where possible, but still set the per-script header explicitly when the engine matters.

---

## Core Development Patterns

### Transaction Management
```python
from Autodesk.Revit.DB import Transaction

# Correct pattern: explicit start/commit
t = Transaction(doc, "Description of operation")
t.Start()
# ... Revit operations here ...
t.Commit()

# Not recommended in Revit API:
# ❌ with Transaction(doc, "Description") as t:
#     ...
# Use explicit Start/Commit and handle rollback via try/except.
```

**Guidelines:**
- Wrap risky operations in `try/except` and call `t.RollBack()` on failure.
- Keep transactions focused and short. Group multiple edits logically to reduce overhead, but avoid very long-running transactions that block the UI.

### .NET Collections
```python
from System.Collections.Generic import List
from Autodesk.Revit.DB import ElementId

# Create a .NET List[ElementId] for API calls that require IList<ElementId>:
ids_net = List[ElementId]()
for eid in element_ids:  # element_ids: iterable of ElementId or int
    ids_net.Add(ElementId(eid) if isinstance(eid, int) else eid)
```

**Guidelines:**
- Prefer `List[T]` (or arrays) when API signatures require .NET collections.
- Convert Python lists to .NET collections at the boundary; keep Python-native types internally for ergonomics.

---

## LLM (Codex/GPT) Interaction Guidelines

Design prompts so the LLM returns production‑ready Revit code:

### Effective Prompting
1. **Be explicit about APIs:** Name classes/methods (e.g., `FilteredElementCollector`, `ViewSheet.Duplicate`).
2. **State input/output contracts:** “Input: list[ElementId]. Output: dict[ElementId, str] of parameter values.”
3. **Include error handling requirements:** “Handle missing parameters, null elements, and invalid ids; rollback on failure.”
4. **Ask for validation hooks:** “Add checks ensuring elements are modifiable and view types are valid.”
5. **Request up-to-date patterns:** “Use Revit 2023 APIs (no obsolete calls).”

### Algorithm Development
- Break the task into steps and ask for code per step.
- Request inline comments that reference the API concept (e.g., “// uses ElementMulticlassFilter”).
- Ask for **preconditions** and **postconditions** for each step.

### Error Handling
- Ask the LLM to enumerate likely exceptions and show `try/except` blocks.
- Require rollback paths and user feedback for failures.
- Ask for defensive checks (element existence, parameter presence, modifiability).

### Code Review with LLM
Provide:
- Full function/class, imports, and context.
- Performance expectations (elements count, frequency).
- UI touch points (modal dialogs, selection requirements).

---

## Best Practices for LLM Integration

### Documentation Generation
Have the LLM produce docstrings that:
- Describe parameters and types (Revit classes).
- Document exceptions and failure modes.
- Include a minimal usage example (transaction scope shown).

### Code Optimization
Ask the LLM to:
- Consolidate transactions where safe.
- Propose bulk patterns (e.g., batched deletes via `doc.Delete(ICollection<ElementId>)`).
- Review collector usage (filter early, minimize passes).
- Comment on memory behavior and object lifetime.

### Testing Scenarios
Leverage the LLM for:
- Edge case lists (empty selection, linked elements, read-only documents).
- Test data generation strategies (small seed models).
- Validation criteria (pre/post counts, parameter invariants).
- Error scenario coverage and expected messages.

---

## Common API Patterns (Revit 2023)

### Element Collection
```python
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

walls = (FilteredElementCollector(doc)
         .OfCategory(BuiltInCategory.OST_Walls)
         .WhereElementIsNotElementType())

walls = list(walls)  # materialize if needed
```

### Parameter Access
```python
param = element.LookupParameter("Parameter Name")
if param and not param.IsReadOnly:
    t = Transaction(doc, "Update Parameter")
    t.Start()
    try:
        param.Set("New Value")
        t.Commit()
    except Exception:
        t.RollBack()
        raise
```

> In 2023+, **Parameter/Units API** uses Forge Type Ids under the hood. When creating or inspecting definitions, prefer `SpecTypeId`/`UnitTypeId` over legacy enums; avoid removed `ParameterType` patterns.

### Creating New Elements (2023 patterns)
Prefer the modern factory/static methods and current overloads; avoid removed `Document.New*` calls.
```python
# Example sketch: creating a floor boundary and using current creation API
from Autodesk.Revit.DB import CurveArray, Line, XYZ, Floor, Transaction

loop = CurveArray()
loop.Append(Line.CreateBound(XYZ(0,0,0), XYZ(10,0,0)))
loop.Append(Line.CreateBound(XYZ(10,0,0), XYZ(10,10,0)))
loop.Append(Line.CreateBound(XYZ(10,10,0), XYZ(0,10,0)))
loop.Append(Line.CreateBound(XYZ(0,10,0), XYZ(0,0,0)))

level = some_level   # Level element
floor_type = some_floor_type  # FloorType element

t = Transaction(doc, "Create Floor")
t.Start()
try:
    # Depending on template, use the up-to-date creation method for 2023
    floor = Floor.Create(doc, [loop], floor_type.Id, level.Id)  # representative modern call
    t.Commit()
except Exception:
    t.RollBack()
    raise
```

### Bulk Modifications
- Use a **single transaction** for many small edits when possible.
- Prefer API calls that accept collections (`doc.Delete(ICollection[ElementId])`, etc.).
- Cache lookups (e.g., map LevelId → Level once) to avoid repeated document queries.

---

## Major Revit 2023 API Highlights

- **Structural Analytical Model Overhaul**  
  Legacy analytical classes and accessors are replaced by a new analytical system (e.g., `AnalyticalElement`, `AnalyticalMember`, `AnalyticalPanel`). Update any code using `Element.GetAnalyticalModel()` and old `AnalyticalModel*` types to the new model.

- **Parameters & Units Modernization**  
  Legacy `ParameterType` enum and related overloads are removed. Use Forge Type Ids (`SpecTypeId`, `UnitTypeId`) and the corresponding creation/query APIs when defining or inspecting parameters/units.

- **ElementId Size Transition**  
  Revit 2023 starts transitioning toward larger (64-bit) element identifiers. Treat IDs as opaque tokens or strings when persisting; avoid assuming 32‑bit integer ranges.

- **Schedules API**  
  New capabilities include reading schedule heights on sheets, splitting into segments, and placing specific segments via API. Look for helpers on `ViewSchedule`, `ScheduleSheetInstance`, and related types.

- **Worksharing: Delete Worksets via API**  
  Use `WorksetTable.DeleteWorkset(...)` with settings to control element disposition (move/delete).

- **Geometry/DirectShape**  
  Additions like `BoundingBoxXYZ.IsSet` and `DirectShapeType.UserAssignability` improve reliability and UX control for custom geometry workflows.

- **Import/Export Formats**  
  OBJ/STL import & link, OBJ export, AXM import options are exposed via dedicated options classes and `Document.Import/Export` methods.

- **Views/Sheets Enhancements**  
  - Duplicate sheets programmatically (`ViewSheet.Duplicate(SheetDuplicateOption)`).
  - Swap a viewport’s view (`Viewport.ViewId` setter) with validation helpers.
  - New transforms for mapping model ↔ view ↔ sheet coordinates.

- **Electrical Design & Analytics**  
  Richer APIs for panel schedules (slot lock/unlock), load classifications, and electrical analytical nodes/graphs for connectivity and load data.

> Recommendation: When prompting an LLM, name the **target API** explicitly (e.g., “Use `ViewSheet.Duplicate` with `SheetDuplicateOption.WithViewsAndDetailing`”).

---

## Troubleshooting Guide

### Common Issues
1. **Transaction scope too broad** → Split logically; avoid UI‑blocking long commits.
2. **.NET collections mismatch** → Convert to `List[T]` or arrays for API calls.
3. **Missing error handling** → Validate existence/modifiability; handle exceptions.
4. **Memory growth in long runs** → Clear large Python/.NET collections; drop references.
5. **Obsolete API usage** → Replace `Document.New*` and legacy analytical/parameter patterns with 2023 equivalents.

### LLM Assistance
- Provide exact exception messages and stack context.
- Share the surrounding code (imports, doc access, transaction state).
- State performance constraints (element counts, time budgets).
- Ask for both **fix** and **explanation** so you understand root cause.

---

## Performance Optimization

### Transactions
- Batch related edits; minimize start/commit churn.
- Consider `TransactionGroup` for staged commits.
- Keep UI responsive: avoid very long single commits if feedback/cancelation matters.

### Collectors & Queries
- Filter early (category/class/parameter filters) to reduce iteration.
- Avoid repeated document scans; cache mappings for repeated use.

### Memory Management
- Release large lists and dictionaries when done.
- Dispose or drop references to temporary objects that may pin memory.
- Treat ElementIds as opaque identifiers when persisting outside a session.

---

## Quality Assurance

### Code Review Checklist
1. Transactions: explicit, correct, and exception‑safe.
2. Errors: validated inputs; clear messages; rollbacks on failure.
3. Performance: minimal collectors, bulk operations where possible.
4. Memory: no unnecessary retained references or large intermediate structures.
5. UI: dialogs/progress where appropriate; no document edits outside transactions.
6. Docs: docstrings cover params, returns, exceptions, and include examples.

### Testing Strategy
1. **Unit‑ish** tests for pure‑Python parts (helpers, transformations).
2. **Integration** runs on small seed models with known expectations.
3. **Performance** timings on representative projects; set budgets.
4. **User validation** in realistic workflows; ensure clean model state post‑run.

---

## Appendix: Prompt Templates (Copy/Paste)

Note: When the script engine matters, explicitly request `#! python` (IronPython) or `#! python3` (CPython) in your prompt.

**“Generate code using Revit 2023 API”**  
> “Write a pyRevit (CPython 3.9) script that collects all Rooms, sums their Area per Level, and writes the total into a project parameter `Level Total Area`. Use explicit transactions, proper .NET collections, and handle missing parameters gracefully. Return a dict[LevelId, double] as a result.”

**“Review and optimize”**  
> “Review this function for Revit 2023: identify obsolete API calls, consolidate transactions if safe, move repeated lookups out of loops, and ensure .NET collection usage matches method signatures. Explain each change briefly.”

**“Document this command”**  
> “Generate a Revit‑style docstring for this function, listing params (types), return type, exceptions thrown, and a minimal usage example showing transaction scope.”

Return back: [`CodexWorkspace/docs/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
