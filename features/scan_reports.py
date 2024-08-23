import streamlit as st
from pypdf import PdfReader 
import time
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import easyocr, os
from features.llama3_response import QA

# os.environ["GROQ_API_KEY"] = "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"

load_dotenv()
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

st.title("Check Medical Test Reports 📄")

language = st.selectbox("Select Languages", ("English", "Hindi", "Hinglish", "Spanish"))
st.write("Selected: ", language)
print(language)
st.divider()

def get_llm_response(context:str, language: str) -> str :
    input = f""" You are MedSathi a helpful pharmacist. This is the Medical test reports context it contains some advance medical terminalogy may be normal human can't understand explain the context in simple form what is actully written in reports even a old ceneterions or kid can also understand not too much long or short, if you found the context non medical test report tell to user is not a medical report or something. In this language {language}
    context:{context}."""
    try:
        model=genai.GenerativeModel('gemini-pro')
        response=model.generate_content(input)
        
        return response.text
    except Exception as e:
        return "Captured Image is not clear enough, please place the name of med before camera"

    
# # Create sections with horizontal placement
col1, col2 = st.columns(2)

with col1:
    # Full-width section for capturing photo
    st.subheader("Click Picture of your report")
    image_data = st.camera_input("Take a picture")

    if image_data is not None:
        st.image(image_data, caption="Captured Image.", use_column_width=True)
        reader = easyocr.Reader(['en'])

        results = reader.readtext(image_data)

        context = ' ' 
        for result in results:
            context += result[1] + ' '
            
        qa = QA()
        response = qa(context)
        str_response = str(response)
    
        output = str_response.split("=")
        output = str(output[2] + output[3]).replace("error", "")
    

        # response = get_llm_response(context, language)
        with st.chat_message("assistant"):
            st.markdown(response)
            
        

with col2:
    st.subheader("Upload Picture of your report")

    image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        image = Image.open(image_file)
        

        st.image(image, caption="Uploaded Image.", use_column_width=True)
        
        
        with st.spinner('Extracting report..'):
            time.sleep(4)
        reader = easyocr.Reader(['en'])

        results = reader.readtext(image)
        
        st.success("Done!")
            
        with st.spinner('Summery Done..'):
            time.sleep(3)
        
        context = ' ' 
        for result in results:
            context += result[1] + ' '
        st.success('Done!')
        
        with st.spinner('Getting Response from LLM..'):
            time.sleep(2)
        # st.write(context)
        qa = QA()
        response = qa(context)
        
        str_response = str(response)
    
        output = str_response.split("=")
        output = str(output[2] + output[3]).replace("error", "")
    

        # response = get_llm_response(context, language)
        with st.chat_message("assistant"):
            st.markdown(output)
        st.success('Done!')



st.divider()
col3, col4 = st.columns(2)
with col3:
    st.header("Upload Medical Test Reports in PDF")

    pdf_file = st.file_uploader("Medical Reports only", type="pdf", key="pdf-upload")
    
    if pdf_file is not None:
        # Display PDF file details
    
    # creating a pdf reader object 
        reader = PdfReader(pdf_file) 
        

        print(len(reader.pages)) 
        
        # creating a page object 
        page = reader.pages[0] 
        
        # extracting text from page 
        context = page.extract_text()
        
        # call
        qa = QA()
        output = qa(context)
        # print(output)
        str_response = str(output)
    
        output = str_response.split("=")
        output = str(output[2] + output[3]).replace("error", "")
    

    # print(type(str_response))
        # st.write(context)
        # response = get_llm_response(context, language)
        with st.chat_message("assistant"):
            st.markdown(output)
            
        
        
        
