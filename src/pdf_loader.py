from pypdf import PdfReader


def extract_text(pdf_file) -> str:
    """Extract all text from a PDF file."""

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()