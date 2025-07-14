import streamlit as st
from backend.file_parser import load_pdf, load_txt
from backend.summarizer import generate_summary
from backend.qa_engine import answer_question
from backend.challenge import generate_questions, evaluate_answer

# ---------------- Page Setup ---------------- #
st.set_page_config(page_title="Smart Summarizer", layout="centered")
st.title("📚 Smart Assistant for Research Summarization")
st.caption("⚡ Powered by Gemini 1.5 Flash (Free Tier)")

# ---------------- File Upload ---------------- #
uploaded_file = st.file_uploader("📂 Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Read document
    if uploaded_file.name.endswith(".pdf"):
        raw_text = load_pdf(uploaded_file)
    else:
        raw_text = load_txt(uploaded_file)

    if not raw_text or raw_text.startswith("❌ Error"):
        st.error("Failed to extract text from the document.")
    else:
        # ---------------- Summary ---------------- #
        st.subheader("📝 Auto Summary")
        with st.spinner("Summarizing document..."):
            summary = generate_summary(raw_text)
        st.success("Summary generated!")
        st.write(summary)

        # ---------------- Interaction Mode ---------------- #
        st.subheader("🎯 Choose Interaction Mode")
        mode = st.radio("Select Mode", ["Ask Anything", "Challenge Me"])

        # ---------- Mode: Ask Anything ---------- #
        if mode == "Ask Anything":
            st.subheader("💬 Ask a Question")
            user_question = st.text_input("What do you want to know from this document?")
            if st.button("Get Answer") and user_question.strip():
                with st.spinner("Thinking..."):
                    answer = answer_question(raw_text, user_question)
                st.write("🧠 **Answer:**")
                st.write(answer)

        # ---------- Mode: Challenge Me ---------- #
        elif mode == "Challenge Me":
            st.subheader("🧩 Logic-Based Questions")
            with st.spinner("Generating questions..."):
                questions = generate_questions(raw_text)

            user_answers = []
            for idx, question in enumerate(questions):
                ans = st.text_input(f"Q{idx+1}: {question}")
                user_answers.append((question, ans))

            if st.button("Evaluate Answers"):
                for idx, (q, user_ans) in enumerate(user_answers):
                    if user_ans.strip():
                        with st.spinner(f"Evaluating Q{idx+1}..."):
                            feedback = evaluate_answer(q, user_ans, raw_text)
                        st.markdown(f"**✅ Feedback for Q{idx+1}:**")
                        st.write(feedback)
else:
    st.info("Please upload a document to get started.")
