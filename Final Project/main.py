from flask import Flask, request, Response
from pandas import json_normalize
from data_preprocessing import data_preprocessing
from prediction import prediction

app = Flask(__name__)
@app.route('/api/predict', methods=['POST'])
def handle_post():
    try :
        data_df = json_normalize(request.get_json())
        new_data = data_preprocessing(data=data_df)

        return {
            "Status" : prediction(new_data)
        }
    except KeyError as e: 
        return Response(e.args[0] + " is not found. Please provide this data !", status = "400")
    except :
        return Response("Something went wrong.",status="500")

if __name__ == '__main__':
    app.run(debug=True)