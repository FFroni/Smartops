import streamlit as st
import time

# Page configurations - MUST be the first Streamlit instruction
st.set_page_config(
    page_title="Manual Generator",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for a modern and elegant design
st.markdown(
    """
    <style>
    /* Global style and font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main container */
    .main-container {
        background: linear-gradient(to bottom right, #ffffff, #f8f9fa);
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        margin: 1rem 0;
    }
    
    /* Main title */
    .main-header {
        color: #2E7D32;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        font-size: 2.4rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Upload area */
    .upload-container {
        border: 2px dashed #4CAF50;
        background-color: rgba(76, 175, 80, 0.05);
        padding: 2rem;
        border-radius: 12px;
        transition: all 0.3s ease;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .upload-container:hover {
        background-color: rgba(76, 175, 80, 0.1);
        transform: translateY(-2px);
    }
    
    /* Buttons */
    .stButton button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 500 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        background-color: #1B5E20 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Animation for success message */
    .success-message {
        background-color: rgba(76, 175, 80, 0.1);
        color: #2E7D32;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2E7D32;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Style for sidebar */
    .sidebar-content {
        background-color: rgba(46, 125, 50, 0.05);
        padding: 1.2rem;
        border-radius: 10px;
        margin-top: 1rem;
        border-left: 4px solid #2E7D32;
    }
    
    /* Style for progress bar */
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #666;
        font-size: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Improved sidebar
with st.sidebar:
    st.markdown("### 📌 Information")
    st.markdown(
        """
        <div class='sidebar-content'>
        <h4>How it works</h4>
        <ol>
            <li>Upload your PDF file</li>
            <li>Wait for processing</li>
            <li>Download the generated manual</li>
        </ol>
        <p><strong>Note:</strong> The process may take a few minutes depending on the file size.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class='sidebar-content' style='margin-top: 20px;'>
        <h4>Support</h4>
        <p>For issues or questions, contact our support team at <strong>assistance@smartops.com</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Header with animation
st.markdown("<h1 class='main-header'>📘 Manual Generator</h1>", unsafe_allow_html=True)

# Description
st.markdown(
    """
    <p style='text-align: center; margin-bottom: 2rem; color: #555; font-size: 1.1rem;'>
    Transform your PDF documents into professional manuals with a single click.
    </p>
    """,
    unsafe_allow_html=True
)

# Improved upload area
st.markdown("<div class='upload-container'>", unsafe_allow_html=True)
uploaded_pdf = st.file_uploader("Select or drag your PDF file here", type="pdf")
st.markdown("We accept PDF files up to 10MB", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Generation process
if uploaded_pdf is not None:
    st.markdown(
        "<div class='success-message'>File successfully uploaded!</div>",
        unsafe_allow_html=True
    )
    
    # Configuration options (added)
    with st.expander("Generation options", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            format_option = st.selectbox(
                "Output format",
                ["Standard PDF", "Interactive PDF", "PDF with index"]
            )
        with col2:
            style_option = st.selectbox(
                "Graphic style",
                ["Modern", "Classic", "Minimalist", "Corporate"]
            )
    
    st.markdown("<div style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    # Generation button
    if st.button("Generate Manual", key="generate_btn"):
        # Show a progress bar to simulate the process
        progress_text = "Document processing in progress..."
        st.text(progress_text)
        
        progress_bar = st.progress(0)
        
        # Simulation of process phases
        stages = [
            "Analyzing document...",
            "Extracting content...",
            "Formatting manual...",
            "Generating index...",
            "Finalizing..."
        ]
        
        stage_weight = 100 / len(stages)
        
        for i, stage in enumerate(stages):
            for percent in range(int(stage_weight)):
                progress_value = min(int(i * stage_weight + percent), 100)
                progress_bar.progress(progress_value)
                time.sleep(0.03)
            st.text(stage)
        
        # Completion
        progress_bar.progress(100)
        st.markdown(
            "<div class='success-message' style='margin-top: 1rem;'>"
            "<h3>✅ Manual successfully generated!</h3>"
            "<p>Your document is ready for download</p>"
            "</div>",
            unsafe_allow_html=True
        )
        
        # Read the predefined PDF file (replace 'mainpdf.pdf' with your file path)
        try:
            with open("mainpdf.pdf", "rb") as file:
                pdf_data = file.read()
                
            # Improved download area
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="Download the generated manual",
                    data=pdf_data,
                    file_name="generated_manual.pdf",
                    mime="application/pdf",
                    key="download_btn"
                )
        except:
            st.error("Unable to load the file. Make sure 'mainpdf.pdf' exists in the application directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class='footer'>
        <p>© 2025 Manual Generator | All rights reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
