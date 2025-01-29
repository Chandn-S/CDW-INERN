import streamlit as st
import os
import tempfile
import shutil
import chain


def upload_page():
    """
    Upload page for handling file uploads (PDFs) and processing them with ChromaDB.
    """
    st.markdown(
        """
        <div style="background-color: #ff9800; padding: 20px; text-align: center; border-radius: 10px; color: white;">
            <h1 style="font-family: Arial, sans-serif;">File Upload</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"], help="Drag and drop your PDF here")
    
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            shutil.copyfileobj(uploaded_file, tmp_file)
            tmp_file_path = tmp_file.name
        
        st.success("File uploaded successfully!")
        
        if st.button("Process File", help="Extract and store data into ChromaDB"):
            with st.spinner("Processing file..."):
                response = chain.process_file(tmp_file_path)  # Ensure process_file exists in chain.py
                st.success("File processed successfully!")
                st.info(response)
                os.remove(tmp_file_path)  # Clean up temporary file after processing
