import json
from extractor.llm_client import get_llm_model
import typing_extensions as typing

class ExtractedInfo(typing.TypedDict):
    model_name: str
    dataset: str
    learning_rate: str
    batch_size: str
    epochs: str
    optimizer: str
    loss_function: str
    architecture_summary: str
    training_summary: str

def extract_implementation_details(paper_text: str) -> dict:
    """
    Uses Gemini to extract hyperparameter and architecture details from a research paper.
    """
    model = get_llm_model(model_name="gemini-2.5-flash")
    
    prompt = f"""
    You are an AI research assistant. Your task is to extract the implementation details from the following research paper text.
    If a specific detail is not explicitly mentioned, use "Not specified" or try to infer a standard default based on the paper context.
    
    Extract the following information in strict JSON format:
    - model_name: Name of the proposed architecture.
    - dataset: Name of the datasets used for evaluation.
    - learning_rate: Learning rate for training.
    - batch_size: Batch size used during training.
    - epochs: Number of training epochs.
    - optimizer: Optimizer used (e.g., Adam, SGD).
    - loss_function: Loss function used.
    - architecture_summary: A brief 2-3 sentence summary of the model architecture.
    - training_summary: A brief 2-3 sentence summary of the training pipeline.
    
    Paper Text:
    {paper_text[:30000]} # Truncating to avoid massive token limits if needed, though Gemini 1.5 supports much more.
    """
    
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        raise ValueError("LLM failed to return a valid JSON response.")
