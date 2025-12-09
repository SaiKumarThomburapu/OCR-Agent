"""Gemini API Client with retry logic"""

import google.generativeai as genai
import time
from typing import Dict, Any, Optional
from src.ocr_tech.config import settings
import logging

logger = logging.getLogger(__name__)
genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiClient:
    def __init__(self, model: str = "gemini-2.0-flash"):
        self.model_name = model
        self.model = genai.GenerativeModel(model)
        logger.info(f"✅ Gemini {model} initialized")
    
    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate with retry logic"""
        for attempt in range(3):
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.3,
                        "max_output_tokens": max_tokens
                    }
                )
                return response.text.strip()
            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt == 2:
                    raise
                time.sleep(1)
        return ""
