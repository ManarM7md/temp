import streamlit as st
from unstructured.partition.pdf import partition_pdf

def main():
    st.title("PDF Text and Table Extractor")

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        output_path = "/tmp/"
        file_path = output_path + uploaded_file.name

        # Write the uploaded file to disk
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the PDF
        chunks = partition_pdf(
            filename=file_path,
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

        # Separate tables and texts
        tables = []
        texts = []

        for chunk in chunks:
            if "Table" in str(type(chunk)):
                tables.append(chunk)

            if "CompositeElement" in str(type(chunk)):
                texts.append(chunk)

        # Display extracted texts
        st.subheader("Extracted Texts")
        for text in texts:
            st.write(str(text))

        # Display extracted tables
        st.subheader("Extracted Tables")
        for table in tables:
            st.write(str(table))

if __name__ == "__main__":
    main()
