"""Main pipeline runner - FULL SYSTEM TEST"""

from services.question_processor import QuestionProcessor
from services.document_formatter import DocumentFormatter
import os

def run_full_pipeline(pdf_path: str = None):
    """Run complete OCR → LLM → Document pipeline"""
    print("🚀 OCR Technologies - Full Pipeline")
    print("=" * 50)
    
    processor = QuestionProcessor()
    formatter = DocumentFormatter()
    
    # Test with sample data if no PDF
    if not pdf_path or not os.path.exists(pdf_path):
        print("📄 No PDF found - using sample data")
        sample_questions = [{
            "question_number": 1,
            "question_text": "Find 3/7 ÷ 3/7 =",
            "options": {"A": "1", "B": "Zero", "C": "-1", "D": "-9/4"},
            "correct_answer": "A",
            "confidence": 0.95
        }]
        formatter.create_bakeer_document(sample_questions, "sample_output.pptx")
        print("✅ SAMPLE PIPELINE COMPLETE!")
        print("📄 Check: sample_output.pptx")
        return
    
    # Real PDF processing
    print(f"📄 Processing: {pdf_path}")
    questions = processor.process_pdf(pdf_path)
    if questions:
        output_path = "processed_questions.pptx"
        formatter.create_bakeer_document(questions, output_path)
        print(f"✅ FULL PIPELINE COMPLETE!")
        print(f"📄 Output: {output_path}")
    else:
        print("❌ No questions found")

if __name__ == "__main__":
    # Test the full system
    run_full_pipeline()
