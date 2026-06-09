# LaTeX Forge Gallery

<p align="center">
  <img src="logo.png" alt="LaTeX Forge Gallery" width="480">
</p>

<p align="center">
  Parcourez et installez des templates LaTeX soigneusement sélectionnés en une seule commande.
</p>

<p align="center">
  <a href="https://thmsgo18.github.io/latex-forge-gallery/"><img src="https://img.shields.io/badge/galerie-en%20ligne-39ff14?style=for-the-badge" alt="Galerie en ligne"></a>
  <a href="https://github.com/thmsgo18/latex-forge"><img src="https://img.shields.io/badge/nécessite-latex--forge-blue?style=for-the-badge" alt="Nécessite latex-forge"></a>
  <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fthmsgo18%2Flatex-forge-gallery%2Fmain%2Fgallery.json&query=%24.templates.length&label=templates&color=39ff14&style=for-the-badge" alt="Nombre de templates">
  <a href="LICENSE"><img src="https://img.shields.io/badge/licence-MIT%20%26%20autres-green?style=for-the-badge" alt="Licence"></a>
</p>

<p align="center">
  <a href="./README.md">Read in English</a>
</p>

---

LaTeX Forge Gallery est le registre officiel de templates pour [latex-forge](https://github.com/thmsgo18/latex-forge). Chaque template est sélectionné, testé et structuré avec un fichier `main.tex` à sa racine — prêt à installer et compiler immédiatement.

Parcourez la galerie complète sur **[thmsgo18.github.io/latex-forge-gallery](https://thmsgo18.github.io/latex-forge-gallery/)**.

## Installation

Installez n'importe quel template en une seule commande :

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/<categorie>/<nom-du-template>
```

**Exemple :**

```bash
latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/cv/awesome-cv
```

## Templates

### CV / Curriculum Vitae

| Nom | Description | Moteur |
|-----|-------------|--------|
| `awesome-cv` | CV élégant avec sections colorées et icônes FontAwesome | XeLaTeX |
| `deedy-resume` | CV deux colonnes avec une mise en page claire et professionnelle | XeLaTeX |
| `altacv` | CV avec barres de compétences TikZ et frise chronologique | LuaLaTeX |
| `moderncv` | CV hautement personnalisable avec plusieurs styles | pdfLaTeX |
| `hipster-cv` | CV avec barre latérale colorée | XeLaTeX |
| `twenty-seconds-cv` | CV barre latérale conçu pour être parcouru en 20 secondes | pdfLaTeX |
| `developer-cv` | CV académique avec liste de publications BibTeX automatique | pdfLaTeX |
| `sidebar-cv` | CV moderne avec barre latérale stylisée | pdfLaTeX |
| `friggeri-cv` | CV A4 élégant avec barres de section colorées et publications | XeLaTeX |
| `resume-openfont` | CV minimaliste une page avec polices open source | pdfLaTeX |
| `billryan-resume` | CV bilingue anglais/chinois avec FontAwesome | XeLaTeX |
| `mcdowell-cv` | CV compatible ATS, style McDowell | pdfLaTeX |
| `rover-resume` | CV compatible ATS avec style unique | pdfLaTeX |
| `classic-cv` | CV classique une colonne | pdfLaTeX |
| `two-column-cv` | CV deux colonnes avec photo et QR code | pdfLaTeX |
| `infographic-cv` | CV infographique avec barres de compétences visuelles | XeLaTeX |
| `minimalist-cv` | CV ultra-minimaliste une page | pdfLaTeX |
| `modern-cv` | CV moderne avec barre latérale colorée et barres de compétences | XeLaTeX |
| `rows-cv` | CV en lignes horizontales avec sections épurées | XeLaTeX |
| `sidebarleft-cv` | CV avec barre latérale gauche et contacts iconographiques | XeLaTeX |
| `infographics2-cv` | Deuxième variante de CV infographique avec frise chronologique | XeLaTeX |
| `cv-en` | CV moderne en anglais par thmsgo18 avec icônes FontAwesome, sections formation, expérience, projets et compétences | LuaLaTeX |
| `cv-fr` | CV moderne en français par thmsgo18 avec icônes FontAwesome | LuaLaTeX |

### Thèse / Mémoire

| Nom | Description | Moteur |
|-----|-------------|--------|
| `clean-thesis` | Style de thèse propre, simple et élégant | pdfLaTeX |
| `cambridge-thesis` | Template de thèse de doctorat pour l'Université de Cambridge | pdfLaTeX |
| `memoir-thesis` | Mémoire professionnel avec une typographie soignée | pdfLaTeX |
| `dissertate` | Templates pré-formatés pour Harvard, Princeton et NYU | XeLaTeX |
| `tufte-thesis` | Thèse style livre inspirée d'Edward Tufte | pdfLaTeX |
| `mimosis-thesis` | Thèse minimaliste avec une typographie élégante | pdfLaTeX |
| `oxford-thesis` | Template de thèse pour l'Université d'Oxford | pdfLaTeX |
| `tuda-thesis` | Thèse officielle TU Darmstadt | pdfLaTeX |

### Article / Communication scientifique

| Nom | Description | Moteur |
|-----|-------------|--------|
| `neurips-paper` | Template pour les grandes conférences académiques | pdfLaTeX |
| `ieee-article` | Article au format IEEE avec la classe IEEEtran | pdfLaTeX |
| `acm-article` | Article LNCS/Springer pour les conférences en informatique | pdfLaTeX |
| `cvpr-paper` | Template CVPR/ICCV, à jour pour 2026 | pdfLaTeX |
| `arxiv-template` | Template de preprint style arXiv | pdfLaTeX |
| `elsarticle` | Template d'article pour les journaux Elsevier CAS | pdfLaTeX |
| `springer-lncs` | Template Springer LNCS amélioré pour les conférences CS | pdfLaTeX |
| `elegantpaper` | Template élégant pour working papers et prépublications | pdfLaTeX |
| `research` | Article de recherche académique en deux colonnes par thmsgo18, avec related work, méthodologie et expériences | LuaLaTeX |

### Rapport

| Nom | Description | Moteur |
|-----|-------------|--------|
| `elegant-report` | Rapport propre et élégant avec support bibliographique | pdfLaTeX |
| `technical-report` | Rapport technique / papier de cours professionnel | pdfLaTeX |
| `internship-report` | Rapport de stage au format UTBM | pdfLaTeX |
| `project-report` | Rapport de projet académique avec pages de certification | pdfLaTeX |
| `math-notes` | Notes de cours minimalistes avec environnements de théorèmes | pdfLaTeX |
| `elegant-notes` | Template de prise de notes avec environnements de théorèmes | pdfLaTeX |
| `homework-template` | Template de devoirs universitaires avec environnements problème/solution | pdfLaTeX |
| `lab-report` | Template de compte rendu de TP en style article | pdfLaTeX |
| `essay-collection` | Recueil d'essais avec résumés individuels et bibliographie | pdfLaTeX |
| `project-report-en` | Rapport de projet universitaire en anglais par thmsgo18, avec requirements, architecture, tests et bibliographie (style ISO/IEEE) | LuaLaTeX |
| `project-report-fr` | Rapport de projet universitaire en français par thmsgo18, avec cahier des charges, architecture, tests et bibliographie (style AFNOR/ISO) | LuaLaTeX |

### Présentation Beamer

| Nom | Description | Moteur |
|-----|-------------|--------|
| `beamer-metropolis` | Thème Beamer moderne et minimaliste | XeLaTeX |
| `beamer-focus` | Thème Beamer minimaliste avec palette de couleurs sombres | pdfLaTeX |
| `beamer-elegant` | Slides Beamer élégantes avec support des figures | pdfLaTeX |
| `beamer-corporate` | Slides Beamer professionnelles avec couleurs configurables | pdfLaTeX |
| `beamer-simple` | Template Beamer simple centré sur le contenu | pdfLaTeX |
| `beamer-auriga` | Présentation Beamer au style moderne et soigné | pdfLaTeX |

### Lettre

| Nom | Description | Moteur |
|-----|-------------|--------|
| `cover-letter-modern` | Lettre de motivation moderne avec une typographie claire | XeLaTeX |
| `formal-letter` | Lettre de motivation au format journal, présentation professionnelle | pdfLaTeX |
| `motivation-letter` | Lettre de motivation pour candidatures académiques et emploi | pdfLaTeX |
| `moderncv-letter` | Lettre de motivation utilisant la classe moderncv | pdfLaTeX |

### Poster académique

| Nom | Description | Moteur |
|-----|-------------|--------|
| `beamerposter-landscape` | Poster académique en format paysage avec Beamer | pdfLaTeX |
| `tikzposter` | Poster académique avec TikZposter | pdfLaTeX |
| `academic-poster` | Poster de conférence académique au thème Gemini | pdfLaTeX |
| `gemini-poster` | Template beamerposter Gemini, design épuré et moderne | pdfLaTeX |

### Livre

| Nom | Description | Moteur |
|-----|-------------|--------|
| `elegantbook` | Template de livre élégant avec un style de chapitres soigné | XeLaTeX |
| `legrand-orange-book` | Template de livre structuré avec chapitres codés par couleur | XeLaTeX |

### Cheatsheet

| Nom | Description | Moteur |
|-----|-------------|--------|
| `cheatsheet` | Template de cheatsheet multi-colonnes compact pour fiches de référence | pdfLaTeX |

### Divers

| Nom | Description | Moteur |
|-----|-------------|--------|
| `invoice-simple` | Facture simple une page avec la classe scrlttr2 | pdfLaTeX |
| `invoice-multipage` | Facture multi-pages avec tableau détaillé et totaux | pdfLaTeX |
| `timesheet` | Feuille de temps mensuelle avec suivi des heures journalières | pdfLaTeX |
| `poem` | Template élégant de composition poétique avec environnements de vers | pdfLaTeX |

### Projet Informatique L3 — Université Paris Cité

Suite de 8 templates pour les documents standard du Projet Informatique L3 à l'Université Paris Cité. Charte graphique UPC, entièrement en français, compilables avec pdfLaTeX.

| Nom | Description |
|-----|-------------|
| `upc-cahier-des-charges` | Cahier des charges |
| `upc-rapport-final` | Rapport final |
| `upc-conception-detaillee` | Conception détaillée |
| `upc-manuel-installation` | Manuel d'installation |
| `upc-manuel-utilisation` | Manuel d'utilisation |
| `upc-rapport-tests` | Rapport de tests |
| `upc-documentation-technique` | Documentation technique interne |
| `upc-cahier-recette` | Cahier de recette |

> **Personnalisation rapide :** modifier les commandes `\renewcommand` en haut de chaque `main.tex` (groupe, encadrant, auteurs, version, résumé).

## Compatibilité

Chaque template contient un fichier `main.tex` à la racine de son répertoire, ce qui le rend entièrement compatible avec [latex-forge](https://github.com/thmsgo18/latex-forge).

## Contribuer

Vous souhaitez ajouter un template ? Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour le guide complet — structure de répertoire requise, placeholders standards, déclaration du moteur, format `gallery.json` et génération des previews.

En résumé : votre template doit avoir un `main.tex`, un `frontmatter/metadata.tex` avec des placeholders standards, et un `latexforge.toml` s'il n'utilise pas LuaLaTeX.

## Sources

Tous les templates sont issus de dépôts GitHub publics avec des licences permissives. Tout le crédit revient à leurs auteurs originaux. Voir [SOURCES.md](SOURCES.md) pour la liste complète.

## Licence

La structure de la galerie, les scripts et les outils sont sous [licence MIT](LICENSE).  
Chaque template conserve sa licence d'origine (MIT, Apache 2.0, LPPL, CC BY/BY-SA/BY-NC-SA).

---

Réalisé par [thmsgo18](https://github.com/thmsgo18)
