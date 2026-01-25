from pypdf import PdfReader


def load_pdf(path, doc_id):
    """
    Each item:
    {
        "doc_id": str,
        "page": int,
        "text": str
    }
    """
    reader = PdfReader(path)

    pages = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
        except Exception:
            text = None

        if text and text.strip():
            pages.append({
                "doc_id": doc_id,
                "page": i + 1,
                "text": text.strip()
            })

    return pages
