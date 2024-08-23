import streamlit as st
from Pine_Process import get_context_new, get_llm_response
import time
import os
from features.llama3_response import QA
from dotenv import load_dotenv
import json
import re

qa = QA()
load_dotenv()


st.title("MedSathi ⚕️")


with st.expander("The Medsathi your personalized helpful AI pharmacist"):
    st.subheader("Project Overview")
    st.markdown(
        """
        The MedSathi is a AI powered LLM chatbot designed to analyze and answer your questions about any type of medicine you have dooubts how and when to use this medicine: paracetamol, hydrocortisone, pantapropozol. 
        It leverages the power of https://medlineplus.gov/ data approved by FDA, including side effects and when is safe to take.
        """
    )
    

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.greetings = False


example_prompts = [
    "How you can help me?",
    "Can i ask about any medicine?",
    "What is Benzoyl Peroxide Topical topical, it's used for?",
    "What are the side effects of hydrocortisone?",
    "When we can take Haemophilus influenzae type b hib?",
    "Tetanus, Diphtheria Any Precautions Before taking?",
    
]


button_cols = st.columns(3)

button_pressed = ""

if button_cols[0].button(example_prompts[0]):
    button_pressed = example_prompts[0]
elif button_cols[1].button(example_prompts[1]):
    button_pressed = example_prompts[1]
elif button_cols[2].button(example_prompts[2]):
    button_pressed = example_prompts[2]

button_cols_2 = st.columns(3)
if button_cols_2[0].button(example_prompts[3]):
    button_pressed = example_prompts[3]
elif button_cols_2[1].button(example_prompts[4]):
    button_pressed = example_prompts[4]
elif button_cols_2[2].button(example_prompts[5]):
    button_pressed = example_prompts[5]
    

on = st.toggle("Switch to User Uploaded data")
query = "A"
if on:
    query="user"
   
    st.warning("The bot will use user uploaded data we do not gurentee it's safety!", icon="⚠️")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

                          
if prompt := (st.chat_input("What is up?") or button_pressed):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


    context = get_context_new(prompt, query)
    print("is file wala context:", context)

    response = get_llm_response(context, prompt)
    # context_and_prompt = context + "\n" + prompt
    # response = qa(context_and_prompt)
    # str_response = str(response)
    
    # output = str_response.split("=")
    # output = output[2] + output[3]
    

    # print(type(str_response))
    
    
    
    
    
    
    with st.chat_message("assistant"):
        
        st.markdown(response)
            

    st.session_state.messages.append({"role": "assistant", "content": response})
  
