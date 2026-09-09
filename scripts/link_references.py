#!/usr/bin/env python3
"""Add stable problem labels and link source-numbered cross-references."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def link_book(root):
    manifest = json.loads((root / "source/conversion.json").read_text())
    texts = {root / d["file"]: (root / d["file"]).read_text() for d in manifest["documents"]}
    labels = set()
    for path, text in texts.items():
        labels.update(re.findall(r"^\(([^)]+)\)=", text, re.M))
        labels.update(re.findall(r"^:label: (\S+)", text, re.M))
    for path, text in texts.items():
        lines = text.splitlines()
        result = []
        for line in lines:
            match = re.match(r"::::\{(?:admonition|tip)\} (Sample|Practice) Problem (\d+-\d+)", line)
            solution = re.match(r"\*\*Problem (\d+-\d+):\*\*", line) if path.name.startswith("app-c-") else None
            label = None
            if match:
                label = ("example-" if match[1] == "Sample" else "problem-") + match[2]
            elif solution:
                label = "solution-" + solution[1]
            if label and label not in labels:
                result.extend([f"({label})=", ""])
                labels.add(label)
            result.append(line)
        texts[path] = "\n".join(result) + "\n"

    pattern = re.compile(r"\b(Figures?|Sections?|Chapters?|Appendix|Equations?|Eq\.|Sample Problem|Practice Problem|Problem)\s+(\d+(?:[.-]\d+)*|[A-C](?:\.\d+)*)\b")
    for path, text in texts.items():
        def replace(match):
            kind, number = match.groups()
            if kind.startswith("Fig"):
                target = "fig-" + number.replace(".", "-")
            elif kind.startswith("Section") or kind.startswith("Chapter") and "." in number:
                target = "sec-" + number.replace(".", "-")
            elif kind.startswith("Chapter"):
                target = "ch-" + number
            elif kind == "Appendix":
                target = "sec-" + number.replace(".", "-") if "." in number else "app-" + number.lower()
            elif kind.startswith(("Eq", "Equation")):
                target = "eq-" + number.replace(".", "-")
            else:
                target = ("example-" if kind == "Sample Problem" else "problem-") + number
            return f"[{match[0]}](#{target})" if target in labels else match[0]

        result = []
        for line in text.splitlines():
            if line.startswith(("#", ":", "(", "<!--")) or re.match(r"\*\*Problem \d+-\d+:\*\*", line):
                result.append(line)
                continue
            # Protect existing links, images, math, and inline code. Running
            # this linker again must leave the book unchanged.
            pieces = re.split(r"(!?\[[^\]]*\]\([^)]*\)|\$[^$]*\$|`[^`]*`)", line)
            result.append("".join(p if i % 2 else pattern.sub(replace, p) for i, p in enumerate(pieces)))
        text = "\n".join(result) + "\n"
        # Navigation next to solution headings helps readers return to the
        # question without changing the source's answer text.
        if path.name.startswith("app-c-"):
            def question_link(match):
                number = match[1]
                target = "problem-" + number
                return match[0] + (f" [Question](#{target})" if target in labels else "")
            text = re.sub(r"^\*\*Problem (\d+-\d+):\*\*$(?!\s*\[Question\])", question_link, text, flags=re.M)
        path.write_text(text)
    return len(labels)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(f"Linked book using {link_book(args.root.resolve())} labels.")
