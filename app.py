from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.job_recommender import recommend_jobs
import pickle
import os


app = Flask(__name__)

# Load trained models
tfidf = pickle.load(open(os.path.join('model', 'tfidf.pkl'), 'rb'))
job_model = pickle.load(open(os.path.join('model', 'job_model.pkl'), 'rb'))

@app.route("/", methods=["GET", "POST"])
def index():
    raw_text = ""
    cleaned_text = ""
    skills = []
    job_recommendations = []

    if request.method == "POST":
        uploaded_file = request.files["resume"]

        if uploaded_file.filename != "":
            raw_text = extract_text_from_pdf(uploaded_file)
            cleaned_text = clean_text(raw_text)
            skills = extract_skills(cleaned_text)
            resume_vector = tfidf.transform([cleaned_text])
            predicted_role = job_model.predict(resume_vector)[0]
            job_recommendations = recommend_jobs(resume_vector, tfidf)

    return render_template(
        "index.html",
        raw_text=raw_text,
        cleaned_text=cleaned_text,
        skills=skills,
        job_recommendations=job_recommendations
    )

if __name__ == "__main__":
    app.run()

