from enum import Enum

from pydantic import BaseModel


class GeminiModel(Enum):
    FLASH_2_0 = "gemini-2.0-flash"
    FLASH_LITE_2_0 = "gemini-2.0-flash-lite"
    PRO_EXPERIMENTAL_2_0 = "gemini-2.0-pro-exp-02-05"
    FLASH_1_5 = "gemini-1.5-flash"
    FLASH_1_5_8B = "gemini-1.5-flash-8b"
    PRO_1_5 = "gemini-1.5-pro"
    EMBEDDING = "gemini-embedding-exp"
    IMAGEN_3 = "imagen-3.0-generate-002"


class BasicPromptRequest(BaseModel):
    prompt: str
    model: GeminiModel = GeminiModel.FLASH_LITE_2_0
