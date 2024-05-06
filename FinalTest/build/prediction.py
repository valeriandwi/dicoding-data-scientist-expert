import joblib

model = joblib.load("gboost_model.joblib")
result_target = joblib.load("encoder_target.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    result = model.predict(data.values)
    final_result = result_target.inverse_transform(result)[0]

    print(final_result)
    return final_result