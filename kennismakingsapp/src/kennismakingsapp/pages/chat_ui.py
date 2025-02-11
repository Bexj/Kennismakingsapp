import streamlit as st
from src.kennismakingsapp.chat import chat_with_gpt

def chat_page():
    """Renders the Chat with AI page in Streamlit."""
    st.title("Chat with Joren's AI")
    st.write("This chatbot knows everything about Joren. Ask anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history only if there are actual messages
    if st.session_state.messages:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        for msg in st.session_state.messages[-4:]:  # Show last 4 messages
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-message chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # User input box (with correct session state handling)
    user_input = st.text_input("Type your message and press Enter", key="chat_input")

    if user_input and "last_input" not in st.session_state:
        st.session_state.last_input = user_input  # Prevent reprocessing
        st.session_state.messages.append({"role": "user", "content": user_input})  
        response = chat_with_gpt(user_input)  
        st.session_state.messages.append({"role": "ai", "content": response})  

        # Instead of modifying session state, just force rerun
        st.rerun()  

    if "last_input" in st.session_state and st.session_state.last_input == user_input:
        del st.session_state.last_input
