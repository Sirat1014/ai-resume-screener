# 🤖 AI Resume Screener & Matcher

An intelligent Applicant Tracking System (ATS) tool built using Python and Streamlit that helps recruiters screen and rank multiple candidate resumes against a Job Description using Natural Language Processing (NLP).

---

## ✨ Features
- 📄 **PDF Text Extraction:** Extracts text from multiple PDF resumes simultaneously using `PyPDF2` and Regular Expressions (`re`).
- 🎯 **Smart NLP Vectorization:** Converts text data into numerical format using `scikit-learn`'s **TF-IDF Vectorizer** (filtering out English stop-words).
- 📊 **Cosine Similarity Ranking:** Computes the mathematical match percentage between the Job Description and each resume.
- 🎨 **Interactive Dashboard:** A clean, user-friendly UI built with Streamlit to display real-time match percentages, scores, and progress bars.

---

## 🛠️ Tech Stack Used
* **Frontend:** Streamlit
* **NLP / Machine Learning:** Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity)
* **File Parsing & Cleaning:** PyPDF2, Re (Regular Expressions)
* **Language:** Python 3.10+

---

## 🚀 How to Run Locally

1. **Clone the repository or download the files:**
   ```bash
   git clone [https://github.com/Sirat1014/ai-resume-screener.git](https://github.com/Sirat1014/ai-resume-screener.git)
