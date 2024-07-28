# Creating a UI demo using Streamlit
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np


# Display the dataframe for reference
st.write("Data Preview:")
st.dataframe(df.head())

# Preprocess the data
# Assuming that the Excel file contains symptoms as features and diseases as target
# This is a placeholder. Adjust it based on your actual data structure.
features = df.drop(columns=['Disease'])  # Replace 'Disease' with the actual column name for the target
target = df['Disease']  # Replace 'Disease' with the actual column name for the target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a simple model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

# Streamlit UI for user inputs
st.title("Disease Prediction System")

# Placeholder for dynamic symptom inputs
user_inputs = {}

# Loop through the symptoms (features) to create input widgets
for column in features.columns:
    user_inputs[column] = st.selectbox(f"Do you have {column}?", ['Yes', 'No'])

# Convert user inputs to model input format
input_data = np.array([[1 if user_inputs[col] == 'Yes' else 0 for col in features.columns]])

# Predict disease probabilities
if st.button("Predict"):
    prediction = model.predict_proba(input_data)[0]
    
    # Display the results
    st.write("Prediction Probabilities:")
    for idx, disease in enumerate(model.classes_):
        st.write(f"{disease}: {prediction[idx] * 100:.2f}%")