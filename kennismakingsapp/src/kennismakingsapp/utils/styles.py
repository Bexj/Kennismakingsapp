import streamlit as st

def load_css():
    """Loads custom CSS from the `styles.css` file."""
    with open("src/kennismakingsapp/styles/styles.css") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
