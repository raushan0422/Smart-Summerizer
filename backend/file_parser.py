from PyPDF2 import PdfReader

def load_pdf(file):
    """Extracts text from a PDF file."""
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        return f"❌ Error reading PDF: {e}"

def load_txt(file):
    """Reads a plain text (.txt) file."""
    try:
        return file.read().decode("utf-8")
    except Exception as e:
        return f"❌ Error reading TXT file: {e}"
