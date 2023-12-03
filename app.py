import streamlit as st
import os
import json
import fitz  # PyMuPDF
import mimetypes
from docx import Document

# Title of the application
st.title('Perfect Resume Generator')

st.markdown("""
Welcome to PRG! Drop your previous CV below, select one of the templates, and let the LLMs generate your resume for you
""")

# File uploader allows user to add their own document
uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt', 'json'])

options = ["Education", "Skills", "Professional Experience", "Projects"]
# Create a dropdown to select an option
selected_option = st.selectbox("Choose an option:", options)

# Display the selected option
st.write(f"You selected: {selected_option}")


if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = 'tempDir'
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getvalue())

    # Read file as string
    try:
        raw_text = uploaded_file.getvalue().decode('utf-8')  # Specify the appropriate encoding

        # Convert raw text to JSON
        try:
            json_data = json.loads(raw_text)

            # Display the JSON data
            st.subheader("JSON Data from Uploaded File:")
            st.json(json_data)

            # Display the selected content based on the chosen option
            if selected_option in json_data:
                st.subheader(f"{selected_option} Information:")
                st.write(json_data[selected_option])

            else:
                st.warning(f"No information found for the selected option: {selected_option}")

        except json.JSONDecodeError:
            st.error("Error: Unable to parse the uploaded file as JSON.")

    except UnicodeDecodeError:
        st.error("Error: Unable to decode the uploaded file. Specify the correct encoding.")

    st.success(f"File uploaded and processed successfully: {file_path}")
    
    # Assuming there is a function to process the uploaded file and generate resume
    # processed_file = process_file(uploaded_file)
    # st.download_button(label="Download Resume", data=processed_file, file_name="resume.pdf", mime='application/octet-stream')

    # For demonstration, we simply display the file name and details
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size)

    # If you want to use the uploaded file in other parts of the app, you might want to save it temporarily
    # Save the uploaded file locally for further processing
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File Saved")

# Function to process the uploaded file and convert it to JSON
def process_file_to_json(uploaded_file, file_type):
        # Process according to file type
    if file_type == "txt" or file_type == "json":
        # Directly read the text content of the file
        text = uploaded_file.read().decode('utf-8')
        structured_data = parse_text_to_json(text)

    elif file_type == "pdf":
        # Open the PDF file
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        structured_data = parse_text_to_json(text)

    elif file_type == "docx":
        # Load the DOCX content
        doc = Document(uploaded_file)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        structured_data = parse_text_to_json(text)

    else:
        raise ValueError("Unsupported file type")

    return structured_data


# Placeholder function for parsing text to JSON
def parse_text_to_json(text):
    # Implement text parsing logic here
    # This is just a placeholder function that returns the text as a JSON object
    return {"content": text}

# Sidebar for navigation or additional settings
with st.sidebar:
    st.header("Main")
    # Add your navigation or control elements here, like:
    # - Render JSON Resume
    # - Edit LaTeX on Overleaf
    # - FAQ
    # - Template Gallery

    # For demonstration, just a simple button
    if st.button('Render JSON Resume'):
        st.sidebar.write("Render JSON Resume clicked")

# ... more app logic ...

# Remember to handle the case where the uploaded file needs to be processed
# and interacted with (e.g., rendering a JSON resume or editing in Overleaf)
