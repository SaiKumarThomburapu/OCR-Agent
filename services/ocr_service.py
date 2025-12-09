"""OCR Service - Extracts text from images/PDFs using PaddleOCR"""

import os
from paddleocr import PaddleOCR
from typing import List, Dict, Any, Tuple
from PIL import Image
import logging
from src.ocr_tech.config import settings

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OCRService:
    def __init__(self):
        """Initialize PaddleOCR with optimized settings"""
        # Use the default constructor to be compatible with the installed PaddleOCR
        self.ocr = PaddleOCR()
        logger.info("OCR Service initialized")

    def extract_text_from_image(self, image_path: str) -> List[Dict[str, Any]]:
        """Extract text from single image with confidence scores"""
        try:
            result = self.ocr.ocr(image_path, cls=True)
            if result[0] is None:
                return []

            texts = []
            for line in result[0]:
                text_data = {
                    "text": line[1][0],
                    "confidence": float(line[1][1]),
                    "bbox": line[0],
                    "position": self._calculate_position(line[0])
                }
                if text_data["confidence"] > settings.MIN_CONFIDENCE_THRESHOLD:
                    texts.append(text_data)

            logger.info(f"Extracted {len(texts)} text blocks from {image_path}")
            return texts

        except Exception as e:
            logger.error(f"OCR failed on {image_path}: {e}")
            return []

    def extract_full_page(self, image_path: str) -> str:
        """Extract full readable text from page (ordered)"""
        texts = self.extract_text_from_image(image_path)
        # Sort by Y position (top to bottom)
        texts.sort(key=lambda x: x["position"]["y_center"])

        full_text = "\n".join([t["text"] for t in texts])
        return full_text

    def _calculate_position(self, bbox: List[List[float]]) -> Dict[str, float]:
        """Calculate center position of bounding box"""
        x_coords = [point[0] for point in bbox]
        y_coords = [point[1] for point in bbox]
        return {
            "x_center": sum(x_coords) / len(x_coords),
            "y_center": sum(y_coords) / len(y_coords),
            "width": max(x_coords) - min(x_coords),
            "height": max(y_coords) - min(y_coords)
        }


# Test function
def test_ocr_service():
    """Quick test - requires sample image in data/ folder"""
    service = OCRService()
    print(" Testing OCR Service...")
    print(" Service ready! (Add test image to data/ to test extraction)")
