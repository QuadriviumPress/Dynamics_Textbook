#!/usr/bin/env python3
"""Record the PDF's structure without treating extracted text as finished MyST."""

import hashlib
import json
import re
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tex/phys206_f25_textbook.pdf"


def main():
    with pymupdf.open(SOURCE) as doc:
        outline = doc.get_toc()
        starts = [entry for entry in outline if entry[0] == 1]
        divisions = []
        for i, (_, title, start) in enumerate(starts):
            end = starts[i + 1][2] - 1 if i + 1 < len(starts) else len(doc)
            divisions.append({
                "number": str(i + 1) if i < 12 else chr(ord("A") + i - 12),
                "title": title,
                "pdf_page_start": start,
                "pdf_page_end": end,
            })
        pages = []
        for i, page in enumerate(doc):
            text = page.get_text()
            pages.append({
                "pdf_page": i + 1,
                "pdf_page_label": page.get_label(),
                "text_characters": len(text),
                "figure_captions": re.findall(r"Figure\s+(\d+\.\d+):", text),
                "sample_problem_labels": re.findall(r"Sample Problem\s+(\d+-\d+)", text),
                "practice_problem_labels": re.findall(r"Practice Problem\s+(\d+-\d+)", text),
                "solution_labels": re.findall(r"(?<!Practice )(?<!Sample )Problem\s+(\d+-\d+):", text) if i >= 288 else [],
                "image_placements": len(page.get_image_info()),
            })
        result = {
            "source": SOURCE.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "edition": "Fall 2025",
            "announced_date": "2025-08-20",
            "page_count": len(doc),
            "page_number_convention": "pdf_page fields are one-based physical PDF pages",
            "pymupdf_version": pymupdf.VersionBind,
            "divisions": divisions,
            "outline": [{"level": level, "title": title, "pdf_page": page}
                        for level, title, page in outline],
            "pages": pages,
        }
    destination = ROOT / "source/inventory.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Recorded {len(pages)} pages, {len(divisions)} divisions, "
          f"and {len(outline)} outline entries in {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
