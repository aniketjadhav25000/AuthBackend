from openai import OpenAI
from dotenv import load_dotenv
import os

# ✅ Correct path: backend/.env
env_path = os.path.join(os.path.dirname(__file__), ".env")
print(f"🔍 Looking for .env at: {env_path}")
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables.")
else:
    print("✅ OPENAI_API_KEY loaded successfully.")

client = OpenAI(api_key=api_key)

def generate_code_from_prompt(prompt: str, language: str) -> str:
    full_prompt = f"Write a {language} program to: {prompt}\n\nCode:\n"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
