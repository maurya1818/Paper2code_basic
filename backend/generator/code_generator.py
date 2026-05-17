import json
from extractor.llm_client import get_llm_model

def generate_project_code(extracted_details: dict) -> dict:
    """
    Uses Gemini to generate PyTorch starter code based on extracted details.
    Returns a dictionary mapping filenames to their string content.
    """
    model = get_llm_model(model_name="gemini-2.5-flash") # Using flash since pro quota exceeded
    
    details_str = json.dumps(extracted_details, indent=2)
    
    prompt = f"""
    You are an expert PyTorch ML Engineer. Based on the following extracted details from a research paper, generate a clean, modular, and runnable PyTorch starter project.
    
    Extracted Details:
    {details_str}
    
    Generate the following files:
    1. model.py : Contains the PyTorch `nn.Module` definition for the architecture.
    2. dataset.py : Contains the PyTorch `Dataset` and `DataLoader` setup.
    3. train.py : Contains the training loop, optimizer setup, and basic logging.
    4. config.yaml : Contains the hyperparameters.
    5. requirements.txt : Contains the necessary Python packages.
    
    Return the output STRICTLY as a JSON object where the keys are the filenames and the values are the raw text contents of the files. Do not include markdown codeblocks around the JSON.
    Example:
    {{
        "model.py": "import torch\\n...",
        "dataset.py": "import torch\\n...",
        "train.py": "...",
        "config.yaml": "...",
        "requirements.txt": "..."
    }}
    """
    
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        raise ValueError("LLM failed to return a valid JSON response for code generation.")
