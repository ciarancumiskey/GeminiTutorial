from pydantic import BaseModel


class BasicPromptRequest(BaseModel):
    prompt: str
    model: str | None = None
