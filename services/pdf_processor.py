"""PDF Processor - Converts PDF pages to images"""

from pdf2image import convert_from_path
from typing import List
import os
from pathlib import Path

class PDFProcessor:
    def __init__(self, dpi: int = 300):
        self.dpi = dpi
    
    def pdf_to_images(self, pdf_path: str, output_dir: str = "temp_images") -> List[str]:
        """Convert PDF pages to images"""
        Path(output_dir).mkdir(exist_ok=True)
        
        images = convert_from_path(
            pdf_path, 
            dpi=self.dpi,
            output_folder=output_dir,
            fmt="png",
            paths_only=True
        )
        
        print(f"✅ Converted {pdf_path} → {len(images)} images")
        return images
    
    def cleanup_images(self, image_paths: List[str]):
        """Clean up temporary images"""
        for img_path in image_paths:
            try:
                os.remove(img_path)
            except:
                pass

# Test function
def test_pdf_processor():
    print("🧪 Testing PDF Processor...")
    print("✅ Ready! (Add test PDF to data/ to test conversion)")
