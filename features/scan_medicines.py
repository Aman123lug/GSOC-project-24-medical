import streamlit as st
from PIL import Image
import easyocr
from string import punctuation, digits
import google.generativeai as genai
from Pine_Process import get_context_new
from dotenv import load_dotenv


load_dotenv()


st.title("Capture Medicine")

def get_llm_response(context:str) -> str :
    input = f""" Your are MedSathi a helpful pharmacist. Use the given context to get the knowledge of the medicine and provide as much information possible about the medicine using the context. You're job is sort of like summarizing and provide all the info.
    context:{context}."""
    try:
        model=genai.GenerativeModel('gemini-pro')
        response=model.generate_content(input)
        
        return response.text
    except Exception as e:
        return "Captured Image is not clear enough, please place the name of med before camera"

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

    path = Image.open("features/sample_images_scan/crotamiton-hydrocortisone-cream.jpeg")
    reader = easyocr.Reader(['en'])

    results = reader.readtext(path)

    text = ' ' 
    for result in results:
        text += result[1] + ' '
        
    # print("old :", text)
    
    remove_digits = str.maketrans('', '', punctuation)
    remove_digits2 = str.maketrans('', '', digits)

    res = text.translate(remove_digits)
    res = res.translate(remove_digits2)

    new_text = ""
    for word in str(res).split():
        if (len(word) > 4):
            new_text += word + " "
            
    print(new_text)
    context = get_context_new(new_text, "A")
    print(context)
    
    
    output = get_llm_response(context)
    with st.chat_message("assistant"):
        st.markdown(output)