# Contributing to LaTeX Forge Gallery

Thank you for your interest in contributing! This guide explains how to add a new template to the gallery so it works seamlessly with the [latex-forge](https://github.com/thmsgo18/latex-forge) CLI.

---

## Table of Contents

- [Requirements](#requirements)
- [Template structure](#template-structure)
- [frontmatter/metadata.tex — standard placeholders](#frontmattermetadatatex--standard-placeholders)
- [latexforge.toml — engine declaration](#latexforgetoml--engine-declaration)
- [gallery.json — registry entry](#galleryjson--registry-entry)
- [Generating a preview](#generating-a-preview)
- [Submitting a pull request](#submitting-a-pull-request)

---

## Requirements

Before submitting, make sure your template:

- Compiles cleanly with a standard TeX Live installation (no proprietary fonts, no commercial packages)
- Is licensed under a **permissive license**: MIT, Apache 2.0, LPPL, CC BY, CC BY-SA, or CC BY-NC-SA
- Is sourced from a publicly available GitHub repository — credit to the original author is mandatory
- Works with latex-forge's install mechanism (one `main.tex` at the root)

---

## Template structure

Every template must follow this directory layout:

```
templates/<category>/<template-name>/
├── main.tex                        # Entry point — must compile standalone
├── latexforge.toml                 # Engine declaration (omit if lualatex)
├── frontmatter/
│   ├── metadata.tex                # Standard placeholders (see below)
│   └── ...                        # Other preamble files if needed
├── sections/                       # Body content (.tex files)
├── backmatter/                     # Appendices, bibliography calls, etc.
├── bibliography/
│   └── references.bib             # BibTeX file (if the template uses one)
└── images/
    └── .gitkeep                   # Empty placeholder (or real images)
```

### Rules

| File | Requirement |
|------|-------------|
| `main.tex` | Must contain `\input{frontmatter/metadata}` |
| `frontmatter/metadata.tex` | Must use standard placeholders (see below) |
| `latexforge.toml` | Required if the engine is **not** lualatex |
| `bibliography/references.bib` | Required if the template uses `\bibliography` or `\addbibresource` |
| `images/.gitkeep` | Required if the images/ directory would otherwise be empty |

### Splitting long documents into one file per section

`main.tex` must stay a clean **entry point** — document class, packages, the
`\input{frontmatter/metadata}` call, and (for long-form documents) a short
list of `\input`/`\include` calls. It must **not** be a multi-hundred-line
monolithic file containing the entire body of the document.

**When to split:**

- Long-form documents — theses, books, multi-chapter reports, papers with
  several major parts — must have their body content broken up into one file
  per chapter/section under `sections/` (or `chapters/` for books), each
  `\input`/`\include`d from `main.tex`:

  ```latex
  % main.tex
  \documentclass{report}
  % ... packages ...
  \input{frontmatter/metadata}

  \begin{document}
  \input{sections/01-introduction}
  \input{sections/02-related-work}
  \input{sections/03-methodology}
  \input{sections/04-results}
  \input{sections/05-conclusion}
  \end{document}
  ```

  Name section files so their order is obvious at a glance (`01-...`,
  `02-...`), and give each one a short header comment describing its content.

- **Short, single-purpose documents** — CVs, cover letters, posters,
  cheatsheets, single-page invoices, timesheets — are fine as a single
  `main.tex`; splitting a one-page document into files would only add
  friction. Use your judgement: if `main.tex` is pushing past ~150 lines of
  body content and covers more than one logical section, split it.

This keeps templates easy to navigate, easy to diff, and easy to reuse
section-by-section — which is the whole point of curating them here rather
than just linking to the original repository.

### Categories

Choose the most appropriate category for your template:

| Category | Description |
|----------|-------------|
| `article` | Academic articles, conference papers, preprints |
| `book` | Books, textbooks, long-form documents |
| `cheatsheet` | Compact multi-column reference cards |
| `cv` | CVs, resumes |
| `letter` | Cover letters, formal letters, motivation letters |
| `misc` | Anything that doesn't fit another category |
| `poster` | Academic and conference posters |
| `presentation` | Beamer slides and presentations |
| `project-upc` | UPC L3 project documents (specific to Université Paris Cité) |
| `report` | Technical reports, internship reports, lab reports, notes |
| `thesis` | Theses and dissertations |

---

## frontmatter/metadata.tex — standard placeholders

The `metadata.tex` file is the single place a user edits to personalise the template. It must use **standard placeholder strings** so that latex-forge can auto-fill them on install.

### English templates

Use these exact strings as default values:

| Field | Placeholder |
|-------|-------------|
| Author / Name | `FirstName LASTNAME` |
| Institution | `Example University` |
| Degree / Programme | `Master's Degree -- Computer Science` |
| Email | `firstname.lastname@example.edu` |
| Address | `123 Main Street, F-75001 Paris, France` |
| Phone | `+33 6 00 00 00 00` |

**Example — article template:**

```latex
% =====================================================================
%  My Template — Metadata
%  Edit this file to personalise your document.
% =====================================================================

\title{Paper Title}
\author{FirstName LASTNAME}
\affiliation{Example University}
\date{\today}
```

**Example — CV template:**

```latex
% =====================================================================
%  My CV — Personal Information
%  Edit this file to personalise your CV.
% =====================================================================

\newcommand{\cvname}{FirstName LASTNAME}
\newcommand{\cvposition}{Master's Degree -- Computer Science}
\newcommand{\cvuniversity}{Example University}
\newcommand{\cvemail}{firstname.lastname@example.edu}
```

### French templates

For French-language templates, use the French equivalents:

| Field | Placeholder |
|-------|-------------|
| Author / Name | `NOM Prenom` |
| Institution | `Universite Paris Cite` |
| Degree / Programme | `Master Informatique` |

**Example — French report:**

```latex
\renewcommand{\docAuthor}{NOM Prenom}
\renewcommand{\docUniversity}{Universite Paris Cite}
\renewcommand{\docDegree}{Master Informatique}
```

### Wiring metadata into main.tex

Add `\input{frontmatter/metadata}` in the **preamble** (before `\begin{document}`), unless the template requires it inside the document body:

```latex
\documentclass{article}

% ... packages ...

\input{frontmatter/metadata}   % <— here

\begin{document}
...
\end{document}
```

---

## latexforge.toml — engine declaration

Create this file at the template root if the template requires **pdflatex** or **xelatex**. If the template works with lualatex (the default), **do not create this file**.

```toml
# latexforge.toml
engine = "pdflatex"   # or "xelatex"
```

| Engine | When to use |
|--------|-------------|
| `lualatex` | Default — do not create `latexforge.toml` |
| `pdflatex` | Template uses pdflatex-only packages or doesn't use `fontspec` |
| `xelatex` | Template uses `fontspec` or OpenType fonts but doesn't need luatex |

---

## gallery.json — registry entry

Add an entry to `gallery.json` under the `"templates"` array:

```json
{
  "name": "my-template",
  "description": "One-line description of what the template is for.",
  "category": "report",
  "source_url": "https://github.com/original-author/original-repo",
  "install_url": "https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/report/my-template",
  "tags": ["report", "academic", "english"],
  "engine": "pdflatex",
  "preview_png": "https://raw.githubusercontent.com/thmsgo18/latex-forge-gallery/main/previews/report/my-template.png",
  "preview_pdf": "https://raw.githubusercontent.com/thmsgo18/latex-forge-gallery/main/previews/report/my-template.pdf"
}
```

| Field | Description |
|-------|-------------|
| `name` | Lowercase, hyphenated. Must match the directory name under `templates/<category>/`. |
| `description` | One sentence, English, no trailing period. |
| `category` | One of the categories listed above. |
| `source_url` | GitHub URL of the **original** template repository. |
| `install_url` | Full GitHub tree URL pointing to your template directory. |
| `tags` | Array of lowercase strings (document type, language, style keywords). |
| `engine` | `"pdflatex"`, `"xelatex"`, or `"lualatex"`. Must match `latexforge.toml`. |
| `preview_png` | Raw GitHub URL — `previews/<category>/<name>.png` |
| `preview_pdf` | Raw GitHub URL — `previews/<category>/<name>.pdf` |

---

## Generating a preview

**A PNG of the first page and the compiled sample PDF are mandatory for every
template.** This isn't just a recommendation: `scripts/validate.py` (run
automatically in CI on every push/PR — see `.github/workflows/validate.yml`)
hard-fails if `previews/<category>/<name>.png` or `previews/<category>/<name>.pdf`
is missing for any template listed in `gallery.json`. A PR that doesn't include
both files for a new template cannot pass validation.

Previews are a single PNG (first page) and the compiled PDF, stored in `previews/<category>/`.

Use the provided script:

```bash
python3 scripts/generate_previews.py --only <template-name>
```

The script reads the engine from `gallery.json` and compiles the template automatically. The output files are placed in `previews/<category>/`.

**Requirements:**
- TeX Live (pdflatex, xelatex, lualatex, biber all in PATH)
- `pdftoppm` (from poppler-utils) for PNG generation
- Python 3.8+

If the script times out (complex templates can exceed 90 s), compile manually:

```bash
# Example for pdflatex + biber
cd templates/<category>/<template-name>
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# Copy to previews/
cp main.pdf ../../../previews/<category>/<name>.pdf
pdftoppm -r 150 -png -singlefile ../../../previews/<category>/<name>.pdf ../../../previews/<category>/<name>
```

Clean up compilation artifacts before committing:

```bash
cd templates/<category>/<template-name>
rm -f *.aux *.log *.bbl *.bcf *.blg *.fls *.fdb_latexmk *.out *.run.xml \
      *.synctex.gz *.toc *.xdv *.nav *.snm *.vrb *.pdf
```

---

## Submitting a pull request

1. **Fork** this repository and create a branch: `add/<template-name>`
2. Add your template under `templates/<category>/<template-name>/`, following
   the [structure rules above](#template-structure) — including splitting
   long documents into one file per section/chapter under `sections/`
3. Add the entry to `gallery.json`
4. Generate the preview files in `previews/<category>/` (PNG of the first
   page **and** the compiled PDF — both are required, see
   [Generating a preview](#generating-a-preview))
5. Run `python3 scripts/validate.py` locally and make sure it passes
6. Open a pull request with:
   - A brief description of the template
   - A link to the original source repository
   - Confirmation that it compiles cleanly

Please do **not** include compilation artifacts (`.aux`, `.log`, `.pdf` inside `templates/`, etc.) in your PR.

### What CI checks automatically

Every PR that touches `templates/**` or `gallery.json` is checked by two
GitHub Actions workflows — you don't need to trigger them yourself:

| Workflow | What it does | Result if it fails |
|----------|--------------|--------------------|
| `validate.yml` | Runs `scripts/validate.py`: required files, `\input{frontmatter/metadata}` wiring, engine consistency, no committed build artifacts, **PNG + PDF previews present**, `gallery.json` completeness | PR cannot be merged |
| `compile-pr.yml` | Compiles every template you added or modified with the declared engine and verifies it actually produces a PDF | PR cannot be merged |

The "one file per section" convention itself is enforced through review
(it's a structural/style convention, not something a script can fully judge —
some templates are legitimately single-file). But in practice a badly-split
document usually fails to compile too, which `compile-pr.yml` will catch.

---

For questions, open an issue or start a discussion on GitHub.
