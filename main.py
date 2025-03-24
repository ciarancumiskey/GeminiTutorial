# Required for running a FastAPI-based microservice
import uvicorn
from fastapi import FastAPI

from controller import prompt_controller

app = FastAPI()
app.include_router(prompt_controller.prompt_router)


@app.get("/")
async def get_root():
    return {"message": "Hello there."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug")
