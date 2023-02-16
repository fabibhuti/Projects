# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/Downloads/trained_model.sav', 'rb')) # Change the location of 'trained_model.sav' as per convinience

def diabetic_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
       
        
def main():
    st.title('Diabetes Predition Web App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age')
    
    
    diagnosis = ''
    if st.button('Diabetes Test Result'):
        diagnosis = diabetic_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
        
# pip install streamlit
# pip install pickle-mixin

# https://www.youtube.com/@SkillLync - Youtube channel link
