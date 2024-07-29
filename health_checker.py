import streamlit as st

# Set page configuration
st.set_page_config(page_title="Health Checker", layout="centered")

# Add some style to make it more user-friendly
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
    background-size: cover;
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

# Page layout
st.title("Health Checker")
st.write("Please fill out your profile and symptoms information.")

# Profile Information
with st.form(key='profile_form'):
    st.header("User Profile")
    st.session_state.name = st.text_input("What's your name?", st.session_state.get('name', ''))
    st.session_state.gender = st.radio("What's your gender?", ("Male", "Female"), index={"Male": 0, "Female": 1}.get(st.session_state.get('gender'), 0))
    st.session_state.dob = st.date_input("What's your date of birth?", st.session_state.get('dob', None))
    st.session_state.smoker = st.radio("Are you a current smoker or have you been a smoker in the past?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('smoker'), 0))
    st.session_state.hypertension = st.radio("Have you ever been diagnosed with high blood pressure?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('hypertension'), 0))
    st.session_state.diabetes = st.radio("Do you have diabetes?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('diabetes'), 0))

    # Symptoms Information
    st.header("Symptom Checker")
    symptoms = {
        "Do you have a headache?": "headache",
        "Do you have an earache?": "earache",
        "Do you have a fever?": "fever",
        "Do you have a cough?": "cough",
        "Do you have a sore throat?": "sore_throat",
        "Do you have muscle pain?": "muscle_pain"
    }

    user_symptoms = {}
    for question, key in symptoms.items():
        user_symptoms[key] = st.radio(question, ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get(key), 0))
        st.session_state[key] = user_symptoms[key]

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.header("Summary")
    st.write("Here is the information you provided:")

    st.write("**Profile Information:**")
    st.write(f"Name: {st.session_state.get('name', '')}")
    st.write(f"Gender: {st.session_state.get('gender', '')}")
    st.write(f"Date of Birth: {st.session_state.get('dob', '')}")
    st.write(f"Smoker: {st.session_state.get('smoker', '')}")
    st.write(f"High Blood Pressure: {st.session_state.get('hypertension', '')}")
    st.write(f"Diabetes: {st.session_state.get('diabetes', '')}")

    st.write("**Symptoms:**")
    for symptom in symptoms.values():
        st.write(f"{symptom.replace('_', ' ').capitalize()}: {st.session_state.get(symptom, '')}")


