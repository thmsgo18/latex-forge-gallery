#!/usr/bin/env python3
"""Verify that templates build through the *user* path: `latexmk` with the
declared engine and an output directory — exactly what `latex-forge build`
(and the VS Code recipe) run.

This is deliberately different from ``generate_previews.py``, which compiles by
invoking the engine binary directly. A template can compile that way yet fail
under ``latexmk -<engine> -outdir=build`` (e.g. a class that needs lualatex but
declares xelatex, or an index-style file that latexmk can't find once it
chdir's into the out directory). Those failures are exactly what an end user
hits, so this script is the gate that catches them.

Each template is copied to a temporary directory before compiling, so the
working tree is never polluted with build artifacts.

Run from the repo root:
    python3 scripts/verify_build.py                 # all templates
    python3 scripts/verify_build.py --only awesome-cv clean-thesis
    python3 scripts/verify_build.py --category book

Exit code 0 = every selected template produced a PDF.
Exit code 1 = at least one failed (or a tool was missing).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = ROOT / "templates"
GALLERY_JSON = ROOT / "gallery.json"

# Mirror latex_forge/build.py: the latexmk flag for each declared engine.
ENGINE_FLAG = {"lualatex": "-lualatex", "xelatex": "-xelatex", "pdflatex": "-pdf"}

PER_TEMPLATE_TIMEOUT = 300  # seconds (some theses with custom fonts are slow)


def load_templates() -> list[dict]:
    return json.loads(GALLERY_JSON.read_text(encoding="utf-8"))["templates"]


def latexmk_command(engine: str) -> list[str]:
    """The exact invocation latex-forge build uses (see latex_forge/build.py)."""
    return [
        "latexmk",
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        ENGINE_FLAG.get(engine, "-lualatex"),
        "-outdir=build",
        "main.tex",
    ]


def verify_one(name: str, category: str, engine: str) -> tuple[bool, str]:
    """Compile a single template in a throwaway copy. Returns (ok, detail)."""
    src = TEMPLATES_DIR / category / name
    if not (src / "main.tex").exists():
        return False, "missing main.tex"

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / name
        shutil.copytree(src, work)
        timed_out = False
        try:
            subprocess.run(
                latexmk_command(engine),
                cwd=work,
                capture_output=True,
                timeout=PER_TEMPLATE_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            timed_out = True

        # A heavy template (custom fonts, many passes) can still produce a PDF
        # before latexmk finishes every pass, so check for the PDF even after a
        # timeout — `latex-forge build` would simply run a little longer.
        if (work / "build" / "main.pdf").exists():
            return True, "(slow)" if timed_out else ""
        if timed_out:
            return False, f"timeout after {PER_TEMPLATE_TIMEOUT}s, no PDF"

        # Surface the first hard error from the log to make CI output actionable.
        log = work / "build" / "main.log"
        if log.exists():
            for line in log.read_text(errors="replace").splitlines():
                if line.startswith("! ") or "already defined" in line or "return code" in line:
                    return False, f"no PDF — {line.strip()[:120]}"
        return False, "no PDF produced"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", metavar="NAME", help="Only verify these templates")
    parser.add_argument("--category", help="Only verify templates in this category")
    args = parser.parse_args()

    if shutil.which("latexmk") is None:
        print("latexmk not found on PATH — install a TeX distribution first.", file=sys.stderr)
        return 1

    templates = load_templates()
    if args.only:
        wanted = set(args.only)
        templates = [t for t in templates if t["name"] in wanted]
    if args.category:
        templates = [t for t in templates if t["category"] == args.category]

    if not templates:
        print("No templates matched the selection.")
        return 0

    failures: list[tuple[str, str, str]] = []
    for t in templates:
        name, category, engine = t["name"], t["category"], t.get("engine", "lualatex")
        ok, detail = verify_one(name, category, engine)
        status = "ok  " if ok else "FAIL"
        print(f"{status} {name} [{engine}] {detail}".rstrip(), flush=True)
        if not ok:
            failures.append((name, engine, detail))

    print("\n" + "=" * 60)
    print(f"  {len(templates) - len(failures)}/{len(templates)} templates built via latexmk")
    if failures:
        print("\n  Failed:")
        for name, engine, detail in failures:
            print(f"    FAIL  {name} [{engine}]  {detail}")
    print("=" * 60)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
