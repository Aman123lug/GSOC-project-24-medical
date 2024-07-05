import streamlit as st

st.title("testing features......")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
