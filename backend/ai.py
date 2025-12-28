import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found")

client = genai.Client(api_key=api_key)

def generate_career_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text
