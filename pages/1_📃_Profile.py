import streamlit as st

def show_profile_page():
    st.title("User Profile")
    st.write("Please fill out your profile information.")

    st.session_state.name = st.text_input("What's your name?", st.session_state.get('name', ''))
    st.session_state.gender = st.radio("What's your gender?", ("Male", "Female"), index={"Male": 0, "Female": 1}.get(st.session_state.get('gender'), 0))
    st.session_state.dob = st.date_input("What's your date of birth?", st.session_state.get('dob', None))
    st.session_state.smoker = st.radio("Are you a current smoker or have you been a smoker in the past?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('smoker'), 0))
    st.session_state.hypertension = st.radio("Have you ever been diagnosed with high blood pressure?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('hypertension'), 0))
    st.session_state.diabetes = st.radio("Do you have diabetes?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('diabetes'), 0))

if __name__ == "__main__":
    show_profile_page()
