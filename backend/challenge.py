import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_questions(text, num=3):
    prompt = f"Generate {num} logic-based or comprehension-focused questions from this document:\n\n{text[:4000]}"
    response = model.generate_content(prompt)
    return response.text.strip().split('\n')

def evaluate_answer(question, user_answer, document_text):
    prompt = f"""Evaluate this answer:
Question: {question}
User Answer: {user_answer}
Document: {document_text[:4000]}

Evaluate if the answer is correct. Justify based on the document."""
    response = model.generate_content(prompt)
    return response.text
