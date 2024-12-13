import streamlit as st
from unstructured.partition.pdf import partition_pdf

# Page configuration
st.set_page_config(
    page_title="LaTeX OCR with Llama 3.2 Vision",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)
