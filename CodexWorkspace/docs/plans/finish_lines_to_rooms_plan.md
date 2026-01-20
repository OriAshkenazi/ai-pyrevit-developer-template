# Finish Lines to Rooms (Revit 2025) - Development Plan

## Goal
Map each finish line in a selected floor plan to the nearest room and export a report with line length (cm), line type, room id/number/name, and room height (limit offset - base offset). Room names are Hebrew, so output must preserve Unicode.

## Inputs
- Target view: user-picked floor plan view (prompted at runtime).
- Line elements: detail lines only representing wall finishes in that view.
- Rooms: `OST_Rooms` on the same level as the target view.
- Ignore unbounded rooms (area <= 0 or missing boundaries).

## Outputs
- Excel-friendly report with columns:
  - LineId
  - LineType
  - LineLengthCm
  - RoomId
  - RoomNumber
  - RoomName
  - RoomHeightCm
  - NearestBoundaryDistanceCm (for lines not inside any room)
- Default format: UTF-8 CSV with BOM (opens cleanly in Excel). If strict `.xlsx` is required, switch to a CPython path (openpyxl) or ship an OpenXML .NET dependency.

## Algorithm (Nearest-Room Match)
1. Resolve the target view:
   - Prompt the user to pick a FloorPlan view from a list (default to active view if it is a FloorPlan).
2. Collect finish lines in that view:
   - `FilteredElementCollector(doc, view.Id)` filtered to `CurveElement` and `DetailCurve`.
   - Optionally allow filtering by line style name if there are multiple line styles in the view.
3. Collect rooms on the same level:
   - `FilteredElementCollector(doc).OfCategory(OST_Rooms)` and filter by `room.LevelId == view.GenLevel.Id`.
   - Skip unbounded rooms (area <= 0 or missing boundaries).
4. Prepare room boundaries:
   - Use `SpatialElementBoundaryOptions` with `SpatialElementBoundaryLocation.Finish`.
   - Build 2D boundary curves in the view plane (XY) for distance checks.
5. Match each line to a room:
   - Compute line start, end, and midpoint.
   - First pass: if any point is inside a room (`Room.IsPointInRoom` with Z = room level elevation), assign that room.
   - Fallback: compute the minimum 2D distance between the line (sampled points) and each room boundary curve using `Curve.Project`/`Distance`.
   - Pick the room with the smallest distance; tie-break by smallest distance to line midpoint.
   - Record `NearestBoundaryDistanceCm` even when a room is assigned (0 for inside-room matches).
6. Extract report fields:
   - Length: `curve.Length` converted via `UnitUtils.ConvertFromInternalUnits(..., UnitTypeId.Centimeters)`.
   - Line type: `doc.GetElement(line.GetTypeId()).Name` or `line.LineStyle.Name`.
   - Room id: `room.Id.IntegerValue`.
   - Room number: `ROOM_NUMBER` parameter.
   - Room name: `ROOM_NAME` parameter.
   - Room height: `(ROOM_UPPER_OFFSET - ROOM_BASE_OFFSET)` converted to cm; fallback to `ROOM_HEIGHT` if upper limit is not set.
   - Nearest boundary distance: smallest computed distance converted to cm; set to 0 when inside-room match succeeds.
7. Export:
   - `forms.save_file` to choose path.
   - Write UTF-8 BOM CSV using `System.Text.UTF8Encoding(True)` to preserve Hebrew names.

## Implementation Notes
- No document changes needed, so no `Transaction` is required.
- Cache room boundary data to avoid repeated boundary extraction.
- Validate: missing rooms, invalid view, unbounded rooms, or non-curve elements.
- Use read-only collectors and keep memory usage low by releasing large lists after export.

## Decisions Locked In
- Detail lines only (no model lines).
- CSV export is acceptable.
- Prompt for a target view at runtime.
