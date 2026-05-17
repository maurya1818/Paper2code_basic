from fastapi import APIRouter, UploadFile, File, HTTPException
from parser.pdf_parser import extract_text_from_pdf
from extractor.info_extractor import extract_implementation_details
from generator.code_generator import generate_project_code

router = APIRouter()

@router.post("/upload-paper")
async def process_paper(file: UploadFile = File(...)):
    """
    Complete pipeline: uploads a PDF, parses it, extracts details, and generates code.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    try:
        # Read file bytes
        pdf_bytes = await file.read()
        
        # 1. Parse PDF
        print(f"Parsing PDF: {file.filename}")
        paper_text = extract_text_from_pdf(pdf_bytes)
        
        if not paper_text:
            raise HTTPException(status_code=400, detail="Failed to extract text from the PDF.")
            
        # 2. Extract Details
        print("Extracting implementation details...")
        extracted_details = extract_implementation_details(paper_text)
        
        # 3. Generate Code
        print("Generating project code...")
        generated_code = generate_project_code(extracted_details)
        
        return {
            "message": "Project generated successfully.",
            "extracted_details": extracted_details,
            "generated_code": generated_code
        }
        
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/extract")
async def extract_details():
    return {"message": "Standalone extraction endpoint (placeholder for future use)"}

@router.post("/generate-code")
async def generate_code():
    return {"message": "Standalone generation endpoint (placeholder for future use)"}

@router.get("/download-project")
async def download_project():
    return {"message": "Download endpoint (to be implemented)"}
