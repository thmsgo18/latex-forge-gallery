#!/usr/bin/env python3
"""Build a flat ZIP for each gallery template.

Each ZIP contains the template directory's files at its root (``main.tex``
at the top level) so `latex-forge template install` can fetch and extract a
single template directly, instead of downloading the whole gallery
repository.

Used by .github/workflows/build-archives.yml, which publishes the output
directory to the `dist` branch. The resulting files are served at:

    https://raw.githubusercontent.com/thmsgo18/latex-forge-gallery/dist/<name>.zip

Run from the repo root:
    python3 scripts/build_archives.py [--output dist-archives]
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = ROOT / "templates"


def build_archive(template_dir: Path, output_dir: Path) -> Path:
    zip_path = output_dir / f"{template_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(template_dir.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(template_dir))
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", default="dist-archives", help="Output directory for the ZIPs"
    )
    args = parser.parse_args()

    output_dir = ROOT / args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for cat_dir in sorted(TEMPLATES_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        for tmpl_dir in sorted(cat_dir.iterdir()):
            if tmpl_dir.is_dir() and (tmpl_dir / "main.tex").exists():
                build_archive(tmpl_dir, output_dir)
                count += 1

    print(f"Built {count} template archives in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
