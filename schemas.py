"""Pydantic schemas for API"""

from pydantic import BaseModel
from typing import List, Dict, Any

class Question(BaseModel):
    question_number: int
    question_text: str
    options: Dict[str, str]
    correct_answer: str | None = None
    confidence: float

class ProcessResponse(BaseModel):
    status: str
    questions_found: int
    download_url: str | None = None
