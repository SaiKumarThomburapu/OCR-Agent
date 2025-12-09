"""Main processor: OCR + LLM pipeline"""

from .ocr_service import OCRService
from .llm_agents import MCQAgent
from .pdf_processor import PDFProcessor
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class QuestionProcessor:
    def __init__(self):
        self.ocr = OCRService()
        self.agent = MCQAgent()
    
    def process_pdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Full pipeline: PDF → Questions"""
        questions = []
        
        # Step 1: OCR extraction
        pdf_processor = PDFProcessor()
        images = pdf_processor.pdf_to_images(pdf_path)
        
        for img_path in images:
            # Step 2: Extract text
            page_text = self.ocr.extract_full_page(img_path)
            
            # Step 3: Classify
            classification = self.agent.classify_question(page_text)
            
            if classification.get("is_valid_mcq", False):
                # Step 4: Extract
                question = self.agent.extract_mcq(page_text)
                questions.append(question)
        
        pdf_processor.cleanup_images(images)
        logger.info(f"✅ Extracted {len(questions)} questions from {pdf_path}")
        return questions

def test_processor():
    print("🧪 Testing Question Processor...")
    processor = QuestionProcessor()
    print("✅ Pipeline ready! (Add PDF to test)")
