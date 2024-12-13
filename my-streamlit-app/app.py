import streamlit as st
from unstructured.partition.pdf import partition_pdf

def process_pdf(file):
    chunks = partition_pdf(
        filename=file,
        infer_table_structure=True,
        strategy="hi_res",
        languages=['eng', 'ara'],
        extract_image_block_types=["Image"],
        extract_image_block_to_payload=True,
        chunking_strategy="by_title",
        max_characters=10000,
        combine_text_under_n_chars=2000,
        new_after_n_chars=6000,
    )

    tables = []
    texts = []

    for chunk in chunks:
        if "Table" in str(type(chunk)):
            tables.append(chunk)
        if "CompositeElement" in str(type(chunk)):
            texts.append(chunk)

    return texts, tables

st.title("PDF Text and Table Extractor")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with open("uploaded_file.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    texts, tables = process_pdf("uploaded_file.pdf")

    st.subheader("Extracted Texts")
    for text in texts:
        st.write(text)

    st.subheader("Extracted Tables")
    for table in tables:
        st.write(table)
