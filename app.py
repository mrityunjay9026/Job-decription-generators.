import streamlit as st
import backend
import time

# Page configuration
st.set_page_config(
    page_title="Job Description Generator",
    page_icon="💼",
    layout="wide"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .title {
        color: #1E3A8A;
        font-family: 'Arial', sans-serif;
    }
    .description {
        font-size: 18px;
        color: #333;
    }
    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='title'>📝 JOB DESCRIPTION GENERATOR</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Create professional job descriptions in seconds with AI assistance</p>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Job Details")
    
    job_title = st.text_input("Job Title*", placeholder="e.g. Software Engineer")
    
    experience = st.select_slider(
        "Experience Range (Years)*",
        options=["Entry Level", "0-1", "1-2", "2-5", "5-7", "7-10", "10+"]
    )
    
    skills = st.text_area("Required Skills*", 
                         placeholder="e.g. Python, SQL, Django, AWS",
                         height=100)
    
    department = st.text_input("Department", placeholder="e.g. Engineering")
    
    location = st.text_input("Location", placeholder="e.g. Remote, New York")
    
    additional_info = st.text_area("Additional Information",
                                  placeholder="Add any other details about the position...",
                                  height=100)

with col2:
    # Preview the JD prompt
    st.markdown("### Generated Job Description")
    
    if not job_title or not skills:
        st.info("Please fill in the required fields (*) to generate a job description")
        jd_placeholder = st.empty()
        jd_placeholder.markdown("""
        <div class="result-box">
            <h3>Job Description Preview</h3>
            <p>Your job description will appear here...</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        prompt = f"Generate a professional job description for a {job_title} position with {experience} years of experience. "
        prompt += f"Required skills: {skills}. "
        
        if department:
            prompt += f"Department: {department}. "
        if location:
            prompt += f"Location: {location}. "
        if additional_info:
            prompt += f"Additional information: {additional_info}. "
            
        prompt += "Format the job description professionally with sections for Overview, Responsibilities, Requirements, and Benefits."
        
        if st.button("Generate Job Description", key="generate"):
            with st.spinner("Generating job description..."):
                # Add artificial delay for better UX
                time.sleep(1)
                try:
                    # Call the backend function to generate JD
                    jd = backend.generate_job_description(prompt)
                    
                    # Display the result
                    st.markdown(f"""
                    <div class="result-box">
                        <h3>Job Description for {job_title}</h3>
                        {jd}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Add download button
                    st.download_button(
                        label="Download as Text",
                        data=jd,
                        file_name=f"{job_title}_job_description.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        
# Footer
st.markdown("---")
st.markdown("### How to use this tool")
st.markdown("""
1. Fill in the required job details in the form
2. Add any additional information that should be included
3. Click 'Generate Job Description'
4. Download or copy the generated content
""")