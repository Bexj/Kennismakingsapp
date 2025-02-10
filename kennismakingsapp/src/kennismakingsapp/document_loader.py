import pypandoc
import pdfplumber
import pandas as pd
import os
import streamlit as st

DATA_FOLDER = "src/kennismakingsapp/data/"
FILE_PREFIX = "joren_info"

def convert_to_text(file_path, file_type):
    """Uses Pandoc for DOCX, MD, TXT (as markdown). Uses pdfplumber for PDFs and pandas for Excel."""
    
    # Map file type to Pandoc's expected format
    pandoc_formats = {
        "text/plain": "markdown",  # Pandoc can handle TXT as Markdown
        "text/markdown": "markdown",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx"
    }

    if file_type == "application/pdf":
        return extract_text_from_pdf(file_path) 

    if file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return extract_text_from_excel(file_path)  # Handle Excel separately

    input_format = pandoc_formats.get(file_type)
    if not input_format:
        st.error(f"Unsupported file format: {file_type}")
        return None

    try:
        text = pypandoc.convert_file(file_path, "plain", format=input_format)
        return text
    except Exception as e:
        st.error(f"Error processing file {file_path}: {e}")
        return None

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text.strip()

def extract_text_from_excel(file_path):
    """Extracts text from an Excel (.xlsx) file using pandas."""
    try:
        df = pd.read_excel(file_path, sheet_name=None)  # Read all sheets
        extracted_text = ""
        for sheet_name, sheet in df.items():
            extracted_text += f"\n--- {sheet_name} ---\n"
            extracted_text += sheet.to_string(index=False)  # Convert data to text
        return extracted_text
    except Exception as e:
        st.error(f"Error processing Excel file {file_path}: {e}")
        return None

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

    file_types = {
        "txt": "text/plain",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "md": "text/markdown",
        "pdf": "application/pdf",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    }

    for ext, file_type in file_types.items():
        file_path = os.path.join(DATA_FOLDER, f"{FILE_PREFIX}.{ext}")
        if os.path.exists(file_path):
            if ext == "pdf":
                knowledge_text += extract_text_from_pdf(file_path) + "\n"
            elif ext == "xlsx":
                knowledge_text += extract_text_from_excel(file_path) + "\n"
            else:
                knowledge_text += convert_to_text(file_path, file_type) + "\n"

    return knowledge_text
