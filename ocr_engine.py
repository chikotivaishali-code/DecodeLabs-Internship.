import pytesseract
import platform

def set_tesseract_path():
    system = platform.system()
    if system == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    elif system == "Darwin":
        pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
    else:
        pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text(image):
    if image is None:
        return ""
    return pytesseract.image_to_string(image)