import streamlit as st

def show_results_page():
    st.title("Summary")
    st.write("Here is the information you provided:")

    st.write("**Profile Information:**")
    st.write(f"Name: {st.session_state.get('name', '')}")
    st.write(f"Gender: {st.session_state.get('gender', '')}")
    st.write(f"Date of Birth: {st.session_state.get('dob', '')}")
    st.write(f"Smoker: {st.session_state.get('smoker', '')}")
    st.write(f"High Blood Pressure: {st.session_state.get('hypertension', '')}")
    st.write(f"Diabetes: {st.session_state.get('diabetes', '')}")

    st.write("**Symptoms:**")
    symptoms = ["headache", "earache", "fever", "cough", "sore_throat", "muscle_pain"]
    for symptom in symptoms:
        st.write(f"{symptom.replace('_', ' ').capitalize()}: {st.session_state.get(symptom, '')}")

if __name__ == "__main__":
    show_results_page()
