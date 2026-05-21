import cv2
import numpy as np

def preprocess_image(image):
    if image is None:
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    return thresh

def convert_for_display(image):
    if image is None:
        return None

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)