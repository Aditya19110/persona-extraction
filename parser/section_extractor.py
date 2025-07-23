import fitz 
import os

def extract_sections(pdf_dir):
    """
    Extracts structured sections from PDFs in the given directory.
    Assumes each heading is a new section (based on font size heuristics).
    """
    sections = []
    section_id = 0

    for filename in os.listdir(pdf_dir):
        if not filename.endswith(".pdf"):
            continue
        doc_path = os.path.join(pdf_dir, filename)
        doc = fitz.open(doc_path)
        for page_num, page in enumerate(doc, start=1):
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                    if not line_text or len(line_text.split()) < 3:
                        continue
                    font_size = max(span["size"] for span in line["spans"])
                    is_heading = font_size >= 13
                    sections.append({
                        "section_id": f"{filename}_sec_{section_id}",
                        "doc_id": filename,
                        "page_number": page_num,
                        "title": line_text if is_heading else f"Untitled Section {section_id}",
                        "content": line_text,
                    })
                    section_id += 1
        doc.close()

    return sections