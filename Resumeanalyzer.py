#!/usr/bin/env python
import fitz
import openai
import os
import sys
from openai import OpenAI
from docx import Document

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv()) # read local .env file
arg1 = sys.argv[1] if len(sys.argv) > 1 else None
arg2 = sys.argv[2] if len(sys.argv) > 1 else None
#openai.api_key  = os.getenv('OPENAI_API_KEY')
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    client = OpenAI(
    # This is the default and can be omitted
   # api_key="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",
    #api_key="asst_YVUfpklQwrhacAapICHIVeoY"
    api_key="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"
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    raw_input= response.choices[0].message
    return raw_input.content
print("Analyzing "+ arg1 +" log file")
#lamp_review =arg1

#prompt = f"Score provided resume on provided {jd_content} file and :\n{log_content}\nScore the resume and also overall score give sepreatly to upload excel."

# Function to read log file content
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        log_content = file.read()
    return log_content

def docx_to_string(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


def pdf_to_string(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    num_pages = pdf_document.page_count
    for page_num in range(num_pages):
        page = pdf_document[page_num]
        text += page.get_text()
    pdf_document.close()
    return text

def is_pdf_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.pdf'

# Example log file path
log_file_path = arg1
jd_file = arg2
# Reading log file content
jd_content = read_log_file(jd_file)

if is_pdf_file(log_file_path):
    log_content = pdf_to_string(log_file_path)
else:
    log_content = docx_to_string(log_file_path)

prompt = f"Score provided resume on provided Job decription {jd_content}  and : please check given resume \n{log_content}\n Score the resume and also overall score outof 10 give sepreatly to upload excel."
response = get_completion(prompt)
print(response)
