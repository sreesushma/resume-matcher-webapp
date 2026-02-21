# AI Resume Matcher — NLP Web Application

An end-to-end deployed NLP system that helps job seekers evaluate resume relevance and identify skill gaps instantly using Natural Language Processing (NLP).

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
User Browser
↓
Frontend (HTML/CSS)
↓
Flask Web Server
↓
NLP Processing Pipeline
↓
TF-IDF Feature Extraction
↓
Cosine Similarity Engine
↓
Match Score + Skill Insights

<pre>
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
</pre>

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
- Render Cloud Platform

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
## Application Preview

### Home Interface
Upload or paste resume and job description to analyze compatibility.

<img width="1631" height="1005" alt="Resume Matcher UI" src="https://github.com/user-attachments/assets/4d1ecd3a-a062-4fb5-a6f6-7cf876b6aa31" />

---

### Analysis Results
System displays match score, matched terms, and missing keywords.

<img width="1703" height="1000" alt="Match Results" src="https://github.com/user-attachments/assets/c8659b58-2014-4f01-8114-9ef4773c200e" />

## What This Project Demonstrates

✔ Designing and deploying an end-to-end ML system  
✔ Transforming raw text into actionable insights  
✔ Building user-facing AI applications  
✔ Applying NLP techniques to real-world workflows  
✔ Bridging machine learning with product usability
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
Portfolio: https://sreesushma.github.io/ai-portfolio-sree/
LinkedIn: https://www.linkedin.com/in/sree-sushma-damineni
