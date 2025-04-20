import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="👨‍🦰🤶")
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = pickle.load(open(f'{working_dir}\\Saved_model\\diabetes.pkl', 'rb'))
scaler = pickle.load(open(f'{working_dir}\\Saved_model\\scaler.pkl', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}\\Saved_model\\heart.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}\\Saved_model\\kidney.pkl', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction", 
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using Machine Learning")

    # Inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies", key="diabetes_pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level", key="diabetes_glucose")
    with col3:
        BloodPressure = st.text_input("BloodPressure Value", key="diabetes_bp")
    with col1:
        SkinThickness = st.text_input("SkinThickness Value", key="diabetes_skin")
    with col2:
        Insulin = st.text_input("Insulin Value", key="diabetes_insulin")
    with col3:
        BMI = st.text_input("BMI Value", key="diabetes_bmi")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value", key="diabetes_dpf")
    with col2:
        Age = st.text_input("Age", key="diabetes_age")

    diabetes_result = ""
    if st.button("Diabetes Test Result", key="diabetes_button"):
        # BMI Categories
        NewBMI_Underweight = NewBMI_Overweight = NewBMI_Obesity_1 = NewBMI_Obesity_2 = NewBMI_Obesity_3 = 0
        if float(BMI) <= 18.5:
            NewBMI_Underweight = 1
        elif 24.9 < float(BMI) <= 29.9:
            NewBMI_Overweight = 1
        elif 29.9 < float(BMI) <= 34.9:
            NewBMI_Obesity_1 = 1
        elif 34.9 < float(BMI) <= 39.9:
            NewBMI_Obesity_2 = 1
        elif float(BMI) > 39.9:
            NewBMI_Obesity_3 = 1

        # Insulin Normal Range
        NewInsulinScore_Normal = 1 if 16 <= float(Insulin) <= 166 else 0

        # Glucose Categories
        NewGlucose_Low = NewGlucose_Normal = NewGlucose_Overweight = NewGlucose_Secret = 0
        if float(Glucose) <= 70:
            NewGlucose_Low = 1
        elif 70 < float(Glucose) <= 99:
            NewGlucose_Normal = 1
        elif 99 < float(Glucose) <= 126:
            NewGlucose_Overweight = 1
        elif float(Glucose) > 126:
            NewGlucose_Secret = 1

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
              DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        input_scaled = scaler.transform(np.array([user_input]))

        prediction = diabetes_model.predict(input_scaled)
        diabetes_result = "The person has diabetes" if prediction[0] == 1 else "The person does not have diabetes"
    st.success(diabetes_result)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age", key="heart_age")
    with col2:
        sex = st.text_input("Sex", key="heart_sex")
    with col3:
        cp = st.text_input("Chest Pain Type", key="heart_cp")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure", key="heart_trestbps")
    with col2:
        chol = st.text_input("Serum Cholesterol in mg/dl", key="heart_chol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl", key="heart_fbs")
    with col1:
        restecg = st.text_input("Resting ECG Result", key="heart_restecg")
    with col2:
        thalach = st.text_input("Max Heart Rate Achieved", key="heart_thalach")
    with col3:
        exang = st.text_input("Exercise Induced Angina", key="heart_exang")
    with col1:
        oldpeak = st.text_input("ST Depression", key="heart_oldpeak")
    with col2:
        slope = st.text_input("Slope of ST Segment", key="heart_slope")
    with col3:
        ca = st.text_input("Major Vessels Colored by Fluoroscopy", key="heart_ca")
    with col1:
        thal = st.text_input("Thal (0=normal, 1=fixed, 2=reversible)", key="heart_thal")

    heart_disease_result = ""
    if st.button("Heart Disease Test Result", key="heart_button"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                      exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        heart_disease_result = "This person has heart disease" if prediction[0] == 1 else "This person does not have heart disease"
    st.success(heart_disease_result)

# Kidney Disease Prediction Page
if selected == 'Kidney Disease Prediction':
    st.title("Kidney Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    inputs = {}
    fields = [
        'Age', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar',
        'Red Blood Cell', 'Pus Cell', 'Pus Cell Clumps', 'Bacteria',
        'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium',
        'Potassium', 'Haemoglobin', 'Packet Cell Volume', 'White Blood Cell Count',
        'Red Blood Cell Count', 'Hypertension', 'Diabetes Mellitus',
        'Coronary Artery Disease', 'Appetitte', 'Peda Edema', 'Aanemia'
    ]

    col_refs = [col1, col2, col3, col4, col5]
    for idx, field in enumerate(fields):
        with col_refs[idx % 5]:
            inputs[field] = st.text_input(field, key=f'kidney_{field.replace(" ", "_").lower()}')

    kidney_diagnosis = ""
    if st.button("Kidney's Test Result", key="kidney_button"):
        try:
            user_input = [float(inputs[f]) for f in fields]
            prediction = kidney_disease_model.predict([user_input])
            kidney_diagnosis = "The person has Kidney's disease" if prediction[0] == 1 else "The person does not have Kidney's disease"
        except ValueError:
            kidney_diagnosis = "Please enter valid numeric values for all fields."
    st.success(kidney_diagnosis)
