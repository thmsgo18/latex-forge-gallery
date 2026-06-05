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
- [ ] `main.tex` is present and compiles cleanly
- [ ] `frontmatter/metadata.tex` exists with standard placeholders (`FirstName LASTNAME`, `Example University`, `Master's Degree -- Computer Science`)
- [ ] `\input{frontmatter/metadata}` is present in `main.tex` (or its delegated file)
- [ ] `latexforge.toml` added with correct `engine` (only if not lualatex)
- [ ] `bibliography/references.bib` added if the template uses a bibliography
- [ ] `images/.gitkeep` added if the images/ directory is empty

### Gallery

- [ ] Entry added to `gallery.json` (all fields filled: `name`, `description`, `category`, `source_url`, `install_url`, `tags`, `engine`, `preview_png`, `preview_pdf`)
- [ ] Preview files generated: `previews/<category>/<name>.png` and `.pdf`
- [ ] No build artifacts committed (`.aux`, `.log`, `.pdf` inside `templates/`, etc.)

### Validation

- [ ] `python3 scripts/validate.py` passes with no errors

---

## Notes for reviewers

<!-- Anything the reviewer should know: tricky compilation, font requirements, known warnings, etc. -->
