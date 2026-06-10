<p align="right"><b>English</b> | <a href="./README.fr.md">Français</a></p>

<p align="center">
  <img src="logo.png" alt="LaTeX Forge Gallery" width="420">
</p>

<p align="center">
  <b>80+ curated LaTeX templates, previewed, tested, and installable in one command.</b>
</p>

<p align="center">
  <a href="https://thmsgo18.github.io/latex-forge-gallery/"><img src="https://img.shields.io/badge/▶_browse_the_gallery-online-39ff14?style=for-the-badge" alt="Browse the gallery"></a>
  <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fthmsgo18%2Flatex-forge-gallery%2Fmain%2Fgallery.json&query=%24.templates.length&label=templates&color=39ff14&style=for-the-badge" alt="Number of templates">
  <a href="https://github.com/thmsgo18/latex-forge"><img src="https://img.shields.io/badge/works_with-latex--forge-blue?style=for-the-badge" alt="Works with latex-forge"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT%20%26%20others-green?style=for-the-badge" alt="License"></a>
</p>

---

<p align="center">
  <a href="https://thmsgo18.github.io/latex-forge-gallery/">
    <img src="previews/cv/awesome-cv.png" alt="awesome-cv" width="135">
    <img src="previews/thesis/clean-thesis.png" alt="clean-thesis" width="135">
    <img src="previews/presentation/beamer-metropolis.png" alt="beamer-metropolis" width="135">
    <img src="previews/article/arxiv-template.png" alt="arxiv-template" width="135">
    <img src="previews/poster/tikzposter.png" alt="tikzposter" width="135">
    <img src="previews/book/elegantbook.png" alt="elegantbook" width="135">
  </a>
  <br>
  <a href="https://thmsgo18.github.io/latex-forge-gallery/"><b>→ Browse all templates with previews</b></a>
</p>

## What is this?

This is the official template registry for the [LaTeX Forge](https://github.com/thmsgo18/latex-forge) ecosystem. Every template is curated, compiles out of the box, and follows the same structure (`main.tex` at the root), so any of them turns into a ready-to-write project in seconds.

| | |
|---|---|
| 🌐 [**Gallery website**](https://thmsgo18.github.io/latex-forge-gallery/) | Browse, filter, and preview every template |
| ⌨️ [**latex-forge CLI**](https://github.com/thmsgo18/latex-forge) | Install templates and create projects from the terminal |
| 🧩 [**VS Code extension**](https://github.com/thmsgo18/latex-forge-vscode) | Browse this gallery and install templates **without any terminal** |

## How to use a template

**From the terminal**: install once, then create as many projects as you want:

<p align="center">
  <img src="docs/assets/demo-install.gif" alt="Installing a gallery template" width="900">
</p>

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/cv/awesome-cv
latex-forge create --name my-cv --template awesome-cv
```

**Without a terminal**: install the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=thmsgo18.latex-forge-vscode), open **LaTeX Forge: Browse Template Gallery**, and click **Install & Create** on any card.

Keep templates up to date with `latex-forge template update`.

## Templates

### CV / Resume

| Name | Description | Engine |
|------|-------------|--------|
| `awesome-cv` | Elegant CV with colored sections and FontAwesome icons | XeLaTeX |
| `deedy-resume` | Two-column resume with a clean, professional layout | XeLaTeX |
| `altacv` | CV with TikZ skill bars and timeline | LuaLaTeX |
| `moderncv` | Highly customizable CV with multiple styles | pdfLaTeX |
| `hipster-cv` | Colorful sidebar CV design | XeLaTeX |
| `twenty-seconds-cv` | Sidebar CV designed to be skimmed in 20 seconds | pdfLaTeX |
| `developer-cv` | Academic CV with automatic BibTeX publication list | pdfLaTeX |
| `sidebar-cv` | Modern CV with styled sidebar | pdfLaTeX |
| `friggeri-cv` | Stylish A4 CV with colored section bars and BibTeX publications | XeLaTeX |
| `resume-openfont` | Minimalist single-page resume using open-source fonts | pdfLaTeX |
| `billryan-resume` | Elegant bilingual (English/Chinese) resume with FontAwesome | XeLaTeX |
| `mcdowell-cv` | McDowell-style ATS-friendly CV | pdfLaTeX |
| `rover-resume` | ATS-friendly resume with unique styling | pdfLaTeX |
| `classic-cv` | Traditional single-column CV | pdfLaTeX |
| `two-column-cv` | Two-column CV with photo and QR code | pdfLaTeX |
| `infographic-cv` | Infographic-style CV with visual skill bars | XeLaTeX |
| `minimalist-cv` | Ultra-minimalist single-page CV | pdfLaTeX |
| `modern-cv` | Modern CV with colored sidebar and skill bars | XeLaTeX |
| `rows-cv` | Row-based CV layout with clean horizontal sections | XeLaTeX |
| `sidebarleft-cv` | CV with left-aligned sidebar and icon-based contact info | XeLaTeX |
| `infographics2-cv` | Second infographic-style CV with visual skill bars and timeline | XeLaTeX |
| `cv-en` | Modern English CV by thmsgo18 with FontAwesome icons, covering education, experience, projects and skills | LuaLaTeX |
| `cv-fr` | Modern French CV by thmsgo18 with FontAwesome icons | LuaLaTeX |

### Thesis / Dissertation

| Name | Description | Engine |
|------|-------------|--------|
| `clean-thesis` | Clean, simple, and elegant thesis style | pdfLaTeX |
| `cambridge-thesis` | PhD thesis template for Cambridge University | pdfLaTeX |
| `memoir-thesis` | Professional dissertation with polished typography | pdfLaTeX |
| `dissertate` | Pre-formatted templates for Harvard, Princeton, and NYU | XeLaTeX |
| `tufte-thesis` | Elegant book-style thesis inspired by Edward Tufte | pdfLaTeX |
| `mimosis-thesis` | Beautiful minimalist thesis with elegant typography | pdfLaTeX |
| `oxford-thesis` | PhD thesis template for the University of Oxford | pdfLaTeX |
| `tuda-thesis` | Official TU Darmstadt thesis following university corporate design | pdfLaTeX |

### Academic Article / Paper

| Name | Description | Engine |
|------|-------------|--------|
| `neurips-paper` | Scientific paper template for modern academic conferences | pdfLaTeX |
| `ieee-article` | IEEE-style article using IEEEtran class | pdfLaTeX |
| `acm-article` | LNCS/Springer-style article for CS conferences | pdfLaTeX |
| `cvpr-paper` | CVPR/ICCV paper template, up-to-date for 2026 | pdfLaTeX |
| `arxiv-template` | Clean arXiv-style preprint template | pdfLaTeX |
| `elsarticle` | Elsevier CAS journal article template | pdfLaTeX |
| `springer-lncs` | Enhanced Springer LNCS article template for CS conferences | pdfLaTeX |
| `elegantpaper` | Elegant working paper and preprint template | pdfLaTeX |
| `research` | Two-column academic research article by thmsgo18, with related work, methodology and experiments | LuaLaTeX |

### Report

| Name | Description | Engine |
|------|-------------|--------|
| `elegant-report` | Clean and elegant report with bibliography support | pdfLaTeX |
| `technical-report` | Professional technical/term paper template | pdfLaTeX |
| `internship-report` | UTBM-style internship report with professional formatting | pdfLaTeX |
| `project-report` | Academic project report with certificate pages | pdfLaTeX |
| `math-notes` | Minimalist math notes with theorem environments | pdfLaTeX |
| `elegant-notes` | Beautiful note-taking template with theorem environments | pdfLaTeX |
| `homework-template` | Clean university homework template with problem/solution environments | pdfLaTeX |
| `lab-report` | Laboratory report template in article style | pdfLaTeX |
| `essay-collection` | Multi-essay collection report with individual abstracts and bibliography | pdfLaTeX |
| `project-report-en` | University project report by thmsgo18, with requirements, architecture, testing and bibliography (ISO/IEEE style) | LuaLaTeX |
| `project-report-fr` | University project report in French by thmsgo18, with specs, architecture and tests (AFNOR/ISO style) | LuaLaTeX |

### Beamer Presentation

| Name | Description | Engine |
|------|-------------|--------|
| `beamer-metropolis` | Modern, minimal Beamer theme | XeLaTeX |
| `beamer-focus` | Minimalist Beamer theme with dark color scheme | pdfLaTeX |
| `beamer-elegant` | Elegant Beamer slides with figure support | pdfLaTeX |
| `beamer-corporate` | Professional Beamer slides with configurable colors | pdfLaTeX |
| `beamer-simple` | Simple Beamer template focused on content | pdfLaTeX |
| `beamer-auriga` | Dark-themed Beamer presentation with a modern, polished look | pdfLaTeX |

### Letter

| Name | Description | Engine |
|------|-------------|--------|
| `cover-letter-modern` | Modern cover letter with clean typography | XeLaTeX |
| `formal-letter` | Journal-style cover letter with professional formatting | pdfLaTeX |
| `motivation-letter` | Motivation letter for academic and job applications | pdfLaTeX |
| `moderncv-letter` | Cover letter using the moderncv class | pdfLaTeX |

### Academic Poster

| Name | Description | Engine |
|------|-------------|--------|
| `beamerposter-landscape` | Landscape academic poster built with Beamer | pdfLaTeX |
| `tikzposter` | Academic poster using TikZposter | pdfLaTeX |
| `academic-poster` | Gemini-themed academic conference poster | pdfLaTeX |
| `gemini-poster` | Gemini beamerposter template with clean, modern design | pdfLaTeX |

### Book

| Name | Description | Engine |
|------|-------------|--------|
| `elegantbook` | Elegant book template with beautiful chapter styling | XeLaTeX |
| `legrand-orange-book` | Structured book template with color-coded chapters | XeLaTeX |

### Cheatsheet

| Name | Description | Engine |
|------|-------------|--------|
| `cheatsheet` | Compact multi-column cheatsheet template for quick reference cards | pdfLaTeX |

### Miscellaneous

| Name | Description | Engine |
|------|-------------|--------|
| `invoice-simple` | Clean single-page invoice template using the scrlttr2 class | pdfLaTeX |
| `invoice-multipage` | Multi-page invoice template with itemized table and totals | pdfLaTeX |
| `timesheet` | Monthly timesheet template with daily hours tracking table | pdfLaTeX |
| `poem` | Elegant poem typesetting template with verse environments | pdfLaTeX |

### Projet Informatique L3 (Université Paris Cité)

8 templates for the standard documents of the L3 Computer Science Project at Université Paris Cité. UPC visual identity, fully in French, compiled with pdfLaTeX.

| Name | Description |
|------|-------------|
| `upc-cahier-des-charges` | Requirements specification |
| `upc-rapport-final` | Final report |
| `upc-conception-detaillee` | Detailed design |
| `upc-manuel-installation` | Installation manual |
| `upc-manuel-utilisation` | User manual |
| `upc-rapport-tests` | Test report |
| `upc-documentation-technique` | Technical documentation |
| `upc-cahier-recette` | Acceptance test plan |

## Compatibility

Every template contains a `main.tex` at the root of its directory, a `frontmatter/metadata.tex` with standard placeholders (auto-filled by your [latex-forge profile](https://github.com/thmsgo18/latex-forge#your-profile)), and declares its engine in `latexforge.toml`, making it fully compatible with `latex-forge create`.

## Contributing a template

Want to add a template? Read [CONTRIBUTING.md](CONTRIBUTING.md): it covers the required structure, standard placeholders, engine declaration, `gallery.json` format, and preview generation. Run `python3 scripts/validate.py` before opening a PR.

The demo GIF is regenerated with [vhs](https://github.com/charmbracelet/vhs): `./docs/demo/record.sh`.

## Sources & licenses

All templates come from publicly available repositories with permissive licenses; full credit goes to their original authors, listed in [SOURCES.md](SOURCES.md). The gallery structure, scripts, and tooling are [MIT](LICENSE); each template retains its original license (MIT, Apache 2.0, LPPL, CC BY/BY-SA/BY-NC-SA).

## Related projects

- [**latex-forge**](https://github.com/thmsgo18/latex-forge): the CLI that turns these templates into ready-to-write projects
- [**latex-forge-vscode**](https://github.com/thmsgo18/latex-forge-vscode): the VS Code extension with a built-in gallery browser

## Author

Made by [thmsgo18](https://github.com/thmsgo18)
