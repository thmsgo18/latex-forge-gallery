#!/usr/bin/env python3
"""
Validate the latex-forge-gallery structure.

Checks every template for:
  - Required files (main.tex, frontmatter/metadata.tex)
  - \\input{frontmatter/metadata} wired in main.tex or its delegated file
  - Engine consistency between gallery.json and latexforge.toml
  - No committed LaTeX build artifacts
  - Preview files (PNG + PDF) present in previews/
  - gallery.json completeness and URL consistency

Run from the repo root:
    python3 scripts/validate.py

Exit code 0 = all checks passed.
Exit code 1 = one or more issues found.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = ROOT / "templates"
PREVIEWS_DIR = ROOT / "previews"
GALLERY_JSON = ROOT / "gallery.json"

PREVIEW_BASE = "https://raw.githubusercontent.com/thmsgo18/latex-forge-gallery/main/previews/"

ARTIFACT_SUFFIXES = {
    ".aux", ".log", ".toc", ".bbl", ".blg", ".lof", ".lot",
    ".fls", ".fdb_latexmk", ".snm", ".nav", ".vrb", ".idx", ".ind",
    ".ilg", ".bcf", ".run.xml", ".synctex.gz", ".xdv",
}

VALID_ENGINES = {"pdflatex", "xelatex", "lualatex"}

VALID_CATEGORIES = {
    "article", "book", "cheatsheet", "cv", "letter", "misc",
    "poster", "presentation", "project-upc", "report", "thesis",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def error(msg: str) -> None:
    print(f"  ✗  {msg}", flush=True)

def warn(msg: str) -> None:
    print(f"  ⚠  {msg}", flush=True)

def ok(msg: str) -> None:
    print(f"  ✓  {msg}", flush=True)


def contains_metadata_input(path: Path) -> bool:
    """Return True if *path* contains \\input{frontmatter/metadata}."""
    try:
        text = path.read_text(errors="replace")
        return "frontmatter/metadata" in text
    except OSError:
        return False


def find_delegated_file(main: Path) -> Path | None:
    """
    Some templates have main.tex as a one-liner `\\input{other}`.
    Return the delegated file if so, otherwise None.
    """
    try:
        lines = [l.strip() for l in main.read_text(errors="replace").splitlines()
                 if l.strip() and not l.strip().startswith("%")]
    except OSError:
        return None

    # Single non-comment line that is an \input{...}
    if len(lines) <= 3:
        for line in lines:
            m = re.match(r'\\input\{([^}]+)\}', line)
            if m:
                target = main.parent / (m.group(1) + ".tex")
                if target.exists():
                    return target
    return None


def read_toml_engine(toml_path: Path) -> str:
    """Parse engine from latexforge.toml. Returns 'lualatex' if file absent."""
    if not toml_path.exists():
        return "lualatex"
    m = re.search(r'engine\s*=\s*"([^"]+)"', toml_path.read_text())
    return m.group(1) if m else "lualatex"

# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_template(name: str, cat: str, gallery_engine: str) -> list[str]:
    """Return list of error strings for this template (empty = OK)."""
    issues: list[str] = []
    tmpl = TEMPLATES_DIR / cat / name

    if not tmpl.is_dir():
        return [f"{cat}/{name}: directory not found"]

    # 1. main.tex exists
    main = tmpl / "main.tex"
    if not main.exists():
        issues.append(f"{cat}/{name}: missing main.tex")
        return issues  # can't continue without it

    # 2. frontmatter/metadata.tex exists
    meta = tmpl / "frontmatter" / "metadata.tex"
    if not meta.exists():
        issues.append(f"{cat}/{name}: missing frontmatter/metadata.tex")

    # 3. \input{frontmatter/metadata} is wired somewhere
    wired = contains_metadata_input(main)
    if not wired:
        delegated = find_delegated_file(main)
        if delegated:
            wired = contains_metadata_input(delegated)
    if not wired:
        issues.append(f"{cat}/{name}: \\input{{frontmatter/metadata}} not found in main.tex")

    # 4. Engine consistency: gallery.json vs latexforge.toml
    toml_engine = read_toml_engine(tmpl / "latexforge.toml")
    if gallery_engine != toml_engine:
        issues.append(
            f"{cat}/{name}: engine mismatch — gallery.json={gallery_engine}, "
            f"latexforge.toml={toml_engine}"
        )

    # 5. latexforge.toml required for non-lualatex engines
    if gallery_engine != "lualatex" and not (tmpl / "latexforge.toml").exists():
        issues.append(f"{cat}/{name}: engine={gallery_engine} but latexforge.toml is missing")

    # 6. No committed build artifacts
    artifacts = [
        p.name for p in tmpl.rglob("*")
        if p.suffix in ARTIFACT_SUFFIXES and p.is_file()
    ]
    if artifacts:
        issues.append(f"{cat}/{name}: committed build artifacts: {', '.join(artifacts[:5])}")

    return issues


def check_previews(templates: list[dict]) -> list[str]:
    issues: list[str] = []
    for t in templates:
        name, cat = t["name"], t["category"]
        for ext in ("png", "pdf"):
            path = PREVIEWS_DIR / cat / f"{name}.{ext}"
            if not path.exists():
                issues.append(f"previews/{cat}/{name}.{ext}: file missing")
    return issues


def check_gallery_json(data: dict) -> list[str]:
    issues: list[str] = []
    templates = data.get("templates", [])

    required_fields = {"name", "description", "category", "source_url", "install_url",
                       "tags", "engine", "preview_png", "preview_pdf"}

    names_seen: set[str] = set()

    for t in templates:
        name = t.get("name", "<unnamed>")
        cat = t.get("category", "")

        # Duplicate names
        if name in names_seen:
            issues.append(f"gallery.json: duplicate name '{name}'")
        names_seen.add(name)

        # Missing fields
        missing = required_fields - set(t.keys())
        if missing:
            issues.append(f"gallery.json/{name}: missing fields: {', '.join(sorted(missing))}")

        # Valid category
        if cat and cat not in VALID_CATEGORIES:
            issues.append(f"gallery.json/{name}: unknown category '{cat}'")

        # Valid engine
        engine = t.get("engine", "")
        if engine not in VALID_ENGINES:
            issues.append(f"gallery.json/{name}: invalid engine '{engine}'")

        # Preview URL format
        expected_png = PREVIEW_BASE + cat + "/" + name + ".png"
        expected_pdf = PREVIEW_BASE + cat + "/" + name + ".pdf"
        if t.get("preview_png") != expected_png:
            issues.append(f"gallery.json/{name}: wrong preview_png URL")
        if t.get("preview_pdf") != expected_pdf:
            issues.append(f"gallery.json/{name}: wrong preview_pdf URL")

        # Non-empty description
        if not t.get("description", "").strip():
            issues.append(f"gallery.json/{name}: empty description")

        # Tags should be a list
        if not isinstance(t.get("tags"), list):
            issues.append(f"gallery.json/{name}: 'tags' must be a list")

    return issues


def check_disk_vs_gallery(data: dict) -> list[str]:
    """Find templates on disk not in gallery.json, and vice versa."""
    issues: list[str] = []
    gallery_names = {t["name"] for t in data["templates"]}

    disk_names: set[str] = set()
    for cat_dir in TEMPLATES_DIR.iterdir():
        if not cat_dir.is_dir():
            continue
        for tmpl_dir in cat_dir.iterdir():
            if tmpl_dir.is_dir() and (tmpl_dir / "main.tex").exists():
                disk_names.add(tmpl_dir.name)

    for name in sorted(disk_names - gallery_names):
        issues.append(f"disk: template '{name}' exists on disk but not in gallery.json")
    for name in sorted(gallery_names - disk_names):
        issues.append(f"gallery.json: template '{name}' listed but not found on disk")

    return issues

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    os.chdir(ROOT)

    print("Loading gallery.json …")
    with open(GALLERY_JSON) as f:
        data = json.load(f)
    templates = data["templates"]

    all_issues: list[str] = []
    sections: dict[str, list[str]] = {}

    # --- gallery.json integrity ---
    print("\n[1/4] Checking gallery.json …")
    issues = check_gallery_json(data)
    issues += check_disk_vs_gallery(data)
    sections["gallery.json"] = issues
    all_issues += issues

    # --- per-template checks ---
    print(f"\n[2/4] Checking {len(templates)} templates …")
    tmpl_issues: list[str] = []
    for t in templates:
        issues = check_template(t["name"], t["category"], t.get("engine", "lualatex"))
        tmpl_issues += issues
    sections["templates"] = tmpl_issues
    all_issues += tmpl_issues

    # --- previews ---
    print(f"\n[3/4] Checking preview files …")
    issues = check_previews(templates)
    sections["previews"] = issues
    all_issues += issues

    # --- root artifacts ---
    print(f"\n[4/4] Checking for stray artifacts at repo root …")
    root_artifacts = [
        p.name for p in ROOT.iterdir()
        if p.suffix in ARTIFACT_SUFFIXES and p.is_file()
    ]
    issues = [f"root: committed artifact '{a}'" for a in root_artifacts]
    sections["root artifacts"] = issues
    all_issues += issues

    # --- Report ---
    print("\n" + "=" * 60)
    if not all_issues:
        print("  All checks passed ✓")
        print("=" * 60)
        return 0

    total = len(all_issues)
    print(f"  {total} issue{'s' if total > 1 else ''} found:\n")
    for section, issues in sections.items():
        if issues:
            print(f"  [{section}]")
            for issue in issues:
                print(f"    ✗  {issue}")
            print()
    print("=" * 60)
    return 1


if __name__ == "__main__":
    sys.exit(main())
