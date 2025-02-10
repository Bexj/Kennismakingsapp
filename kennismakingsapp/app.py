import streamlit as st
from src.kennismakingsapp.chat import chat_with_gpt
from src.kennismakingsapp.document_loader import save_uploaded_file, convert_to_text

st.set_page_config(page_title="Kennismakingsapp", page_icon="📄")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Chat with AI", "Upload Documents", "About Me"])

if page == "Chat with AI":
    st.title("Chat with Joren's AI")
    st.write("This chatbot knows everything about Joren")

    user_input = st.text_input("Ask ChatGPT something:")
    
    if user_input:
        response = chat_with_gpt(user_input)
        st.write("### Response:")
        st.write(response)

elif page == "Upload Documents":
    st.title("Upload Documents for Analysis")
    uploaded_file = st.file_uploader("Upload a document (TXT, PDF, DOCX, Markdown, Excel)", type=["txt", "pdf", "docx", "md", "xlsx"])

    if uploaded_file:
        file_path = save_uploaded_file(uploaded_file)
        file_text = convert_to_text(file_path, uploaded_file.type)

        st.text_area("Extracted Text", file_text, height=200)

        if st.button("Analyze with AI"):
            response = chat_with_gpt(f"Analyze this document:\n{file_text}")
            st.write("### AI Analysis:")
            st.write(response)

elif page == "About Me":
    st.title("About Me")
    st.write("👋 **Hi, I'm Joren Bex!** This app lets you get to know me better.")
    st.write("💼 **Background:** Student in Applied Computer Science (AI & Data).")
    st.write("🎓 **University:** UCLL Leuven")
    st.write("🚀 **Interests:** AI, data engineering, and building intelligent applications.")
    st.write("📂 **Want to know more?** Upload a document and I'll analyze it for you!")
