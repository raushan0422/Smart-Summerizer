import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_summary(text):
    prompt = f"Summarize this document in under 150 words:\n\n{text[:4000]}"
    response = model.generate_content(prompt)
    return response.text
