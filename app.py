import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader
st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg, #f5f7fa, #c3cfe2);
}
h1 {
    color: #1f2937;
    text-align: center;
}

.stButton>button {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    border-radius:25px;
    height:50px;
    width:220px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)
st.markdown(
"""
<h1>🚀 AI Resume Analyzer</h1>
<p style='text-align:center; font-size:20px; color:#374151;'>
AI-powered resume review & career improvement assistant
</p>
""",
unsafe_allow_html=True
)
load_dotenv(dotenv_path=".env", override=True)

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def analyze_resume(resume_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                 "role": "user",
                "content": f"""
You are an expert HR recruiter and resume reviewer.

Analyze the following resume and provide a detailed report.

Resume:
{resume_text}

Give output in this format:

1. Resume Score (out of 100)

2. Summary

3. Key Skills Found

4. Technical Skills Missing

5. Strengths

6. Weaknesses

7. ATS Compatibility Score

8. Recommended Improvements

9. Suitable Job Roles

10. Final Verdict
"""
            }
        ]
    )

    return response.choices[0].message.content

st.markdown(
"""
<div style="
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
">
<h2>📄 Upload Resume</h2>
<p>Upload your PDF resume and get AI feedback instantly.</p>
</div>
""",
unsafe_allow_html=True
)


uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    if st.button("Analyze Resume"):

        with st.spinner("🤖 AI is analyzing your resume..."):
            result = analyze_resume(resume_text)

        st.markdown(
        """
        <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.1);
        ">
        <h2>📊 Resume Analysis Report</h2>
        </div>
        """,
        unsafe_allow_html=True
        )

        st.write(result)