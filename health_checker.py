import streamlit as st
import datetime
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Health Checker",
                   page_icon = ":hospital:",
                   layout="centered")






# Add some style to make it more user-friendly
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://img.freepik.com/premium-vector/abstract-medical-background-with-icons-symbols-template-with-concept-idea-healthcare-technology-innovation-medicine-health-science-research_120542-544.jpg?size=626&ext=jpg&ga=GA1.1.1714815104.1722218449&semt=ais_user');
        background-size: cover;
    }
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    .st-emotion-cache-1whx7iy p {
        font-size: 20px;
    }

    p {
        font-size: 20px;
    }
    .reportview-container {
        background: #f5f5f5;
        font-size: 16px;
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
    input {
        font-size: 20px !important;
    }

    </style>
    """, unsafe_allow_html=True
)

# Page layout
st.title("Health Checker :hospital:")
st.write("Please fill out your profile and symptoms information.")


# Initialize session state
if 'profile_submitted' not in st.session_state:
    st.session_state.profile_submitted = False

if 'symptoms_submitted' not in st.session_state:
    st.session_state.symptoms_submitted = False
placeholder = st.empty()
# Profile Information Form
if not st.session_state.profile_submitted:
    with placeholder.form(key='profile_form'):
        st.header("Your Profile")
        st.session_state.name = st.text_input("What's your name?", st.session_state.get('name', ''))
        st.session_state.gender = st.radio("What's your gender?", ("Male", "Female"), index={"Male": 0, "Female": 1}.get(st.session_state.get('gender'), 0))
        st.session_state.dob = st.date_input("What's your date of birth?", min_value=datetime.date(year=1975, month=1, day=1), format="MM/DD/YYYY")
        st.session_state.smoker = st.radio("Are you a current smoker or have you been a smoker in the past?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('smoker'), 0))
        st.session_state.hypertension = st.radio("Have you ever been diagnosed with high blood pressure?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('hypertension'), 0))
        st.session_state.diabetes = st.radio("Do you have diabetes?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('diabetes'), 0))

        submit_profile = st.form_submit_button(label='Submit Profile')

        if submit_profile:
            st.session_state.profile_submitted = True
            placeholder.empty()
            

# Symptoms Form
if st.session_state.profile_submitted and not st.session_state.symptoms_submitted:
    with placeholder.form(key='symptom_form'):
        st.header("Symptom Checker")
        st.write(f"Hello {st.session_state.get('name', '')}! Please complete the following questions:")
        symptoms = {
            "Do you have a headache?": "headache",
            "Do you have an earache?": "earache",
            "Do you have a fever?": "fever",
            "Do you have cough a lot recent?": "cough",
            "Do you have a sore throat?": "sore_throat",
            "Do you have muscle pain?": "muscle_pain",
            "Do you have earache?" : "earache",
            "Do you find it difficult to sleep?": "difficulty_sleeping",
            "Do you feel itchy?": "feel_itchy",
            "Does your heart beat rapidly?": "rapid_heartbeat",
            "Do you feel agitated?": "agitation",
            "Do you wheeze?": "wheezing",
            "Do you have loss of smell?": "loss_of_smell",
            "Do you have breathing problem?": "breathing",
            
        }

        for question, key in symptoms.items():
            st.session_state[key] = st.radio(question, ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get(key), 0))

        submit_symptoms = st.form_submit_button(label='Submit Symptoms')

        if submit_symptoms:
            st.session_state.symptoms_submitted = True
            placeholder.empty()

# Report Summary
if st.session_state.profile_submitted and st.session_state.symptoms_submitted:
    st.header("Summary")
    st.write("Here is the information you provided:")
    st.write("")

    st.write("**Profile Information:**")
    st.write(f"Name: {st.session_state.get('name', '')}")
    st.write(f"Gender: {st.session_state.get('gender', '')}")
    st.write(f"Date of Birth: {st.session_state.get('dob', '')}")
    st.write(f"Smoker: {st.session_state.get('smoker', '')}")
    st.write(f"High Blood Pressure: {st.session_state.get('hypertension', '')}")
    st.write(f"Diabetes: {st.session_state.get('diabetes', '')}")
    st.write('')
    st.write("**Symptoms:**")
    symptoms = {
        "headache": "Do you have a headache?",
        "earache": "Do you have an earache?",
        "fever": "Do you have a fever?",
        "cough": "Do you have cough a lot recently?",
        "sore_throat": "Do you have a sore throat?",
        "muscle_pain": "Do you have muscle pain?",
        "earache": "Do you have earache?",
        "difficulty_sleeping": "Do you find it difficult to sleep?",
        "feel_itchy": "Do you feel itchy?",
        "rapid_heartbeat": "Does your heart beat rapidly?",
        "agitation": "Do you feel agitated?",
        "wheezing": "Do you wheeze?",
        "loss_of_smell": "Do you have loss of smell",
        "breathing": "Do you have breathing problem?"
    }
    for key, question in symptoms.items():
        st.write(f"{question}")
        st.write(f"Answer: {st.session_state.get(key, '')}")
        
    # # Prediction logic
    # def calculate_probabilities(symptoms):
    #     # Define simple rules for probabilities
    #     conditions = {
    #         "Flu": {"fever": 1, "cough": 1, "sore_throat": 1},
    #         "COVID-19": {"fever": 1, "cough": 1, "headache": 0.5, "muscle_pain": 0.5},
    #         "Common Cold": {"cough": 1, "sore_throat": 1, "headache": 0.5},
    #     }

    #     results = {}
    #     for condition, symptom_weights in conditions.items():
    #         score = sum(symptom_weights.get(symptom, 0) * (1 if st.session_state.get(symptom, "No") == "Yes" else 0) for symptom in symptom_weights)
    #         results[condition] = score * 100

    #     # Normalize probabilities to sum to 100
    #     total = sum(results.values())
    #     if total > 0:
    #         results = {condition: prob / total * 100 for condition, prob in results.items()}

    #     return results

    # probabilities = calculate_probabilities(symptoms.keys())
    # st.write('')
    # st.write("**Prediction Results:**")
    # for condition, probability in probabilities.items():
    #     st.write(f"{condition}: {probability:.2f}%")