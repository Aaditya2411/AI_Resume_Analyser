import streamlit as st
from chatbot import get_response
from resume_parser import extract_text
from job_match import recommend_jobs

st.set_page_config(page_title="AI Resume Analyzer")

st.title(" AI Resume Analyzer & Chatbot")

# Chatbot Section
st.header("Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = get_response(user_input)
    st.success(response)

# Resume Upload
st.header("Upload Resume")

uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Text")
    st.write(resume_text[:1000])

    st.subheader("Recommended Jobs")

    jobs = recommend_jobs(resume_text)

    st.dataframe(
    jobs[['job_title', 'company', 'salary', 'match']]
)