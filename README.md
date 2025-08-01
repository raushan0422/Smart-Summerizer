# 📚 Smart Summarizer – AI-Powered Research Assistant

Smart Summarizer is an intelligent, locally running web app that helps users read and understand long documents like research papers, legal files, or technical manuals.

It:
- 📄 Reads user-uploaded PDF/TXT files
- ✨ Generates a concise summary
- 💬 Answers free-form questions with context
- 🧠 Generates and evaluates logic-based questions
- 📌 Justifies all responses based on content
- ⚡ Uses Google Gemini 1.5 Flash (Free Tier) for fast, reliable LLM responses

## 🚀 Features

| Feature                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 📂 Upload Support          | Accepts `.pdf` and `.txt` files                                              |
| 📝 Auto Summary            | Summarizes content within 150 words                                          |
| ❓ Ask Anything             | Context-aware Q&A using Gemini 1.5 Flash                                     |
| 🧠 Challenge Me Mode       | Generates and evaluates logic-based questions                                |
| 🔍 Answer Justification    | Each answer includes supporting reference from the document                  |
| ⚡ Gemini-Powered           | Fast and cost-free with `models/gemini-1.5-flash`                             |

## 📁 Project Structure
```
Smart Summarizer/
├── app.py
├── .env
├── requirements.txt
├── backend/
│ ├── file_parser.py
│ ├── summarizer.py
│ ├── qa_engine.py
│ └── challenge.py
```
## ⚙️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/SmartSummarizer.git
cd SmartSummarizer

##Create Virtual Environment

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt

Add Your Gemini API Key

Create a .env file in the project root directory and add:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Make sure your .env file is listed in .gitignore to keep it private.

▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Then open the app in your browser at: http://localhost:8501

🧠 Model Used
Model	Description
models/gemini-1.5-flash	Free, fast LLM from Google Generative AI — ideal for summarization, Q&A, and logic tasks.

🧪 Technologies Used
Python 3.10+

Streamlit – for UI

Google Generative AI SDK (google-generativeai)

PyPDF2 – for PDF parsing

python-dotenv – for loading the API key securely


