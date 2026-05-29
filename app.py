import streamlit as st
from utils import extract_text_from_pdf, match_resumes

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("🧠 AI Resume Screener")

job_desc = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Candidates"):

    if not job_desc:
        st.warning("Please enter job description")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume")
        st.stop()

    resumes_text = []
    names = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)

        if not text:
            st.warning(f"{file.name} is empty or unreadable")
            continue

        resumes_text.append(text)
        names.append(file.name)

    results = match_resumes(job_desc, resumes_text)

    combined = list(zip(names, results))
    combined.sort(key=lambda x: x[1]["final"], reverse=True)

    st.subheader("🏆 ATS Ranking Results")

    for rank, (name, res) in enumerate(combined, start=1):

        st.markdown(f"### #{rank} {name}")

        st.progress(float(res["final"]))

        st.write(f"⭐ Final Score: {round(res['final'] * 100, 2)}%")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Skills", f"{round(res['skills'] * 100, 2)}%")

        with col2:
            st.metric("Experience", f"{round(res['experience'] * 100, 2)}%")

        with col3:
            st.metric("Education", f"{round(res['education'] * 100, 2)}%")

        st.divider()