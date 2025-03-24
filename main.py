# Required for running a FastAPI-based microservice
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "Hello there."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug")
