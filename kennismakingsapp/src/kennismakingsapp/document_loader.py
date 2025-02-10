import streamlit as st
import pdfplumber
import pypandoc
import pandas as pd
from docx import Document
from pydub import AudioSegment

def process_uploaded_file(uploaded_file):
    file_type = uploaded_file.type
    text = ""

    if file_type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    elif file_type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif file_type == "audio/mpeg":
        audio = AudioSegment.from_file(uploaded_file)
        text = "[Audio file uploaded]"  # Add transcription logic later
    elif file_type == "application/vnd.ms-excel" or file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        text = df.to_string()

    return text
