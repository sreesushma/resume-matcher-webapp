from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

def extract_keywords(text):
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    keywords = [
        w for w in words
        if w not in ENGLISH_STOP_WORDS and len(w) > 2
    ]
    return set(keywords)

def compute_match(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])

    similarity_score = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:2]
    )[0][0] * 100

    feature_names = vectorizer.get_feature_names_out()

    resume_vector = tfidf_matrix[0].toarray()[0]
    jd_vector = tfidf_matrix[1].toarray()[0]

    resume_terms = {
        feature_names[i]
        for i in resume_vector.argsort()[-20:]
        if resume_vector[i] > 0
    }

    jd_terms = {
        feature_names[i]
        for i in jd_vector.argsort()[-20:]
        if jd_vector[i] > 0
    }

    matched_skills = sorted(resume_terms.intersection(jd_terms))
    missing_skills = sorted(jd_terms - resume_terms)

    return similarity_score, matched_skills[:5], missing_skills[:5]


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    matched = []
    missing = []
    resume_text = ""
    jd_text = ""

    if request.method == "POST":
        resume_text = request.form["resume"]
        jd_text = request.form["jd"]
        score, matched, missing = compute_match(resume_text, jd_text)

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing,
        resume_text=resume_text,
        jd_text=jd_text
    )


if __name__ == "__main__":
    app.run(debug=True)
