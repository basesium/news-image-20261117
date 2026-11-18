#!/usr/bin/env python3
"""News-image entry for make.fun competition news-image-20261117.

The entry is a program that writes one image summing up the world's news
of Tuesday 17 November 2026 to /output/entry.png. The image is bundled
with this repository as entry.png (a newspaper front page: Iran's drone
attack on the U.S. radar in Bahrain, Ukraine's strike on the Crimea
bridge, the third U.S. carrier reaching the Middle East, Trump heading
to Asia for nuclear talks, Britain sanctioning Israeli settlement
firms, and the Pentagon failing its audit for a ninth year).

This program copies that bundled image to the output directory. It is
fully deterministic: the same bytes every run, no network, no clock,
no randomness. Standard library only, Python 3.13.

Run it outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"news-image: bundled image missing: {SOURCE}", file=sys.stderr)
        return 2
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    size = target.stat().st_size
    print(f"news-image: copied entry.png ({size} bytes) to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
