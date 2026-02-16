# AI Resume ↔ Job Description Matcher

An interactive NLP application that evaluates how well a resume aligns with a job description using TF-IDF vectorization and cosine similarity.

## Features
- Computes semantic similarity score
- Identifies overlapping high-importance terms
- Highlights missing terms from job description
- Web-based interface using Flask
- Clean, interpretable NLP pipeline

## Tech Stack
Python, Flask, scikit-learn, NLP, HTML/CSS

## How It Works
1. Text preprocessing and normalization
2. TF-IDF feature extraction
3. Cosine similarity computation
4. Term importance comparison

## Future Improvements
- PDF/DOC resume upload
- Semantic embeddings using transformers
- Skill ontology mapping
- Cloud deployment

## Run Locally
pip install -r requirements.txt
python app.py
