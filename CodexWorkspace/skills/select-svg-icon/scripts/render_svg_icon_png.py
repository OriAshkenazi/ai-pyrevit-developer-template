#!/usr/bin/env python3
"""
Render an SVG file to a square PNG icon for pyRevit commands.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render SVG to PNG with rsvg-convert for pyRevit icon output."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input SVG path.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output PNG path.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=96,
        help="Square PNG size in pixels. Default: 96",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print("Input SVG not found: {0}".format(input_path), file=sys.stderr)
        return 2

    converter = shutil.which("rsvg-convert")
    if not converter:
        print("Missing required tool: rsvg-convert", file=sys.stderr)
        return 2

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        converter,
        "-w",
        str(args.size),
        "-h",
        str(args.size),
        str(input_path),
        "-o",
        str(output_path),
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        print("Rendering failed with exit code {0}".format(exc.returncode), file=sys.stderr)
        return exc.returncode or 1

    print("Rendered PNG: {0}".format(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
