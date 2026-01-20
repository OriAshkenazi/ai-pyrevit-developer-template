#! python
# pyRevit script template aligned with Revit 2023 guidelines (IronPython-safe).

from Autodesk.Revit.DB import (
    BuiltInCategory,
    ElementId,
    FilteredElementCollector,
    Transaction,
)
from pyrevit import forms
from System.Collections.Generic import List

doc = __revit__.ActiveUIDocument.Document  # type: ignore[name-defined]


def collect_elements():
    """Return a list of walls as Element references."""
    collector = (
        FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Walls)
        .WhereElementIsNotElementType()
    )
    return list(collector)


def to_element_ids(elements):
    """Convert python elements to a .NET List[ElementId] for API calls."""
    ids = List[ElementId]()
    for element in elements:
        ids.Add(element.Id if hasattr(element, "Id") else ElementId(element))
    return ids


def main():
    walls = collect_elements()
    if not walls:
        forms.alert("No walls found.", exitscript=True)

    transaction = Transaction(doc, "New Command Template")
    transaction.Start()
    try:
        # TODO: Implement command logic here. Make edits to `walls` as needed.
        # Example: for wall in walls: ...
        transaction.Commit()
    except Exception as exc:
        transaction.RollBack()
        forms.alert("Command failed:\n{}".format(exc))
        raise


if __name__ == "__main__":
    main()
