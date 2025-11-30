import streamlit as st
import fitz  # PyMuPDF for PDF extraction
from model import JobRecommendationSystem

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Job Recommender",
    page_icon="tao",
    layout="wide"
)

# --- 1. LOAD MODEL WITH CACHING (Crucial for Speed) ---
@st.cache_resource
def load_model():
    # This function runs only once!
    return JobRecommendationSystem("JobsFE.csv")

try:
    with st.spinner("Loading AI Model... (This may take a moment)"):
        recommender = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# --- 2. TITLE & HEADER ---
st.title("AI-Powered Job Recommendation System")
st.markdown("Upload your resume as a **PDF**, and get **20 job recommendations** tailored to your skills.")

# --- 3. FILE UPLOADER ---
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

# --- 4. TEXT EXTRACTION FUNCTION ---
def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF resume"""
    try:
        # Read the file as bytes
        pdf_bytes = pdf_file.read() 
        # Open with PyMuPDF
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "\n".join([page.get_text("text") for page in doc])
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# --- 5. MAIN LOGIC ---
if uploaded_file:
    # Extract text immediately upon upload
    resume_text = extract_text_from_pdf(uploaded_file)
    
    if resume_text:
        st.success("Resume uploaded and processed successfully!")
        
        # Recommendation Button
        if st.button("Recommend Jobs", type="primary"):
            with st.spinner("Analyzing your resume and matching with database..."):
                try:
                    # Get recommendations
                    recommendations = recommender.recommend_jobs(resume_text, top_n=20)
                    job_results = recommendations["recommended_jobs"]

                    st.markdown("### 🎯 Recommended Jobs For You")
                    
                    # Display recommended jobs in a clean format
                    for i, job in enumerate(job_results, start=1):
                        with st.container():
                            st.subheader(f"{i}. {job['position']}")
                            col1, col2 = st.columns([1, 3])
                            
                            with col1:
                                st.write(f"**🏢 Company:**\n{job['workplace']}")
                                st.write(f"**📍 Mode:**\n{job['working_mode']}")
                            
                            with col2:
                                st.write(f"**📋 Duties:**\n{job['job_role_and_duties']}")
                                st.info(f"**💡 Skills:** {job['requisite_skill']}")
                            
                            st.divider()

                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
    else:
        st.error("Could not extract text from the PDF. Please try a different file.")