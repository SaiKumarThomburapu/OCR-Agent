import streamlit as st
import os
import uuid
from services.document_formatter import DocxFormatter

st.set_page_config(
    page_title="OCR Technologies - Bakeer Academy",
    page_icon="📚",
    layout="wide"
)

formatter = DocxFormatter()

def generate_demo_questions():
    return [
        {
            "question_number": 1,
            "question_text": "Find the value (1/32 ÷ 1/4) × (1/16 ÷ 1/8) =",
            "options": {"A": "1/16", "B": "1/8", "C": "16/1", "D": "4/16"},
            "correct_answer": "A",
            "confidence": 0.95
        },
        {
            "question_number": 2,
            "question_text": "√60 + 63 ≈ ?",
            "options": {"A": "11", "B": "10", "C": "12", "D": "8"},
            "correct_answer": "C",
            "confidence": 0.92
        },
        {
            "question_number": 3,
            "question_text": "The largest number multiplied by 7 such that their product is less than 115:",
            "options": {"A": "17", "B": "15", "C": "16", "D": "14"},
            "correct_answer": "D",
            "confidence": 0.88
        }
    ]

def main():
    st.title("📚 Bakeer Academy – MCQ DOCX Generator")
    st.write("Upload your mathematics PDF. The system will extract MCQs and build a Bakeer-style DOCX.")

    uploaded_file = st.file_uploader("Upload Mathematics PDF", type=["pdf"])

    if uploaded_file is not None:
        st.info(f"Uploaded file: **{uploaded_file.name}**")

        # TODO: replace demo with real OCR+LLM pipeline
        with st.spinner("Processing PDF (demo mode)…"):
            questions = generate_demo_questions()
            st.success(f"Extracted {len(questions)} questions (demo).")

        st.subheader("Preview of extracted questions")
        for q in questions:
            with st.expander(f"Q{q['question_number']}: {q['question_text'][:80]}"):
                st.write(q["question_text"])
                st.write("Options:")
                for label, text in q["options"].items():
                    st.write(f"- **{label})** {text}")
                if q.get("correct_answer"):
                    st.write(f"✅ Answer: **{q['correct_answer']}**")
                st.write(f"Confidence: {q.get('confidence', 0):.2f}")

        st.markdown("---")
        st.subheader("Generate DOCX")

        if st.button("✅ Looks good – create DOCX"):
            job_id = str(uuid.uuid4())
            output_name = f"Bakeer_Academy_Questions_{job_id}.docx"
            output_path = os.path.join(os.getcwd(), output_name)

            with st.spinner("Generating Word document…"):
                formatter.create_bakeer_docx(questions, output_path)

            with open(output_path, "rb") as f:
                st.success("DOCX generated successfully.")
                st.download_button(
                    label="📥 Download DOCX",
                    data=f.read(),
                    file_name=output_name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

if __name__ == "__main__":
    main()
