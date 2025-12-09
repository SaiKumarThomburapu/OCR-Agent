from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    DEBUG: bool = True
    OCR_LANGUAGE: str = "en"
    LLM_MODEL: str = "gemini-2.0-flash"
    MIN_CONFIDENCE_THRESHOLD: float = 0.85
    
    class Config:
        env_file = ".env"

settings = Settings()
