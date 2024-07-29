import streamlit as st

# Set page configuration
st.set_page_config(page_title="Health Checker", layout="centered")

# Main page content
st.title("Welcome to Health Checker")
st.write("Navigate through the pages to fill out your profile, symptoms, and view the results.")

# Add some style to make it more user-friendly
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f5f5f5;
    }
    .stButton button {
        background: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        margin: 8px 0;
        cursor: pointer;
        border: none;
        border-radius: 4px;
    }
    .stButton button:hover {
        background: #45a049;
    }
    </style>
    """, unsafe_allow_html=True
)

