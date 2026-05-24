import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_text):
    jobs = pd.read_csv("jobs.csv")

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(jobs['skills'].tolist() + [resume_text])

    similarity = cosine_similarity(matrix[-1], matrix[:-1])

    jobs['match'] = similarity[0]

    return jobs.sort_values(by='match', ascending=False).head(5)