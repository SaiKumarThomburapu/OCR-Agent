def test_imports():
    tests = [
        "from paddleocr import PaddleOCR",
        "import google.generativeai", 
        "from fastapi import FastAPI",
        "from pdf2image import convert_from_path"
    ]
    for test in tests:
        try:
            exec(test)
            print(f"✅ {test.split()[1]} OK")
        except Exception as e:
            print(f"❌ {test.split()[1]} FAILED: {e}")

if __name__ == "__main__":
    print("Testing imports...")
    test_imports()
    print("\n✅ All good! Run: pip install -r requirements.txt")
