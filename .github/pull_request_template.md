## Summary

<!-- One sentence: what does this PR add or fix? -->

## Type of change

- [ ] New template
- [ ] Fix a broken template
- [ ] Gallery / tooling improvement
- [ ] Documentation

---

## New template checklist

<!-- Complete this section only if you are adding a template. -->

### Source

- **Original repository:** <!-- https://github.com/author/repo -->
- **License:** <!-- MIT / Apache 2.0 / LPPL / CC BY ... -->
- **Engine:** <!-- pdflatex / xelatex / lualatex -->

### Structure

- [ ] Template is under `templates/<category>/<name>/`
- [ ] `main.tex` is present, compiles cleanly, and stays a clean entry point (document class, packages, `\input{frontmatter/metadata}`, and `\input`/`\include` calls — not the whole document body inline)
- [ ] **Long/multi-section documents** (thesis, book, multi-chapter report, multi-part article, …) have their body **split into one file per section/chapter** under `sections/` (or `chapters/`), each `\input`/`\include`d from `main.tex` — see [CONTRIBUTING.md § Splitting long documents](../CONTRIBUTING.md#splitting-long-documents-into-one-file-per-section). *(Short single-purpose documents — CV, cover letter, poster, cheatsheet, invoice — may stay single-file.)*
- [ ] `frontmatter/metadata.tex` exists with standard placeholders (`FirstName LASTNAME`, `Example University`, `Master's Degree -- Computer Science`)
- [ ] `\input{frontmatter/metadata}` is present in `main.tex` (or its delegated file)
- [ ] `latexforge.toml` added with correct `engine` (only if not lualatex)
- [ ] `bibliography/references.bib` added if the template uses a bibliography
- [ ] `images/.gitkeep` added if the images/ directory is empty

### Gallery & previews

- [ ] Entry added to `gallery.json` (all fields filled: `name`, `description`, `category`, `source_url`, `install_url`, `tags`, `engine`, `preview_png`, `preview_pdf`)
- [ ] **PNG preview of the first page** generated and committed: `previews/<category>/<name>.png`
- [ ] **Sample-rendering PDF** generated and committed: `previews/<category>/<name>.pdf`
- [ ] No build artifacts committed (`.aux`, `.log`, `.pdf` inside `templates/`, etc.)

### Validation

- [ ] `python3 scripts/validate.py` passes with no errors locally
- [ ] CI is green: `validate` (structure, previews, gallery.json) and `Compile changed templates` (the template actually compiles to a PDF) both pass

---

## Notes for reviewers

<!-- Anything the reviewer should know: tricky compilation, font requirements, known warnings, etc. -->
