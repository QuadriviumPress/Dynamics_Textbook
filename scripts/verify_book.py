#!/usr/bin/env python3
"""Check the generated MyST edition against the source PDF inventory.

Structural checks cannot establish that the mathematics is right; they
establish that nothing was dropped, no reference dangles, and no page of the
source went unrepresented. Run with ``npm run verify``.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

#: labels the linker assigns, and the source numbering each is built from
LABEL_KINDS = (
    ("fig", "figure"), ("eq", "equation"), ("sec", "section"),
    ("ch", "chapter"), ("app", "appendix"), ("example", "sample problem"),
    ("problem", "practice problem"), ("solution", "solution"),
)


class Report:
    def __init__(self):
        self.failures = []
        self.notes = []

    def check(self, ok, message, detail=""):
        if ok:
            self.notes.append(f"ok      {message}")
        else:
            self.failures.append(f"FAILED  {message}" + (f"\n        {detail}" if detail else ""))
        return ok

    def note(self, message):
        self.notes.append(f"note    {message}")


def documents(config):
    """Every markdown file the table of contents points at, in order."""
    found = []
    for line in config.splitlines():
        match = re.search(r"^\s*-?\s*file:\s*\"?([^\"\n]+?)\"?\s*$", line)
        if match:
            found.append(match[1])
    return found


def load(paths):
    return {path: (ROOT / path).read_text() for path in paths
            if (ROOT / path).exists() and path.endswith(".md")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="print failures only")
    args = parser.parse_args()
    report = Report()

    inventory = json.loads((ROOT / "source/inventory.json").read_text())
    conversion = json.loads((ROOT / "source/conversion.json").read_text())
    config = (ROOT / "myst.yml").read_text()
    listed = documents(config)

    # --- every file the table of contents names must exist -----------------
    missing = [f for f in listed if not (ROOT / f).exists()]
    report.check(not missing, "every table-of-contents entry exists", ", ".join(missing))

    texts = load(listed)
    body = "\n".join(texts.values())

    # --- the whole source must be represented ------------------------------
    report.check(conversion.get("complete") is True,
                 "the conversion manifest covers the complete book")
    report.check(conversion["sha256"] == inventory["sha256"],
                 "conversion and inventory describe the same PDF")
    converted = {p["pdf_page"] for p in conversion["pages"]}
    expected = set()
    for division in [{"pdf_page_start": 2, "pdf_page_end": 5}] + inventory["divisions"]:
        expected.update(range(division["pdf_page_start"], division["pdf_page_end"] + 1))
    report.check(expected <= converted, "every source page was converted",
                 f"absent: {sorted(expected - converted)[:20]}")

    # --- chapters and appendices -------------------------------------------
    for division in inventory["divisions"]:
        number = division["number"]
        label = f"ch-{number}" if number.isdigit() else f"app-{number.lower()}"
        report.check(f"({label})=" in body,
                     f"division {number} ({division['title']}) is present and labelled")

    # --- figures ------------------------------------------------------------
    source_figures = sorted({n for page in inventory["pages"]
                             for n in page["figure_captions"]},
                            key=lambda s: [int(p) for p in s.split(".")])
    present = set(re.findall(r"^:label: (fig-[\d-]+)$", body, re.M))
    absent = [n for n in source_figures if "fig-" + n.replace(".", "-") not in present]
    report.check(not absent, f"all {len(source_figures)} numbered figures are present",
                 f"absent: {absent[:20]}")

    # --- assets exist and nothing is orphaned -------------------------------
    referenced = set()
    for path, text in texts.items():
        base = (ROOT / path).parent
        for target in re.findall(r"\]\(((?:\.\./)?images/[^)\s]+)\)", text):
            referenced.add((base / target).resolve())
        for target in re.findall(r"^:::\{image\}\s+(\S+)", text, re.M):
            referenced.add((base / target).resolve())
        for target in re.findall(r"^:::\{figure\}\s+(\S+)", text, re.M):
            referenced.add((base / target).resolve())
    absent = sorted(p for p in referenced if not p.exists())
    report.check(not absent, f"all {len(referenced)} referenced images exist",
                 ", ".join(str(p.relative_to(ROOT)) for p in absent[:10]))
    on_disk = {p.resolve() for p in (ROOT / "images").rglob("*") if p.is_file()}
    orphans = sorted(on_disk - referenced)
    report.check(not orphans, f"no orphaned files under images/ ({len(on_disk)} on disk)",
                 ", ".join(str(p.relative_to(ROOT)) for p in orphans[:10]))

    # --- labels and cross-references ---------------------------------------
    labels = collections.Counter(re.findall(r"^\(([^)]+)\)=", body, re.M))
    labels.update(re.findall(r"^:label: (\S+)$", body, re.M))
    labels.update(re.findall(r"^\$\$ \((\S+)\)$", body, re.M))
    duplicates = [name for name, count in labels.items() if count > 1]
    report.check(not duplicates, f"all {len(labels)} labels are unique",
                 ", ".join(duplicates[:10]))
    targets = set(re.findall(r"\]\(#([^)]+)\)", body))
    dangling = sorted(t for t in targets if t not in labels)
    report.check(not dangling, f"all {len(targets)} internal references resolve",
                 ", ".join(dangling[:10]))

    # --- problems and their solutions --------------------------------------
    for key, prefix, name in (("practice_problem_labels", "problem", "practice problems"),
                              ("solution_labels", "solution", "solutions")):
        source = {n for page in inventory["pages"] for n in page[key]}
        absent = sorted(n for n in source if f"({prefix}-{n})=" not in body)
        report.check(not absent, f"all {len(source)} {name} are present and labelled",
                     ", ".join(absent[:10]))
    unanswered = sorted(n for n in {m for p in inventory["pages"] for m in p["practice_problem_labels"]}
                        if f"(solution-{n})=" not in body)
    report.note(f"{len(unanswered)} practice problems have no solution in Appendix C"
                + (f": {unanswered[:8]}" if unanswered else ""))

    # --- transcription artefacts -------------------------------------------
    stray = []
    for path, text in texts.items():
        for number, line in enumerate(text.splitlines(), 1):
            for ch in line:
                point = ord(ch)
                if point < 32 and ch != "\t" or 0xE000 <= point <= 0xF8FF or point == 0xFFFD:
                    stray.append(f"{path}:{number} U+{point:04X}")
                    break
    report.check(not stray, "no control or private-use characters survive",
                 ", ".join(stray[:10]))
    headers = [f"{p}:{i}" for p, t in texts.items()
               for i, line in enumerate(t.splitlines(), 1)
               if re.match(r"^\s*(CHAPTER \d+|Second-Year Dynamics)\s*\d*\s*$", line)]
    report.check(not headers, "no running headers or footers leaked into the text",
                 ", ".join(headers[:10]))

    # --- mathematics --------------------------------------------------------
    sys.path.insert(0, str(ROOT / "scripts"))
    import mathtext

    bad = []
    for path, text in texts.items():
        stripped = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
        for match in re.finditer(r"\$\$(.+?)\$\$|(?<![\$\\])\$([^\$\n]+)\$", stripped, re.S):
            fragment = match[1] or match[2]
            if not mathtext.latex_is_well_formed(fragment):
                bad.append(f"{path}: {fragment.strip()[:60]}")
    report.check(not bad, "every LaTeX fragment is structurally well formed",
                 "\n        ".join(bad[:10]))

    kinds = collections.Counter(b["kind"] for b in conversion["blocks"])
    latex = kinds["inline-math-latex"] + kinds["display-math-latex"]
    artwork = kinds["inline-math-svg"] + kinds["display-math-svg"]
    report.note(f"{latex} expressions rebuilt as LaTeX, {artwork} kept as source artwork "
                f"({100 * latex / max(latex + artwork, 1):.1f}% LaTeX)")
    report.note(f"{len(conversion.get('unresolved', []))} regions are recorded as unresolved "
                "in source/conversion.json")

    if not args.quiet:
        print("\n".join(report.notes))
    if report.failures:
        print("\n" + "\n".join(report.failures))
        print(f"\n{len(report.failures)} check(s) failed.")
        return 1
    print(f"\nAll {len(report.notes)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
