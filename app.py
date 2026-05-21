import streamlit as st
import numpy as np
from PIL import Image
import cv2

from utils.preprocessing import preprocess_image
from utils.ocr_engine import extract_text, set_tesseract_path
from utils.file_utils import save_text_to_file

st.set_page_config(page_title="AI Text Recognition", page_icon="📝", layout="centered")

st.title("AI Text Recognition")
st.write("Upload an image with text, and the app will extract the text using OCR.")

set_tesseract_path()

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        image_pil = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image_pil)
        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        st.subheader("Original Image")
        st.image(image_pil, use_container_width=True)

        processed_image = preprocess_image(image_cv)

        st.subheader("Processed Image")
        st.image(processed_image, use_container_width=True, clamp=True)

        text = extract_text(processed_image)

        st.subheader("Extracted Text")
        st.text_area("OCR Result", value=text, height=250)

        if text.strip():
            saved_path = save_text_to_file(text, filename="extracted_text.txt")
            st.success(f"Text saved to: {saved_path}")
        else:
            st.warning("No text was detected in the image.")

    except Exception as e:
        st.error(f"Error processing image: {e}")