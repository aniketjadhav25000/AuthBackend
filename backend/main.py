from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import generate_code_from_prompt

app = FastAPI()

# ✅ Enable CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class CodeRequest(BaseModel):
    prompt: str
    language: str

# ✅ POST /generate_code
@app.post("/generate_code")
def generate_code(request: CodeRequest):
    try:
        code = generate_code_from_prompt(request.prompt, request.language)
        return {"code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
