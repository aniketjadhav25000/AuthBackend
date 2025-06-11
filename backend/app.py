from fastapi import FastAPI
from pydantic import BaseModel
from backend.utils import generate_code_from_prompt
from dotenv import load_dotenv

import os # Required for path and env variable handling

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))  
# Load environment variables

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str
    language: str

@app.post("/generate_code")
def generate_code(request: CodeRequest):
    return {"code": generate_code_from_prompt(request.prompt, request.language)}
