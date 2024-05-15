from flask import Flask, request
from pandas import json_normalize
from data_preprocessing import data_preprocessing
from prediction import prediction

app = Flask(__name__)
@app.route('/api/predict', methods=['POST'])
def handle_post():
    data_df = json_normalize(request.get_json())
    new_data = data_preprocessing(data=data_df)

    return {
        "Status" : prediction(new_data)
    }

if __name__ == '__main__':
    app.run(debug=True)