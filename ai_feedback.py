from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("API Key:", api_key)
def analyze_resume(resume_text):
    prompt = f"""
You are an ATS Resume Expert.

Analyze this resume and provide:

1. ATS Score out of 100
2. Strengths
3. Missing Skills
4. Grammar Suggestions
5. Resume Improvement Tips

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content