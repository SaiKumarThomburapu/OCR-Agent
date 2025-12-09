"""Production-ready prompts for MCQ extraction"""

CLASSIFICATION_PROMPT = """
You are an expert MCQ classifier. Analyze this OCR text:

{text}

Return ONLY JSON:
{{
    "is_valid_mcq": true/false,
    "question_type": "math|science|language|general",
    "has_four_options": true/false,
    "confidence": 0.95
}}

Valid MCQ = Question + exactly 4 options (A,B,C,D)
"""

EXTRACTION_PROMPT = """
Extract this MCQ exactly as written. Preserve math notation.

TEXT: {text}

Return ONLY JSON:
{{
    "question_number": 1,
    "question_text": "exact question",
    "options": {{"A": "text", "B": "text", "C": "text", "D": "text"}},
    "correct_answer": "A|B|C|D|null",
    "confidence": 0.95
}}

CRITICAL: Never guess missing options. Mark "MISSING" if unclear.
"""

VALIDATION_PROMPT = """
Validate this extracted MCQ:

{question_data}

Return ONLY JSON:
{{
    "is_valid": true/false,
    "issues": ["list of problems"],
    "confidence": 0.95
}}
"""

def get_prompt(prompt_name: str, **kwargs) -> str:
    """Get prompt template"""
    prompts = {
        "classification": CLASSIFICATION_PROMPT,
        "extraction": EXTRACTION_PROMPT,
        "validation": VALIDATION_PROMPT
    }
    return prompts[prompt_name].format(**kwargs)
