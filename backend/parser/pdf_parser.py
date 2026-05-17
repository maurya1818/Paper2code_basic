import fitz  # PyMuPDF
import io
import re

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts and cleans text from a PDF byte stream.
    """
    try:
        # Open the PDF from bytes
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        full_text = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            full_text.append(text)
            
        raw_text = "\n".join(full_text)
        
        # Basic cleaning: remove excessive newlines and multiple spaces
        cleaned_text = re.sub(r'\n{3,}', '\n\n', raw_text)
        cleaned_text = re.sub(r' {2,}', ' ', cleaned_text)
        
        return cleaned_text.strip()
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {str(e)}")
