# Paper2Code

Paper2Code is an AI-powered platform that converts AI/ML research papers into executable PyTorch starter code and experiment pipelines. It automates the extraction of implementation details (hyperparameters, datasets, and architectures) from a PDF and uses the Google Gemini API to generate runnable project structures.

## Features

- **PDF Parsing:** Upload any machine learning research paper PDF to extract its raw text using `PyMuPDF`.
- **Intelligent Extraction:** Uses Google Gemini (`gemini-2.5-flash`) to identify and extract crucial hyperparameters, dataset names, and architectural summaries into a structured format.
- **Code Generation:** Automatically generates a PyTorch implementation based on the extracted details, including `model.py`, `dataset.py`, `train.py`, and `config.yaml`.
- **Modern UI:** Built with React, Vite, and Tailwind CSS v4 for a seamless and responsive user experience.

---

## Tech Stack

**Frontend:**
- React (Vite)
- Tailwind CSS v4

**Backend:**
- FastAPI (Python)
- SQLAlchemy (SQLite by default)
- PyMuPDF (Text Extraction)
- Google Generative AI SDK (Gemini API)

---

## Getting Started

Follow these instructions to set up the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/maurya1818/Paper2code_basic.git
cd paper2code_basic
```

### 2. Environment Variables
In the root directory, create a `.env` file (you can copy the provided `.env` template):
```bash
GOOGLE_API_KEY="your_google_gemini_api_key_here"
```

### 3. Backend Setup
Navigate to the backend directory and set up the Python environment:
```bash
cd backend
python -m venv venv

# Activate the virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```
The backend API will run at `http://localhost:8000`.

### 4. Frontend Setup
Open a new terminal window, navigate to the frontend directory, and start the Vite dev server:
```bash
cd frontend
npm install
npm run dev
```
The frontend application will be available at `http://localhost:5173`.

---

## Usage
1. Open the frontend URL in your browser.
2. Select an AI/ML research paper (PDF format).
3. Click "Generate Code".
4. The system will process the paper, extract the hyperparameters, and display the generated PyTorch starter code!

## Future Scope
- Support for Groq and DeepSeek models.
- Downloadable ZIP files for the generated code.
- Multi-agent orchestration for autonomous debugging.


# Upload UI
<img width="1392" height="556" alt="image" src="https://github.com/user-attachments/assets/f44de5d7-0703-40ae-b13a-1ef77067b614" />

# Generated File
<img width="1355" height="945" alt="image" src="https://github.com/user-attachments/assets/89d3894f-a5fc-4f8c-b25e-8fa81829970a" />


