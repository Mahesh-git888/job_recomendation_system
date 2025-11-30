# AI-Powered Job Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![FAISS](https://img.shields.io/badge/FAISS-Search-green)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-orange)

An intelligent job recommendation engine that leverages Natural Language Processing (NLP) and Semantic Search to bridge the gap between candidates and their ideal roles. By analyzing the content of resumes, this system suggests the most relevant job positions based on extracted skills and experience.

## Features

* **PDF Resume Support:** Upload your resume in PDF format for instant analysis.
* **AI-Driven Matching:** Utilizes SentenceTransformer to create deep semantic embeddings of resumes and job descriptions.
* **High-Speed Search:** Powered by FAISS (Facebook AI Similarity Search) for efficient similarity retrieval.
* **Smart Filtering:** Implements TF-IDF pre-filtering to narrow down the search space to the most relevant candidates before semantic matching.
* **Interactive UI:** A clean, user-friendly web interface built with Streamlit.

---

## Tech Stack

* **Language:** Python
* **Interface:** Streamlit
* **Vector Search:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** Sentence Transformers (Hugging Face)
* **PDF Processing:** PyMuPDF
* **Text Analysis:** scikit-learn (TF-IDF)

---

## Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YomnaWaleed/job-recommendation-system-ai.git](https://github.com/YomnaWaleed/job-recommendation-system-ai.git)
cd job-recommendation-system-ai

2. Install Dependencies
Ensure you have Python installed, then run:

Bash

pip install -r requirements.txt
3. Run the Application
Launch the Streamlit interface:

Bash

streamlit run streamlit.py
4. Access the Interface
Open your browser and navigate to the local URL provided in the terminal (usually http://localhost:8501).

How It Works
Resume Parsing: The user uploads a PDF resume. PyMuPDF extracts the raw text.

TF-IDF Filtering: To improve performance, scikit-learn uses TF-IDF to filter out irrelevant job descriptions, reducing the dataset to a manageable size.

Semantic Embedding: The SentenceTransformer model converts both the resume text and the filtered job descriptions into high-dimensional vector embeddings.

Vector Search: FAISS calculates the similarity distance between the resume vector and job vectors to find the closest semantic matches.

Recommendation: The top-ranked jobs are displayed to the user.

Dataset
The system relies on a dataset of job listings.

File Name: JobsFE.csv

Content: Job descriptions, required skills, and role details.

Note: Ensure this file is located in the root directory of the project for the application to function correctly.

Roadmap & Future Improvements
[ ] Support for additional resume formats (DOCX, TXT).

[ ] Advanced filtering options (Location, Salary range, Experience level).

[ ] Integration with live LinkedIn job postings.

[ ] User feedback loop to improve recommendation accuracy over time.