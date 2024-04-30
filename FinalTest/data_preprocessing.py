import joblib
import numpy as np
import pandas as pd

pca_1 = joblib.load("./model/pca_1.joblib")
pca_2 = joblib.load("./model/pca_2.joblib")
scaler_Age_at_enrollment = joblib.load("./model/scaler_Age_at_enrollment.joblib")
scaler_Application_order = joblib.load("./model/scaler_Application_order.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("./model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("./model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("./model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("./model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("./model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("./model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("./model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("./model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_GDP = joblib.load("./model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("./model/scaler_Inflation_rate.joblib")
scaler_Unemployment_rate = joblib.load("./model/scaler_Unemployment_rate.joblib")

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
  "Application_order",
  "Age_at_enrollment",
  "Unemployment_rate",
  "Inflation_rate",
  "GDP"
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
    
    # df["Age"] = scaler_Age.transform(np.asarray(data["Age"]).reshape(-1,1))[0]
    
    # df["Credit_Mix"] = encoder_target.transform(data["Credit_Mix"])[0]
    # df["Payment_of_Min_Amount"] = encoder_Payment_of_Min_Amount.transform(data["Payment_of_Min_Amount"])
    # df["Payment_Behaviour"] = encoder_Payment_Behaviour.transform(data["Payment_Behaviour"])
    
    # PCA 1
    data["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]


    df[["pc1_1", "pc1_2", "pc1_3", "pc1_4", "pc1_5"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    # PCA 2
    data["Application_order"] = scaler_Application_order.transform(np.asarray(data["Application_order"]).reshape(-1,1))[0]
    data["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    data["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]
    data["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]

    df[["pc2_1", "pc2_2"]] = pca_2.transform(data[pca_numerical_columns_2])
    
    return df