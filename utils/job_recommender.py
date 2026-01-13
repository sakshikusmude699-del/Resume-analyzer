import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_vector, tfidf, job_file="data/job_descriptions.csv"):
    jobs = pd.read_csv(job_file)

    job_vectors = tfidf.transform(jobs["job_description"])
    similarity_scores = cosine_similarity(resume_vector, job_vectors)

    jobs["similarity"] = similarity_scores[0]
    top_jobs = jobs.sort_values(by="similarity", ascending=False).head(3)

    return top_jobs[["job_role", "similarity"]].to_dict(orient="records")
