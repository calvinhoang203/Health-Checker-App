
import streamlit as st
import datetime
import pandas as pd
import os
from io import BytesIO
from openpyxl import Workbook


# File paths
CSV_FILE_PATH = 'health_data.csv'
EXCEL_FILE_PATH = 'health_data.xlsx'
ID_FILE_PATH = 'current_id.txt'


# Set page configuration
st.set_page_config(page_title="Health Checker",
                   page_icon = ":hospital:",
                   layout="centered")

# Function to get the next ID
def get_next_id():
    if os.path.exists(ID_FILE_PATH):
        with open(ID_FILE_PATH, 'r') as f:
            current_id = int(f.read().strip())
    else:
        current_id = 0
    next_id = current_id + 1
    with open(ID_FILE_PATH, 'w') as f:
        f.write(str(next_id))
    return next_id

# Function to decrement the ID
def decrement_id():
    if os.path.exists(ID_FILE_PATH):
        with open(ID_FILE_PATH, 'r') as f:
            current_id = int(f.read().strip())
        if current_id > 0:
            new_id = current_id - 1
            with open(ID_FILE_PATH, 'w') as f:
                f.write(str(new_id))

# Function to append data to a CSV file
def append_to_csv(data, file_path=CSV_FILE_PATH):
    df = pd.DataFrame([data])
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

# Function to save data to Excel
def save_to_excel(data, file_path=EXCEL_FILE_PATH):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False, engine='openpyxl')

# Update the question handling to use actual questions
def headache_answers():
    headache_answers = {}
    if st.session_state.headache_status['Headache'] == 'Yes':
        for question in st.session_state.questions['Headache']:
            answer_key = f'Headache_{question}'
            headache_answers[question] = st.session_state.get(answer_key, '')
    else:
        for question in st.session_state.questions['Headache']:
            headache_answers[question] = ''
    # print(headache_answers)
    return {**headache_answers}

def earache_answers():
    earache_answers = {}
    if st.session_state.earache_status['Earache'] == 'Yes':
        for question in st.session_state.questions['Earache']:
            answer_key = f'Earache_{question}'
            earache_answers[question] = st.session_state.get(answer_key, '')

    else:
        for question in st.session_state.questions['Earache']:
            earache_answers[question] = ''
    # print(earache_answers)
    return {**earache_answers}

def difficult_sleeping_answers():
    difficult_sleeping_answers = {}
    if st.session_state.difficult_sleeping_status['Difficult Sleeping'] == 'Yes':
        for question in st.session_state.questions['Difficult Sleeping']:
            answer_key = f'Difficult_Sleeping_{question}'
            difficult_sleeping_answers[question] = st.session_state.get(answer_key, '')

    else:
        for question in st.session_state.questions['Difficult Sleeping']:
            difficult_sleeping_answers[question] = ''
    # print(difficult_sleeping_answers)
    return {**difficult_sleeping_answers}

def fever_answers():
    fever_answers = {}
    if st.session_state.fever_status['Fever'] == 'Yes':
        for question in st.session_state.questions['Fever']:
            answer_key = f'Fever_{question}'
            fever_answers[question] = st.session_state.get(answer_key, '')

    else:
        for question in st.session_state.questions['Fever']:
            fever_answers[question] = ''
    # print(fever_answers)
    return {**fever_answers}

def rapid_heartbeat_answers():
    rapid_heartbeat_answers = {}
    if st.session_state.rapid_heartbeat_status['Rapid Heartbeat'] == 'Yes':
        for question in st.session_state.questions['Rapid Heartbeat']:
            answer_key = f'Rapid_Heartbeat_{question}'
            rapid_heartbeat_answers[question] = st.session_state.get(answer_key, '')

    else:
        for question in st.session_state.questions['Rapid Heartbeat']:
            rapid_heartbeat_answers[question] = ''
    # print(fever_answers)
    return {**rapid_heartbeat_answers}


# Ask headache questions
def ask_headache_questions(questions):
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        answer_options = (
            ("Less than a day", 
             "A day to a week", 
             "A week to one month", 
             "A month to a year", 
             "More than a year") if st.session_state.current_question == 0 else
            ("One side", "Both sides") if st.session_state.current_question == 1 else
            ("Worsens", "No effect") if st.session_state.current_question == 2 else
            ("Mild", "Moderate", "Severe")
        )
        print(st.session_state.current_question)
        answer = st.radio(question, answer_options, index=0)
        submit_question = st.form_submit_button(label='Submit Answer')

        if submit_question:
            st.session_state[f'Headache_{question}'] = answer
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(questions):
                st.session_state.show_more_symptoms = True
                st.session_state.symptom_data.update(headache_answers())
                st.rerun()
            else:
                st.rerun()

# Ask earache questions
def ask_earache_questions(questions):
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        print(st.session_state.current_question)
        answer_options = (
            ("Less than a day", 
             "A day to a week", 
             "A week to one month", 
             "A month to a year", 
             "More than a year") if st.session_state.current_question == 0 else
            ("One side", "Both sides") if st.session_state.current_question == 1 else
            ("Mild", "Moderate", "Severe")
        )
        answer = st.radio(question, answer_options, index=0)
        submit_question = st.form_submit_button(label='Submit Answer')
        if submit_question:
            st.session_state[f'Earache_{question}'] = answer
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(questions):
                st.session_state.show_more_symptoms = True
                st.session_state.symptom_data.update(earache_answers())
                st.rerun()
            else:
                st.rerun()

# Ask difficult sleeping questions
def ask_difficult_sleeping_questions(questions):
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        print(st.session_state.current_question)
        answer_options = (
            ("Less than a day", 
             "A day to a week", 
             "A week to one month", 
             "A month to a year", 
             "More than a year") if st.session_state.current_question == 0 else
            ("Yes", "No")
        )
        answer = st.radio(question, answer_options, index=0)
        submit_question = st.form_submit_button(label='Submit Answer')
        if submit_question:
            st.session_state[f'Difficult_Sleeping_{question}'] = answer
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(questions):
                st.session_state.show_more_symptoms = True
                st.session_state.symptom_data.update(difficult_sleeping_answers())
                st.rerun()
            else:
                st.rerun()


# Ask fever questions
def ask_fever_questions(questions):
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        print(st.session_state.current_question)
        answer_options = (
            ("Less than a day", 
             "A day to a week", 
             "A week to one month", 
             "A month to a year", 
             "More than a year") if st.session_state.current_question == 0 else
            ("Between 99.5°F (37.5°C) and 100.4°F (38°C)", 
             "Between 100.5°F (38.1°C) and 104.0°F (40°C)", 
             "Between 104.1°F (40.1°C) and 106.0°F (41.1°C)", 
             "Higher than 106.0°F (41.1°C)") if st.session_state.current_question == 1 else
            ("Mild", "Moderate", "Severe")
        )
        answer = st.radio(question, answer_options, index=0)
        submit_question = st.form_submit_button(label='Submit Answer')
        if submit_question:
            st.session_state[f'Fever_{question}'] = answer
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(questions):
                st.session_state.show_more_symptoms = True
                st.session_state.symptom_data.update(fever_answers())
                st.rerun()
            else:
                st.rerun()


# Ask fever questions
def ask_rapid_heartbeat_questions(questions):
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        print(st.session_state.current_question)
        answer_options = (
            ("Less than a day", 
             "A day to a week", 
             "A week to one month", 
             "A month to a year", 
             "More than a year") if st.session_state.current_question == 0 else
            ("Yes", "No")
        )
        answer = st.radio(question, answer_options, index=0)
        submit_question = st.form_submit_button(label='Submit Answer')
        if submit_question:
            st.session_state[f'Rapid_Heartbeat_{question}'] = answer
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(questions):
                st.session_state.show_more_symptoms = True
                st.session_state.symptom_data.update(rapid_heartbeat_answers())
                st.rerun()
            else:
                st.rerun()


    
def main():
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
        .stDownloadButton button {
            background: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            margin: 8px 0;
            cursor: pointer;
            border: none;
            border-radius: 4px;
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

    if 'symptom_type' not in st.session_state:
        st.session_state.symptom_type = None

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    if 'more_symptoms' not in st.session_state:
        st.session_state.more_symptoms = None
        
    if 'show_summary' not in st.session_state:
        st.session_state.show_summary = False

    if 'show_more_symptoms' not in st.session_state:
        st.session_state.show_more_symptoms = False

    if 'user_data' not in st.session_state:
        st.session_state.user_data = []

    if 'symptom_data' not in st.session_state:
        st.session_state.symptom_data = {}

    if 'headache_status' not in st.session_state:
        st.session_state.headache_status = {
            'Headache': 'No'
        }

    if 'earache_status' not in st.session_state:
        st.session_state.earache_status = {
            'Earache': 'No'
        }
    
    if 'difficult_sleeping_status' not in st.session_state:
        st.session_state.difficult_sleeping_status = {
            'Difficult Sleeping': 'No'
        }
    
    if 'fever_status' not in st.session_state:
        st.session_state.fever_status = {
            'Fever': 'No'
        }

    if 'rapid_heartbeat_status' not in st.session_state:
        st.session_state.rapid_heartbeat_status = {
            'Rapid Heartbeat': 'No'
        }

    if 'questions' not in st.session_state:
        st.session_state.questions = {
            "Headache": [
                "How long has this headache been troubling you?",
                "Is your headache mainly located on one or both sides of the head?",
                "How does bending forward affect your headache?",
                "How would you describe the intensity of your headache?"
            ],
            "Earache": [
                "How long has this earache been troubling you?",
                "Does this affect one or both ears?",
                "How would you describe the intensity of your earache?"
            ],
            "Difficult Sleeping": [
                "How long has this sleeping issue been troubling you?",
                "Is this problem with sleep caused by physical symptoms, such as pain, cough, breathlessness or needing to urinate?"
            ],
            "Fever": [
                "How long has this fever been troubling you?",
                "How high is your temperature?",
                "How bad is it right now?"
            ],
            "Rapid Heartbeat": [
                "How long has this heartbeat issue been troubling you?",
                "Do you feel like your heart is pounding or has skipped a beat?"
            ]
        }



    placeholder = st.empty()

    # Profile Information Form

    if not st.session_state.profile_submitted:
        with placeholder.form(key='profile_form'):
            st.header("Your Profile")
            name = st.text_input("What's your name?", st.session_state.get('name', ''))
            gender = st.radio("What's your gender?", ("Male", "Female"), index={"Male": 0, "Female": 1}.get(st.session_state.get('gender'), 0))
            dob = st.date_input("What's your date of birth?", min_value=datetime.date(year=1975, month=1, day=1), format="MM/DD/YYYY")
            smoker = st.radio("Are you a current smoker or have you been a smoker in the past?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('smoker'), 0))
            hypertension = st.radio("Have you ever been diagnosed with high blood pressure?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('hypertension'), 0))
            diabetes = st.radio("Do you have diabetes?", ("Yes", "No"), index={"Yes": 0, "No": 1}.get(st.session_state.get('diabetes'), 0))

            submit_profile = st.form_submit_button(label='Submit Profile')
            
            if submit_profile:
                st.session_state.profile_submitted = True
                st.session_state.name = name
                st.session_state.gender = gender
                st.session_state.dob = dob
                st.session_state.smoker = smoker
                st.session_state.hypertension = hypertension
                st.session_state.diabetes = diabetes
                st.session_state.symptom_type = None  # Reset symptom type
                st.session_state.current_question = 0  # Reset question index
                st.rerun()
                
                

    


    # Symptoms Form
    if st.session_state.profile_submitted and not st.session_state.show_summary:
        if st.session_state.symptom_type is None and not st.session_state.show_more_symptoms:
            with placeholder.form(key='symptom_selection_form'):
                st.header("Symptom Checker")
                st.write(f"Hello {st.session_state.get('name', '')}!")
                symptom_type = st.selectbox(
                        "What symptoms are you experiencing?",
                        list(st.session_state.questions.keys()),
                        index=None,
                        placeholder="e.g. headache"
                )
                submit_symptom = st.form_submit_button(label='Submit Symptom')
                if submit_symptom:
                    st.session_state.symptom_type = symptom_type
                    st.session_state.current_question = 0
                    st.session_state.show_more_symptoms = False
                    st.rerun()


        

        elif st.session_state.symptom_type and not st.session_state.show_more_symptoms:
            with placeholder.form(key='symptom_questions_form'):
                st.header(f"{st.session_state.symptom_type} Checker")


                st.session_state.symptom_data.update(st.session_state.headache_status)
                st.session_state.symptom_data.update(headache_answers())
                st.session_state.symptom_data.update(st.session_state.earache_status)
                st.session_state.symptom_data.update(earache_answers())
                st.session_state.symptom_data.update(st.session_state.difficult_sleeping_status)
                st.session_state.symptom_data.update(difficult_sleeping_answers())
                st.session_state.symptom_data.update(st.session_state.fever_status)
                st.session_state.symptom_data.update(fever_answers())
                st.session_state.symptom_data.update(st.session_state.rapid_heartbeat_status)
                st.session_state.symptom_data.update(rapid_heartbeat_answers())


                
                if st.session_state.symptom_type == "Headache":
                    ask_headache_questions(st.session_state.questions['Headache'])
                    st.session_state.headache_status['Headache'] = 'Yes'
                    st.session_state.symptom_data.update(st.session_state.headache_status)
                    st.session_state.symptom_data.update(headache_answers())
                if st.session_state.symptom_type == "Earache":
                    ask_earache_questions(st.session_state.questions['Earache'])        
                    st.session_state.earache_status['Earache'] = 'Yes'
                    st.session_state.symptom_data.update(st.session_state.earache_status)
                    st.session_state.symptom_data.update(earache_answers())
                if st.session_state.symptom_type == "Difficult Sleeping":
                    ask_difficult_sleeping_questions(st.session_state.questions['Difficult Sleeping'])        
                    st.session_state.difficult_sleeping_status['Difficult Sleeping'] = 'Yes'
                    st.session_state.symptom_data.update(st.session_state.difficult_sleeping_status)
                    st.session_state.symptom_data.update(difficult_sleeping_answers())
                if st.session_state.symptom_type == "Fever":
                    ask_fever_questions(st.session_state.questions['Fever'])        
                    st.session_state.fever_status['Fever'] = 'Yes'
                    st.session_state.symptom_data.update(st.session_state.fever_status)
                    st.session_state.symptom_data.update(fever_answers())
                if st.session_state.symptom_type == "Rapid Heartbeat":
                    ask_rapid_heartbeat_questions(st.session_state.questions['Rapid Heartbeat'])        
                    st.session_state.rapid_heartbeat_status['Rapid Heartbeat'] = 'Yes'
                    st.session_state.symptom_data.update(st.session_state.rapid_heartbeat_status)
                    st.session_state.symptom_data.update(rapid_heartbeat_answers())
                            

        


        # Ask about more symptoms after questions for the current symptom type are done
        if st.session_state.show_more_symptoms:
            with placeholder.form(key='more_symptoms_form'):
                more_symptoms = st.radio("Do you have any other symptoms?", ("Yes", "No"))
                submit_more_symptoms = st.form_submit_button(label='Submit Answer')

                if submit_more_symptoms:
                    st.session_state.more_symptoms = more_symptoms
                    
                    if more_symptoms == "Yes":
                        st.session_state.symptom_type = None
                        st.session_state.current_question = 0
                        st.session_state.show_more_symptoms = False
                        # st.rerun()
                    else:
                        st.session_state.show_summary = True
                        # st.session_state.show_more_symptoms = False
                        
                    st.rerun()    
                    


    
    # Report Summary
    if st.session_state.show_summary:
        st.header("Summary")
        st.write("Thank you for providing your information!")
        st.write("")
        user_data = {
            'ID': get_next_id(),
            'Name': st.session_state.get('name', ''),
            'Gender': st.session_state.get('gender', ''),
            'Date of Birth': st.session_state.get('dob', ''),
            'Smoker': st.session_state.get('smoker', ''),
            'Hypertension': st.session_state.get('hypertension', ''),
            'Diabetes': st.session_state.get('diabetes', '')
        }

    
        
        user_data.update(st.session_state.symptom_data)

        if not any(ud['Name'] == user_data['Name'] and ud['Date of Birth'] == user_data['Date of Birth'] for ud in st.session_state.user_data):
            st.session_state.user_data.append(user_data)
            append_to_csv(user_data)  # Append to CSV file
            save_to_excel(st.session_state.user_data)  # Save to Excel file
        st.write("**Profile**")
        st.write(f"Name: {user_data['Name']}")
        st.write(f"Gender: {user_data['Gender']}")
        st.write(f"Date of Birth: {user_data['Date of Birth']}")
        st.write(f"Smoker: {user_data['Smoker']}")
        st.write(f"Hypertension: {user_data['Hypertension']}")
        st.write(f"Diabetes: {user_data['Diabetes']}")
        st.write("")
        st.write("**Symptoms**")
        # Display symptoms and answers
        
        for key, value in st.session_state.symptom_data.items():
            if value != 'No' and value  != '':
                st.write(f"{key}: {value}")
        st.write("Thank you for using Health Checker!") 

        if st.button('Back'):
            st.session_state.profile_submitted = False
            st.session_state.symptom_type = None
            st.session_state.current_question = 0
            st.session_state.more_symptoms = None
            st.session_state.show_summary = False
            st.session_state.show_more_symptoms = False
            st.session_state.name = ''
            st.session_state.gender = ''
            st.session_state.dob = ''
            st.session_state.smoker = ''
            st.session_state.hypertension = ''
            st.session_state.diabetes = ''
            for symptom in st.session_state.questions.keys():
                for i in range(len(st.session_state.questions[symptom])):
                    answer_key = f'{symptom}_question_{i}'
                    if answer_key in st.session_state:
                        del st.session_state[answer_key]
            st.session_state.user_data = []
            decrement_id()
            st.rerun()
        
        # # Create download links for CSV and Excel files
        # csv_file = 'health_data.csv'
        # excel_file = 'health_data.xlsx'

        # with open(csv_file, 'rb') as f:
        #     st.download_button(
        #         label='Download CSV',
        #         data=f,
        #         file_name=csv_file,
        #         mime='text/csv'
        #     )

        # with open(excel_file, 'rb') as f:
        #     st.download_button(
        #         label='Download Excel',
        #         data=f,
        #         file_name=excel_file,
        #         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        #     )
        

        
        # symptoms = {
        #     "headache": "Do you have a headache?",
        #     "earache": "Do you have an earache?",
        #     "fever": "Do you have a fever?",
        #     "cough": "Do you have cough a lot recently?",
        #     "sore_throat": "Do you have a sore throat?",
        #     "muscle_pain": "Do you have muscle pain?",
        #     "earache": "Do you have earache?",
        #     "difficulty_sleeping": "Do you find it difficult to sleep?",
        #     "feel_itchy": "Do you feel itchy?",
        #     "rapid_heartbeat": "Does your heart beat rapidly?",
        #     "agitation": "Do you feel agitated?",
        #     "wheezing": "Do you wheeze?",
        #     "loss_of_smell": "Do you have loss of smell",
        #     "breathing": "Do you have breathing problem?"
        # }
        # for key, question in symptoms.items():
        #     st.write(f"{question}")
        #     st.write(f"Answer: {st.session_state.get(key, '')}")
            
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


if __name__ == '__main__':
    main()


        
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