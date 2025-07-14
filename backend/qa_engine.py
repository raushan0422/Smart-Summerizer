import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def answer_question(text, query):
    prompt = f"""You are a smart assistant.
Document: {text[:4000]}
Question: {query}
Answer the question based only on the document and include justification (e.g., paragraph or section)."""
    response = model.generate_content(prompt)
    return response.text
