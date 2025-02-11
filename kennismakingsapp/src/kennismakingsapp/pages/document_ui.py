import streamlit as st
from src.kennismakingsapp.document_loader import convert_to_text, save_uploaded_file
from src.kennismakingsapp.chat import chat_with_gpt

def document_page():
    """Renders the Upload Documents page in Streamlit."""
    st.title("Upload Documents for Analysis")
    uploaded_file = st.file_uploader(
        "Upload a document (TXT, PDF, DOCX, Markdown, Excel)", 
        type=["txt", "pdf", "docx", "md", "xlsx"]
    )

    if uploaded_file:
        file_path = save_uploaded_file(uploaded_file)
        file_text = convert_to_text(file_path)

        st.text_area("Extracted Text", file_text, height=200)

        if st.button("Analyze with AI"):
            response = chat_with_gpt(f"Analyze this document:\n{file_text}")
            st.write("### AI Analysis:")
            st.write(response)
