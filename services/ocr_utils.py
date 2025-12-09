"""OCR Utility Functions"""

import re
from typing import List, Dict, Any

def detect_questions(text: str) -> List[Dict[str, Any]]:
    """Detect potential question patterns in OCR text"""
    question_patterns = [
        r"Q\d+\.?\s*",
        r"\d+\.\s*",
        r"(Find|What|How|Which|When|Where|Why)\s",
        r"[A-D][\)\.]?\s"
    ]
    
    questions = []
    lines = text.split("\n")
    
    for i, line in enumerate(lines):
        for pattern in question_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                questions.append({
                    "line_number": i,
                    "text": line.strip(),
                    "type": "potential_question"
                })
                break
    
    return questions

def clean_ocr_text(text: str) -> str:
    """Clean common OCR errors"""
    replacements = {
        "O": "0",  # O → 0
        "o": "0",
        "l": "1",  # l → 1
        "I": "1",
        "|": "1",
        "÷": "/",  # Division symbol
        "×": "*",
        "√": "sqrt",
        "²": "^2",
        "³": "^3"
    }
    
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    
    return text.strip()

def test_ocr_utils():
    sample = "Q1. Find 3/7 ÷ 3/7 = A) 1 B) Zero"
    print("🧪 Testing OCR Utils...")
    print(f"Cleaned: {clean_ocr_text(sample)}")
    print("✅ Utils ready!")
