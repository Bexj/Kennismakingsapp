import streamlit as st
from src.kennismakingsapp.utils.styles import load_css
from src.kennismakingsapp.pages.aboutme_ui import aboutme_page
from src.kennismakingsapp.pages.document_ui import document_page
from src.kennismakingsapp.pages.chat_ui import chat_page

st.set_page_config(page_title="Kennismakingsapp", page_icon="📄", layout="wide")

load_css()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Chat with AI", "Upload Documents", "About Me"])

if page == "Chat with AI":
    chat_page()

elif page == "Upload Documents":
    document_page()

elif page == "About Me":
    aboutme_page()