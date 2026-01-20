# Selecting Elements and Accessing/Editing Parameters in Revit 2023 with pyRevit

## Introduction

Autodesk Revit’s API provides robust ways to select elements and manipulate their parameters programmatically. Using **pyRevit v5+** (which supports both IronPython 2.7 and CPython 3 engines), developers can write script buttons to automate element selection and parameter operations without Dynamo. This report covers:

* Manual element selection via user interaction, and filtered selection via the API.
* Retrieving each element’s **Category**, **Family**, and **Type** information.
* Accessing all types of parameters (built-in, shared, and project parameters) and editing their values.
* Techniques to discover all available parameters of an element when names/structure are unknown.
* Best practices (null checks, performance considerations, transaction handling) and common mistakes to avoid.

All examples assume **Revit 2023** on Windows 11, with pyRevit and the Revit API available. Code samples are provided for both the **IronPython** (pyRevit’s default) and **CPython** engines. The code is intended for use within a pyRevit script, where the Revit document (`doc`) and UI document (`uidoc`) are readily accessible. No external output (tables, CSV, etc.) is produced – the focus is on the Revit API interactions.

## Manual Element Selection (User Interaction)

Manual selection involves either using the current user-selected elements or prompting the user to pick elements through the Revit UI. In a pyRevit script, the active document and UI document are obtained as follows (works for both IronPython and CPython engines):

```python
# Get the active document and UI document (pyRevit provides __revit__ handle)
doc   = __revit__.ActiveUIDocument.Document   # type: Autodesk.Revit.DB.Document
uidoc = __revit__.ActiveUIDocument            # type: Autodesk.Revit.UI.UIDocument
```

Once we have `uidoc`, we can access Revit’s selection API. The current selection (pre-selected elements) is available via `uidoc.Selection.GetElementIds()`, which returns a collection of element IDs. We can use this to detect if something is already selected and retrieve it:

```python
selected_ids = list(uidoc.Selection.GetElementIds())
if selected_ids:
    element = doc.GetElement(selected_ids[0])
    # element is the first selected Element, if any
else:
    # No pre-selection; we will prompt the user to pick an element
    from Autodesk.Revit.UI.Selection import ObjectType
    try:
        ref = uidoc.Selection.PickObject(ObjectType.Element, "Select an element.")
        element = doc.GetElement(ref)  # ref is a Reference; GetElement retrieves the Element
    except Exception:
        element = None  # User canceled selection
```

In the above IronPython example, `PickObject()` opens a selection prompt in Revit (restricted to whole elements by using `ObjectType.Element`). The returned `ref` is a **Reference** to the picked element, which we convert to an `Element` via `doc.GetElement(ref)`. It’s good practice to wrap `PickObject` in a try/except, since it throws an exception if the user cancels the prompt. In the CPython engine, the code is virtually identical – just ensure the Revit API assemblies are loaded via Python.NET (e.g. `import clr; clr.AddReference("RevitAPIUI")` and `"RevitAPI"` if not already loaded). For example, a CPython snippet to get the current selection might be:

```python
#! python3
import clr
clr.AddReference("RevitAPIUI"); clr.AddReference("RevitAPI")
from Autodesk.Revit.UI import Selection
from Autodesk.Revit.DB import ElementId

# ... (doc and uidoc as above) ...
sel_ids = uidoc.Selection.GetElementIds()
elements = [doc.GetElement(id) for id in sel_ids]  # list of selected Element objects
```

We can also prompt for multiple picks using `uidoc.Selection.PickObjects(ObjectType.Element, "Prompt")` which returns a list of References. Each can be resolved to an Element similarly. For more refined control during picking, an `ISelectionFilter` can be implemented (for example, to allow only Walls to be picked), but that is optional.

**Null checks:** Always verify the result of selection. If no element is selected or the user cancels, your `element` will be `None` – handle this before proceeding to avoid `NoneType` errors. The example above sets `element = None` if selection is canceled, which you should check and possibly inform the user or exit gracefully.

## Filtered Selection by Criteria

Filtered selection uses the Revit API to collect elements meeting certain criteria, without user interaction. The primary tool is **FilteredElementCollector**, which can gather elements from the document efficiently. Common filters include by category or by class. For example, to get all wall instances in the active document:

```python
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

walls = FilteredElementCollector(doc) \
          .OfCategory(BuiltInCategory.OST_Walls) \
          .WhereElementIsNotElementType() \
          .ToElements()
# walls will be a list of Wall elements (instances only)
```

Here, `OfCategory(OST_Walls)` restricts to elements in the Walls category, and `WhereElementIsNotElementType()` excludes the definition objects (so we get wall instances, not Wall Types). Similarly, one could use `OfClass(FamilyInstance)` to get all family instance elements, or combine filters. The above code works in both IronPython and CPython (just remember to `clr.AddReference("RevitAPI")` in a CPython script and import the necessary classes).

Using a FilteredElementCollector is generally a best practice for performance when you need a broad selection. It leverages Revit’s internal filtering – far faster than retrieving everything and manually checking category in Python. Always include a filter like `WhereElementIsNotElementType` when you only need physical elements, to avoid accidentally pulling in family/type objects that also belong to the category.

## Retrieving Element Category, Family, and Type

Every Revit element has a **Category** (e.g. Doors, Walls, Furniture), and an associated **Element Type**. If the element is a family instance (of a loadable family), it also has an associated **Family** definition. In Revit API terms, the element’s *type* is itself an Element (typically a subclass of **ElementType** such as a **FamilySymbol** or a system family type like **WallType**). To get these:

* **Category**: Use `element.Category`. This returns a `Category` object; you can get its name via `element.Category.Name`. (Be aware some elements might not have a category, in which case this will be `None` – always check.)
* **Type**: Use `element.GetTypeId()` to get the ElementId of the element’s type, then `doc.GetElement(type_id)` to get the ElementType object. This works for any element that has a type. For example, a Wall returns a WallType, a family instance returns a FamilySymbol, etc. It is safer to use `GetTypeId()` rather than properties like `element.Symbol`, because not all elements expose a “Symbol” property (e.g. a TextNote doesn’t have FamilySymbol, but still has a TextNoteType via GetTypeId). Always verify the type ElementId is valid (not equal to `ElementId.InvalidElementId`) before using it.
* **Family**: Once you have the ElementType, you can retrieve the family information. The **ElementType.FamilyName** property gives the family name or grouping for that type. For loadable families, `type_elem.FamilyName` is the name of the Family (e.g. "Door Family XYZ"); for system families, it returns the grouping name (e.g. for a Basic Wall type, FamilyName might be "Basic Wall"). If you specifically have a FamilySymbol (a type of a loadable family), you can also get the **Family** object via `symbol.Family`. In many cases, the family name and type name together identify an element (e.g. Family: "Basic Wall", Type: "Generic 200mm").

**Example (IronPython):** For an element `elem`, get its category, family, and type names:

```python
type_id = elem.GetTypeId()
type_elem = doc.GetElement(type_id)  # ElementType
cat_name  = elem.Category.Name if elem.Category else "<None>"
type_name = type_elem.Name if type_elem else "<No Type>"
fam_name  = ""
if hasattr(type_elem, "FamilyName"):
    fam_name = type_elem.FamilyName  # works for both system and loadable families:contentReference[oaicite:11]{index=11}
# Alternatively, if type_elem is a FamilySymbol: fam_name = type_elem.Family.Name
print("Category:", cat_name, "/ Family:", fam_name, "/ Type:", type_name)
```

The code checks that the element and its type exist. We used `hasattr(type_elem, "FamilyName")` to safely get FamilyName only if available. Note that some elements (like levels, views, etc.) have no “family/type” concept in the usual sense – their `GetTypeId()` may return invalid and their Category could be None. Always guard against those cases. In normal model elements, you should get a valid type. If `type_elem` is a FamilySymbol, `type_elem.Family.Name` would give the family name as well. But using the general `ElementType.FamilyName` is convenient since it covers system families too.

## Accessing Element Parameters

Revit parameters come in several flavors: **Built-in parameters**, **Project parameters**, **Shared parameters**, as well as **Global** and **Family** parameters (the latter two are less relevant in this context). In practice, for any given element, you can retrieve parameter values in a few different ways:

* **By name (LookupParameter):** Use `element.LookupParameter("Parameter Name")` to get a parameter by its visible name. This works for shared parameters and project parameters which are defined by name, and also for built-in parameters *if* you use the exact local name. However, be cautious: built-in parameter names are language-dependent, so using names for built-ins can break on non-English Revit or different locales. For consistency, use LookupParameter primarily for custom (project/shared) parameters whose names you know. Always check if it returned a valid `Parameter` object – it will return `None` if the element doesn’t have a parameter by that name.
* **By built-in ID (get\_Parameter):** For Revit-defined built-in parameters, the safer method is `element.get_Parameter(BuiltInParameter.PARAM_ENUM)`. The `BuiltInParameter` enumeration contains all internal parameter IDs (e.g. `ALL_MODEL_INSTANCE_COMMENTS` for the “Comments” field). This is locale-independent. For example: `param = elem.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)` would retrieve the *Comments* parameter. Using the built-in ID ensures your code works regardless of the Revit display language. Finding the right BuiltInParameter can be done via RevitLookup (which shows `Definition.BuiltInParameter` for a selected parameter) or the RevitAPI docs.
* **By iteration:** If you need to discover all parameters on an element without knowing names, you can iterate through `element.Parameters`, which returns a collection of all **instance parameters** the element has. For each `param` in that list, you can access `param.Definition.Name` to get its name. This approach is useful for surveying what data is available on an unfamiliar element. Keep in mind this list by default includes only instance-level parameters; type parameters are not included there. If you need type parameters, you must get the element’s ElementType (as shown earlier) and then iterate through `typeElem.Parameters` for the type’s own parameters. In Revit API, **instance and type parameters are accessed from different objects** – a common beginner pitfall is to look for type-only parameters on the instance directly.

**Example: Listing all parameter names of an element** (IronPython):

```python
elem = element  # some Revit element
param_names = [p.Definition.Name for p in elem.Parameters]  # instance param names:contentReference[oaicite:24]{index=24}
# If you also want type parameter names:
type_param_names = []
type_id = elem.GetTypeId()
if type_id and type_id != ElementId.InvalidElementId:
    type_elem = doc.GetElement(type_id)
    type_param_names = [p.Definition.Name for p in type_elem.Parameters]
print("Instance parameters:", param_names)
print("Type parameters:", type_param_names)
```

This will gather all parameter names. In a pyRevit context, you might use `script.get_output().print(param_names)` or simply print as above (pyRevit captures print output). The code checks that the element has a valid type before listing type parameters. As a developer, you can use such a list to identify the exact names or IDs of parameters you might want to get or set.

### Reading Parameter Values

Once you have a `Parameter` object (from any of the methods above), you need to retrieve its value in the correct way. A Revit `Parameter` stores data in one of a few storage types, given by `Parameter.StorageType`:

* **String:** Use `param.AsString()` to get the string value. (For text parameters or any free-form text like Comments, Mark, etc., StorageType will be String.)
* **Integer:** Use `param.AsInteger()`. Integers are used for integer fields and also for some **Yes/No** booleans (which return 0 or 1), or enumerated choices.
* **Double:** Use `param.AsDouble()`. *All Revit floating-point numeric values (lengths, areas, angles, etc.) are stored as doubles in **internal units***. For example, lengths are in feet internally, regardless of the project’s display units. So a wall length parameter might return `10.0` (feet) which you would interpret or convert to the user’s unit if needed. Revit’s `UnitUtils` can convert to display units if necessary, or `param.AsValueString()` will give a formatted string in project units for some parameters.
* **ElementId:** Use `param.AsElementId()`. Many parameters don’t hold a numeric or text value but reference another element – for example, a “Level” parameter on a wall is an ElementId pointing to a Level element. `AsElementId()` gives you the ID; you can then do `doc.GetElement(id)` to get the referenced element (or compare it to `ElementId.InvalidElementId` which denotes no reference). If the parameter is a *dropdown (enum)* like structural material type, it might also be stored as an ElementId pointing to a **ElementType** representing that choice.

Use the StorageType to decide which `As...` method to call. If you call the wrong one, it may throw an error or just return meaningless data. (For example, calling AsDouble on a string parameter returns 0.0). For safety, you can use a conditional or `if/elif` to handle each StorageType. For instance:

```python
param = element.LookupParameter("Comments")
if param:
    if param.StorageType == StorageType.String:
        value = param.AsString()
    elif param.StorageType == StorageType.Double:
        value = param.AsDouble()  # likely in feet or sq. ft, etc.
    elif param.StorageType == StorageType.Integer:
        value = param.AsInteger()
    elif param.StorageType == StorageType.ElementId:
        valId = param.AsElementId()
        value = None
        if valId != ElementId.InvalidElementId:
            value_elem = doc.GetElement(valId)
            value = value_elem.Name if value_elem else str(valId.IntegerValue)
    print(f"Parameter '{param.Definition.Name}' value: {value}")
```

In many cases, `Parameter.AsValueString()` is convenient for read-only display of the value with units formatting (as seen in Revit UI). But `AsValueString` may return `None` if no value is set or if the value cannot be formatted. It’s generally used for reporting rather than for logic.

### Editing Parameter Values

To **modify** a parameter’s value, a few important rules apply:

* You **must** open a **Transaction** in Revit API before making any changes. All write operations are blocked unless done inside a started transaction. Forgetting this is a common mistake – the code will throw an exception if you call `param.Set()` outside a transaction.
* Use the `Parameter.Set(value)` method to assign a new value. The type of the value you pass must match the parameter’s storage type. For example, pass a float for a double parameter, an int for an integer or ElementId parameter (actually for ElementId you pass an `Autodesk.Revit.DB.ElementId` object), and a string for a string parameter. If you pass the wrong type (e.g. an int to a double parameter, or a Python int where a 64-bit .NET int is expected), **Revit will typically fail to set the value without throwing an error**. It will simply ignore the assignment. This silent failure can be confusing, so ensure you provide the correct data type. (In CPython with Python.NET, the types are auto-converted in many cases, but the safest approach is to match types exactly – e.g., use `ElementId(x)` for element id parameters, use `float(5.0)` for doubles, etc.)
* Some parameters are **read-only** (`param.IsReadOnly` is True). These cannot be set at all. Attempting to call `Set` on a read-only parameter will throw an exception or do nothing. Examples are many computed parameters (like Area of a room, which is calculated by Revit) or system-defined properties. Always check `Parameter.IsReadOnly` before setting, and avoid trying to change such parameters.
* If the parameter is a **type parameter**, modifying it will affect all instances of that type. In that case, you need to retrieve the ElementType and set the parameter on that type element (still within a transaction). The API treats type parameters as properties of the type element. For instance, to change the “Type Mark” for a door type, you’d do `typeElem.LookupParameter("Type Mark").Set("X")` inside a transaction – this changes it for the type, and all instances update accordingly.

**Example: Setting a parameter (IronPython):** Suppose we want to set the Comments parameter of all selected walls to "Checked". We can do:

```python
from Autodesk.Revit.DB import Transaction
ids = uidoc.Selection.GetElementIds()
wall_elems = [doc.GetElement(id) for id in ids if doc.GetElement(id).Category.Name == "Walls"]
if wall_elems:
    t = Transaction(doc, "Update Comments")
    t.Start()
    for wall in wall_elems:
        param = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
        if param and not param.IsReadOnly:
            param.Set("Checked")  # setting a string value
    t.Commit()
```

This code collects the selected elements that are in the Walls category, starts a transaction, then iterates and sets the *Comments* built-in parameter (which is a writable text field on most elements). We ensure the parameter exists and is not read-only before calling `Set`. After the loop, we `Commit()` the transaction to finalize changes. Always `Commit` or `RollBack` a transaction you started – leaving a transaction open (e.g. due to an error) can lock the Revit model in an unstable state until the script ends. It’s good practice to wrap transactions in try/except or use a context manager if available to guarantee closure. pyRevit’s `revit` module may provide a context manager for transactions as well (e.g. `with revit.Transaction("Name"):`).

**Note on units when setting values:** The value passed to `Set` for a double parameter must be in Revit’s internal units. For example, to set a length to 3 meters, you must convert that to feet (approximately 9.8425 ft) before calling `Set`, since Revit expects the internal value in feet. The `UnitUtils.ConvertToInternalUnits()` method can be used for conversion if needed. This is a common oversight – if you set a length or area directly with a number thinking it’s in your display units, you might be entering the wrong value by a large factor.

## Best Practices and Common Mistakes

* **Use Transactions for Edits:** Enclose all parameter modifications inside a `Transaction.Start()` / `Transaction.Commit()` pair. Failing to start a transaction is a common error that leads to runtime exceptions. For multiple edits, prefer wrapping them in a single transaction rather than many small ones for performance.

* **Null and Validity Checks:** Always verify that objects you retrieve are valid before use. For example, after using `Selection.PickObject`, ensure the result is not None (catch the cancellation exception) to avoid using a null reference. When getting an element’s type, check that `GetTypeId()` didn’t return invalid ID. When using `LookupParameter`, check the result is not `None` before calling methods on it. These checks prevent unexpected AttributeErrors or accessing invalid data.

* **Parameter Retrieval Methods:** Choose the right method to get a parameter. Use `get_Parameter(BuiltInParameter)` for built-ins to avoid localization issues. Use `LookupParameter(name)` for custom named parameters, but remember that it’s case-sensitive and must match exactly. Do not use `LookupParameter` for built-ins with hard-coded English names – they might not match on a non-English Revit.

* **Instance vs Type Parameters:** Understand the distinction between an element and its type in the API. Instance parameters are accessed from the element itself, whereas type parameters are accessed from the ElementType (FamilySymbol, etc.). A common mistake is trying to `LookupParameter` a type-only parameter on the instance – it will return None. Instead, get the element’s type and then retrieve the parameter. For example, “Type Name” or any type-level property needs `doc.GetElement(element.GetTypeId())` first.

* **Performance – Filtering and Caching:** Leverage **FilteredElementCollector** to retrieve specific elements efficiently rather than filtering in Python. For example, getting all doors by `FilteredElementCollector(doc).OfCategory(OST_Doors)…` is much faster than collecting everything and checking each element’s category in Python. If you need to process a large number of elements and frequently access their type or other related objects, consider caching those to avoid repetitive API calls. For instance, if iterating thousands of elements to get each’s type name, store already fetched types in a dictionary (keyed by typeId) so that each unique type is only retrieved once from the document. The Revit API calls like `doc.GetElement` are relatively fast, but caching can still help if the same type is looked up many times. Also, when setting many parameters, one transaction wrapping all changes is more efficient than many small transactions.

* **Parameter Value Types:** When calling `Parameter.Set`, ensure the value is of an appropriate type and unit. This bears repeating because it’s a silent failure scenario. For example, don’t pass a Python string to set an integer parameter (convert it to int first), and ensure numeric values are in internal units (feet, radians, etc.) if applicable. If nothing happens and no error is thrown, double-check that the parameter isn’t read-only and that you provided the correct data type.

* **Read-only Parameters:** Attempting to set read-only parameters is a no-op. Check `param.IsReadOnly` before setting. Similarly, some parameters are read-only on instances but writable on types (or vice versa). For example, the “Width” of a door might be a type parameter – you can’t set it on the instance, you must set it on the FamilySymbol. Adjust your approach depending on the parameter’s definition (use RevitLookup or the API docs to determine whether a parameter is instance or type bound, and read-only or writable).

* **User Selection Handling:** When using interactive selection, be mindful of the user experience. If your script expects a selection, you can use pyRevit’s UI forms or simply document the requirement. pyRevit also supports a **selection context** meta-tag to require pre-selection. If using `PickObjects`, consider providing a clear prompt message. Always handle the case where the selection is empty or canceled – perhaps by showing a `TaskDialog` warning (Revit API UI) to the user instead of failing silently.

* **Using .NET Collections:** Some Revit API methods expect .NET collection types (e.g. `IList<ElementId>`). In IronPython, a Python list often works (it can enumerate as an IEnumerable); in CPython with Python.NET, you may need to explicitly construct a `List[ElementId]` for certain calls. For example, setting a new selection set requires a `ICollection<ElementId>` – you can do `ids = List[ElementId](); ids.Add(id1); ids.Add(id2); uidoc.Selection.SetElementIds(ids)`. Be prepared to use `System.Collections.Generic.List` when needed for interoperability.

* **Avoiding Common API Misuses:** Do not modify the Revit document outside of valid API contexts (e.g. not during iteration of a collector without proper filtering – use `.ToElements()` to finalize the collection first). Do not keep references to Element objects past the scope of a script; if the script runs and finishes, those references shouldn’t be reused later (elements can become invalid if deleted or if a transaction is rolled back). And remember that pyRevit scripts run in Revit’s single-threaded API context – avoid long blocking loops without feedback, as it can freeze Revit. If processing many elements, consider using `TransactionGroup` to batch commits or occasionally calling `doc.Regenerate()` if needed (for example, after activating a FamilySymbol as seen above, regeneration is required). These are more advanced considerations depending on the task.

By adhering to these best practices – careful selection handling, proper API usage for parameters, and mindful transaction management – you can successfully select elements and edit their parameters in Revit 2023 using pyRevit. This enables powerful automation of model data, all through Python scripting integrated directly in Revit. The combination of IronPython (for direct .NET integration) and CPython (for advanced libraries, if needed) under pyRevit provides flexibility, but as demonstrated, the core Revit API usage remains the same. With careful coding and knowledge of Revit’s quirks, developers can avoid common pitfalls and create reliable tools for Revit parameter management.

**Sources:** Recent discussions and official documentation were referenced to ensure accuracy, including pyRevit developer forums and Revit API guides for parameter handling and selection techniques, among others.
