import streamlit as st
import pytesseract
from PIL import Image

st.title("testing features......")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

# If you installed Tesseract OCR using the installer on Windows, you might need to specify the path to the executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image from file
image = Image.open('features/sample_images_scan/crotamiton-hydrocortisone-cream.jpeg')

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

print(text)
st.write(text)