# About this edition and credits

## Original textbook

Sarah Sadavoy, with support from Cora Sleegers and Lance Schonberg.
*Untitled Dynamics Textbook (A work in progress)*. Queen’s University,
Fall 2025. Developed for PHYS 206 and flipped-classroom instruction.

The source repository is [OSTP/Dynamics_Textbook](https://github.com/OSTP/Dynamics_Textbook).
Its August 20, 2025 update identifies the PDF used here. The original file is
preserved as {download}`phys206_f25_textbook.pdf <tex/phys206_f25_textbook.pdf>`.
The older 2023 and 2024 editions remain in the repository.

## Conversion conventions

This edition converts the introduction, twelve chapters, and three appendices
into editable MyST Markdown. The web navigation replaces the printed contents.
Author numbering and the original scientific content are retained. Source
typos and statements have not been systematically corrected or modernized.

Prose, headings, teaching boxes, figure captions, and the constants table are
editable text.

Mathematics is rebuilt as LaTeX from the glyph geometry the PDF records:
baseline and size give scripts, the drawn rules give fractions and radicals,
the marks drawn over a letter give vectors, hats and dots, and the font’s own
encoding identifies grown delimiters, integrals and sums together with their
limits. **4,453 of the book’s 4,725 expressions — 94% — are native LaTeX**,
including every numbered equation that could be read whole. They are
selectable, searchable, and available to screen readers.

A reconstruction is only used when it can be checked. Each one must account for
every glyph the PDF drew and must be structurally well formed; the 272 regions
that fail either test keep the source’s original glyph outlines as SVG instead,
so that no expression is silently mistranscribed. Most are fractions the page
layout splits across a line boundary, so that one region holds only half the
structure. Twenty are expressions grouped by a horizontal brace, which this
conversion does not model. Every such region is listed under `unresolved` in
`source/conversion.json`, with its physical page, the reason, and the glyphs
that did not reconcile, so it can be checked or transcribed by hand.

Equation numbers set in the right margin become cross-reference labels rather
than part of the expression, so `(1.1)` in the source is linkable as `eq-1-1`.

The figure artwork is extracted from the PDF. The original textual figure
descriptions are used where available. Some descriptions sit on the next
printed page; any fallback descriptions are identified in the manifest.

The conversion tooling and source maps are in `scripts/` and `source/` in the
repository. This edition follows the MyST project conventions used by
Quadrivium Press’s *University Physics I: Classical Mechanics*, *Principles of
Mechanics*, and *Energy and Human Ambitions on a Finite Planet*. The text/math
rendering helper was adapted from the latter project’s extraction script.

## License notices

The original README calls the license “Creative Commons Attribution 4.0
International License” and abbreviates it “CC-BY-SA-NC,” while linking to
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
This edition uses **CC-BY-NC-SA-4.0**, the identifier corresponding to that link,
and preserves the original wording in the extracted introduction.

The source README separately states **CC0** for the Jupyter notebooks. They are
included as authored, with one exception: two Markdown cells in *Ch9 Energy
Conservation Exercises* used LaTeX’s `eqnarray*`, which the web renderer does
not support. They are set as `aligned` instead; the mathematics is unchanged.
The videos are credited to **Lance Schonberg and Sarah Sadavoy** and carry
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
They are linked in their original form.
