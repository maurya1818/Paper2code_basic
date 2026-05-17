import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    
def get_llm_model(model_name="gemini-2.5-flash"):
    """
    Returns a generative model instance.
    Uses flash by default for fast, cost-effective extraction.
    For more complex coding tasks, consider gemini-1.5-pro.
    """
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file.")
        
    return genai.GenerativeModel(model_name)
