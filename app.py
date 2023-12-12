import streamlit as st
import os
import json
import fitz  # PyMuPDF
import mimetypes
import docx
from PyPDF2 import PdfReader
from prompt_engineering import engineering_prompt
import openai

import requests

# need to run pip install transformers==4.20  

def process_pdf_to_str(file_path):
    """ Convert pdf input to string """
    with open(file_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            pdf_text = ""
            # Iterate through all pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()
    return pdf_text

def process_docs_to_str(file_path):
    """ Convert docs inputs to string """
    doc = docx.Document(file_path)
    doc_text = ""
    for paragraph in doc.paragraphs:
        doc_text += paragraph.text + "\n"
    return doc_text

# Function to process the uploaded file and convert it to JSON
def process_file_to_str(uploaded_file):
    """ Takes in the uploaded file and returns a string """
    temp_dir = 'tempDir'
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getvalue())

    # Detect file type and decode accordingly
    file_extension = uploaded_file.name.split('.')[-1].lower()

    found_text = ""

    if file_extension == 'pdf':
    # Read the contents of the PDF file
        found_text=process_pdf_to_str(file_path)

    elif file_extension == 'docx':
        # Read the contents of the DOCX file
        found_text=process_docs_to_str(file_path)

    elif file_extension == 'txt':
        # Read the contents of the TXT file
        with open(file_path, 'r', encoding='utf-8') as f:
            txt_text = f.read()
        found_text=txt_text

    elif file_extension == 'json':
        # Read the contents of the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            found_text=json.dumps(json_data)
    else:
        st.warning(f"Unsupported file type: {file_extension}")

    return found_text


def parse_text_to_json(text):
    return json.dumps(text)

# Title of the application
st.title('Perfect Resume Generator')

st.markdown("""
Welcome to PRG! Drop your previous CV below, select one of the templates, and let the LLMs generate your resume for you
""")

# File uploader allows user to add their own document
uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt', 'json'])

job_description = ""

job_description_area = st.text_area(label="Job Description", height=200)

if st.button("Submit Job Description"):
    job_description = job_description_area.strip()

    if job_description:
        st.write("Job Description saved successfully!")
    else:
        st.write("Please fill in the section before submitting.")

# Sections
sections = ["Education", "Skills", "Professional Experience", "Projects"]

# Select option
selected_section = st.selectbox("Choose an option:", sections)

# Display selected option
st.write(f"You selected: {selected_section}")

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    resume_section = process_file_to_str(uploaded_file)

    # Assuming there is a function to process the uploaded file and generate resume
    # processed_file = process_file(uploaded_file)
    # st.download_button(label="Download Resume", data=processed_file, file_name="resume.pdf", mime='application/octet-stream')

    # For demonstration, we simply display the file name and details
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size)

    # If you want to use the uploaded file in other parts of the app, you might want to save it temporarily
    # Save the uploaded file locally for further processing
    # with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
    #     f.write(uploaded_file.getbuffer())

    # st.success("File Saved")

# # Check if OpenAI API key is set as an environment variable
# if "OPENAI_API_KEY" not in os.environ:
#     # Display a message and input field for user to enter their key
#     st.info("OpenAI API key not found. Please enter your key:")
#     api_key = st.text_input("OpenAI API Key:")

#     # Check if the user submitted a key
#     if api_key:
#         # Set the environment variable with the provided key
#         os.environ["OPENAI_API_KEY"] = api_key
#         st.success("OpenAI API key set.")
#     else:
#         # Stop execution if no key is provided
#         st.error("Please enter a valid OpenAI API key.")
#         st.stop()

# openai.api_key = os.environ["OPENAI_API_KEY"]

# Sidebar for navigation or additional settings
with st.sidebar:
    st.header("Main")
    # Add your navigation or control elements here, like:
    # - Render JSON Resume
    # - Edit LaTeX on Overleaf
    # - FAQ
    # - Template Gallery

    # When clicked will generate new resume section
    if st.button('Render JSON Resume'):
        job_description = job_description_area.strip()
        prompt = engineering_prompt(resume_section, job_description, selected_section)
        print("Prompt: "+ prompt)

        # Function to generate resume section
        # def generate_resume_section(prompt):
        #     response = openai.Completion.create(
        #         model="gpt-3.5-turbo",
        #         prompt=prompt,
        #         temperature=0.4, # higher values like 0.8 make the output mode random, range 0-2
        #     )
        #     return response["choices"][0]["text"]
        
        # answer = generate_resume_section(prompt)
        # st.write("This is the generated resume section: "+ answer)
        
        


# ... more app logic ...

# Remember to handle the case where the uploaded file needs to be processed
# and interacted with (e.g., rendering a JSON resume or editing in Overleaf)
