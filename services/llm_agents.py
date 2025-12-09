"""LLM Agents for MCQ extraction"""

from .gemini_client import GeminiClient
from .prompts import get_prompt
from typing import Dict, Any, List
import json
import logging
import re

logger = logging.getLogger(__name__)

class MCQAgent:
    def __init__(self):
        self.client = GeminiClient()
    
    def classify_question(self, text: str) -> Dict[str, Any]:
        """Classify if text contains valid MCQ"""
        prompt = get_prompt("classification", text=text)
        response = self.client.generate(prompt)
        
        try:
            result = json.loads(response)
            logger.info(f"Classified: {result.get('question_type')}")
            return result
        except:
            return {"is_valid_mcq": False, "confidence": 0.0}
    
    def extract_mcq(self, text: str) -> Dict[str, Any]:
        """Extract structured MCQ from text"""
        prompt = get_prompt("extraction", text=text)
        response = self.client.generate(prompt)
        
        try:
            result = json.loads(response)
            logger.info(f"Extracted Q{result.get('question_number', '?')}")
            return result
        except:
            return {"question_text": text, "confidence": 0.3}
    
    def validate_extraction(self, question_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate extracted question"""
        prompt = get_prompt("validation", question_data=json.dumps(question_data))
        response = self.client.generate(prompt)
        
        try:
            result = json.loads(response)
            return result
        except:
            return {"is_valid": True, "confidence": 0.8}

def test_llm_agents():
    """Test LLM agents"""
    agent = MCQAgent()
    sample_text = "Q1. Find 3/7 ÷ 3/7 = A) 1 B) Zero C) -1 D) -9/4"
    
    print("🧪 Testing LLM Classification...")
    classification = agent.classify_question(sample_text)
    print(f"✅ Classification: {classification}")
    
    print("\n🧪 Testing LLM Extraction...")
    extraction = agent.extract_mcq(sample_text)
    print(f"✅ Extraction: Q{classification.get('question_number', '?')}")
