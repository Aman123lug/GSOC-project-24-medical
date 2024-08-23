import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
import random, string, os
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone
from dotenv import load_dotenv
import google.generativeai as genai

st.title("Add data to train")

CHUNK_SIZE = 3000
# GENAI_API_KEY = ""
HF_EMBEDDINGS = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
pine = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pine.Index(os.environ.get("PINECONE_INDEX"))


data = st.file_uploader("Upload your data to train the bot, using pdf or txt", type=["txt"])


def upsert_data(text, medname="user"):
    ''' Funtiom to upsert data into Pinecone with company name and text as metadata :
        @param medname = name of the medicine text belongs to
        @param text = text extracted from the company pdf files
        
        @ returns None
    '''

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=30)
    text_chunks = text_splitter.split_text(text)
    print("This the the length of Text chunks : ",len(text_chunks))
    for chunk in text_chunks:
        
        metadata = {"med_intial": medname, "text":chunk}
        # Text to be embedded
        vector = HF_EMBEDDINGS.embed_query(chunk)

        # Ids generation for vectors
        _id = ''.join(random.choices(string.ascii_letters + string.digits, k=10,))

        # Upserting vector into pinecone database
        index.upsert(vectors=[{"id":_id, "values": vector, "metadata": metadata}])

        print("Vector upserted successfully")

# def data_cleaner(text)-> str:
#     clean_data = text.strip()
#     return clean_data
    
if data:
    read_file = data.read()
    # clean = data_cleaner(read_file)
    upsert_data(str(read_file))
    # st.write(clean)
    st.success("wow")
    st.balloons()
    

