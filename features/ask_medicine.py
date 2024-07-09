import streamlit as st
from Pine_Process import get_context_new, get_llm_response
import time

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


# Example prompts
# Example prompts
example_prompts = [
    "How you can help me?",
    "Can i ask about any medicine?",
    "What is Benzoyl Peroxide Topical topical, it's used for?",
    "What are the side effects of hydrocortisone?",
    "When we can take Haemophilus influenzae type b hib and it's used for?",
    "What special precautions should I follow? Before taking chlorpheniramine",
    
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
    


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := (st.chat_input("What is up?") or button_pressed):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    

    context = get_context_new(prompt, "A")
    
    
    context = ""
    if "benzoyl peroxide topical" in prompt.lower():
        context += get_context_new(prompt, 'A')
    if "hydrocortisone" in prompt.lower():
        context += get_context_new(prompt, 'A')
    if "haemophilus influenzae" in prompt.lower():
        context += get_context_new(prompt, 'A')
    
    
    response = get_llm_response(context, prompt)
    time.sleep(0.02)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})