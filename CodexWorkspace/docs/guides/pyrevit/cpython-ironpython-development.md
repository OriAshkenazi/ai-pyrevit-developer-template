# Best Practices for PyRevit Scripts in IronPython 2.7 vs. CPython (`#! python3`)

Verified against pyRevitLabs documentation:
- https://pyrevitlabs.notion.site/Anatomy-of-CPython-Scripts-0e4cffeb545c4aa699fbe722c837c8d0
- https://pyrevitlabs.notion.site/Create-Your-First-CPython-Command-b8a7718c554645d1a18454c0b363e3c9

## Overview: IronPython and CPython in PyRevit

PyRevit supports two Python engines for scripting: **IronPython 2.7** (a .NET-integrated Python 2 interpreter) and **CPython 3.x** (a standard Python 3 interpreter with .NET access via Python.NET). Each engine has strengths and limitations, and a robust PyRevit extension can leverage both. In general, **IronPython is preferred for Revit API interaction and UI**, while **CPython is used when heavy data manipulation or external libraries (NumPy, Pandas, SciPy, openpyxl, etc.) are needed**. PyRevit’s developers note that the CPython integration is still not as mature or fully supported as IronPython, so it should be used judiciously. The typical relationship is to let IronPython handle Revit-centric tasks (scraping model data, updating the model, and UI) and offload computationally intensive or library-dependent tasks to CPython. Below, we outline best practices for each environment and how to architect a project that combines them effectively.

## IronPython vs. CPython – Roles and Key Differences

**IronPython (Python 2.7)** is embedded in Revit’s .NET runtime, which means it interacts with the Revit API very naturally. IronPython’s `clr` module is built-in, and Revit API assemblies are usually preloaded by PyRevit – you can often import Revit API classes directly without manually adding references. IronPython seamlessly handles .NET types and conventions (e.g. properties, indexers, enums) in Python code. However, being Python 2.7, it lacks modern Python features and cannot use many PyPI libraries built in C (like NumPy/Pandas), and it has a different string/Unicode handling than Python 3.

**CPython (`#! python3`)** in pyRevit runs on pyRevit's embedded CPython engine and uses **pythonnet** to bridge .NET. The pyRevitLabs docs warn the CPython engine is under active development and might be unstable; prefer IronPython unless you need C-based packages (e.g., `numpy`, `scipy`).

If you need to explicitly load additional .NET assemblies in CPython, use `clr.AddReference(...)`. For example, a CPython script could start with:

```python
#! python3
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')  # if UI interactions or Selection needed
from Autodesk.Revit.DB import *
# (Now __revit__ and other pyRevit injection variables can be used)
doc = __revit__.ActiveUIDocument.Document  # Current document
```

Once assemblies are loaded, you can call Revit API functions, but **certain patterns differ**. IronPython often auto-converts or exposes .NET properties/methods more Pythonically, whereas CPython (via Python.NET) may require explicit method calls or type conversions. For instance, an IronPython script can index a **`IntersectionResultArray`** via `.Item[0]`, but in CPython the same property is not directly accessible – you must call the underlying `.get_Item(0)` method. Similarly, Revit API methods that return enum values or tuples might appear differently. Be prepared to inspect .NET objects (with `dir()` or `.__class__`) in CPython and call their methods explicitly.

**Implementing Revit API .NET interfaces in CPython:** The pyRevitLabs docs note that when using CPython+pythonnet to implement Revit API interfaces (e.g., `Autodesk.Revit.DB.ISelectionFilter` for `PickObject`), you must set a `__namespace__` attribute on the derived class, and it must be unique per execution (to avoid “Duplicate type name within an assembly”). A common pattern is:

```python
from pyrevit import EXEC_PARAMS

class MySelectionFilter(Selection.ISelectionFilter):
    __namespace__ = EXEC_PARAMS.exec_id
```

**Stability and Support:** The pyRevitLabs docs warn the CPython engine is under active development and might be unstable. Prefer IronPython for general development and use CPython primarily when you need C-based packages (e.g., `numpy`, `scipy`).

**CPython basics (from pyRevitLabs docs):**
- Put `#! python3` on the first line to run a command under CPython.
- Use a 64-bit CPython environment (Revit is 64-bit).
- pyRevit's embedded CPython engine looks at `PYTHONPATH` for additional module search paths.
- CPython scripts are read using UTF-8; there is no need for `# -*- coding: utf-8 -*-`.

## Script Architecture and Module Separation

Designing a clean architecture is critical, especially in an *“AI-first”* development approach where code may be generated or assisted by AI (Codex/Claude). A clear separation of modules will make it easier to develop, maintain, and even auto-generate parts of the code. Here are best practices for organizing the project:

* **Separate by Responsibility:** Divide the functionality into distinct modules: e.g., `data_extraction.py` for scraping model data, `data_processing.py` for heavy analysis, `data_writing.py` for updating the model, and `ui.py` for user interface dialogs. Each module can be developed and tested somewhat independently. IronPython will primarily use the extraction, writing, and UI modules, while the CPython environment will execute the processing module.

* **Use a `lib` Folder for Shared Code:** PyRevit supports a special `.lib` directory within your extension where you can place reusable modules. Code placed in `yourextension.lib` can be imported by your scripts. This is ideal for utility functions, data structure definitions, or configuration constants that both IronPython and CPython parts might use. For example, you might define a data schema (classes or namedtuples for element data) in the lib so that both engines interpret the data consistently. Using a lib also aids collaboration and AI development, since the logic is broken into smaller, clear units.

* **PyRevit Script Bundles:** Remember that each PyRevit “command” is typically a folder (a bundle) containing a script (and optionally an icon, markup, etc.). You might implement the main command as an IronPython script (no `#! python3` shebang) that orchestrates the process. If needed, you can also include a separate CPython script in your extension (marked with `#! python3`) which isn’t directly on the ribbon but can be called internally. Keep the command entry-point script concise – it should parse inputs, call into well-defined functions (imported from your lib or other modules), and handle high-level flow, rather than doing everything inline. This improves readability and debuggability.

* **AI-Friendly Code Style:** Use clear function/method names and docstrings to describe each module’s purpose. For instance, a function `collect_model_data(doc) -> dict` can clearly signal that it returns a dictionary of relevant model data. This not only helps human developers but also assists AI coding assistants in understanding and modifying each part correctly. Short, single-responsibility functions are easier for an AI to reason about.

* **Testing and Iteration:** Since IronPython runs inside Revit, debugging can be slower. Consider writing and testing the data processing logic purely in CPython outside of Revit first (using sample data), which is easier to debug with standard Python tools. By designing the CPython module to take input from a file (or function arguments) and output results to a file, you can run it independently of Revit. This modular approach means the heavy logic can be developed with quick iteration cycles, and once it’s stable, integrated back into the PyRevit workflow.

## Data Scraping from the Revit Model (IronPython)

**Use IronPython for data extraction** from the Revit model, as it interfaces directly with the Revit API and model database. Best practices for scraping model data include:

* **Efficient Element Collection:** Utilize the Revit API’s filtering to gather only the needed elements. For example, use `FilteredElementCollector` with category or class filters to target relevant elements (e.g., all walls or all elements that have certain parameters) rather than iterating over the entire model. In IronPython, you can import the necessary classes directly:

  ```python
  from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
  elems = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)...
  ```

  This filtering happens within the API (C# level), which is much faster than filtering in pure Python. Minimize the data pulled into Python: collect element **IDs and essential properties** instead of heavy objects.

* **Gather Required Parameters:** For each element of interest, retrieve the parameters and properties needed for your analysis. For **Product Breakdown Structure (PBS)** codes, this likely means reading type names, family names, or a custom parameter that correlates to the PBS classification. For **Geographical Breakdown Structure (GBS)**, you might need geometry or location data (level, coordinates, room/zone containment, etc.). Focus on lightweight representations: e.g., get element’s **UniqueId** or **ElementId** (to uniquely identify elements in results), relevant parameter values (strings or numbers), and maybe a representative point (such as the element’s base point or centroid). If full geometry is needed (for complex spatial analysis), consider using bounding boxes or outline curves instead of triangulated geometry to keep data volume manageable.

* **Use PyRevit/Revit API Wrappers:** PyRevit’s `revit` module provides convenient shortcuts. For example, `from pyrevit import revit, DB` gives access to `revit.doc` (the current document) and the `DB` namespace. You can also get the current selection or active view via `revit.uidoc`. These helpers can simplify your scraping code. Just be cautious to remain in IronPython for this part; trying to do it in CPython would require complex marshaling of .NET objects.

* **Avoid Complex Calculations in Scraping Loop:** Just collect raw data. Do not attempt heavy computations or Pandas data manipulation while iterating over Revit elements in IronPython – this should be deferred to the CPython stage. Keep the IronPython scraping focused on **I/O with Revit** (which it does best) and package the data for export.

* **Serialize Data for Transfer:** Once data is collected, **serialize it into a neutral format** to pass to the CPython process. Common choices are JSON (if the data is primarily numeric/string) or CSV/Excel. JSON is convenient for hierarchical data (e.g., a dictionary of element info). Ensure any complex objects are converted: e.g., a XYZ point can be stored as a tuple of three floats, an ElementId as its integer value or string UniqueId, etc. This decoupling is important because IronPython .NET objects won’t be directly understood by CPython. By converting everything to basic Python types (int, float, str, list, dict), you create a clean hand-off. PyRevit’s `script.get_temp_file()` can be used to generate a temporary file path for such data exchange.

**Example:** You might end up with an IronPython function that produces a list of element records like:

```python
data = [
  {"id": elem.Id.IntegerValue, "pbs_code": pbsParam.AsString(), 
   "center": (cx, cy, cz), "volume": volParam.AsDouble(), ...},
  ... 
]
```

This list (or dict mapping IDs to values) can then be written as JSON to a file for the CPython stage.

## Data Manipulation and Analysis (CPython)

Heavy data crunching – such as tabular data manipulation with **Pandas**, numerical computations with **NumPy/SciPy**, or reading/writing Excel via **openpyxl** – should be done in a **CPython script** (`#! python3`). Here’s how to make the most of CPython while avoiding pitfalls:

* **Setting Up the CPython Environment:** pyRevit uses an embedded CPython engine and looks at the `PYTHONPATH` environment variable for additional module search paths. Install required packages (e.g., with `pip`/`pipenv`) and ensure they are discoverable via `PYTHONPATH` for pyRevit CPython commands. Also ensure you use a 64-bit CPython environment (Revit is 64-bit).

* **Running CPython from IronPython (optional):** If you want the command itself to be IronPython (e.g., for UI/stability) but still leverage CPython-only packages, run the CPython logic as a separate step (e.g., an external process) and exchange data via files (JSON/CSV). Keep the interface small and well-defined.

  ```python
  import subprocess, sys
py_exec = r"C:\Users\<User>\AppData\Roaming\pyRevit\Python312\python.exe"  # Example path
  script_path = r"C:\path\to\yourextension\scripts\heavy_analysis.py"
  subprocess.run([py_exec, script_path, input_data_file, output_data_file])
  ```

  Here `heavy_analysis.py` would be your CPython script (with `#! python3` shebang if it’s inside a pyRevit extension) that reads the `input_data_file` (JSON/CSV) and writes results to `output_data_file`. Passing file paths as command-line args is a simple way to hand off data. The IronPython code can wait for the subprocess to finish (the `run` call will block until completion), or show a progress bar if needed.

  *Rationale:* Using a separate process isolates the CPython execution. This is considered a good workaround because PyRevit’s in-process CPython engine can be **“tedious to debug”** and not fully reliable for complex tasks. An external process also avoids conflicts between IronPython and CPython state and keeps Revit responsive (Revit’s main thread waits for result without being locked into running Python computations). The downside is a slight overhead of launching a process and doing file I/O, but this is usually negligible compared to heavy computations.

* **Performing the Analysis:** Inside the CPython script, follow normal best practices for the libraries:

  * Use **Pandas** to filter, join, or aggregate data by PBS/GBS codes. For instance, you might load the JSON into a DataFrame, or if using CSV, directly use `pandas.read_csv`. Pandas can help match elements to reference data (perhaps an external mapping of element types to PBS codes, or computing statistics like total quantities).
  * Use **NumPy/SciPy** for numerical operations – e.g., if determining GBS zones by coordinates, you could use NumPy arrays for distance calculations or SciPy clustering algorithms if needed (though often simpler geometric logic might suffice with raw math).
  * Use **openpyxl** if you need to read or write Excel files (e.g., reading a PBS code mapping table maintained in Excel, or exporting results). Since openpyxl is pure Python, it could run under IronPython, but installing it in IronPython is harder; with CPython it’s straightforward. If reading an Excel mapping, do it here and perhaps include the mapping logic in the analysis.
  * Ensure **minimal Revit API usage in CPython**. Ideally, the CPython script works with plain data. It should not try to call back into Revit’s document (leave that to IronPython). However, if absolutely necessary, CPython *can* access the Revit API via Python.NET (for example, creating geometry or using `XYZ` math) as long as you `clr.AddReference` to the needed DLLs. Note: pyRevit helper modules can be available in CPython (e.g., the official "Create Your First CPython Command" example uses `from pyrevit import revit`). If you hit UI/tooling limitations, keep UI and complex Revit interactions in IronPython and use CPython mainly for heavy, library-driven work. If you need certain .NET functionality (say, using the `XYZ` struct for geometry math or the `Transform` class), you can import those from `Autodesk.Revit.DB` after adding references, and they will function. The earlier example of an intersection calculation in CPython demonstrated that you can call Revit API methods, but sometimes need to handle the results carefully (like using tuple results and `.get_Item` methods). Generally, try to limit Revit API calls in CPython to avoid complexity. Do any complex Revit interactions back in IronPython.

* **Handling Results:** After crunching the data, the CPython script should output a result dataset in a form that IronPython can easily consume. Again, JSON is a good choice for structured data (or CSV for tabular data). For example, the CPython script could produce a JSON mapping of element IDs to the determined PBS and GBS codes, or a CSV with columns `ElementId, PBSCode, GBSCode, [Other metrics]`. Write this to the `output_data_file` path provided. Keep the output minimal – just the information needed to update the model or to present to the user. This might be a list of elements that couldn’t be matched (for reporting) and the values for those that did match.

* **Error Handling and Logging:** Because the CPython process runs outside of PyRevit’s direct control, you won’t see errors in Revit’s PyRevit console if something fails. You should include robust error handling in the CPython script. Consider logging errors to a text file or writing error info into the output (or a dedicated error file) so that the IronPython side can detect if the CPython processing succeeded. You could also have the CPython script print to stdout; if you use `subprocess.run`, you can capture output and display it via PyRevit on the IronPython side. This way, if something went wrong (e.g., pandas couldn’t parse the Excel, or a key was missing), you can alert the user via a PyRevit form or at least via the output window.

## Writing Data Back to the Revit Model (IronPython)

After CPython returns the processed results, **IronPython takes over again to push the data into Revit**. Best practices for this stage:

* **Read and Parse Results:** The IronPython script (resuming after the subprocess call) should load the CPython output file. Use a straightforward approach – e.g., Python’s built-in `json` module for JSON, or `csv` module for CSV. This yields a Python data structure (dict, list of dicts, etc.) in IronPython.

* **Open a Transaction:** All modifications to the Revit model must occur within an Autodesk Revit API `Transaction`. PyRevit’s `revit` module provides a convenient context manager `revit.Transaction()` to simplify this. For example:

  ```python
  from pyrevit import revit
  with revit.Transaction("Seed PBS/GBS parameters"):
      for elem_id, values in results_dict.items():
          elem = doc.GetElement(DB.ElementId(int(elem_id)))
          # assume values has {"PBS": "X123", "GBS": "Zone 5"}
          pbs_val = values["PBS"]; gbs_val = values["GBS"]
          # Retrieve the parameter objects (shared parameters presumably)
          pbs_param = elem.LookupParameter("My PBS Code")
          gbs_param = elem.LookupParameter("My GBS Code")
          if pbs_param and pbs_param.StorageType == DB.StorageType.String:
              pbs_param.Set(pbs_val)
          if gbs_param and gbs_param.StorageType == DB.StorageType.String:
              gbs_param.Set(gbs_val)
  ```

  Wrapping the updates in a single transaction is efficient and ensures atomicity (all changes apply together). Make sure to replace `"My PBS Code"` with the actual shared parameter names or GUIDs that were set up in advance. Since the question explicitly mentions **setting shared parameters in advance**, it implies those parameters exist and are bound to the categories of interest. The script should verify their existence on each element and perhaps warn if an element is missing the parameter (e.g., if a category wasn’t properly bound to the shared parameter, the `LookupParameter` might return None).

* **Avoid Long Transactions if Needed:** If the dataset is huge (thousands of elements), a single transaction is okay and usually fastest. However, Revit might experience UI lag during a long-running transaction. It’s often fine, but as a refinement, you could chunk the updates into batches or at least inform the user of progress (e.g., update a progress bar or print status every N elements – these messages can appear in the PyRevit output window live). Since PyRevit output is easily accessible in IronPython, you can use the logger or print statements to give feedback like `logger.info(f"Updated {count} of {total} elements...")`.

* **Commit and Error Check:** When the `with revit.Transaction():` block exits, the transaction is committed. If any exception occurs inside, the transaction will roll back (if using the context manager). You should catch exceptions around the transaction or inside it to handle cases like invalid parameter values or elements that can’t be modified. Log errors clearly so the user knows if some elements failed to update (perhaps listing their IDs).

* **Performance Considerations:** Setting a parameter on an element is generally fast, but thousands of updates can still take a noticeable time. It’s mostly unavoidable, but using the fastest lookups (e.g., caching parameter definitions if possible, though `LookupParameter` is usually fine) and avoiding redundant operations (like do not fetch an element twice) will help. Since you have element IDs from earlier, use `Document.GetElement` to retrieve each element. If you have a very large number of elements, an alternative is to use the *Bulk Update* via the Revit API if available (not common for parameters, unless using the PropertyBatchAPI in recent Revit versions, but that’s advanced). For most cases, iterating in IronPython is acceptable given the heavy lifting was already done in CPython.

* **Verify Results:** After seeding the data, you might want to verify or report the outcome. For instance, count how many elements got a PBS/GBS assigned and how many were skipped (perhaps because no matching code was found). This can be output to the PyRevit console or shown in a message box for the user. A quick summary like `"100 elements processed: 95 updated successfully, 5 had no matching code."` gives confidence that the script did what was expected.

## User Interface and PyRevit UI Stack (IronPython)

User interaction is an important aspect of a robust tool. For stability, prefer implementing complex UI in IronPython (especially WPF-based dialogs). CPython scripts can still use many pyRevit helpers (e.g., `from pyrevit import revit`), but test UI-dependent pieces and fall back to IronPython if needed. Here are UI considerations and best practices:

* **Using `pyrevit.forms`:** PyRevit provides a `forms` module for common dialogs and forms. For example, `forms.alert(msg)` can show a simple message box; `forms.ask_for_string()` can prompt the user for input; `forms.select_file()` can open a file dialog. More complex interfaces can be built with **WPF XAML** definitions and loaded via `pyrevit.forms.WPFWindow()` if needed. If your script needs to let the user choose options (like which Excel file to load, or which categories to process, etc.), do this via forms in IronPython **before** kicking off the CPython process. This ensures you gather all necessary input while still in the IronPython context.

* **Category Selection Pattern:** The PBS Handler implements a reusable category selection UI component following pyRevit-Elements.md patterns:

  ```python
  from lib.ui.category_selector import select_categories
  from lib.collector.category_mapping import get_available_categories
  
  # Get available categories from model (uses FilteredElementCollector for performance)
  available_categories = get_available_categories(doc)
  
  # Show category selection dialog
  selected_categories = select_categories(
      doc, 
      title="Select Categories for Analysis", 
      multiselect=True
  )
  
  if selected_categories is None:
      # User selected "All Categories" or cancelled
      # None means process all categories
      process_all_categories = True
  else:
      # User selected specific categories for filtering
      process_all_categories = False
  ```

  This pattern provides graceful error handling, user cancellation support, and integrates with the category mapping utilities for consistent behavior across modules.

* **PyRevit Ribbon and Context:** You can use **script meta-variables** to integrate with Revit’s context. For instance, setting `__context__ = "Selection"` at the top of your IronPython script will make the button only active when the user has selected elements, which you could then use as a filtered scope for processing. Meta-variables can also define things like a description, author, etc., which appear in the UI. Use these to make the tool more user-friendly.

* **Feedback to User:** While the CPython computation runs (which might take a few seconds for large data), you can’t directly update a PyRevit form (since the main script is waiting). However, you can give immediate feedback *before* and *after*. For example, display a message: `"Gathering data, please wait..."` before data extraction, then maybe a `"Running analysis..."` just before launching CPython (perhaps using `script.get_output().print(...)` to the output pane). After the CPython returns and the model is updated, use `forms.alert("Successfully updated X elements")` or write a detailed summary to the output window. The PyRevit output window is a great place to show logs or even HTML tables of results if needed (PyRevit allows writing simple HTML to the output for formatted display).

* **CPython UI:** Prefer keeping user interaction in IronPython. If you run into issues using `pyrevit.forms`/WPF from CPython, move dialogs to IronPython and pass inputs/results to CPython via a simple handoff (e.g., JSON files).

* **Progress Indicators:** If your data processing might take a long time, consider informing the user. A simple approach is printing progress messages as mentioned. A more advanced approach could be to use the Revit status bar (not straightforward from Python) or a modal progress window. PyRevit doesn’t have a built-in progress bar widget accessible to IronPython that easily updates during a long process (since Revit’s UI thread would be blocked), so often just textual feedback or splitting work into chunks (so Revit’s message pump can breathe) is used. For example, if scraping 10,000 elements, you might collect in batches and call `revit.uidoc.RefreshActiveView()` occasionally, but this can be overkill. In summary, keep the user informed but not with overly complex UI that could itself introduce instability.

## IronPython–CPython Integration Strategies

Finally, a closer look at **how IronPython and CPython scripts work together** in PyRevit:

* **Execution Model:** When you click a PyRevit button, PyRevit determines which engine to use by examining the script’s shebang or file extension. For Python scripts, if the first line is `#! python3`, PyRevit will launch the CPython engine; if not (or if it’s `#! python2` or left blank), it uses IronPython by default. In a combined workflow, typically **the IronPython script is the one bound to the button**, and it explicitly calls the CPython script as described. This is because only one engine can run a given script; you cannot mix engines within one `.py` file. The “relationship” is thus one of master (IronPython script controlling the process) and subordinate (CPython script performing a task and returning data).

* **Data Handoff:** As discussed, use files or other IPC mechanisms to hand off data. Files are simplest and very reliable (just ensure you write to a path both processes can access, such as a temp directory or a known location). In theory, one could use in-memory techniques like sockets or named pipes to stream data between IronPython and CPython, but that adds complexity with little benefit for a single-user tool. A temporary JSON or CSV works well for even thousands of records (JSON serialization of a few MB is fine).

* **Synchronization:** The IronPython script should wait for CPython to finish before continuing. The `subprocess.run` approach inherently waits. If you wanted more asynchrony (e.g., show a non-blocking progress bar), you could spawn the CPython process in a non-blocking way (`subprocess.Popen`) and periodically check if it’s done. However, doing so in Revit’s single-threaded environment is tricky and usually not necessary unless the process is extremely long-running. For most applications, it’s acceptable for the Revit UI to be unresponsive during the computation (the user is expecting the tool to finish). Just make sure to wrap the entire operation in try/except so that if something hangs or fails, you can catch it and perhaps terminate the subprocess to avoid leaving a zombie process.

* **Error Propagation:** Decide how the IronPython side will know if the CPython script succeeded. A good pattern is to have the CPython script exit with a non-zero code on error. In Python, this can be done by calling `sys.exit(1)` on exceptions. The IronPython `subprocess.run` will give you a return code; if it’s not zero, you know something went wrong. You can then handle it (perhaps read an error log file that CPython produced, or at least alert the user that the analysis step failed). This way, issues in the data processing won’t be silently ignored. This rigor is important for an AI-assisted development approach as well – it makes debugging easier if the AI or developer can see clear error signals.

* **Logging and Debugging:** In IronPython, use `script.get_logger()` for consistent logging to the PyRevit console. In CPython, since `pyrevit.script` may not be fully functional, you might use Python’s built-in `logging` module to log to a file. This separation ensures that each environment records what happens in its own domain. If something goes wrong, you have logs from both sides. For example, IronPython log can show “Called CPython script with X elements, waiting…”, and CPython log can show “Loaded data, processing element 1234…, encountered KeyError on element 5678…”.

* **Maintainability:** Keep the interface between IronPython and CPython as small and simple as possible – e.g., a defined JSON schema for data exchange and a known sequence of steps. If changes are needed (like adding a new parameter to process), you’ll update both sides (IronPython extraction and CPython processing), so minimizing coupling helps. Clearly document this interface in comments so future developers (or AI assistants) know how data flows.

By following these practices, IronPython and CPython can collaborate effectively in your PyRevit extension. In summary, IronPython drives the Revit-side logic (UI, selection, data collection, and final model update) with stable integration to Revit’s API, while CPython operates as a powerful helper for computation and data handling using modern libraries. This division reflects the current best practices: *“If you want to use Python for development \[in PyRevit], it is preferred to use IronPython. CPython should only be used when accessing C-based Python packages is necessary.”*

## Conclusion

Developing a PyRevit tool with both IronPython 2.7 and CPython (`#! python3`) requires a thoughtful architecture but offers the best of both worlds: direct access to the Revit API and UI through IronPython, and advanced data processing capabilities of CPython. Ensure that the heavy tasks (e.g. statistical computations, Excel I/O, large dataset manipulations) are isolated in the CPython domain, whereas any operation that touches Revit (reading or writing the model, or interacting with the user through Revit’s interface) stays in the IronPython domain. The **relationship between the two engines is cooperative but loosely coupled** – think of IronPython as the orchestrator and CPython as a computational service. By exchanging information through well-defined channels (files or other means) and respecting each engine’s strengths, you can build a robust automation solution. This separation of concerns not only improves stability (since CPython’s known limitations won’t compromise your UI or Revit interaction) but also makes the code more modular and testable, which aligns perfectly with an AI-first iterative development process.

Finally, maintain rigorous documentation within your code. Clearly comment on where IronPython ends and CPython begins, list the required libraries and their versions, and document the data formats used for communication. This will aid any future maintenance – whether by a human team or an AI coding assistant. With these best practices, your project on Revit 2023 with PyRevit 5.2 can efficiently leverage IronPython for model handling and CPython for heavy data manipulation, providing a powerful and extensible toolchain for PBS/GBS data management in BIM.

**Sources:**

* PyRevit official guidance on IronPython vs. CPython usage https://pyrevitlabs.notion.site/Anatomy-of-CPython-Scripts-0e4cffeb545c4aa699fbe722c837c8d0#:~:text=CPython%20engine%20is%20under%20active,numpy%2C%20scipy%29%20is%20necessary
* PyRevit developer notes on CPython support limitations https://github.com/pyrevitlabs/pyRevit/releases#:~:text= https://discourse.pyrevitlabs.io/t/newbie-question-about-cpython/3038#:~:text=as%20of%20today%2C%20there%20are,be%20really%20tedious%20to%20debug
* PyRevit forum discussions on mixing CPython with PyRevit (using subprocess) https://discourse.pyrevitlabs.io/t/newbie-question-about-cpython/3038#:~:text=as%20of%20today%2C%20there%20are,be%20really%20tedious%20to%20debug https://discourse.pyrevitlabs.io/t/cpython-and-pyrevit/1739#:~:text=Thanks%20for%20your%20input,1731%20·%20eirannejad%2FpyRevit%20·%20GitHub
* PyRevit forum confirmation that PyRevit UI (WPF) is unavailable in CPython https://discourse.pyrevitlabs.io/t/cpython-and-ui-elements-eg-dialogs/8687#:~:text=You%20can%20use%20winforms%20for,not%20available%20for%20cpython%20scripts
* Example of adding Revit API references and using .NET classes in CPython https://discourse.pyrevitlabs.io/t/pyrevit-cpython-python-3-equivalent-of-the-ironpython-python-2-import-clr/533#:~:text=
* PyRevit script structuring tips (use of lib folder, imports) https://learnrevitapi.com/newsletter/pyrevit-script-anatomy#:~:text=reusable https://learnrevitapi.com/newsletter/pyrevit-script-anatomy#:~:text=We%20pretty%20much%20always%20need,them%20straight%20in%20your%20code
* PyRevit script logging and output utilities for IronPython https://pyrevitlabs.notion.site/Python-Script-Facilities-dcaf1e4660134974ba69e023b3714ddc?pvs=21#:~:text=from%20pyrevit%20import%20script

Return back: [`CodexWorkspace/docs/guides/pyrevit/README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/CodexWorkspace/docs/guides/pyrevit/README.md)
Return to root: [`README.md`](https://github.com/OriAshkenazi/ai-pyrevit-developer-template/blob/main/README.md)
