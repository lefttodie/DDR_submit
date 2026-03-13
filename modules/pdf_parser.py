import fitz
import json
import os

def parse_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(doc):

        text = page.get_text()

        pages.append({
            "page": page_num,
            "text": text
        })

    os.makedirs("extracted", exist_ok=True)

    with open("extracted/parsed_text.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2)

    return pages