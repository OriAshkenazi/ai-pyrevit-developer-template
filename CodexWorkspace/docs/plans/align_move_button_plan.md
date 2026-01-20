#! codex-env plan

# Align+Move Wall Opening Tool

## Product Snapshot
- **Value**: One-step command aligns a selected opening family to a picked reference line in the active view and offsets it perpendicular by a user-entered distance, eliminating repeated Align/Move operations.
- **Target Users**: As-built coordinators updating wall openings in section views; BIM modelers applying survey adjustments across coordination sets.
- **Problem**: Field measurements currently require manual align-then-move sequences on multiple axes, which is slow and introduces placement mistakes.
- **Job to Be Done**: "When I receive updated as-made measurements, I want to align a wall opening to the correct axis and apply the measured perpendicular offset in a single confirmation so I can refresh sections quickly without misplacement."
- **Primary Scenario**: User launches Align+Move from the Wall Openings ribbon tab, selects one or more openings, picks a visible reference line/edge, enters signed offset and axis mode, previews the displacement text, confirms, and the tool applies alignment plus perpendicular move within one transaction.
- **Success Metric**: Opening(s) are coincident with the reference line within Revit tolerance and translated exactly by the specified offset.

### Acceptance Criteria
- Align + Move executes in one confirmation on a single opening referencing a linear edge or detail line in the active view.
- Batch mode reuses the same reference and offset for multiple selected openings.
- Pinned or design-option elements are skipped with a clear warning.
- Transaction appears as a single undo step.
- Preview text reports the computed displacement before apply.

### Out of Scope
- Cross-view or 3D alignment with geometry invisible in the active view.
- Automatic detection of ceilings/floors beyond the provided reference + offset workflow.

## Development Plan
- **Command Container**: pyRevit external command surfaced via Wall Openings ribbon group, transaction titled "Align+Move Wall Opening".
- **API Surface**: `Selection.PickObject/PickObjects`, `ElementTransformUtils.RotateElement`, `ElementTransformUtils.MoveElement`, `Reference.ParseFromStableRepresentation` (future enhancement).
- **Inputs**: Opening elements (Generic Models/Windows/custom families), reference line or edge in-view, signed perpendicular offset (double, feet internal units), axis mode toggle (vertical vs horizontal alignment priority).
- **Outputs**: Transformed elements and a summary dialog logging applied offsets or failures.
- **UI Spec**: Ribbon button labeled Align+Move; pyRevit dialog with axis radio buttons, offset textbox (unit string displayed), batch-apply checkbox, preview text of delta; warnings for pinned/non-modifiable elements.

## Work Paths
### Path A - Command Scaffolding & Ribbon Wiring
- **A1**: Audit existing tab/panel structure under `Test.extension` to confirm whether a `Wall Openings.tab` exists or should be created; decide final pushbutton location.
- **A2**: Copy `CodexWorkspace/scripts/new_command_template.py` into the chosen pushbutton folder (e.g., `Wall Openings.tab\Adjust.panel\Align+Move.pushbutton\script.py`) and retitle the transaction to "Align+Move Wall Opening".
- **A3**: Add required pyRevit metadata (icon, optional `bundle.yaml`, tooltip) so the Align+Move button appears on the desired ribbon tab and loads inside pyRevit.

### Path B - Selection Workflow & Validation
- **B1**: Implement selection intake that respects active view preselection, falling back to `Selection.PickObjects` for wall opening families.
- **B2**: Enforce category/modifiability checks (pinned, design option, read-only) and collect per-element warnings for the summary dialog.
- **B3**: Cache validated openings with host wall references and geometry handles needed for downstream alignment.

### Path C - Geometry Alignment & Offset Calculations
- **C1**: Build helper utilities for parsing the picked reference into view-plane vectors and determining alignment axis (vertical vs horizontal modes).
- **C2**: Project each opening's driving point/curve onto the reference and apply the necessary rotation/slide to achieve coincidence within tolerance.
- **C3**: Derive the perpendicular offset vector, convert user-entered units to internal feet, and queue move transforms for batch execution.

### Path D - Transaction Execution & Feedback UX
- **D1**: Create a pyRevit dialog capturing axis mode, signed offset, batch reuse toggle, and a live preview string of the computed displacement.
- **D2**: Execute the align + move sequence inside a single `Transaction`, applying `ElementTransformUtils` calls and buffering failures without partial commits.
- **D3**: Surface a results dialog summarizing applied offsets, skipped elements (pinned/design option), and provide undo guidance.

### Path E - Testing, Documentation, and Hardening
- **E1**: Geometry harness `CodexWorkspace/scripts/align_move_geometry_harness.py` loads the command module and runs smoke checks for normalization, projection, and offset direction math.
- **E2**: Manual regression steps outlined below leverage `docs/checklists/testing_strategy.md` and capture edge-case observations for future test sessions.
- **E3**: Integration dry-run procedure defined below details how to exercise the ribbon pushbutton in a sample project, confirm transaction behavior, and review warnings.

#### Manual Regression Steps (E2)
1. Review `docs/checklists/testing_strategy.md` for general guidance, then target Align+Move specific coverage.
2. Launch Revit with a coordination model containing wall openings; ensure pyRevit loads the updated extension.
3. Validate selection workflow: attempt preselection, direct selection, and cancellation paths; confirm skip messages for pinned and design-option elements.
4. Exercise geometry scenarios: horizontal and vertical axis modes, zero and non-zero offsets, multiple openings sharing a reference, elements lacking LocationCurve (bounding-box fallback).
5. Run the geometry harness (`CodexWorkspace/scripts/align_move_geometry_harness.py`) to confirm helper math after any refactor.
6. Record findings and anomalies in the plan doc or project issue tracker before sign-off.

#### Integration Dry Run Guidance (E3)
1. In a staging project, add the Align+Move pushbutton to a dedicated ribbon panel if not already present, then reload pyRevit.
2. Trigger the command, select a mix of supported and unsupported openings, pick a reference, and apply offsets; observe preview text matches expected move vectors.
3. After execution, inspect the Revit undo stack (single entry) and verify applied openings now align with the reference line plus offset in project units.
4. Review the results dialog for applied, failed, and skipped entries; cross-reference Revit warnings or failure messages for any skipped elements.
5. Commit outcomes to team notes, including screenshots or measured dimensions, to build a repeatable regression history.

### Engineering Considerations
- Hosted openings may depend on host wall constraints; adjust transforms relative to host plane before applying offsets.
- Generic models lacking `LocationCurve` should use bounding-box centroids projected onto the view plane.
- Skip references outside the active view plane with an informative alert.
- Maintain exception handling with rollback to keep document clean on failures.

### Testing Plan
- **Unit-like**: Verify geometry helpers (projection, perpendicular vector determination) and unit conversion utilities.
- **Integration**: Section view fixture with wall, ceiling, floor; test vertical/horizontal modes, pinned-element warnings, multi-selection reuse.
- **Regression**: Add to nightly pyRevit smoke run ensuring command loads and executes on template project without unhandled exceptions.

### Risks & Open Questions
- Elements without `LocationCurve` may not align cleanly; might require per-family adjustments.
- Large offsets risk breaking host relationships; need guardrails or prompts.
- Preview accuracy hinges on consistent view-plane calculations.
- Should offset persist across sessions (project parameter or config)?
- Do we extend reference selection to linked-model geometry?
