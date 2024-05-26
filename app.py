import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore
import os
import PyPDF2 as pdf # type: ignore
from dotenv import load_dotenv # type: ignore
import json
from cachetools import cached, TTLCache # type: ignore

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a cache with a time-to-live (TTL) of 300 seconds (5 minutes)
cache = TTLCache(maxsize=128, ttl=300)

@cached(cache)
def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
    
        
        # Parse the response JSON
        response_json = json.loads(response)
        
        # Extracting JD Match, Missing Keywords, and Profile Summary
        jd_match = response_json.get("JD Match", "N/A")
        missing_keywords = response_json.get("MissingKeywords", [])
        profile_summary = response_json.get("Profile Summary", "")
        
        # Format the response string
        final_response = f"**JD Match:** {jd_match}\n\n**Missing Keywords:**\n\n"
        for keyword in missing_keywords:
            final_response += f"- {keyword}\n"
        final_response += f"\n**Profile Summary:**\n\n{profile_summary}"
        
        st.subheader(final_response)
