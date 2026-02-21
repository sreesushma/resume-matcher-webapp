# AI Resume Matcher — NLP Web Application

A deployed machine learning web application that analyzes the similarity between a resume and a job description using Natural Language Processing (NLP).

The system extracts meaningful terms, computes semantic similarity, and provides a match score along with matched and missing skills.

🔗 Live Application: https://resume-matcher-webapp.onrender.com

---

## Problem

Recruiters manually screen resumes by comparing them with job descriptions. This process is time-consuming, inconsistent, and difficult to scale.

There is a need for an automated system that:
- Evaluates resume relevance objectively
- Identifies missing skill gaps
- Provides fast and interpretable matching results

---

## Solution

This project implements an end-to-end NLP pipeline that:

1. Accepts resume text or PDF input
2. Processes and cleans textual content
3. Extracts important technical terms
4. Computes similarity between resume and job description
5. Displays a match score with insights

The application is deployed as a web interface accessible through a browser.

---

## Key Features

✔ Resume text input or PDF upload  
✔ Automated text preprocessing pipeline  
✔ TF-IDF vectorization for feature extraction  
✔ Cosine similarity scoring  
✔ Matched vs Missing terms analysis  
✔ Interactive web UI  
✔ Cloud deployment

---

## Machine Learning Pipeline

### 1. Text Preprocessing
- Lowercasing
- Stopword removal
- Tokenization
- Noise filtering

### 2. Feature Extraction
TF-IDF vectorization converts textual content into numerical representations that capture term importance across documents.

### 3. Similarity Computation
Cosine similarity measures semantic closeness between resume and job description vectors.

### 4. Insight Generation
The system identifies:
- Matched terms
- Missing terms
- Overall compatibility score

---

## System Architecture

User (Browser)
        │
        ▼
Frontend Interface (HTML / CSS)
        │
        ▼
Flask Web Server (Python)
        │
        ▼
NLP Processing Pipeline
  • Text Cleaning
  • Tokenization
  • Stopword Removal
        │
        ▼
Feature Extraction
  • TF-IDF Vectorization
        │
        ▼
Similarity Engine
  • Cosine Similarity
        │
        ▼
Results Generation
  • Match Score
  • Matched Skills
  • Missing Skills
        │
        ▼
Response Rendered to User

The system is deployed as a live web application and processes user input in real time.

---

## Technology Stack

**Programming Language**
- Python

**Libraries**
- Scikit-learn
- Pandas
- NumPy
- Flask

**NLP Techniques**
- TF-IDF Vectorization
- Cosine Similarity
- Text Normalization

**Deployment**
- Cloud Web Hosting

---

## How to Run Locally

### 1. Clone Repository
git clone https://github.com/your-username/your-repo-name.git

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run Application
python app.py

### 4. Open in Browser
http://localhost:5000

---

## Future Improvements

- Skill ontology for better term filtering
- Semantic embeddings (BERT-based similarity)
- Resume feedback suggestions
- Job role classification
- API endpoint for integration
- Authentication and user history

---

## Author

Sree Sushma Damineni  
M.S. Computer Science — Machine Learning Focus  
Kansas City, Missouri
