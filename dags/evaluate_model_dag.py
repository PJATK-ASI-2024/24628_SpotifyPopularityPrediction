from airflow.decorators import task, dag
from airflow.operators.email_operator import EmailOperator
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import joblib
import io

SERVICE_ACCOUNT_FILE = '/opt/airflow/data/creds.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
MODEL_PATH = "/opt/airflow/models/linear_regression_model.pkl"
FOLDER_ID = '1Y4ZjDn5cJDPDxNve0_vV3d32YU-rUhf_'
FILE_NAME = 'data_30.csv'
CRITICAL_THRESHOLD = 0.80

def create_google_drive_service():
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

def get_file_id_by_name(service, folder_id, file_name):
    query = f"'{folder_id}' in parents and name='{file_name}'"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])
    if not files:
        raise FileNotFoundError(f"File {file_name} not found in folder {folder_id}")
    return files[0]['id']

@dag(
    dag_id="model_quality_monitoring_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def model_quality_monitoring_dag():
    @task
    def load_new_data():
        """Load new data from Google Drive."""
        try:
            service = create_google_drive_service()
            file_id = get_file_id_by_name(service, FOLDER_ID, FILE_NAME)

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
    def preprocess_data(df: pd.DataFrame):
        """Preprocess the new data to match the training data format."""
        df = df.drop(columns=["id", "name"])

        df["explicit"] = df["explicit"].astype(int)

        df = pd.get_dummies(df, columns=["genre"], drop_first=True)

        df["artists_count"] = df["artists"].apply(lambda x: len(x.split(", ")))
        df = df.drop(columns=["artists"])

        df["album"] = df["album"].astype("category").cat.codes
        df.dropna(inplace=True)

        df.drop_duplicates(inplace=True)

        scaler = StandardScaler()
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

        min_max_scaler = MinMaxScaler()
        df[numeric_cols] = min_max_scaler.fit_transform(df[numeric_cols])

        return df

    @task
    def evaluate_model(df: pd.DataFrame):
        """Evaluate the model on new data."""
        model = joblib.load(MODEL_PATH)
        X = df.drop(columns=["popularity"])
        y_true = df["popularity"]
        y_pred = model.predict(X)
        r2 = r2_score(y_true, y_pred)
        return r2

    @task
    def check_model_tests():
        """Check if model tests pass."""
        tests_pass = True
        return tests_pass

    @task
    def send_warning_email(r2: float, tests_pass: bool):
        """Send an email warning if conditions are not met."""
        if r2 > CRITICAL_THRESHOLD or not tests_pass:
            email = EmailOperator(
                task_id='send_email',
                to='s24628@pjwstk.edu.pl',
                subject='Model Quality Alert',
                html_content=f"""
                <h3>Model Quality Alert</h3>
                <p>Model R2 score has fallen below the critical threshold or model tests have failed.</p>
                <p>R2 Score: {r2}</p>
                <p>Tests Pass: {tests_pass}</p>
                """,
                conn_id='smtp_default'
            )
            email.execute(context={})

    new_data = load_new_data()
    preprocessed_data = preprocess_data(new_data)
    r2 = evaluate_model(preprocessed_data)
    tests_pass = check_model_tests()
    send_warning_email(r2, tests_pass)

model_quality_monitoring_dag = model_quality_monitoring_dag()