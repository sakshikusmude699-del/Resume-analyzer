import streamlit as st
import pickle

from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.job_recommender import recommend_jobs

# Load models
with open("model/job_model.pkl", "rb") as f:
    job_model = pickle.load(f)

with open("model/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer & Job Recommendation System")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(raw_text)
    skills = extract_skills(cleaned_text)

    resume_vector = tfidf.transform([cleaned_text])
    predicted_role = job_model.predict(resume_vector)[0]

    st.subheader("Predicted Job Role")
    st.success(predicted_role)

    st.subheader("Extracted Skills")
    st.write(", ".join(skills))

    st.subheader("Recommended Jobs")
    jobs = recommend_jobs(resume_vector, tfidf)
    for job in jobs:
        st.write(f"**{job['job_role']}** — {round(job['similarity']*100,2)}% match")
