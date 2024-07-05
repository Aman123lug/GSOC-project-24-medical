import streamlit as st
import google.generativeai as genai
import os
# from dotenv import load_dotenv

API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Ask Medicine")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})