---
name: select-svg-icon
description: Choose and validate SVG icons for pyRevit extension commands. Use when creating or updating a pyRevit pushbutton and you need an SVG-only icon workflow with automated acquisition from svgrepo.com first, manual fallback on svgfind.com, and vision-based semantic ranking before finalizing icon assets.
---

# Select SVG Icon

Use this skill to pick an icon that matches a pyRevit command's behavior, not just its name.

## SVG-Only Policy

- Acquire source assets as `.svg` only.
- Reject PNG-only sources during acquisition.
- Generate `icon.png` only in the finalization step for pyRevit compatibility.

## Workflow

1. Read the target command script and capture an intent brief:
- Primary verb (`select`, `align`, `export`, `delete`).
- Primary object (`walls`, `views`, `parameters`, `sheets`).
- Risk level (`safe`, `warning`, `destructive`).
- User context (`single element`, `batch`, `analysis`, `settings`).

2. Build 3-6 SVG search queries from the brief.
- Start with `verb noun`.
- Add one domain synonym.
- Add one metaphor fallback only if literal matches are weak.

3. Collect 3-5 candidate SVG icons with ordered sources.
- Keep candidate downloads and previews under `tmp/icons/<command-name>/`.
- Record each source URL and license note.
- Run `scripts/acquire_svgrepo_svg.py --command-id <command-name> -q "<query>" ...` first.
- Run `references/svgrepo_automated_acquisition.md` first.
- If automated acquisition yields fewer than 3 valid candidates, run `references/svgfind_acquisition.md` as manual fallback.

4. Run a vision pass before deciding.
- Compare candidates against the script intent and UI context.
- Score and rank with `references/icon_review_rubric.md`.
- Reject icons that imply the wrong action direction or risk level.
- If vision tools are unavailable, use candidate metadata as fallback and mark confidence as low.

5. Finalize for pyRevit.
- Save the selected icon to the command folder as `icon.png`.
- Generate `icon.png` from the selected SVG with `scripts/render_svg_icon_png.py`.
- Check legibility at `16px`, `24px`, and `32px` before finalizing.
- Keep rejected candidates in `tmp/` only.
- Add a one-line rationale in task/review notes to preserve intent for future changes.

## Use With Other Skills

- Pair with `develop-pyrevit-extensions` for command scaffolding and workflow docs.
- Pair with `pyrevit-revit-20xx` skills when API behavior affects icon semantics.

## Technical Reference

- Open `scripts/acquire_svgrepo_svg.py` for deterministic automated SVG acquisition.
- Open `scripts/render_svg_icon_png.py` to render final `icon.png` from SVG.
- Open `references/svgrepo_automated_acquisition.md` for the default automated acquisition path.
- Open `references/svgfind_acquisition.md` for the manual fallback path.
- Use `references/icon_review_rubric.md` after acquisition to rank candidates with vision.
