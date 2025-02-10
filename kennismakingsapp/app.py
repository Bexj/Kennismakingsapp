import streamlit as st
from src.kennismakingsapp.chat import chat_with_gpt

st.title("Azure OpenAI Chatbot (LangChain)")

st.write("Chat with an AI powered by Azure OpenAI and LangChain!")

# Chat input
user_input = st.text_input("Ask ChatGPT something:")

if user_input:
    response = chat_with_gpt(user_input)
    st.write("### Response:")
    st.write(response)
