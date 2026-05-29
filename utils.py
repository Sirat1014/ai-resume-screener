from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text.strip()

def _cosine_score(a, b):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([a, b])
    return cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()[0]


def _extract_section(text, keywords):
    text_lower = text.lower()

    for kw in keywords:
        match = re.search(rf"{kw}(.{{0,800}})", text_lower)
        if match:
            return match.group(0)

    return text_lower  # fallback


def match_resumes(job_desc, resumes_text):
    results = []

    for resume in resumes_text:

        
        job_skills = _extract_section(job_desc, ["skills", "requirements", "qualifications"])
        resume_skills = _extract_section(resume, ["skills", "technical skills"])

        skills_score = _cosine_score(job_skills, resume_skills)

        
        job_exp = _extract_section(job_desc, ["experience", "requirements"])
        resume_exp = _extract_section(resume, ["experience", "work experience"])

        experience_score = _cosine_score(job_exp, resume_exp)

       
        job_edu = _extract_section(job_desc, ["education", "qualification"])
        resume_edu = _extract_section(resume, ["education"])

        education_score = _cosine_score(job_edu, resume_edu)

       
        final_score = (
            0.5 * skills_score +
            0.3 * experience_score +
            0.2 * education_score
        )

        results.append({
            "skills": skills_score,
            "experience": experience_score,
            "education": education_score,
            "final": final_score
        })

    return results