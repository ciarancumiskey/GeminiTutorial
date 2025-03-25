from dotenv import load_dotenv
from fastapi import APIRouter
from google import genai
import os
from models.basic_prompt_model import PromptRequest
from services.gemini_client import ask_close_ended_question, send_n_shot_prompt, send_text_prompt

prompt_router = APIRouter(
    prefix="/api/v1/prompts",
    tags=["prompts"]
)
# Load the API key and create a Gemini client
load_dotenv()
gemini_api_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@prompt_router.post("/basic")
async def basic_prompt(prompt_body: PromptRequest):
    if prompt_body.model:
        model = prompt_body.model.value
    # Default to the lite model if one's not specified
    else:
        model = "gemini-2.0-flash-lite"
    # Remove trailing whitespace
    gemini_response = send_text_prompt(gemini_api_client, model, prompt_body.prompt)
    return {"response": gemini_response}


@prompt_router.post("/nshot")
async def n_shot_prompt(prompt_body: PromptRequest):
    if prompt_body.model:
        model = prompt_body.model.value
    # Default to the lite model if one's not specified
    else:
        model = "gemini-2.0-flash-lite"
    gemini_response = send_n_shot_prompt(gemini_api_client, model, prompt_body.instructions, prompt_body.chat_history,
                                         prompt_body.prompt)
    # Remove trailing whitespace
    return {"response": gemini_response}


@prompt_router.post("/closed_ended")
async def closed_ended_question(prompt_body: PromptRequest):
    if prompt_body.model:
        model = prompt_body.model.value
    # Default to the lite model if one's not specified
    else:
        model = "gemini-2.0-flash-lite"
    # Remove trailing whitespace
    gemini_response = ask_close_ended_question(gemini_api_client, model, prompt_body.prompt).rstrip()
    return {"response": gemini_response}
