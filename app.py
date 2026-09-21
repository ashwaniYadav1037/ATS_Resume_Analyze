from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq

groq_api_key = os.environ.get("GROQ_API_KEY") 

def get_groq_response(input, pdf_content, prompt):
    model = ChatGroq(
        model="qwen/qwen3.8-27b",
        api_key=groq_api_key,
        temperature=0
    )

    final_prompt = f"""
You are an expert ATS Resume Analyzer.

JOB DESCRIPTION

{input}

RESUME

{pdf_content}

INSTRUCTION

{prompt}

Analyze the resume against the job description.

Do not invent information.

Only use information present in the resume and job description.

Give clear, structured and actionable results.

"""

    response = model.invoke(final_prompt)
   
    return response.content
   


def input_pdf_setup(uploaded_file):

    if uploaded_file is not None:

        reader = pdf.PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
Analyze this resume against the provided job description.

Provide:

### Resume Summary
Summarize the candidate's profile.

### Relevant Experience
Identify experience relevant to the job.

### Matching Skills
List skills from the resume that match the JD.

### Experience Match
Explain how the candidate's experience relates to the position.

### Project Match
Identify relevant projects.

### Education Match
Compare education requirements.

### Strengths
List the strongest aspects of the resume for this job.

### Weaknesses
Identify areas that may reduce ATS compatibility.

### Final Assessment
Give an actionable assessment.
"""

input_prompt2 = """
Analyze the resume against the job description.

Identify the skills the candidate should develop to become
a stronger candidate for this specific position.

Separate the results into:

### Already Have
Skills already demonstrated in the resume.

### Partially Demonstrated
Skills that appear indirectly or with limited evidence.

### Missing Skills
Important skills from the job description that are not
demonstrated in the resume.

### Recommended Learning
For each missing skill, explain what the candidate should learn.

### Priority
Classify each missing skill as:

High
Medium
Low

Do not recommend skills that are unrelated to the job description.
"""

input_prompt3 = """
Evaluate the resume against the job description.

Calculate an approximate ATS compatibility score.

Consider:

1. Required technical skills
2. Preferred technical skills
3. Work experience
4. Education
5. Projects
6. Responsibilities
7. Keywords
8. Domain knowledge

Return:

### ATS MATCH
XX%

### SKILL MATCH
XX%

### EXPERIENCE MATCH
XX%

### EDUCATION MATCH
XX%

### KEYWORD MATCH
XX%

### MATCHING KEYWORDS
- keyword
- keyword
- keyword

### MISSING KEYWORDS
- keyword
- keyword
- keyword

### FINAL ASSESSMENT
Explain the major reasons for the score.

Do not claim that this is an actual score produced by a company's
proprietary ATS. It is an estimated compatibility score based
on the supplied resume and job description.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_groq_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
        
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_groq_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")        

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_groq_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   
