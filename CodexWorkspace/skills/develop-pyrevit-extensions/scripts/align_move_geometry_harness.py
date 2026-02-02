#! python
# Align+Move geometry helper harness for quick smoke checks (IronPython-safe).

import imp
import os

from Autodesk.Revit.DB import Line, XYZ  # type: ignore import
from pyrevit import forms, script

OUTPUT = script.get_output()
HARNESS_CASES = []


def load_align_move_module():
    """Load the Align+Move command module so we can reuse its math helpers."""
    scripts_dir = os.path.dirname(__file__)
    command_path = os.path.abspath(
        os.path.join(
            scripts_dir,
            "..",
            "..",
            "Wall Openings.tab",
            "Adjust.panel",
            "Align+Move.pushbutton",
            "script.py",
        )
    )
    module = imp.load_source("align_move_command", command_path)
    return module


def record_case(name, passed, detail=""):
    """Track individual harness assertions."""
    HARNESS_CASES.append((name, bool(passed), detail))


def vector_almost_equal(vec, other, tol=1e-6):
    """Return True when two XYZ vectors are approximately the same."""
    if vec is None or other is None:
        return False
    return (vec - other).GetLength() <= tol


def run_geometry_smoke_tests(module):
    """Execute lightweight checks for geometry helpers."""
    normalize = module.normalize
    project_point_to_plane = module.project_point_to_plane
    project_point_to_line = module.project_point_to_line
    ensure_line_in_view_plane = module.ensure_line_in_view_plane
    compute_offset_direction = module.compute_offset_direction
    get_view_context = module.get_view_context

    vector = XYZ(3, 4, 0)
    unit = normalize(vector)
    record_case(
        "normalize length",
        unit is not None and abs(unit.GetLength() - 1.0) <= 1e-6,
    )
    record_case(
        "normalize direction",
        vector_almost_equal(unit, XYZ(0.6, 0.8, 0.0)),
    )

    origin = XYZ(0, 0, 0)
    normal = XYZ.BasisZ
    point = XYZ(5, 5, 7)
    projected = project_point_to_plane(point, origin, normal)
    record_case("project_point_to_plane z=0", abs(projected.Z) <= 1e-6)

    line = Line.CreateBound(XYZ.Zero, XYZ.BasisX.Multiply(10))
    point_off_line = XYZ(3, 5, 0)
    on_line = project_point_to_line(point_off_line, line)
    record_case("project_point_to_line x preserved", abs(on_line.X - 3.0) <= 1e-6)
    record_case("project_point_to_line y cleared", abs(on_line.Y) <= 1e-6)

    view = __revit__.ActiveUIDocument.ActiveView  # type: ignore[name-defined]
    view_context = get_view_context(view)
    elevated_line = Line.CreateBound(XYZ(0, 0, 5), XYZ(10, 0, 5))
    flattened = ensure_line_in_view_plane(elevated_line, view_context)
    if flattened is None:
        record_case("ensure_line_in_view_plane flatten", False, "Flattened line is None.")
        return
    record_case(
        "ensure_line_in_view_plane flatten",
        abs(flattened.GetEndPoint(0).Z) <= 1e-6,
    )

    horizontal_direction = compute_offset_direction("Horizontal", flattened, view_context)
    vertical_direction = compute_offset_direction("Vertical", flattened, view_context)
    ref_dir = normalize(flattened.Direction)
    if horizontal_direction is None:
        record_case("compute_offset_direction horizontal unit", False, "Horizontal direction unresolved.")
    else:
        record_case(
            "compute_offset_direction horizontal unit",
            abs(horizontal_direction.GetLength() - 1.0) <= 1e-6,
        )
        record_case(
            "compute_offset_direction horizontal perpendicular",
            ref_dir is not None and abs(horizontal_direction.DotProduct(ref_dir)) <= 1e-6,
        )
    if vertical_direction is None:
        record_case("compute_offset_direction vertical", False, "Vertical direction unresolved.")
    else:
        record_case(
            "compute_offset_direction vertical alignment",
            vector_almost_equal(vertical_direction, view_context.get("up")),
        )


def report_results():
    """Display harness results via pyRevit output and alert."""
    passing = [name for name, passed, _ in HARNESS_CASES if passed]
    failing = [(name, detail) for name, passed, detail in HARNESS_CASES if not passed]

    OUTPUT.print_md("## Align+Move Geometry Harness Results")
    for name, passed, detail in HARNESS_CASES:
        status = "PASS" if passed else "FAIL"
        OUTPUT.print_md("- {0}: {1} {2}".format(status, name, detail))

    summary_lines = ["Geometry harness completed.", "Passing checks: {0}".format(len(passing))]
    if failing:
        summary_lines.append("Failing checks: {0}".format(len(failing)))
        summary_lines.append("")
        summary_lines.append("Failures:")
        for name, detail in failing:
            if detail:
                summary_lines.append("- {0}: {1}".format(name, detail))
            else:
                summary_lines.append("- {0}".format(name))
    else:
        summary_lines.append("All checks passed.")

    forms.alert("\n".join(summary_lines))


def main():
    del HARNESS_CASES[:]
    module = load_align_move_module()
    run_geometry_smoke_tests(module)
    report_results()


if __name__ == "__main__":
    main()

