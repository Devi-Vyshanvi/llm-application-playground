import os
from dotenv import load_dotenv
from openai import OpenAI

import streamlit as st


load_dotenv()

api_key=os.getenv("Groq_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["Groq_API_KEY"]
    except (KeyError, FileNotFoundError):
        api_key = None

if not api_key:
    st.error("API key not found. check .env file")
    st.stop()
    
client=OpenAI(api_key=api_key,base_url="https://api.groq.com/openai/v1")

st.title("LLM APPLICATION PLAYGROUND")
st.write("welcom to LLM Playground")
prompt=st.text_input("Enter Your Prompt")

if st.button("Generate Response"):
    if prompt:
        with st.spinner("Generating response"):

            response=client.responses.create(
                model="openai/gpt-oss-20b",
                input=prompt
                )
            
        st.write("AI Response:")
        st.write(response.output_text)

    else:
        st.warning("Enter the prompt:")