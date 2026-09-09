#!/usr/bin/env python3
"""Extract the Fall 2025 Dynamics PDF into a staged MyST book.

Uses PDF glyphs, outlines, image placements and teaching-box geometry. Complex
mathematics is preserved as original SVG glyph outlines, not guessed LaTeX.
Run with --output build/converted (default); use --publish to copy a reviewed
staging edition into the repository. Publication refuses to overwrite files
unless --overwrite is also supplied. No network calls or notebook execution.
"""
from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import json
import math
import re
import shutil
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

import pymupdf
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path

import mathtext

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "tex/phys206_f25_textbook.pdf"
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
ACCENTS = set("⃗ˆ˙¨¯ˇ˘˜̸")
UNSAFE = ACCENTS | set("∫∑∏√∮")


@dataclass
class Char:
    c: str
    x: float
    y: float
    size: float
    font: str
    color: int = 0
    w: float = 0
    bbox: tuple = ()
    block: int = -1
    glyph: str = ""


def font_encodings(doc):
    """Map ``family -> {code: glyph name}`` from every font's /Differences.

    The extension font's big delimiters, integrals and radicals reach text
    extraction as unrelated ASCII letters, so the PDF's own encoding is the
    only reliable way to learn which glyph was actually drawn.
    """
    maps = collections.defaultdict(dict)
    seen = set()
    for number in range(doc.page_count):
        for xref, _name, _type, basefont, *_ in doc[number].get_fonts(full=True):
            if xref in seen:
                continue
            seen.add(xref)
            reference = re.search(r"/Encoding\s+(\d+) 0 R", doc.xref_object(xref))
            if not reference:
                continue
            body = re.search(r"/Differences\s*\[(.*?)\]",
                             doc.xref_object(int(reference[1])), re.S)
            if not body:
                continue
            family = re.sub(r"^[A-Z]{6}\+", "", basefont)
            code = 0
            for token in re.findall(r"\d+|/[A-Za-z0-9._]+", body[1]):
                if token.startswith("/"):
                    maps[family][code] = token[1:]
                    code += 1
                else:
                    code = int(token)
    return dict(maps)


#: Adobe Symbol's private-use slots for the pieces of a grown delimiter, which
#: text extraction reports in place of any name the font itself supplies
SYMBOL_PUA = {
    0xF8E5: "radicalex", 0xF8EB: "parenlefttp", 0xF8EC: "parenleftex",
    0xF8ED: "parenleftbt", 0xF8EE: "bracketlefttp", 0xF8EF: "bracketleftex",
    0xF8F0: "bracketleftbt", 0xF8F1: "bracelefttp", 0xF8F2: "braceleftmid",
    0xF8F3: "braceleftbt", 0xF8F4: "braceex", 0xF8F6: "parenrighttp",
    0xF8F7: "parenrightex", 0xF8F8: "parenrightbt", 0xF8F9: "bracketrighttp",
    0xF8FA: "bracketrightex", 0xF8FB: "bracketrightbt", 0xF8FC: "bracerighttp",
    0xF8FD: "bracerightmid", 0xF8FE: "bracerightbt",
}


def glyph_name(encodings, font, char):
    """The PostScript glyph name behind one extracted character, if known."""
    code = ord(char) if len(char) == 1 else -1
    if code in SYMBOL_PUA:
        return SYMBOL_PUA[code]
    if not 0 <= code <= 255:
        return ""
    for family, table in encodings.items():
        # PyMuPDF truncates long font names, so match on the recorded prefix
        if family.startswith(font):
            name = table.get(code)
            if name:
                return name
    return ""


def rect(chars):
    boxes = [c.bbox for c in chars if c.bbox and c.c.strip()]
    return pymupdf.Rect(min(b[0] for b in boxes), min(b[1] for b in boxes),
                        max(b[2] for b in boxes), max(b[3] for b in boxes))


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def plain(chars):
    return "".join(c.c for c in chars)


EQUATION_NUMBER = re.compile(r"^\((\d+\.\d+)\)$")


def split_equation_number(chars):
    """Separate a right-margin equation number from the equation itself.

    The author's number is set flush right on one line of the display, well
    clear of the mathematics, and becomes the cross-reference label rather
    than part of the transcribed expression.
    """
    body = [c for c in chars if c.c.strip()]
    if len(body) < 6:
        return list(chars), ""
    anchor = max(body, key=lambda c: c.x)
    line = sorted((c for c in body if abs(c.y - anchor.y) <= 1.0),
                  key=lambda c: c.x)
    for width in range(5, 9):
        if len(line) <= width:
            break
        tail = line[-width:]
        match = EQUATION_NUMBER.match(plain(tail))
        if not match:
            continue
        previous = line[-width - 1]
        if tail[0].x - (previous.x + (previous.w or 0.0)) < 12:
            continue                        # part of the expression, not a label
        marked = {id(c) for c in tail}
        return [c for c in chars if id(c) not in marked], match[1]
    return list(chars), ""


def join_lines(lines):
    result = ""
    for line in lines:
        if result.endswith("-") and re.match(r"[a-z]", line):
            result = result[:-1] + line
        else:
            result += (" " if result else "") + line
    return result


class Page:
    def __init__(self, page, output, encodings=None):
        self.encodings = encodings if encodings is not None else font_encodings(page.parent)
        self.page = page
        self.number = page.number + 1
        self.output = output
        self.left = 75.6 if self.number % 2 else 72.0
        self.chars = []
        self.descriptions = []
        self.captions = []
        self.blocks = []
        self.assets = []
        self.records = []
        self.unresolved = []
        self.math_count = 0
        self.native_math_count = 0
        self.boxes = []
        self.bars = []
        self.svg_tree = None
        for drawing in page.get_drawings():
            box = drawing["rect"]
            if drawing["type"] == "fs" and box.width > 200 and box.height > 20:
                self.boxes.append({"bbox": list(box), "color": drawing["color"]})
            if drawing["type"] == "s" and box.height < 0.6 and 1 < box.width < 300 and box.y0 > 60:
                self.bars.append((box.x0, box.y0, box.x1, drawing["width"]))
        raw = page.get_text("rawdict")
        for bi, b in enumerate(raw["blocks"]):
            if b["type"] != 0:
                continue
            block_chars = []
            skip_title = any(s["size"] > 40 for l in b["lines"] for s in l["spans"])
            for line in b["lines"]:
                for span in line["spans"]:
                    cc = [Char(c["c"], *c["origin"], span["size"], span["font"],
                               span["color"], c["bbox"][2] - c["bbox"][0],
                               c["bbox"], bi) for c in span["chars"]]
                    # Some extensible delimiters map to whitespace/control
                    # characters despite drawing visible parentheses or bars.
                    for c, original in zip(cc, span["chars"]):
                        if "Extension" in c.font or ord(c.c[0]) in SYMBOL_PUA:
                            c.glyph = glyph_name(self.encodings, c.font, c.c)
                        if "Extension" in c.font and not c.c.strip() and not original.get("synthetic"):
                            c.c = "�"
                    if span["size"] < 3:
                        self.descriptions.extend(cc)
                    elif not skip_title and not ("LMSans17" in span["font"] and span["size"] > 18):
                        block_chars.extend(c for c in cc if 60 < c.y < 735)
            if block_chars:
                self.chars.extend(block_chars)
                self.blocks.append(block_chars)
                text = plain(block_chars)
                if re.match(r"Figure\s+\d+\.\d+:", text):
                    self.captions.append({"chars": block_chars, "bbox": rect(block_chars),
                                          "number": re.match(r"Figure\s+(\d+\.\d+):", text)[1]})
        # Use the PDF drawing positions for accents. The text extractor may
        # attach combining marks to an unrelated preceding character.
        self.load_svg()
        self.chars = [c for c in self.chars if c.c not in ACCENTS]
        for cc in self.blocks:
            cc[:] = [c for c in cc if c.c not in ACCENTS]
        for x, y, element, fill in self.accents:
            if not 60 < y < 735:
                continue
            possible = [c for c in self.chars if c.c.strip() and abs(c.x - x) < 16 and abs(c.y - y) < 16]
            if not possible:
                continue
            base = min(possible, key=lambda c: abs(c.x - x) + abs(c.y - y) * 0.4
                       + (0 if c.font.startswith("LMMath") else 4))
            bounds = self.glyph_rect(element)
            if not bounds:
                continue
            char = Char(element.get("data-text"), x, y, base.size, "LMMathItalic12-Regular",
                        0, 0, tuple(bounds), base.block)
            self.chars.append(char)
            for cc in self.blocks:
                if cc and cc[0].block == base.block:
                    cc.append(char)
                    break

    def record(self, kind, chars, **extra):
        item = {"kind": kind, "pdf_page": self.number,
                "bbox": [round(v, 3) for v in rect(chars)],
                "source_text": plain(chars), **extra}
        self.records.append(item)
        return item

    def load_svg(self):
        if self.svg_tree is not None:
            return
        source_svg = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: "�" if int(m[1], 16) < 32
                            else m[0], self.page.get_svg_image())
        self.svg_tree = ET.fromstring(source_svg)
        self.defs = {e.get("id"): e for d in self.svg_tree if d.tag == f"{{{SVG}}}defs" for e in d}
        self.glyph_bounds = {}
        self.glyphs = collections.defaultdict(list)
        self.accents = []
        # Latin Modern text is drawn in page coordinates, including in colored
        # teaching boxes. Capture inherited fill along with each glyph outline.
        def visit(e, fill="black"):
            fill = e.get("fill", fill)
            if e.tag == f"{{{SVG}}}use" and e.get("data-text") is not None:
                values = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", e.get("transform", ""))
                if len(values) == 6:
                    x, y = map(float, values[-2:])
                    self.glyphs[(round(x, 1), round(y, 1))].append((e, fill))
                    if e.get("data-text") in ACCENTS:
                        self.accents.append((x, y, e, fill))
            for child in e:
                if child.tag != f"{{{SVG}}}defs":
                    visit(child, fill)
        visit(self.svg_tree)

    def glyph_rect(self, element):
        key = element.get(f"{{{XLINK}}}href", "")[1:]
        if key not in self.glyph_bounds:
            pen = BoundsPen(None)
            parse_path(self.defs[key].get("d", ""), pen)
            self.glyph_bounds[key] = pen.bounds
        bounds = self.glyph_bounds[key]
        if not bounds:
            return None
        transform = [float(v) for v in re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", element.get("transform", ""))]
        return pymupdf.Rect(bounds) * pymupdf.Matrix(*transform)

    def math_svg(self, chars, inline=False):
        self.load_svg()
        chars = [c for c in chars if c.bbox and c.c.strip()]
        box = rect(chars)
        selected = []
        seen = set()
        missing = []
        for char in chars:
            candidates = []
            for dx in (-0.1, 0, 0.1):
                for dy in (-0.1, 0, 0.1):
                    candidates.extend(self.glyphs.get((round(char.x + dx, 1), round(char.y + dy, 1)), []))
            positional = candidates
            candidates = [(e, fill) for e, fill in candidates
                          if "Extension" in char.font or e.get("data-text") in (char.c, "�")]
            if not candidates and char.c not in ACCENTS:
                candidates = positional  # PDF ligature expansion can rename a glyph.
            if not candidates and char.c in ACCENTS:
                near = [(math.hypot(x - char.x, y - char.y), e, fill) for x, y, e, fill in self.accents
                        if abs(x - char.x) < 10 and abs(y - char.y) < 6 and e.get("data-text") == char.c]
                candidates = [(e, fill) for _, e, fill in sorted(near, key=lambda x: x[0])[:1]]
            if not candidates and char.c not in ACCENTS:
                missing.append(char.c)
            for e, fill in candidates:
                if id(e) not in seen:
                    seen.add(id(e))
                    clone = copy.deepcopy(e)
                    clone.set("fill", "black")
                    selected.append(clone)
        # PDF text extraction can suppress an accent that overlaps its base.
        # Recover such glyphs directly from the original SVG drawing stream.
        for x, y, e, fill in self.accents:
            if box.x0 - 2 <= x <= box.x1 + 2 and box.y0 <= y <= box.y1 and id(e) not in seen:
                seen.add(id(e))
                clone = copy.deepcopy(e)
                clone.set("fill", "black")
                selected.append(clone)
        if missing:
            raise ValueError(f"Page {self.number}: SVG glyphs missing for {missing!r}")
        bars = [b for b in self.bars if box.x0 - 1 <= b[0] and b[2] <= box.x1 + 1
                and box.y0 - 1 <= b[1] <= box.y1 + 1]
        for x0, y, x1, width in bars:
            selected.append(ET.Element(f"{{{SVG}}}path", {
                "d": f"M{x0} {y}H{x1}", "stroke": "black", "stroke-width": str(width), "fill": "none"}))
        for element in selected:
            if element.tag.endswith("use"):
                actual = self.glyph_rect(element)
                if actual:
                    box |= actual
        box += (-1.2, -1.2, 1.2, 1.2)
        root = ET.Element(f"{{{SVG}}}svg", {
            "version": "1.1", "width": f"{box.width * 1.4:.2f}",
            "height": f"{box.height * 1.4:.2f}",
            "viewBox": " ".join(f"{x:.3f}" for x in (box.x0, box.y0, box.width, box.height)),
            "role": "img", "aria-label": f"Mathematical expression from source PDF page {self.number}"})
        defs = ET.SubElement(root, f"{{{SVG}}}defs")
        used = {e.get(f"{{{XLINK}}}href", "")[1:] for e in selected if e.tag.endswith("use")}
        for key in sorted(used):
            defs.append(copy.deepcopy(self.defs[key]))
        root.extend(selected)
        data = ET.tostring(root, encoding="unicode")
        digest = hashlib.sha256(data.encode()).hexdigest()[:12]
        name = f"images/math/p{self.number:03d}-{digest}.svg"
        path = self.output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data + "\n")
        self.math_count += 1
        self.assets.append(name)
        self.record("inline-math-svg" if inline else "display-math-svg", chars,
                    asset=name, glyph_count=len(chars), matched_glyphs=len(seen))
        if inline:
            return f"![Formula, source page {self.number}](../{name})"
        labels = re.findall(r"\((\d+\.\d+)\)", plain(sorted(chars, key=lambda c: (round(c.y), c.x))))
        label = f"(eq-{labels[-1].replace('.', '-')})=\n" if labels else ""
        return (label + f":::{'{image}'} ../{name}\n:alt: Mathematical expression from source PDF page {self.number}\n"
                ":class: source-equation\n:align: center\n:::")

    # a fraction rule is set a little wider than the terms it divides
    RULE_OVERHANG = 2.5

    def region_bars(self, box):
        """The drawn rules lying inside a region, labelled by what they are."""
        found = [b for b in self.bars
                 if box.x0 - self.RULE_OVERHANG <= b[0]
                 and b[2] <= box.x1 + self.RULE_OVERHANG
                 and box.y0 - 1 <= b[1] <= box.y1 + 1]
        return mathtext.classify_bars(self.chars, found)

    def rule_owner(self, char, anchors):
        """The prose line carrying the fraction rule this glyph is stacked on."""
        middle = char.x + (char.w or 0.0) / 2.0
        for x0, y, x1, _width in self.bars:
            if not x0 - 1 <= middle <= x1 + 1 or not 0 < abs(char.y - y) <= 8:
                continue
            near = [a for a in anchors if abs(y - a["baseline"]) < 12
                    and a["x0"] - 8 <= x0 and x1 <= a["x1"] + 10]
            if near:
                return min(near, key=lambda a: abs(y - a["baseline"]))
        return None

    def straddling_rule(self, box):
        """Whether a rule crosses this region's edge instead of lying inside it.

        Such a rule means the region holds only part of a fraction. Reading the
        stacked rows as scripts would turn a quotient into a power, so the
        region keeps its artwork instead.
        """
        for x0, y, x1, _width in self.bars:
            if not box.y0 - 1 <= y <= box.y1 + 1:
                continue
            inside = box.x0 - self.RULE_OVERHANG <= x0 and x1 <= box.x1 + self.RULE_OVERHANG
            overlaps = x0 < box.x1 and x1 > box.x0
            if overlaps and not inside:
                return True
        return False

    def reconstruct(self, chars, bars):
        """LaTeX for a region, or ``None`` when it cannot be fully accounted for.

        The reconstruction is only accepted when every glyph the PDF drew is
        represented in the result, so an expression this module cannot model
        keeps its original artwork instead of being silently mistranscribed.
        """
        # A horizontal brace labels a span of terms from below. Nothing here
        # models that grouping, and reading its label as ordinary glyphs would
        # interleave it with the expression, so the artwork is kept instead.
        if any(c.glyph.startswith("braceh") for c in chars):
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(chars)[:120],
                "reason": "underbrace grouping not modelled"})
            return None
        try:
            latex = mathtext.render_display(chars, bars)
        except Exception:
            return None
        # a multi-line display is newline-separated; any other control
        # character means a glyph reached the output unmapped
        if not latex or any(ord(c) < 32 and c != "\n" for c in latex):
            return None
        # An empty group means a fraction or radical was drawn partly outside
        # this region, so the region does not hold the whole structure.
        if "{}" in latex.replace(" ", ""):
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(chars)[:120],
                "reason": "structure split across regions", "latex": latex[:160]})
            return None
        if not mathtext.latex_is_well_formed(latex):
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(chars)[:120],
                "reason": "malformed structure", "latex": latex[:160]})
            return None
        missing, added = mathtext.coverage_gap(chars, latex)
        if missing or added:
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(chars)[:120],
                "missing": dict(missing), "added": dict(added)})
            return None
        return latex

    def inline_math(self, chars):
        visible = [c for c in chars if c.c.strip() and c.bbox]
        if not visible:
            return ""
        box = rect(visible)
        self.load_svg()
        unsafe = any(c.c in UNSAFE or ord(c.c[0]) < 32 or "Extension" in c.font for c in visible)
        unsafe |= any(box.x0 - 2 <= x <= box.x1 + 2 and box.y0 <= y <= box.y1 for x, y, _, _ in self.accents)
        unsafe |= any(box.x0 - self.RULE_OVERHANG <= b[0]
                      and b[2] <= box.x1 + self.RULE_OVERHANG
                      and box.y0 <= b[1] <= box.y1 for b in self.bars)
        if self.straddling_rule(box):
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(visible)[:120],
                "reason": "fraction rule crosses the region edge"})
            return self.math_svg(visible, inline=True)
        # Accents, fraction rules and extensible delimiters are rebuilt from
        # the drawing geometry; only what that cannot explain keeps its SVG.
        if unsafe:
            latex = self.reconstruct(visible, self.region_bars(box))
            if latex is None or "\\begin{aligned}" in latex:
                return self.math_svg(visible, inline=True)
            self.native_math_count += 1
            self.record("inline-math-latex", visible, latex=latex)
            return "$" + latex + "$"
        value = mathtext.render_math_only(chars)
        if any(ord(c) < 32 for c in value) or "{" not in value and "\\sqrt" in value:
            return self.math_svg(visible, inline=True)
        if not mathtext.latex_is_well_formed(value):
            self.unresolved.append({
                "pdf_page": self.number, "text": plain(visible)[:120],
                "reason": "malformed structure", "latex": value[:160]})
            return self.math_svg(visible, inline=True)
        self.native_math_count += 1
        self.record("inline-math-latex", visible, latex=value)
        return "$" + value + "$"

    def line_text(self, chars, italics=True):
        text = mathtext.render_line(sorted(chars, key=lambda c: (round(c.x, 3), round(c.y, 3))), sidenotes=False,
                                    italics=italics, math_renderer=self.inline_math).strip()
        text = re.sub(r"(?<=[A-Za-z,])!\[", " ![", text)
        for link in self.page.get_links():
            uri = link.get("uri", "")
            if not uri.startswith(("https://", "http://")):
                continue
            area = link["from"]
            linked = [c for c in chars if area.contains(pymupdf.Point(c.x + c.w / 2, c.y - 2))]
            label = plain(sorted(linked, key=lambda c: (round(c.x, 3), round(c.y, 3)))).strip()
            if len(label) >= 2 and label in text and not any(c in label for c in "$[]"):
                text = text.replace(label, f"[{label}]({uri})", 1)
        return text

    def figures(self):
        images = self.page.get_image_info()
        groups = collections.defaultdict(list)
        for ii, image in enumerate(images):
            box = pymupdf.Rect(image["bbox"])
            if box.width < 5 or box.height < 5:
                continue
            def score(cap):
                cb = cap["bbox"]
                horizontal = max(0, cb.x0 - box.x1, box.x0 - cb.x1)
                vertical = max(0, cb.y0 - box.y1, box.y0 - cb.y1)
                return vertical * 2 + horizontal * 0.15
            nearest = min(self.captions, key=score, default=None)
            key = nearest["number"] if nearest and score(nearest) < 140 else f"p{self.number:03d}-{ii + 1}"
            groups[key].append(box)
        events = []
        excluded = set()
        for key, boxes in groups.items():
            box = pymupdf.Rect(boxes[0])
            for b in boxes[1:]:
                box |= b
            cap = next((c for c in self.captions if c["number"] == key), None)
            name = f"images/figures/figure-{key.replace('.', '-')}.png"
            path = self.output / name
            path.parent.mkdir(parents=True, exist_ok=True)
            # Original diagrams are embedded raster art; crop at 180 dpi to
            # include any overlaid labels while preserving source proportions.
            self.page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), clip=box, alpha=False).save(path)
            self.assets.append(name)
            desc = self.description_near(box)
            width = min(650, round(box.width * 1.4))
            if cap:
                excluded.update(id(c) for c in cap["chars"])
                seeds = []
                for y in sorted({round(c.y, 1) for c in cap["chars"] if c.size >= 10
                                 and c.font.startswith("LMRoman") and c.c.isalpha()}):
                    if not seeds or y - seeds[-1] > 0.7:
                        seeds.append(y)
                for c in cap["chars"]:
                    if c.size >= 10 and c.c not in ACCENTS and "Extension" not in c.font and min(abs(y - c.y) for y in seeds) > 8:
                        seeds.append(c.y)
                seeds.sort()
                baselines = collections.defaultdict(list)
                for c in cap["chars"]:
                    baselines[min(seeds, key=lambda y: abs(y - c.y))].append(c)
                caption = join_lines([self.line_text(cc, italics=False) for _, cc in sorted(baselines.items())])
                caption = re.sub(r"^Figure\s+[\d.$]+:\s*", "", caption)
                text = (f":::{'{figure}'} ../{name}\n:label: fig-{key.replace('.', '-')}\n:enumerator: {key}\n"
                        f":alt: {desc or 'Figure ' + key + ' from the source textbook'}\n:width: {width}px\n\n{caption}\n:::")
                top = min(box.y0, cap["bbox"].y0)
            else:
                text = (f":::{'{image}'} ../{name}\n:alt: {desc or 'Illustration from source PDF page ' + str(self.number)}\n"
                        f":width: {width}px\n:align: center\n:::")
                top = box.y0
            events.append({"kind": "figure", "y0": top, "y1": max(box.y1, cap["bbox"].y1 if cap else 0),
                           "text": text, "x": box.x0})
            self.records.append({"kind": "figure", "pdf_page": self.number, "bbox": list(box),
                                 "asset": name, "figure_number": key if cap else None,
                                 "caption": plain(cap["chars"]) if cap else None, "alt": desc})
        return events, excluded

    def description_near(self, box):
        # Original alternative descriptions are tiny text placed below each
        # figure, sometimes on the following page. Same-page matches only.
        groups = collections.defaultdict(list)
        for c in self.descriptions:
            groups[round(c.y, 1)].append(c)
        candidates = [(y, cc) for y, cc in groups.items() if box.y0 <= y <= box.y1 + 80]
        if not candidates:
            return ""
        _, cc = min(candidates, key=lambda entry: abs(entry[0] - box.y1))
        return re.sub(r"\s+", " ", plain(cc)).strip()

    def extract(self):
        events, excluded = self.figures()
        for override in json.loads((ROOT / "source/overrides.json").read_text()):
            if override["pdf_page"] != self.number:
                continue
            bounds = pymupdf.Rect(override["bbox"])
            cc = [c for c in self.chars if bounds.contains(pymupdf.Point(c.x + c.w / 2, c.y))]
            excluded.update(id(c) for c in cc)
            events.append({"kind": "override", "y0": bounds.y0, "y1": bounds.y1,
                           "text": override["markdown"], "x": bounds.x0})
            self.record("reviewed-override", cc, reason=override["reason"])
        chars = [c for c in self.chars if id(c) not in excluded]
        self.load_svg()
        for c in chars:
            if "Extension" in c.font and c.c.strip():
                possible = self.glyphs.get((round(c.x, 1), round(c.y, 1)), [])
                for e, _ in possible:
                    actual = self.glyph_rect(e)
                    if actual:
                        c.bbox = tuple(pymupdf.Rect(c.bbox) | actual)
        # Establish prose baselines from Roman words near the left margin.
        # Math-only baselines are deliberately left unassigned for a lossless
        # display rendering, including matrices and aligned derivations.
        groups = collections.defaultdict(list)
        for c in chars:
            if c.size >= 10 and c.c not in ACCENTS and "Extension" not in c.font:
                groups[round(c.y, 1)].append(c)
        anchors = []
        merged = {}
        previous = None
        for baseline, cc in sorted(groups.items()):
            if previous is not None and baseline - previous < 0.7:
                merged[previous].extend(cc)
            else:
                previous = baseline
                merged[baseline] = list(cc)
        for baseline, cc in merged.items():
            normal = [c for c in cc if not c.font.startswith("LMMath")]
            words = plain(sorted(normal, key=lambda c: c.x))
            first = min((c.x for c in cc if c.c.strip()), default=1000)
            is_title = any("LMSans" in c.font or c.size >= 14 for c in cc)
            prose_words = [w for w in re.findall(r"[A-Za-z]{3,}", words) if w not in mathtext.MATH_WORDS]
            prose = bool(prose_words) and first <= self.left + 65
            short = bool(re.match(r"\s*(?:Solution|Problem\s+\d+-\d+|[A-Z][a-z]+\s*:)", words))
            if is_title or prose or short:
                anchors.append({"baseline": baseline, "chars": [], "seed": cc,
                                "x0": first, "x1": max(c.x + c.w for c in cc)})
        remaining = []
        for c in chars:
            effective_y = c.bbox[3] - 3 if "Extension" in c.font else c.y
            matches = [a for a in anchors if abs(effective_y - a["baseline"]) < (9 if c.size < 10 else 5.5)
                       and a["x0"] - 8 <= c.x <= a["x1"] + 10]
            if matches:
                match = min(matches, key=lambda a: abs(effective_y - a["baseline"]))
                match["chars"].append(c)
            else:
                remaining.append(c)
        # A fraction set inside a sentence stacks its rows above and below the
        # baseline, close enough to be claimed by the neighbouring line. Such a
        # glyph belongs to whichever line carries its own rule; leaving it where
        # it landed drops a digit into the middle of a word.
        for anchor in anchors:
            for c in list(anchor["chars"]):
                owner = self.rule_owner(c, anchors)
                if owner is not None and owner is not anchor:
                    anchor["chars"].remove(c)
                    owner["chars"].append(c)
        for a in anchors:
            cc = a["chars"]
            if not any(c.c.strip() for c in cc):
                continue
            box = rect(cc)
            text = self.line_text(cc)
            raw = plain(sorted(cc, key=lambda c: c.x)).strip()
            sizes = max(c.size for c in cc)
            title = any("LMSans" in c.font for c in cc)
            if sizes >= 14:
                kind = "heading"
                section = re.match(r"^([\dA-C]+(?:\.\d+)+)\s*(.*)", raw)
                if section:
                    num = section[1]
                    level = num.count(".") + 1
                    text = f"(sec-{num.replace('.', '-')})=\n" + "#" * level + f" {num} {section[2]}"
                else:
                    text = "**" + text.strip("*") + "**"
            elif title:
                kind = "box-title"
                text = raw
            else:
                kind = "line"
                text = re.sub(r"^•\s*", "- ", text)
                # Preserve parenthesized/roman enumerators as authored; normal
                # numeric lists receive Markdown's required punctuation.
            events.append({"kind": kind, "y0": box.y0, "y1": box.y1,
                           "baseline": a["baseline"], "text": text, "x": box.x0})
            self.record(kind, cc)
        # All unassigned glyphs are retained. Adjacent vertically overlapping
        # fragments make a display, even if PDF block order is disjoint.
        pending = sorted([c for c in remaining if c.c.strip()], key=lambda c: c.bbox[1])
        clusters = []
        for c in pending:
            if clusters and c.bbox[1] <= clusters[-1]["bottom"] + 2:
                clusters[-1]["chars"].append(c)
                clusters[-1]["bottom"] = max(clusters[-1]["bottom"], c.bbox[3])
            else:
                clusters.append({"chars": [c], "bottom": c.bbox[3]})
        for cluster in clusters:
            cc = cluster["chars"]
            box = rect(cc)
            body, number = split_equation_number(cc)
            latex = self.reconstruct(body, self.region_bars(box))
            if latex is None:
                text = self.math_svg(cc)
            else:
                self.native_math_count += 1
                self.record("display-math-latex", body, latex=latex, number=number)
                label = f" (eq-{number.replace('.', '-')})" if number else ""
                text = f"$$\n{latex}\n$${label}"
            events.append({"kind": "display", "y0": box.y0, "y1": box.y1,
                           "text": text, "x": box.x0})
        events.sort(key=lambda e: (e["y0"], e["x"]))
        return self.emit(events)

    def emit(self, events):
        parts = []
        paragraph = []
        last = None
        current_box = None

        def flush():
            if paragraph:
                parts.append(join_lines(paragraph))
                paragraph.clear()

        for event in events:
            center = (event["y0"] + event["y1"]) / 2
            box = next((i for i, b in enumerate(self.boxes)
                        if b["bbox"][1] - 15 <= center <= b["bbox"][3] + 1), None)
            if current_box != box:
                flush()
                if current_box is not None:
                    parts.append("::::")
                current_box = box
                if box is not None:
                    title_event = next((e for e in events if e["kind"] == "box-title"
                                        and self.boxes[box]["bbox"][1] - 18 <= e["y0"] <= self.boxes[box]["bbox"][1] + 10), None)
                    title = title_event["text"] if title_event else "Continued"
                    style = "tip" if "Question" in title else "admonition"
                    parts.append(f"::::{'{' + style + '}'} {title}")
            if event["kind"] == "box-title":
                flush()
                if box is None:
                    parts.append("**" + event["text"] + "**")
            elif event["kind"] == "line":
                starts_list = bool(re.match(r"(?:- |\d+[.)] |[a-zA-Z][)] )", event["text"]))
                if last and (event["y0"] - last["y1"] > 7 or starts_list or last["kind"] != "line"):
                    flush()
                paragraph.append(event["text"])
            else:
                flush()
                parts.append(event["text"])
            last = event
        flush()
        if current_box is not None:
            parts.append("::::")
        return "\n\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build/converted")
    parser.add_argument("--pages", help="Physical PDF pages, e.g. 11-14,259,277-282 (pilot only)")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    out = args.output.resolve()
    if out == ROOT:
        parser.error("Generate into a staging directory; use --publish to install the result.")
    out.mkdir(parents=True, exist_ok=True)
    selected = None
    if args.pages:
        selected = set()
        for part in args.pages.split(","):
            bounds = list(map(int, part.split("-")))
            selected.update(range(bounds[0], bounds[-1] + 1))
        if args.publish:
            parser.error("A pilot cannot be published as a complete edition.")
    doc = pymupdf.open(PDF)
    encodings = font_encodings(doc)
    inventory = json.loads((ROOT / "source/inventory.json").read_text())
    divisions = [{"number": "", "title": "Introduction", "pdf_page_start": 2, "pdf_page_end": 5}]
    divisions += inventory["divisions"]
    manifest = {"source": str(PDF.relative_to(ROOT)), "sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
                "complete": selected is None, "documents": [], "pages": [], "assets": [], "blocks": [], "unresolved": [],
                "math_policy": "Mathematics is rebuilt as LaTeX from glyph geometry and accepted only when every drawn glyph is accounted for; regions that fail that check keep the source artwork and are listed under \"unresolved\"."}
    for division in divisions:
        number = division["number"]
        folder = "front" if not number else "chapters" if number.isdigit() else "appendices"
        filename = f"{folder}/" + (f"ch-{int(number):02d}-" if number.isdigit() else f"app-{number.lower()}-" if number else "") + slug(division["title"]) + ".md"
        parts = [f"({'ch-' + number if number.isdigit() else 'app-' + number.lower() if number else 'introduction'})=\n# "
                 + (number + ". " if number else "") + division["title"]]
        pages = []
        for p in range(division["pdf_page_start"], division["pdf_page_end"] + 1):
            if selected is not None and p not in selected:
                continue
            page = Page(doc[p - 1], out, encodings)
            parts.append(f"<!-- Source PDF page {p}; printed label {doc[p - 1].get_label()}. -->\n\n" + page.extract())
            manifest["pages"].append({"pdf_page": p, "document": filename,
                                       "native_inline_math": page.native_math_count, "svg_math": page.math_count})
            manifest["assets"].extend(page.assets)
            manifest["unresolved"].extend(page.unresolved)
            for item in page.records:
                item["document"] = filename
            manifest["blocks"].extend(page.records)
            pages.append(p)
            if p % 20 == 0 or selected:
                print(f"Extracted PDF page {p}: {page.native_math_count} native expressions, {page.math_count} source SVGs", flush=True)
        if pages:
            path = out / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n\n".join(parts) + "\n")
            manifest["documents"].append({"file": filename, "title": division["title"], "number": number, "pages": pages})
    (out / "source").mkdir(exist_ok=True)
    (out / "source/conversion.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(manifest['documents'])} documents and {len(manifest['assets'])} asset references to {out}")
    if args.publish:
        targets = [out / d["file"] for d in manifest["documents"]]
        targets += [out / "source/conversion.json"]
        targets += [out / name for name in sorted(set(manifest["assets"]))]
        if not args.overwrite and any((ROOT / p.relative_to(out)).exists() for p in targets):
            parser.error("Destination files exist. Review staging output and pass --overwrite explicitly.")
        for path in targets:
            destination = ROOT / path.relative_to(out)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        # Each run names a maths asset after its own content, so a rerun that
        # transcribes an expression leaves the artwork it replaced behind.
        kept = {ROOT / name for name in manifest["assets"]}
        stale = [p for p in (ROOT / "images/math").glob("*.svg") if p not in kept]
        for path in stale:
            path.unlink()
        print(f"Installed staged book files into repository"
              + (f"; removed {len(stale)} superseded maths images." if stale else "."))


if __name__ == "__main__":
    main()
