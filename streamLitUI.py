import streamlit as st

from langchain_google_genai import GoogleGenerativeAI
Api_Key = "AIzaSyC8OJrvD6yG0tTOlFuxu8wO5omSSfZuzKM"
LLM = GoogleGenerativeAI(google_api_key=Api_Key, model="gemini-2.0-flash")

st.title("COOL AI 123")

st.write("Enter an ai prompt")

st.write("")

prompt = st.text_input("Enter your prompt")

template = f"""
This is a chatbot specifically designed to help sarosh cheat on his homework,
with precise and accurate answers,
that are swift to read.
ADDRESS ME AS SIR.
answer to the following question {prompt}
"""

if st.button("Search"):
    response = LLM.invoke(template)
    st.write(response)
