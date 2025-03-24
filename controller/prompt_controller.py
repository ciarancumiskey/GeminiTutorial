from dotenv import load_dotenv
from fastapi import APIRouter
from google import genai
import os
from models.basic_prompt_model import BasicPromptRequest
from services.gemini_client import send_text_prompt

prompt_router = APIRouter(
    prefix="/api/v1/prompts",
    tags=["prompts"]
)
# Load the API key and create a Gemini client
load_dotenv()
gemini_api_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@prompt_router.post("/basic")
async def basic_prompt(prompt_body: BasicPromptRequest):
    if prompt_body.model:
        model = prompt_body.model.value
    # Default to the lite model if one's not specified
    else:
        model = "gemini-2.0-flash-lite"
    gemini_response = send_text_prompt(gemini_api_client, model, prompt_body.prompt)
    return {"response": gemini_response}
