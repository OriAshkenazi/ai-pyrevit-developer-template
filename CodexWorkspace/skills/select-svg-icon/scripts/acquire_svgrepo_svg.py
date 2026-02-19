#!/usr/bin/env python3
"""
Automated SVG acquisition from SVGRepo for the select-svg-icon skill.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
SEARCH_URL_TMPL = "https://www.svgrepo.com/search/?q={query}"
DETAIL_URL_TMPL = "https://www.svgrepo.com/svg/{icon_id}/{slug}/"
DOWNLOAD_URL_TMPL = "https://www.svgrepo.com/download/{icon_id}/{slug}.svg"
DETAIL_LINK_RE = re.compile(r"/svg/(?P<icon_id>\d+)/(?P<slug>[A-Za-z0-9_-]+)")
BACKOFF_SECONDS = (0, 3, 10)
CHALLENGE_MARKERS = (
    b"security checkpoint",
    b"cloudflare",
    b"vercel",
    b"cf-ray",
    b"please enable javascript",
)


@dataclass(frozen=True)
class Candidate:
    icon_id: str
    slug: str
    query: str

    @property
    def detail_url(self) -> str:
        return DETAIL_URL_TMPL.format(icon_id=self.icon_id, slug=self.slug)

    @property
    def download_url(self) -> str:
        return DOWNLOAD_URL_TMPL.format(icon_id=self.icon_id, slug=self.slug)

    @property
    def file_name(self) -> str:
        return "{0}-{1}.svg".format(self.icon_id, self.slug)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Acquire SVG candidates from svgrepo.com."
    )
    parser.add_argument(
        "--command-id",
        required=True,
        help="Command identifier for output folder naming (for example: hello-world).",
    )
    parser.add_argument(
        "-q",
        "--query",
        action="append",
        default=[],
        help="Search query. Repeat for multiple queries.",
    )
    parser.add_argument(
        "--seed-icon",
        action="append",
        default=[],
        help="Seed candidate in icon_id:slug format. Repeatable.",
    )
    parser.add_argument(
        "--base-dir",
        default="tmp/icons",
        help="Base output directory. Default: tmp/icons",
    )
    parser.add_argument(
        "--min-valid",
        type=int,
        default=3,
        help="Minimum valid downloads required for success. Default: 3",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=5,
        help="Stop after this many valid downloads. Default: 5",
    )
    parser.add_argument(
        "--max-download-attempts",
        type=int,
        default=20,
        help="Maximum candidate download attempts. Default: 20",
    )
    return parser.parse_args()


def http_get(url: str) -> tuple[int, dict, bytes]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.svgrepo.com/",
    }
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=45) as response:
            return response.getcode(), dict(response.headers), response.read()
    except HTTPError as exc:
        try:
            body = exc.read()
        except Exception:
            body = b""
        return exc.code, dict(exc.headers or {}), body
    except URLError:
        return 0, {}, b""


def fetch_with_retries(url: str) -> tuple[int, dict, bytes]:
    last_status = 0
    last_headers: dict = {}
    last_body = b""
    for delay in BACKOFF_SECONDS:
        if delay:
            time.sleep(delay)
        status, headers, body = http_get(url)
        last_status, last_headers, last_body = status, headers, body
        if status != 429:
            return status, headers, body
    return last_status, last_headers, last_body


def is_challenge_payload(body: bytes) -> bool:
    lowered = body.lower()
    if b"<html" not in lowered:
        return False
    return any(marker in lowered for marker in CHALLENGE_MARKERS)


def is_valid_svg_payload(body: bytes) -> bool:
    lowered = body.lower()
    if b"<svg" not in lowered and b"<?xml" not in lowered:
        return False
    if is_challenge_payload(body):
        return False
    return True


def parse_seed_icon(seed: str) -> Candidate | None:
    if ":" not in seed:
        return None
    icon_id, slug = seed.split(":", 1)
    icon_id = icon_id.strip()
    slug = slug.strip().strip("/")
    if not icon_id.isdigit() or not slug:
        return None
    return Candidate(icon_id=icon_id, slug=slug, query="seed")


def parse_search_candidates(query: str, html: str) -> list[Candidate]:
    found: list[Candidate] = []
    seen: set[tuple[str, str]] = set()
    for match in DETAIL_LINK_RE.finditer(html):
        icon_id = match.group("icon_id")
        slug = match.group("slug")
        key = (icon_id, slug)
        if key in seen:
            continue
        seen.add(key)
        found.append(Candidate(icon_id=icon_id, slug=slug, query=query))
    return found


def write_sources_csv(csv_path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "source_site",
        "query",
        "detail_url",
        "download_url",
        "license_note",
        "attribution_required",
        "downloaded_at_utc",
        "sha256",
        "status",
    ]
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    args = parse_args()

    if not args.query and not args.seed_icon:
        print("No acquisition source provided. Add --query or --seed-icon.", file=sys.stderr)
        return 2

    command_dir = Path(args.base_dir) / args.command_id
    raw_dir = command_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    csv_path = command_dir / "sources.csv"

    candidate_queue: list[Candidate] = []
    queued_keys: set[tuple[str, str]] = set()
    rows: list[dict[str, str]] = []

    for seed in args.seed_icon:
        candidate = parse_seed_icon(seed)
        if not candidate:
            print("Skipping invalid --seed-icon value: {0}".format(seed), file=sys.stderr)
            continue
        key = (candidate.icon_id, candidate.slug)
        if key in queued_keys:
            continue
        queued_keys.add(key)
        candidate_queue.append(candidate)

    for query in args.query:
        search_url = SEARCH_URL_TMPL.format(query=quote_plus(query))
        status, _, body = fetch_with_retries(search_url)
        if status != 200 or is_challenge_payload(body):
            rows.append(
                {
                    "source_site": "svgrepo",
                    "query": query,
                    "detail_url": search_url,
                    "download_url": "",
                    "license_note": "",
                    "attribution_required": "",
                    "downloaded_at_utc": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "sha256": "",
                    "status": "search_failed",
                }
            )
            continue

        html = body.decode("utf-8", errors="ignore")
        for candidate in parse_search_candidates(query, html):
            key = (candidate.icon_id, candidate.slug)
            if key in queued_keys:
                continue
            queued_keys.add(key)
            candidate_queue.append(candidate)

    valid_count = 0
    attempts = 0

    for candidate in candidate_queue:
        if valid_count >= args.max_candidates:
            break
        if attempts >= args.max_download_attempts:
            break

        attempts += 1
        status, _, body = fetch_with_retries(candidate.download_url)
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        row = {
            "source_site": "svgrepo",
            "query": candidate.query,
            "detail_url": candidate.detail_url,
            "download_url": candidate.download_url,
            "license_note": "",
            "attribution_required": "",
            "downloaded_at_utc": timestamp,
            "sha256": "",
            "status": "",
        }

        if status != 200:
            row["status"] = "http_{0}".format(status)
            rows.append(row)
            continue

        if not is_valid_svg_payload(body):
            row["status"] = "invalid_payload"
            rows.append(row)
            continue

        output_path = raw_dir / candidate.file_name
        output_path.write_bytes(body)
        row["sha256"] = sha256_bytes(body)
        row["status"] = "downloaded"
        rows.append(row)
        valid_count += 1

    write_sources_csv(csv_path, rows)

    print("Candidates queued: {0}".format(len(candidate_queue)))
    print("Download attempts: {0}".format(attempts))
    print("Valid SVG downloads: {0}".format(valid_count))
    print("Sources CSV: {0}".format(csv_path))

    if valid_count < args.min_valid:
        print(
            "Valid candidates below threshold ({0} < {1}).".format(
                valid_count, args.min_valid
            ),
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
