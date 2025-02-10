import os
import streamlit as st
import pdfplumber
import pandas as pd
from markitdown import MarkItDown

DATA_FOLDER = "src/kennismakingsapp/data/"
FILE_PREFIX = "joren_info"

md_converter = MarkItDown()

def convert_to_text(file_path):
    """Uses MarkItDown to extract text from various file types."""
    try:
        result = md_converter.convert(file_path)
        return result.text_content.strip() if result.text_content else "No readable content found."
    except Exception as e:
        st.error(f"Error processing file {file_path}: {e}")
        return "Error reading file."

def save_uploaded_file(uploaded_file):
    """Saves uploaded file temporarily for processing."""
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def load_joren_documents():
    """Loads Joren's documents from the data folder and extracts knowledge."""
    knowledge_text = ""

    file_extensions = ["txt", "docx", "md", "pdf", "xlsx", "csv", "json", "xml"]
    
    for ext in file_extensions:
        file_path = os.path.join(DATA_FOLDER, f"{FILE_PREFIX}.{ext}")
        if os.path.exists(file_path):
            file_content = convert_to_text(file_path)
            knowledge_text += file_content + "\n"

    return knowledge_text
