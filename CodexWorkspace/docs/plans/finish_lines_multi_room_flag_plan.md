# Finish Lines Multi-Room Flag (Revit 2025) - Development Plan

## Goal
Identify detail lines in a selected floor plan that cross or cover multiple rooms and export a report that flags those lines.

## Inputs
- Target view: user-picked FloorPlan view (prompted at runtime).
- Line elements: detail lines only in the selected view.
- Rooms: `OST_Rooms` on the same level as the selected view.
- Ignore unbounded rooms (area <= 0 or missing boundaries).

## Outputs
- CSV (UTF-8 BOM) with columns:
  - LineId
  - LineType
  - LineLengthCm
  - RoomCount
  - RoomIds (semicolon-separated)
  - RoomNumbers (semicolon-separated)
  - RoomNames (semicolon-separated)
  - MultiRoomFlag (Yes/No)

## Algorithm (Multi-Room Detection)
1. Resolve the target view:
   - Prompt for a FloorPlan view (default to active view if valid).
2. Collect detail lines in the view:
   - `FilteredElementCollector(doc, view.Id).OfClass(CurveElement)` filtered to `DetailCurve`.
3. Collect rooms on the same level:
   - `FilteredElementCollector(doc).OfCategory(OST_Rooms)` filtered by `room.LevelId == view.GenLevel.Id`.
   - Skip unbounded rooms (area <= 0 or missing boundaries).
4. Prepare room boundaries:
   - `SpatialElementBoundaryOptions` with `SpatialElementBoundaryLocation.Finish`.
   - Cache boundary curves per room and a Z height for point-in-room checks.
5. For each line:
   - Extract its `Curve`.
   - Find intersections between the line and all room boundary curves:
     - Use `Curve.Intersect` to gather intersection parameters along the line.
     - De-duplicate intersection params with a small tolerance.
   - Build segments between sorted params (including 0.0 and 1.0).
   - For each segment, test the midpoint:
     - Use `Room.IsPointInRoom(XYZ(x, y, z))` with `z` at the room's inside height.
     - Collect distinct room ids/numbers/names that contain a segment midpoint.
   - Fallback: if no intersections are found, test line endpoints + midpoint.
   - If more than one unique room is found, set `MultiRoomFlag = Yes`.
6. Export CSV:
   - Use UTF-8 BOM encoding to preserve Hebrew room names.

## Implementation Notes
- No document edits required; no `Transaction`.
- Cache room boundaries and Z heights for performance.
- Add tolerance when comparing intersection parameters to avoid duplicates.
- If a line runs exactly along a boundary, it may produce two rooms; that is desired.

## Decisions Locked In
- Include room ids and room numbers in the output.
- Skip unbounded rooms.
