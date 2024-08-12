import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import os

st.set_page_config(page_title="Financial Report Extraction", layout="wide")
# Load the image for the circular display
image_path = "app/assets/images/86480339.jpeg"
image = Image.open(image_path)

# Load the LinkedIn and GitHub icons
linkedin_icon_path = "app/assets/icons/linkedin.png"
github_icon_path = "app/assets/icons/github.png"
resume_icon_path = "app/assets/icons/approved.png"

# Function to load images with error handling
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Image not found: {image_path}")
        return None

linkedin_icon = load_image(linkedin_icon_path)
github_icon = load_image(github_icon_path)
resume_icon = load_image(resume_icon_path)

# Convert images to base64 for inline display
def image_to_base64(image):
    if image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

linkedin_icon_base64 = image_to_base64(linkedin_icon)
github_icon_base64 = image_to_base64(github_icon)
resume_icon_base64 = image_to_base64(resume_icon)

# Display the image in a circular shape using CSS
st.markdown("""
    <style>
    .circle-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        margin: 20px auto;
    }
    .circle-image img {
        width: 100%;
        height: auto;
        object-fit: cover;
    }
    .sidebar-text {
        text-align: left;
        margin-bottom: 10px;
    }
    .sidebar-link {
        text-align: center;
        margin-bottom: 10px;
    }
    .sidebar-section-title {
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .social-icons img {
        width: 24px;
        height: 24px;
        margin: 0 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Convert the image to base64 for inline display
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display the circular image in the sidebar
with st.sidebar:
    st.markdown(f'<div class="circle-image"><img src="data:image/jpeg;base64,{img_str}"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Harshal Honde</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Contact Information:</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">HarshalHonde50@gmail.com</div>', unsafe_allow_html=True)
    if linkedin_icon_base64 and github_icon_base64:
        st.markdown(f"""
            <div class="social-icons" style="text-align: center;">
                <a href="https://www.linkedin.com/in/harshal-honde268/">
                    <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn">
                </a>
                <a href="https://github.com/Harry262000">
                    <img src="data:image/png;base64,{github_icon_base64}" alt="GitHub">
                </a>
                <a href="/assets/Resume/Harshal_Honde_Intern.pdf">
                    <img src="data:image/png;base64,{resume_icon_base64}" alt="Resume">
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .sidebar-list {
        list-style-type: disc; /* Adds bullet points */
        padding-left: 20px; /* Adjust the indentation */
    }
    .sidebar-text {
        margin-bottom: 5px; /* Space between list items */
    }
    </style>
    <div class="sidebar-section-title">Skills</div>
    <ul class="sidebar-list">
        <li class="sidebar-text">Python</li>
        <li class="sidebar-text">Machine Learning</li>
        <li class="sidebar-text">NLP</li>
        <li class="sidebar-text">Text Extraction</li>
        <li class="sidebar-text">Unstructured Data Handling</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Hobbies and Interests</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Reading</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Traveling</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Gaming</div>', unsafe_allow_html=True)

# Title of the app
st.title("Interactive PDF Analysis and Extraction Tool")

# Instructions
st.write("""
## Instructions
This application allows you to upload a PDF document, automatically extract its text and tables, and interactively query the extracted data.

### Features:
- **Upload a PDF:** Select and upload a PDF file (up to 50 MB).
- **Text Extraction:** View the raw text extracted from the PDF.
- **Table Extraction:** See tables extracted from the PDF displayed in a readable format.
- **Interactive Chat:** Ask questions about the extracted data (functionality to be improved in future versions).

### Upload Guidelines:
- The application is designed to handle annual reports and similar documents. Performance may vary with other types of PDFs.
- The maximum file size allowed is 5 MB.
""")
