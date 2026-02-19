# SVGFind Manual Acquisition (Fallback)

Use this protocol only after the automated `svgrepo` path fails to produce enough valid SVG candidates.

## When to Use
- Automated source run completed with fewer than 3 valid candidates.
- Automated source is blocked by rate limiting or challenge flows.
- A domain-specific icon is not available on the automated source.

## Inputs
- Search query list derived from script intent.
- Command identifier for folder naming (for example `align-walls`).
- Output base directory (`tmp/icons/<command-id>/`).

## URL Patterns
- Search page: `https://www.svgfind.com/?q=<url-encoded-query>`
- Icon detail page: `https://www.svgfind.com/icon/<icon-id>/<slug>/` or `https://www.svgfind.com/svg/<icon-id>/<slug>/`
- Download link pattern on detail pages: `https://www.svgfind.com/download/<icon-id>/<slug>.svg`

Always prefer the actual download button/link `href` found on the detail page over reconstructed URLs.

## Manual Browser Flow
1. Open one query at a time on the search page.
2. Open 3-6 promising icon detail pages in new tabs.
3. On each detail page, locate SVG download links.
4. Prefer `Download SVG` over optimized variants for source-of-truth storage.
5. Save files into `tmp/icons/<command-id>/raw/<icon-id>-<slug>.svg`.
6. Record provenance and license notes in `tmp/icons/<command-id>/sources.csv`.

## Challenge Handling
`svgfind.com` may present anti-bot checkpoints (`HTTP 429`, verification pages).

If challenged:
1. Continue in an interactive browser session.
2. Complete checkpoint once, then reuse the same session tabs.
3. If blocked repeatedly, mark candidate as blocked and move on.

## File Validation Checks
Run checks immediately after each manual download:

```bash
test -s "<file>.svg"
head -c 512 "<file>.svg" | rg -i "<svg|<\\?xml"
rg -n "<html|vercel|cloudflare|security checkpoint" "<file>.svg"
```

Expected:
- File is non-empty.
- XML/SVG signature appears near the top.
- No challenge/HTML indicators are present.

## Naming and Storage
- Raw downloads: `tmp/icons/<command-id>/raw/<icon-id>-<slug>.svg`
- Candidate shortlist: `tmp/icons/<command-id>/selected/`
- Final command icon asset: `<command-folder>/icon.png` (generated from selected SVG)

Keep rejected candidates under `tmp/` only.

## Provenance Record
Create `tmp/icons/<command-id>/sources.csv` with:
- `source_site`
- `query`
- `detail_url`
- `download_url`
- `license_note`
- `attribution_required`
- `downloaded_at_utc`
- `sha256`
- `status`
