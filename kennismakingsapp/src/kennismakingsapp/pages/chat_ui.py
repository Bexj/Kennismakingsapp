import streamlit as st
from src.kennismakingsapp.chat import chat_with_gpt

def chat_page():
    """Renders the Chat with AI page in Streamlit."""
    st.title("💬 Chat with Joren's AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        response = chat_with_gpt(user_input) 
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
