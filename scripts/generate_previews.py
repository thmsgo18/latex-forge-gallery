#!/usr/bin/env python3
"""Compile each template and generate preview.pdf + preview.png in previews/<category>/."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = ROOT / "templates"
PREVIEWS_DIR = ROOT / "previews"
GALLERY_JSON = ROOT / "gallery.json"

LATEX_BIN = Path("/Library/TeX/texbin")
PDFTOPPM = Path("/opt/homebrew/bin/pdftoppm")

BUILD_ARTIFACTS = {
    ".aux", ".log", ".toc", ".out", ".bbl", ".blg", ".lof", ".lot",
    ".fls", ".fdb_latexmk", ".snm", ".nav", ".vrb", ".idx", ".ind",
    ".ilg", ".bcf", ".run.xml", ".synctex.gz", ".xdv",
}


def load_gallery() -> dict:
    with open(GALLERY_JSON) as f:
        return json.load(f)


def get_template_info(gallery: dict) -> dict[str, dict]:
    return {t["name"]: t for t in gallery["templates"]}


def run_cmd(cmd: list, cwd: Path, timeout: int = 90) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr).decode("utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return -1, "Timeout"


def needs_biber(template_dir: Path) -> bool:
    main = (template_dir / "main.tex").read_text(errors="replace")
    return "biber" in main.lower() or "biblatex" in main.lower()


def compile(template_dir: Path, engine: str) -> tuple[Path | None, str]:
    """Compile main.tex with optional biber pass. Returns (pdf, error_msg)."""
    exe = str(LATEX_BIN / engine)
    # No -halt-on-error: some templates have non-fatal warnings treated as errors;
    # we check for PDF output to determine success.
    latex_cmd = [exe, "-interaction=nonstopmode", "main.tex"]

    def pdf_exists() -> Path | None:
        p = template_dir / "main.pdf"
        if p.exists():
            return p
        pdfs = list(template_dir.glob("*.pdf"))
        return pdfs[0] if pdfs else None

    # Pass 1
    code, log = run_cmd(latex_cmd, template_dir)
    if pdf_exists() is None and code != 0:
        return None, "Pass 1 failed (no PDF):\n" + "\n".join(log.splitlines()[-25:])

    # Biber pass if needed (prefer Homebrew biber, fallback to TeX Live)
    BIBER = Path("/opt/homebrew/bin/biber")
    if not BIBER.exists():
        BIBER = LATEX_BIN / "biber"
    if needs_biber(template_dir) and (template_dir / "main.bcf").exists():
        code, blog = run_cmd([str(BIBER), "main"], template_dir, timeout=60)
        # Only fail if biber produced no .bbl output at all (warnings are OK)
        if code != 0 and not (template_dir / "main.bbl").exists():
            return None, "Biber failed:\n" + "\n".join(blog.splitlines()[-15:])

    # Pass 2
    run_cmd(latex_cmd, template_dir)

    # Pass 3 (biber documents need an extra pass for cross-ref resolution)
    if needs_biber(template_dir):
        run_cmd(latex_cmd, template_dir)

    pdf = pdf_exists()
    if pdf is None:
        return None, "No PDF generated\n" + "\n".join(log.splitlines()[-15:])

    return pdf, ""


def pdf_to_png(pdf: Path, png: Path) -> bool:
    """Convert first page of pdf to png via pdftoppm."""
    prefix = str(png.with_suffix(""))
    r = subprocess.run(
        [str(PDFTOPPM), "-r", "150", "-png", "-singlefile", str(pdf), prefix],
        capture_output=True,
    )
    return r.returncode == 0 and png.exists()


def cleanup_artifacts(template_dir: Path) -> None:
    for p in template_dir.iterdir():
        if p.suffix in BUILD_ARTIFACTS:
            p.unlink(missing_ok=True)
    # Remove main.pdf from template dir (we copied it to previews/)
    (template_dir / "main.pdf").unlink(missing_ok=True)


def process_template(name: str, info: dict, skip_existing: bool) -> str:
    """Return 'ok', 'skip', or an error string."""
    category = info["category"]
    engine = info.get("engine", "pdflatex")
    template_dir = TEMPLATES_DIR / category / name

    out_dir = PREVIEWS_DIR / category
    out_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = out_dir / f"{name}.pdf"
    out_png = out_dir / f"{name}.png"

    if skip_existing and out_png.exists():
        return "skip"

    if not template_dir.is_dir():
        return f"template dir not found: {template_dir}"

    print(f"  [{engine}] compiling...", end=" ", flush=True)
    pdf, err = compile(template_dir, engine)

    if pdf is None:
        cleanup_artifacts(template_dir)
        return err

    # Copy PDF to previews/
    shutil.copy2(pdf, out_pdf)

    # Generate PNG from the preview PDF (not the one in template dir)
    ok = pdf_to_png(out_pdf, out_png)

    # Clean build artifacts from template dir
    cleanup_artifacts(template_dir)

    if not ok:
        return "PDF compiled but PNG conversion failed"

    return "ok"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate template previews")
    parser.add_argument("--only", nargs="+", metavar="NAME", help="Only compile these templates")
    parser.add_argument("--skip-existing", action="store_true", help="Skip templates that already have a preview.png")
    parser.add_argument("--category", help="Only compile templates in this category")
    args = parser.parse_args()

    gallery = load_gallery()
    templates = get_template_info(gallery)

    targets = list(templates.items())
    if args.only:
        targets = [(n, i) for n, i in targets if n in args.only]
    if args.category:
        targets = [(n, i) for n, i in targets if i["category"] == args.category]

    succeeded, skipped, failed = [], [], []

    for name, info in targets:
        print(f"\n{'─' * 60}")
        print(f"  {name}  ({info['category']} / {info.get('engine', 'pdflatex')})")
        result = process_template(name, info, args.skip_existing)
        if result == "ok":
            print("OK")
            succeeded.append(name)
        elif result == "skip":
            print("already exists, skipped")
            skipped.append(name)
        else:
            print(f"FAILED")
            print(f"    {result[:300]}")
            failed.append((name, result))

    print(f"\n{'=' * 60}")
    print(f"  Done — {len(succeeded)} OK  |  {len(skipped)} skipped  |  {len(failed)} failed")
    if failed:
        print("\n  Failed templates:")
        for name, err in failed:
            first_line = err.splitlines()[0] if err else "unknown error"
            print(f"    ✗ {name}: {first_line}")
    print()


if __name__ == "__main__":
    os.chdir(ROOT)
    main()
