# Dynamics textbook: PDF to MyST conversion plan

## Source established

Use `tex/phys206_f25_textbook.pdf`, the Fall 2025 edition announced on
August 20, 2025 in the local and upstream README. It contains 305 physical
PDF pages. The 2023 and 2024 PDFs remain historical sources.

The upstream repository inspected on September 9, 2026 still advertises this
edition: <https://github.com/OSTP/Dynamics_Textbook>. A live Git ref comparison
could not be completed because shell DNS access to GitHub was unavailable.
Do not claim that upstream HEAD has been verified against this checkout.

The cover reads *Untitled Dynamics Textbook (A work in progress)*. The
introduction credits Sarah Sadavoy, with support from Cora Sleegers and Lance
Schonberg at Queen's University. Use “Second-Year Dynamics” as the site title
and preserve the original title and development status in the provenance page.
No LaTeX source or embedded source files are available in this checkout.

`source/inventory.json` records the PDF checksum, all 165 outline entries,
chapter boundaries, page labels, image placements, and detected figure and
sample-problem labels. Regenerate with `python3 scripts/inventory_source.py`.
Counts from text matching are inventory aids, not proof of extraction fidelity.

## What the neighboring projects establish

| Repository | Useful precedent | Limitation for this conversion |
| --- | --- | --- |
| `../UniversityPhysicsIClassicalMechanics` | Root MyST project, chapter files, preserved LaTeX intermediate, conversion and cross-reference scripts, verify/build workflows | Its converter starts from an already extracted LaTeX document |
| `../PrinciplesOfMechanics` | Editable MyST chapters, source-number preservation, explicit fidelity policy | Its final conversion also used EPUB XHTML and equation metadata |
| `../EnergyAndHumanAmbitions` | Reproducible PyMuPDF extraction, geometry-based math reconstruction, figure crops, teaching-box conversion, source coverage checks | Geometry and font rules are specific to a different book and must be adapted |

All three use `book-theme` and pin MyST CLI 1.10.1. Follow their project layout
and commands: `npm run start`, `npm run build`, and `npm run verify`.

## Target book structure

Include the introduction, all twelve chapters, all three appendices, eight
existing notebooks, video links, and a provenance/credits page. Replace the
printed table of contents with MyST navigation.

| Division | Title | Physical PDF pages |
| --- | --- | --- |
| Front matter | Cover, introduction, printed contents | 1–10 |
| 1 | Calculus and Vectors | 11–37 |
| 2 | Newtonian Motion | 38–60 |
| 3 | Simple Harmonic Motion | 61–79 |
| 4 | Introduction to Non-Inertial and Rotating Frames | 80–100 |
| 5 | Application of Non-Inertial and Rotating Frames | 101–121 |
| 6 | Momentum and Variable Mass | 122–146 |
| 7 | Angular Momentum and Torque | 147–172 |
| 8 | Work and Energy | 173–197 |
| 9 | Application of Energy Conservation | 198–215 |
| 10 | Central Forces and Motion in Space | 216–236 |
| 11 | Orbits and Kepler’s Laws | 237–256 |
| 12 | The Lagrange Method | 257–276 |
| A | Resources | 277–282 |
| B | Derivations and Approximations | 283–288 |
| C | Solutions to Problems | 289–305 |

Physical PDF page numbers and printed labels differ. Preserve both in source
maps rather than applying one universal offset, especially in front matter.

## Implementation sequence

1. **Pilot the extraction on representative material.** Convert Chapter 1,
   a worked example from Chapter 12, and the vector-operator tables in Appendix
   A before scaling up. Check body prose, inline fractions, vectors, unit
   vectors, time derivatives, matrices, numbered displays, embedded images,
   figure captions, and boxes spanning pages. Compare rendered MyST against
   PDF page renders. This establishes whether the geometry-based approach is
   sufficient and identifies formulas requiring explicit transcription.

2. **Build a reproducible PDF intermediate.** Extract text spans and glyph
   coordinates, font information, drawing paths, image bounds, links, and
   outline destinations with PyMuPDF. Keep physical-page and bounding-box
   provenance for each block. Remove running headers and footers by geometry;
   identify chapter and section headings using both outline and typography.
   Detect teaching-box boundaries from their drawing geometry and titles.
   Keep unresolved regions in a review manifest rather than silently emitting
   damaged mathematical text.

3. **Recover native math and artwork.** Reconstruct LaTeX from glyph positions
   and math fonts, including stacked fractions, scripts, accents, radicals,
   integrals, and matrices. Use explicit reviewed corrections for ambiguous
   cases. Extract complete figures, including vector annotations, as SVG or
   suitable raster crops; preserve captions, source numbering, credits, and
   existing textual figure descriptions. The initial text inventory finds
   130 distinct numbered figure captions; reconcile these against actual
   figures. Page screenshots may be comparison aids, but do not count as
   completed editable chapter content.

4. **Emit and review MyST.** Write `front/`, `chapters/`, `appendices/`, and
   `images/`, using native headings, math, figures, tables, and admonitions.
   Preserve learning objectives, quick questions, student commentary, worked
   examples, takeaways, important equations, real-world applications, practice
   problems, and solutions. Retain author numbering and assign stable labels
   for sections, figures, equations, examples, and problems. Link textual
   cross-references and problem/solution pairs. Preserve scientific content
   without silently correcting the source.

5. **Assemble the site and supplements.** Add `myst.yml`, `index.md`, pinned
   `package.json` and lockfile, ignore rules, build documentation, and
   provenance. Include the existing notebooks as readable supplemental pages
   and downloads without requiring execution to build. Link the original
   videos with their attribution. Match the neighboring books' navigation and
   static site conventions. Prepare CI and Pages workflows; use the actual
   publication repository when known. The current `origin` is
   `OSTP/Dynamics_Textbook`, so do not silently change the remote or claim that
   a Quadrivium Press fork already exists.

6. **Validate the entire edition.** Check complete page/block coverage,
   chapter/appendix/section parity, figures and captions, problem and solution
   coverage, missing assets, duplicate labels, unresolved references,
   malformed math, conversion artifacts, and accidental running headers.
   Review all mathematical regions and ambiguous blocks against the PDF.
   Build HTML and inspect representative pages, narrow layouts, tables,
   equations, navigation, notebooks, and download links. Structural checks
   alone do not establish mathematical accuracy. Document any remaining
   exceptions explicitly.

## Tooling and reproducibility

The WSL environment already has Python 3, PyMuPDF 1.28.2, Poppler utilities,
Pandoc, Node.js, npm, and MyST 1.10.1. An initial OCR installation is unnecessary
because the PDF contains selectable text. Plain `pdftotext` is useful for
inventory, but visibly loses math structure and is not a final converter.

Record extraction dependencies separately from site dependencies. Keep raw
intermediates and comparison renders under an ignored build directory; commit
conversion scripts, a source manifest, reviewed correction data, final MyST,
and figure assets. Regeneration should write to a staging directory or require
an explicit overwrite option so it cannot erase editorial improvements.

## Attribution details to preserve

The source README's license name and abbreviation are inconsistent with its
linked license URL (`https://creativecommons.org/licenses/by-nc-sa/4.0/`).
Record that discrepancy and use the linked CC-BY-NC-SA-4.0 identifier for the
adaptation metadata; preserve the source notice in provenance. The repository
separately states CC0 for notebooks and CC-BY-NC-ND-4.0 for videos. Keep those
distinctions instead of assigning one license to all supplementary material.

## Completion criteria

The finished deliverable is an editable, locally buildable MyST edition with
all chapters and appendices, faithful prose and mathematics, complete figures
and instructional material, functioning references and supplements, recorded
source provenance, repeatable conversion tooling, and passing verification
and HTML builds. A raw text dump, screenshot-only site, or scaffold with
unreviewed formulas is an intermediate, not a completed conversion.

## Status

All six steps above are complete. The edition builds with no MyST errors or
warnings, and `npm run verify` passes 32 structural checks.

### Mathematics

Step 3 originally left every display equation, and every inline expression
containing an accent, rule or grown delimiter, as SVG glyph outlines: 2,100
images in all. Those are now reconstructed as LaTeX from the same geometry.
The pieces that made this possible:

- **The PDF's own `/Encoding` `/Differences`.** Grown delimiters, integrals,
  sums and radicals reach text extraction as unrelated ASCII letters — a big
  `[` arrives as `h`. Only the font's encoding says which glyph was drawn.
  Adobe Symbol's private-use slots cover the pieces of an extensible fence.
- **Left-edge accent anchoring.** An accent carries no advance width, so its
  recorded origin is its only stable anchor; it is matched to the nearest
  unclaimed glyph on its own line, allowing for the lift over an ascender and
  for stacked marks such as `\dot{\vec r}`.
- **Rules as structure.** A drawn rule is a fraction or a radical vinculum,
  split recursively; a rule is set slightly wider than the terms it divides,
  so the region tolerance allows for the overhang.
- **Rows, columns and limits.** A display is cut into baselines, then into the
  columns the source sets side by side, and a big operator's limits are folded
  in from above and below before the row is read left to right.

### What keeps its artwork, and why

A reconstruction is accepted only when it accounts for every glyph the PDF
drew *and* is structurally well formed. Glyph coverage alone cannot see a
fault: a base carrying two subscripts keeps every glyph and still fails to
typeset. The automated conversion recorded 262 unresolved regions, represented
by 272 source SVG assets, under `unresolved` in `source/conversion.json`:

| Reason | Count |
| --- | --- |
| A fraction split across a line boundary, so the region holds half of it | 167 |
| A fraction rule crossing the region edge | 50 |
| A horizontal brace grouping terms, which is not modelled | 20 |
| Glyphs the reconstruction could not account for | 17 |
| A reconstruction that would not typeset | 8 |

The first two are the same underlying limitation: the prose/display
segmentation splits an inline fraction between a sentence and a display. Fixing
that means teaching `render_line` to keep a stacked structure inside one math
run; until then these regions render as faithful images rather than as guesses.

Chapters 1--12 were subsequently reviewed against the source PDF, and their 223
remaining SVG assets were manually transcribed as native LaTeX. The published
chapter Markdown therefore contains no SVG equations. The 49 source-math SVGs
that remain are referenced by the appendices. The conversion manifest retains
the automated pass's unresolved records as an extraction audit trail.

### Checking the result

Structural checks do not establish that the mathematics is right. Chapter 1's
opening derivations, the Lagrange pulley worked example (source page 262), the
spring potential integral (page 185) and the momentum sum (page 123) were
compared glyph by glyph against renders of their source pages. That comparison
is what found the mis-placed grown delimiters, the lost integral limits and the
interleaved brace labels; it is the check worth repeating on any further work.
