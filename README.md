# 📚 Smart Summarizer – AI-Powered Research Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/LLM-Gemini%201.5%20Flash-orange)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent AI-powered document assistant that helps users summarize, understand, and interact with long documents such as research papers, legal files, technical manuals, and reports.

Built using **Streamlit + Google Gemini 1.5 Flash**, the application enables contextual Q&A, logic-based challenge generation, and answer justification from uploaded documents.

---

# 🚀 Live Demo

🔗 [Launch App](https://smart-summerizer-bdpuelzvx3fyzoevjffkdf.streamlit.app/)

# 📂 GitHub Repository

🔗 https://github.com/raushan0422/SmartSummarizer

---

# ✨ Features

## 📄 Smart Document Understanding
- Upload `.pdf` and `.txt` documents
- Extracts and processes document content instantly
- Supports research papers, reports, legal documents, and notes

## 📝 AI-Powered Summarization
- Generates concise summaries within seconds
- Captures key insights and important concepts
- Optimized for readability and quick understanding

## 💬 Context-Aware Question Answering
- Ask free-form questions about uploaded documents
- Responses are generated using document context
- Reduces hallucination using contextual grounding

## 🧠 Challenge Me Mode
- Generates logic-based and comprehension questions
- Evaluates user responses intelligently
- Helps in active learning and revision

## 📌 Answer Justification
- Every answer includes supporting evidence
- Improves transparency and trustworthiness
- Makes outputs more explainable

## ⚡ Gemini 1.5 Flash Powered
- Uses Google's fast and lightweight LLM
- Free-tier compatible
- Optimized for low-latency responses

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core backend logic |
| Streamlit | Interactive frontend UI |
| Google Gemini 1.5 Flash | LLM-based reasoning and generation |
| PyPDF2 | PDF parsing and text extraction |
| python-dotenv | Environment variable management |

---

# 📁 Project Structure

```bash
Smart Summarizer/
│
├── app.py
├── .env
├── requirements.txt
│
├── backend/
│   ├── file_parser.py
│   ├── summarizer.py
│   ├── qa_engine.py
│   └── challenge.py
│
├── screenshots/
├── demo/
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/raushan0422/SmartSummarizer.git
cd SmartSummarizer
```

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Gemini API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

⚠️ Never expose your API key publicly.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application will start at:

```bash
http://localhost:8501
```

---

# 🧠 Model Information

| Model | Description |
|------|-------------|
| Gemini 1.5 Flash | Fast and lightweight LLM optimized for summarization, contextual reasoning, and Q&A |

---

# 🔍 Core Functionalities

| Module | Responsibility |
|--------|---------------|
| file_parser.py | Extracts text from uploaded documents |
| summarizer.py | Generates concise summaries |
| qa_engine.py | Handles contextual question answering |
| challenge.py | Creates and evaluates logic-based questions |

---

# 📊 Workflow

```text
Upload Document
       ↓
Extract Text
       ↓
Generate Summary
       ↓
Ask Questions / Challenge Mode
       ↓
Contextual AI Responses
```

---

# 🎯 Use Cases

- 📚 Research Paper Summarization
- ⚖️ Legal Document Understanding
- 🏫 Student Study Assistant
- 📑 Technical Manual Simplification
- 🧠 Interview & Exam Preparation
- 📄 Report Analysis

---

# 🔒 Security Notes

- API keys are stored securely using `.env`
- No uploaded documents are permanently stored
- Local execution supported for privacy-focused use cases

---

# 🚀 Future Improvements

- Multi-document support
- PDF highlighting and citation mapping
- Voice-based interaction
- Chat history memory
- Vector database integration
- RAG pipeline implementation
- Multi-language document support

---

# 👨‍💻 Author

## Raushan Kumar

🎓 AI/ML Enthusiast  
💼 Machine Learning & Generative AI Developer  

### 🔗 Connect With Me

- GitHub: https://github.com/raushan0422
- LinkedIn: https://www.linkedin.com/in/raushan-kumar-gupta-2aa47b247/

---

# ⭐ Support

If you found this project useful:
- Star the repository
- Share feedback
- Connect on LinkedIn

---
