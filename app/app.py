from flask import Flask, request, jsonify
import joblib
import pandas as pd
from data_cleaning import clean_data
from drive_service import download_model_from_drive

app = Flask(__name__)

MODEL_PATH = "./linear_regression_model.pkl"

# Download the model before starting the app
download_model_from_drive(MODEL_PATH)

# Load the trained model
model = joblib.load(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    cleaned_df = clean_data(df, model.feature_names_in_)
    prediction = model.predict(cleaned_df)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)