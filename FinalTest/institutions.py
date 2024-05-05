import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Institutions App')

data = []

col1, col2, col3 = st.columns(3)
  
with col1:
    Application_mode = int(st.selectbox(label='Application_mode', options=["1","2","5","7","10","15","16","17","18","27","39","43","44","51","53","57"],index=0))
    data.append({"Application_mode": Application_mode})

with col2:
    Course = int(st.selectbox(label='Course', options=["33","171"],index=0))
    data[-1]["Course"] = Course

with col3:
    Daytime_evening_attendance = int(st.selectbox(label='Daytime evening att', options=["1","0"],index=0))
    data[-1]["Daytime_evening_attendance"] = Daytime_evening_attendance

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Debtor = int(st.selectbox(label='Debtor', options=["1","0"],index=0))
    data[-1]["Debtor"] = Debtor
 
with col2:
    Displaced = int(st.selectbox(label='Displaced', options=["1","0"],index=0))
    data[-1]["Displaced"] = Displaced

with col3:
    Educational_special_needs = int(st.selectbox(label='Education special needs', options=["1","0"],index=0))
    data[-1]["Educational_special_needs"] = Educational_special_needs

with col4:
    Fathers_occupation = int(st.selectbox(label='Fathers_occupation', options=["1","0"],index=0))
    data[-1]["Fathers_occupation"] = Fathers_occupation

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Fathers_qualification = int(st.selectbox(label='Fathers_qualification', options=["1","0"],index=0))
    data[-1]["Fathers_qualification"] = Fathers_qualification
 
with col2:
    Gender = int(st.selectbox(label='Gender', options=["1","0"],index=0))
    data[-1]["Gender"] = Gender

with col3:
    International = int(st.selectbox(label='International', options=["1","0"],index=0))
    data[-1]["International"] = International

with col4:
    Marital_status = int(st.selectbox(label='Marital_status', options=["1","0"],index=0))
    data[-1]["Marital_status"] = Marital_status

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Mothers_occupation = int(st.selectbox(label='Mothers_occupation', options=["1","0"],index=0))
    data[-1]["Mothers_occupation"] = Mothers_occupation
 
with col2:
    Mothers_qualification = int(st.selectbox(label='Mothers_qualification', options=["1","0"],index=0))
    data[-1]["Mothers_qualification"] = Mothers_qualification

with col3:
    Nacionality = int(st.selectbox(label='Nacionality', options=["1","0"],index=0))
    data[-1]["Nacionality"] = Nacionality

with col4:
    Previous_qualification = int(st.selectbox(label='Previous_qualification', options=["1","0"],index=0))
    data[-1]["Previous_qualification"] = Previous_qualification

col1, col2, col3,col4 = st.columns(4)
 
with col1:
    Scholarship_holder = int(st.selectbox(label='Scholarship_holder', options=["1","0"],index=0))
    data[-1]["Scholarship_holder"] = Scholarship_holder
 
with col2:
    Tuition_fees_up_to_date = int(st.selectbox(label='Tuition_fees_up_to_date', options=["1","0"],index=0))
    data[-1]["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date

with col3:
    Admission_grade = int(st.number_input(label='Admission_grade', value=1))
    data[-1]["Admission_grade"] = Admission_grade

with col4:
    Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=1))
    data[-1]["Previous_qualification_grade"] = Previous_qualification_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=1))
    data[-1]["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=1))
    data[-1]["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=1))
    data[-1]["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col4:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade', value=0))
    data[-1]["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0))
    data[-1]["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0))
    data[-1]["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=0))
    data[-1]["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col4:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=0))
    data[-1]["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Application_order = int(st.number_input(label='Application_order', value=0, max_value=9))
    data[-1]["Application_order"] = Application_order

with col2:
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=14))
    data[-1]["Age_at_enrollment"] = Age_at_enrollment

with col3:
    Unemployment_rate = float(st.number_input(label='Unemployment_rate'))
    data[-1]["Unemployment_rate"] = Unemployment_rate

with col4:
    Inflation_rate = float(st.number_input(label='Inflation_rate'))
    data[-1]["Inflation_rate"] = Inflation_rate

with col5:
    GDP = float(st.number_input(label='GDP'))
    data[-1]["GDP"] = GDP

with st.expander("View the Raw Data"):
    data_df = pd.DataFrame(data)
    st.dataframe(data_df, width=800)

if st.button('Predict'):
    new_data = data_preprocessing(data=data_df)
    print(data_df)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800)

    st.write("Status : {}".format(prediction(new_data)))