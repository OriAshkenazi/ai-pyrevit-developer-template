# SVGRepo Automated Acquisition (Default)

Use this protocol first for automated SVG acquisition.

## Inputs
- Search query list derived from script intent.
- Command identifier for folder naming (for example `align-walls`).
- Output base directory (`tmp/icons/<command-id>/`).

## URL Patterns
- Search page: `https://www.svgrepo.com/search/?q=<url-encoded-query>`
- Icon detail page: `https://www.svgrepo.com/svg/<icon-id>/<slug>/`
- Download URL: `https://www.svgrepo.com/download/<icon-id>/<slug>.svg`

## Automated Flow
Preferred implementation: `scripts/acquire_svgrepo_svg.py`.

1. Run queries against the search page and collect detail links.
2. Extract icon identifiers (`<icon-id>`) and slugs from detail URLs.
3. Download candidate SVG files from direct download URLs.
4. Validate each file immediately.
5. Stop when you have at least 3 valid candidates or query budget is exhausted.

## Script Quick Start

```bash
python3 CodexWorkspace/skills/select-svg-icon/scripts/acquire_svgrepo_svg.py \
  --command-id hello-world \
  -q "hello message bubble" \
  -q "chat icon" \
  --min-valid 3 \
  --max-candidates 5
```

## Download Routine
Use bounded retries and backoff for `HTTP 429` responses.

```bash
curl -L "https://www.svgrepo.com/download/${id}/${slug}.svg" -o "<output>.svg" -w '%{http_code}'
```

Suggested retry policy:
- Attempt up to 3 times per candidate.
- Backoff 3s, 10s, 30s on repeated `429`.
- Mark as `rate_limited` after final failure.

## Validation Checks
Run checks after every successful HTTP response:

```bash
test -s "<file>.svg"
head -c 512 "<file>.svg" | rg -i "<svg|<\\?xml"
rg -n "<html|vercel|cloudflare|security checkpoint" "<file>.svg"
```

Expected:
- File is non-empty.
- XML/SVG signature appears near the top.
- No challenge/HTML indicators are present.

## Fallback Trigger
Switch to `references/svgfind_acquisition.md` manual flow when either is true:
- Fewer than 3 valid candidates remain after query/retry budget.
- Site blocking prevents stable automated retrieval.

## Naming and Storage
- Raw downloads: `tmp/icons/<command-id>/raw/<icon-id>-<slug>.svg`
- Candidate shortlist: `tmp/icons/<command-id>/selected/`
- Final command icon asset: `<command-folder>/icon.png` (generated from selected SVG)

Keep discarded candidates under `tmp/` only.

## Provenance Record
Create `tmp/icons/<command-id>/sources.csv` with:
- `source_site` (`svgrepo`)
- `query`
- `detail_url`
- `download_url`
- `license_note`
- `attribution_required`
- `downloaded_at_utc`
- `sha256`
- `status`
