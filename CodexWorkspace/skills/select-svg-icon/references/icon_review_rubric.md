# SVG Icon Review Rubric

Use this rubric during the vision pass to rank candidates consistently.

## Required Inputs
- Command name and script path.
- One-sentence command outcome.
- Risk level (`safe`, `warning`, `destructive`).
- Candidate icon images and source URLs.

## Weighted Scoring (0-5 Each)
1. Semantic match (weight 3).
Does the icon clearly represent the command verb and object?
2. Action polarity (weight 3).
Does the icon signal safe vs destructive behavior correctly?
3. Small-size legibility (weight 2).
Is the icon readable at `16px`, `24px`, and `32px`?
4. Style fit (weight 1).
Does stroke/fill density match nearby command icons?
5. License fit (weight 2).
Can the icon be used and redistributed in the target repo?

## Decision Rule
- Prefer candidates with no score below `3` in criteria 1-3.
- Break ties by higher semantic match, then higher legibility.
- If all candidates score below `3` in semantic match, run another search round.

## Vision Prompt Template
Use this template when asking a vision-capable model to compare icon candidates:

```text
Task: pick the best icon for a pyRevit command.

Command:
- Name: <command>
- Script summary: <what the script does>
- Risk level: <safe|warning|destructive>
- User action expected: <what user clicks to do>

Evaluate each candidate icon image using:
1) semantic match,
2) action polarity,
3) legibility at small sizes,
4) style fit,
5) license risk.

Return:
- Ranked table with 0-5 score per criterion.
- One recommended icon.
- One-sentence rationale and one risk callout.
```

## Common Mismatch Patterns
- Magnifier icons for commands that modify data.
- Trash/delete symbols for reversible hide/filter actions.
- Generic gear icons for action commands that are not settings.
- Over-detailed glyphs that blur at button size.
