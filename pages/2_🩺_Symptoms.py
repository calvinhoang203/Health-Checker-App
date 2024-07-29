import streamlit as st

def show_symptom_page():
    st.title("Symptom Checker")
    st.write("Please answer the following questions about your symptoms.")

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

if __name__ == "__main__":
    show_symptom_page()

