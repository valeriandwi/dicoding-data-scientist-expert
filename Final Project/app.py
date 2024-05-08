import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

application_mode_options = ['1 - 1st phase - general contingent', '2 - Ordinance No. 612/93', '5 - 1st phase - special contingent (Azores Island)', '7 - Holders of other higher courses', '10 - Ordinance No. 854-B/99', '15 - International student (bachelor)', '16 - 1st phase - special contingent (Madeira Island)', '17 - 2nd phase - general contingent', '18 - 3rd phase - general contingent', '26 - Ordinance No. 533-A/99, item b2) (Different Plan)', '27 - Ordinance No. 533-A/99, item b3 (Other Institution)', '39 - Over 23 years old', '42 - Transfer', '43 - Change of course', '44 - Technological specialization diploma holders', '51 - Change of institution/course', '53 - Short cycle diploma holders', '57 - Change of institution/course (International)']
course_options = ['33 - Biofuel Production Technologies', '171 - Animation and Multimedia Design', '8014 - Social Service (evening attendance)', '9003 - Agronomy', '9070 - Communication Design', '9085 - Veterinary Nursing', '9119 - Informatics Engineering', '9130 - Equinculture', '9147 - Management', '9238 - Social Service', '9254 - Tourism', '9500 - Nursing', '9556 - Oral Hygiene', '9670 - Advertising and Marketing Management', '9773 - Journalism and Communication', '9853 - Basic Education', '9991 - Management (evening attendance)']
fathers_occupation_options = ['0 - Student', '1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', '2 - Specialists in Intellectual and Scientific Activities', '3 - Intermediate Level Technicians and Professions', '4 - Administrative staff', '5 - Personal Services, Security and Safety Workers and Sellers', '6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', '7 - Skilled Workers in Industry, Construction and Craftsmen', '8 - Installation and Machine Operators and Assembly Workers', '9 - Unskilled Workers', '10 - Armed Forces Professions', '90 - Other Situation', '99 - (blank)', '101 - Armed Forces Officers', '102 - Armed Forces Sergeants', '103 - Other Armed Forces personnel', '112 - Directors of administrative and commercial services', '114 - Hotel, catering, trade and other services directors', '121 - Specialists in the physical sciences, mathematics, engineering and related techniques', '122 - Health professionals', '123 - teachers', '124 - Specialists in finance, accounting, administrative organization, public and commercial relations', '131 - Intermediate level science and engineering technicians and professions', '132 - Technicians and professionals, of intermediate level of health', '134 - Intermediate level technicians from legal, social, sports, cultural and similar services', '135 - Information and communication technology technicians', '141 - Office workers, secretaries in general and data processing operators', '143 - Data, accounting, statistical, financial services and registry-related operators', '144 - Other administrative support staff', '151 - personal service workers', '152 - sellers', '153 - Personal care workers and the like', '154 - Protection and security services personnel', '161 - Market-oriented farmers and skilled agricultural and animal production workers', '163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence', '171 - Skilled construction workers and the like, except electricians', '172 - Skilled workers in metallurgy, metalworking and similar', '174 - Skilled workers in electricity and electronics', '175 - Workers in food processing, woodworking, clothing and other industries and crafts', '181 - Fixed plant and machine operators', '182 - assembly workers', '183 - Vehicle drivers and mobile equipment operators', '192 - Unskilled workers in agriculture, animal production, fisheries and forestry', '193 - Unskilled workers in extractive industry, construction, manufacturing and transport', '194 - Meal preparation assistants', '195 - Street vendors (except food) and street service providers']
mothers_occupation_options = ['0 - Student', '1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', '2 - Specialists in Intellectual and Scientific Activities', '3 - Intermediate Level Technicians and Professions', '4 - Administrative staff', '5 - Personal Services, Security and Safety Workers and Sellers', '6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', '7 - Skilled Workers in Industry, Construction and Craftsmen', '8 - Installation and Machine Operators and Assembly Workers', '9 - Unskilled Workers', '10 - Armed Forces Professions', '90 - Other Situation', '99 - (blank)', '122 - Health professionals', '123 - teachers', '125 - Specialists in information and communication technologies (ICT)', '131 - Intermediate level science and engineering technicians and professions', '132 - Technicians and professionals, of intermediate level of health', '134 - Intermediate level technicians from legal, social, sports, cultural and similar services', '141 - Office workers, secretaries in general and data processing operators', '143 - Data, accounting, statistical, financial services and registry-related operators', '144 - Other administrative support staff', '151 - personal service workers', '152 - sellers', '153 - Personal care workers and the like', '171 - Skilled construction workers and the like, except electricians', '173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', '175 - Workers in food processing, woodworking, clothing and other industries and crafts', '191 - cleaning workers', '192 - Unskilled workers in agriculture, animal production, fisheries and forestry', '193 - Unskilled workers in extractive industry, construction, manufacturing and transport', '194 - Meal preparation assistants']
father_mother_qualification_options = ['1 - Secondary Education - 12th Year of Schooling or Eq.', "2 - Higher Education - Bachelor's Degree", '3 - Higher Education - Degree', "4 - Higher Education - Master's", '5 - Higher Education - Doctorate', '6 - Frequency of Higher Education', '9 - 12th Year of Schooling - Not Completed', '10 - 11th Year of Schooling - Not Completed', '11 - 7th Year (Old)', '12 - Other - 11th Year of Schooling', '13 - 2nd year complementary high school course', '14 - 10th Year of Schooling', '18 - General commerce course', '19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', '20 - Complementary High School Course', '22 - Technical-professional course', '25 - Complementary High School Course - not concluded', '26 - 7th year of schooling', '27 - 2nd cycle of the general high school course', '29 - 9th Year of Schooling - Not Completed', '30 - 8th year of schooling', '31 - General Course of Administration and Commerce', '33 - Supplementary Accounting and Administration', '34 - Unknown', "35 - Can't read or write", '36 - Can read without having a 4th year of schooling', '37 - Basic education 1st cycle (4th/5th year) or equiv.', '38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', '39 - Technological specialization course', '40 - Higher education - degree (1st cycle)', '41 - Specialized higher studies course', '42 - Professional higher technical course', '43 - Higher Education - Master (2nd cycle)', '44 - Higher Education - Doctorate (3rd cycle)']
marital_status_options = ["1 - Single","2 - Married","3 - Widower","4 - Divorced", "5 - Facto union", "6 - Legally separated"]
previous_qualification_options = ['1 - Secondary education', "2 - Higher education - bachelor's degree", '3 - Higher education - degree', "4 - Higher education - master's", '5 - Higher education - doctorate', '6 - Frequency of higher education', '9 - 12th year of schooling - not completed', '10 - 11th year of schooling - not completed', '12 - Other - 11th year of schooling', '14 - 10th year of schooling', '15 - 10th year of schooling - not completed', '19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.', '38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.', '39 - Technological specialization course', '40 - Higher education - degree (1st cycle)', '42 - Professional higher technical course', '43 - Higher education - master (2nd cycle)']
nacionality_options = ['1 - Portuguese', '2 - German', '6 - Spanish', '11 - Italian', '13 - Dutch', '14 - English', '17 - Lithuanian', '21 - Angolan', '22 - Cape Verdean', '24 - Guinean', '25 - Mozambican', '26 - Santomean', '32 - Turkish', '41 - Brazilian', '62 - Romanian', '100 - Moldova (Republic of)', '101 - Mexican', '103 - Ukrainian', '105 - Russian', '108 - Cuban', '109 - Colombian']

st.header('Institutions App')
    

data = []

# Personal Information Section

st.write("Personal Information")

col1, col2, col3 = st.columns(3)
with col1:
    Gender = st.selectbox(label='Gender', options=["Male","Female"],index=0)
    data.append({"Gender": 1 if Gender == "Male" else 0})
    
with col2:
    Marital_status = st.selectbox(label='Marital Status', options=marital_status_options,index=0)
    data[-1]["Marital_status"] = Marital_status.split(" - ")[0]

with col3:
    Nacionality = st.selectbox(label='Nacionality', options=nacionality_options,index=0)
    data[-1]["Nacionality"] = Nacionality.split(" - ")[0]

col1, col2 = st.columns(2)

with col1:
    Fathers_occupation = st.selectbox(label='Father occupation', options=fathers_occupation_options,index=0)
    data[-1]["Fathers_occupation"] = Fathers_occupation.split(' - ')[0]

with col2:
    Fathers_qualification = st.selectbox(label='Father qualification', options=father_mother_qualification_options,index=0)
    data[-1]["Fathers_qualification"] = Fathers_qualification.split(' - ')[0]

col1, col2 = st.columns(2)

with col1:
    Mothers_occupation = st.selectbox(label='Mother occupation', options=mothers_occupation_options,index=0)
    data[-1]["Mothers_occupation"] = Mothers_occupation.split(' - ')[0]
 
with col2:
    Mothers_qualification = st.selectbox(label='Mother qualification', options=father_mother_qualification_options,index=0)
    data[-1]["Mothers_qualification"] = Mothers_qualification.split(' - ')[0]

# Application Information

st.write("Application Information")
col1, col2, col3 = st.columns(3)
with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime Evening att', options=["Day","Evening"], index=0)
    data[-1]["Daytime_evening_attendance"] = 1 if Daytime_evening_attendance == "Day" else 0

with col2:
    Previous_qualification = st.selectbox(label='Previous Qualification', options=previous_qualification_options,index=0)
    data[-1]["Previous_qualification"] = Previous_qualification.split(" - ")[0]

with col3:
    International = st.selectbox(label='International', options=["Yes","No"],index=0)
    data[-1]["International"] = 1 if International == "Yes" else 0


col1, col2 = st.columns(2)

with col1:
    Application_mode = st.selectbox(label='Application Mode', options=application_mode_options,index=0)
    data[-1]["Application_mode"] = Application_mode.split(" - ")[0]

with col2:
    Course = st.selectbox(label='Course', options=course_options,index=0)
    data[-1]["Course"] = Course.split(" - ")[0]

col1, col2 = st.columns(2)

with col1:
    Admission_grade = int(st.number_input(label='Admission Grade', value=100))
    data[-1]["Admission_grade"] = Admission_grade

with col2:
    Previous_qualification_grade = int(st.number_input(label='Previous Qualification Grade', value=1))
    data[-1]["Previous_qualification_grade"] = Previous_qualification_grade


col1, col2 = st.columns(2)
 
with col1:
    Displaced = st.selectbox(label='Displaced?', options=["Yes","No"],index=0)
    data[-1]["Displaced"] = 1 if Displaced == "Yes" else 0

with col2:
    Educational_special_needs = st.selectbox(label='Education Special Needs?', options=["Yes","No"],index=0)
    data[-1]["Educational_special_needs"] = 1 if Educational_special_needs == "Yes" else 0

# Financial Information

st.write("Financial Information")

col1, col2, col3 = st.columns(3)
 
with col1:
    Debtor = st.selectbox(label='Debtor?', options=["Yes","No"],index=0)
    data[-1]["Debtor"] = 1 if Debtor == "Yes" else 0
 

with col2:
    Scholarship_holder = st.selectbox(label='Scholarship Holder?', options=["Yes","No"],index=0)
    data[-1]["Scholarship_holder"] = 1 if Scholarship_holder == "Yes" else 0
 
with col3:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition Fees Up To Date?', options=["Yes","No"],index=0)
    data[-1]["Tuition_fees_up_to_date"] = 1 if Tuition_fees_up_to_date == "Yes" else 0

# Student Progress

st.write("Student Progress")

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular Units 1st Sem Enrolled', value=1))
    data[-1]["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular Units 1st Sem Evaluations', value=1))
    data[-1]["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular Units 1st Sem Approved', value=1))
    data[-1]["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col4:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular Units 1st Sem Grade', value=0))
    data[-1]["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular Units 2nd Sem Enrolled', value=0))
    data[-1]["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular Units 2nd Sem Evaluations', value=0))
    data[-1]["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular Units 2nd Sem Approved', value=0))
    data[-1]["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col4:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular Units 2nd Sem Grade', value=0))
    data[-1]["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    data[-1]["Application_order"] = Application_order

with col2:
    Age_at_enrollment = int(st.number_input(label='Age at Enrollment', value=18))
    data[-1]["Age_at_enrollment"] = Age_at_enrollment

with col3:
    Unemployment_rate = float(st.number_input(label='Unemployment Rate'))
    data[-1]["Unemployment_rate"] = Unemployment_rate

with col4:
    Inflation_rate = float(st.number_input(label='Inflation Rate'))
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