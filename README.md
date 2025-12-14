# AI-Powered Job Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![FAISS](https://img.shields.io/badge/FAISS-Search-green)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-orange)

An AI-driven job recommendation system that uses Natural Language Processing (NLP) and semantic search techniques to match resumes with relevant job opportunities. The system analyzes resume content and job descriptions to recommend roles based on contextual similarity rather than simple keyword matching.

---

## Features

- **PDF Resume Parsing:** Upload resumes in PDF format for automated text extraction.
- **Semantic Matching:** Uses SentenceTransformer models to generate semantic embeddings of resumes and job descriptions.
- **Efficient Similarity Search:** FAISS enables fast and scalable vector similarity search.
- **Search Space Reduction:** TF-IDF pre-filtering narrows down candidate jobs before semantic ranking.
- **Interactive Web Interface:** Clean and user-friendly interface built with Streamlit.

---

## Tech Stack

- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **Vector Search:** FAISS (Facebook AI Similarity Search)  
- **Embeddings:** Sentence Transformers (Hugging Face)  
- **PDF Processing:** PyMuPDF  
- **Text Processing:** scikit-learn (TF-IDF)

---

## Installation & Setup

Follow the steps below to run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Mahesh-git888/job_recomendation_system.git
cd job_recomendation_system
2. Install Dependencies

Ensure Python 3.8+ is installed, then run:

pip install -r requirements.txt

3. Run the Application

Launch the Streamlit application:

streamlit run streamlit.py

4. Access the Application

Open your browser and navigate to:

http://localhost:8501

How It Works

Resume Upload & Parsing
Users upload a PDF resume. Text is extracted using PyMuPDF.

TF-IDF Pre-Filtering
TF-IDF similarity is used to remove clearly irrelevant job descriptions, reducing the search space.

Semantic Embedding Generation
Resume text and filtered job descriptions are converted into dense vector embeddings using SentenceTransformer models.

Vector Similarity Search
FAISS performs fast similarity search to identify the most relevant job matches.

Recommendation Display
The top-ranked job recommendations are displayed in the Streamlit interface.

Dataset

File: JobsFE.csv

Description: Contains job titles, descriptions, and required skills.

Note: The dataset must be present in the root directory for the application to function correctly.

Future Enhancements

Support for additional resume formats (DOCX, TXT)

Advanced filtering options (location, salary, experience level)

Integration with live job posting APIs

User feedback loop to improve recommendation accuracy


-
