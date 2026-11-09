
from pathlib import Path
from pypdf import PdfReader


def load_pdf(pdf_path: str | Path) -> str:
    """
    Extract text from a PDF document.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Extracted text from all PDF pages.
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("The provided file must be a PDF.")

    reader = PdfReader(pdf_path)

    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")

    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        if page_text.strip():
            extracted_pages.append(page_text)

    return "\n\n".join(extracted_pages)
