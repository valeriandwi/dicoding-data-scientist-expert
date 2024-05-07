import joblib
import numpy as np
import pandas as pd
import os

dirname = os.path.dirname(__file__)

pca_1 = joblib.load(os.path.join(dirname, "model/pca_1.joblib"))
pca_2 = joblib.load(os.path.join(dirname, "model/pca_2.joblib"))
encoder_Application_mode = joblib.load(os.path.join(dirname, "model/encoder_Application_mode.joblib"))
encoder_Course = joblib.load(os.path.join(dirname, "model/encoder_Course.joblib"))
encoder_Daytime_evening_attendance = joblib.load(os.path.join(dirname, "model/encoder_Daytime_evening_attendance.joblib"))
encoder_Debtor = joblib.load(os.path.join(dirname, "model/encoder_Debtor.joblib"))
encoder_Displaced = joblib.load(os.path.join(dirname, "model/encoder_Displaced.joblib"))
encoder_Educational_special_needs = joblib.load(os.path.join(dirname, "model/encoder_Educational_special_needs.joblib"))
encoder_Fathers_occupation = joblib.load(os.path.join(dirname, "model/encoder_Fathers_occupation.joblib"))
encoder_Fathers_qualification = joblib.load(os.path.join(dirname, "model/encoder_Fathers_qualification.joblib"))
encoder_Gender = joblib.load(os.path.join(dirname, "model/encoder_Gender.joblib"))
encoder_International = joblib.load(os.path.join(dirname, "model/encoder_International.joblib"))
encoder_Marital_status = joblib.load(os.path.join(dirname, "model/encoder_Marital_status.joblib"))
encoder_Mothers_occupation = joblib.load(os.path.join(dirname, "model/encoder_Mothers_occupation.joblib"))
encoder_Mothers_qualification = joblib.load(os.path.join(dirname, "model/encoder_Mothers_qualification.joblib"))
encoder_Nacionality = joblib.load(os.path.join(dirname, "model/encoder_Nacionality.joblib"))
encoder_Previous_qualification = joblib.load(os.path.join(dirname, "model/encoder_Previous_qualification.joblib"))
encoder_Scholarship_holder = joblib.load(os.path.join(dirname, "model/encoder_Scholarship_holder.joblib"))
encoder_Tuition_fees_up_to_date = joblib.load(os.path.join(dirname, "model/encoder_Tuition_fees_up_to_date.joblib"))

scaler_Previous_qualification_grade = joblib.load(os.path.join(dirname, "model/scaler_Previous_qualification_grade.joblib"))
scaler_Admission_grade = joblib.load(os.path.join(dirname, "model/scaler_Admission_grade.joblib"))
scaler_Age_at_enrollment = joblib.load(os.path.join(dirname, "model/scaler_Age_at_enrollment.joblib"))
scaler_Application_order = joblib.load(os.path.join(dirname, "model/scaler_Application_order.joblib"))
scaler_Curricular_units_1st_sem_approved = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_1st_sem_approved.joblib"))
scaler_Curricular_units_1st_sem_enrolled = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_1st_sem_enrolled.joblib"))
scaler_Curricular_units_1st_sem_evaluations = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_1st_sem_evaluations.joblib"))
scaler_Curricular_units_1st_sem_grade = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_1st_sem_grade.joblib"))
scaler_Curricular_units_2nd_sem_approved = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_2nd_sem_approved.joblib"))
scaler_Curricular_units_2nd_sem_enrolled = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_2nd_sem_enrolled.joblib"))
scaler_Curricular_units_2nd_sem_evaluations = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_2nd_sem_evaluations.joblib"))
scaler_Curricular_units_2nd_sem_grade = joblib.load(os.path.join(dirname, "model/scaler_Curricular_units_2nd_sem_grade.joblib"))
scaler_GDP = joblib.load(os.path.join(dirname, "model/scaler_GDP.joblib"))
scaler_Inflation_rate = joblib.load(os.path.join(dirname, "model/scaler_Inflation_rate.joblib"))
scaler_Unemployment_rate = joblib.load(os.path.join(dirname, "model/scaler_Unemployment_rate.joblib"))

pca_numerical_columns_1 = [
  "Curricular_units_1st_sem_enrolled",
  "Curricular_units_1st_sem_evaluations",
  "Curricular_units_1st_sem_approved",
  "Curricular_units_1st_sem_grade",
  "Curricular_units_2nd_sem_enrolled",
  "Curricular_units_2nd_sem_evaluations",
  "Curricular_units_2nd_sem_approved",
  "Curricular_units_2nd_sem_grade",
]

pca_numerical_columns_2 = [
  "Admission_grade",
  "GDP",
  "Age_at_enrollment",
  "Previous_qualification_grade"
]

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    df["Application_mode"] = data["Application_mode"]
    df["Course"] = data["Course"]
    df["Daytime_evening_attendance"] = data["Daytime_evening_attendance"]
    df["Debtor"] = data["Debtor"]
    df["Displaced"] = data["Displaced"]
    df["Educational_special_needs"] = data["Educational_special_needs"]
    df["Fathers_occupation"] = data["Fathers_occupation"]
    df["Fathers_qualification"] = data["Fathers_qualification"]
    df["Gender"] = data["Gender"]
    df["International"] = data["International"]
    df["Marital_status"] = data["Marital_status"]
    df["Mothers_occupation"] = data["Mothers_occupation"]
    df["Mothers_qualification"] = data["Mothers_qualification"]
    df["Nacionality"] = data["Nacionality"]
    df["Previous_qualification"] = data["Previous_qualification"]
    df["Scholarship_holder"] = data["Scholarship_holder"]
    df["Tuition_fees_up_to_date"] = data["Tuition_fees_up_to_date"]

    df["Application_order"] = scaler_Application_order.transform(np.asarray(data["Application_order"]).reshape(-1,1))[0]
    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    df["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]

    data["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]


    df[["pc1_1", "pc1_2"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    # PCA 2
    data["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    data["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]
    data["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]

    df[["pc2_1", "pc2_2"]] = pca_2.transform(data[pca_numerical_columns_2])
    
    return df