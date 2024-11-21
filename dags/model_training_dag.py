from airflow.decorators import task, dag
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os
import io

SERVICE_ACCOUNT_FILE = '/opt/airflow/data/creds.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
CLEAN_DATA_PATH = "/tmp/cleaned_data.csv"
MODEL_PATH = "/tmp/model.pkl"
EVALUATION_REPORT_PATH = "/tmp/evaluation_report.txt"
OUTPUT_FOLDER_ID = "1Y4ZjDn5cJDPDxNve0_vV3d32YU-rUhf_"

def create_google_drive_service():
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

# DAG
@dag(
    dag_id="ml_model_training_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def ml_training_dag():
    """DAG to clean data, train ML model, and save model + evaluation report."""

    @task
    def download_cleaned_data():
        """Download the cleaned data file from Google Drive."""
        try:
            service = create_google_drive_service()

            query = f"'{OUTPUT_FOLDER_ID}' in parents and name='{os.path.basename(CLEAN_DATA_PATH)}'"
            results = service.files().list(q=query, fields="files(id)").execute()
            files = results.get('files', [])

            if not files:
                raise FileNotFoundError(f"File {os.path.basename(CLEAN_DATA_PATH)} not found in Google Drive")

            file_id = files[0]['id']

            request = service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()

            fh.seek(0)
            df = pd.read_csv(fh)
            return df

        except HttpError as error:
            raise RuntimeError(f"An error occurred while accessing the Google Drive file: {error}")

    @task
    def train_ml_model(df: pd.DataFrame):
        """Train and save an ML regression model."""
        # Separate features and target
        X = df.drop(columns=["popularity"])  # Features
        y = df["popularity"]  # Target

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Train regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict on test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Log metrics
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"Mean Absolute Error (MAE): {mae}")
        print(f"R-squared (R2): {r2}")

        # Save the model
        joblib.dump(model, "/opt/airflow/models/linear_regression_model.pkl")

        # Save metrics to a report file
        with open("/opt/airflow/reports/evaluation_report.txt", "w") as f:
            f.write(f"Mean Squared Error: {mse}\n")
            f.write(f"Mean Absolute Error: {mae}\n")
            f.write(f"R-squared: {r2}\n")

        return {
            "model_path": "/opt/airflow/models/linear_regression_model.pkl",
            "report_path": "/opt/airflow/reports/evaluation_report.txt"
        }

    @task
    def upload_files_to_drive(paths: dict):
        """Upload model and evaluation report to Google Drive."""
        try:
            service = create_google_drive_service()

            def upload_file(local_path, file_name):
                query = f"'{OUTPUT_FOLDER_ID}' in parents and name='{file_name}'"
                results = service.files().list(q=query, fields="files(id)").execute()
                files = results.get('files', [])

                if files:
                    file_id = files[0]['id']
                    service.files().delete(fileId=file_id).execute()

                file_metadata = {
                    'name': file_name,
                    'parents': [OUTPUT_FOLDER_ID]
                }

                media = MediaFileUpload(local_path, mimetype='text/plain' if file_name.endswith('.txt') else 'application/octet-stream')
                service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            upload_file(paths["model_path"], "model.pkl")
            upload_file(paths["report_path"], "evaluation_report.txt")

        except HttpError as error:
            raise RuntimeError(f"An error occurred while uploading files: {error}")

    # Task flow
    cleaned_data = download_cleaned_data()
    ml_outputs = train_ml_model(cleaned_data)
    upload_files_to_drive(ml_outputs)


ml_training_dag = ml_training_dag()
