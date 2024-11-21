from airflow.decorators import task, dag
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split

SERVICE_ACCOUNT_FILE = '/opt/airflow/data/creds.json'
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    "https://www.googleapis.com/auth/spreadsheets"
]

# File and folder details
INPUT_FILE_ID = "1fnY4_r2fH-HIN5W8Fh8iO_zIMTOBrqBAJdjLj5AZL6U"
OUTPUT_FOLDER_ID = "1Y4ZjDn5cJDPDxNve0_vV3d32YU-rUhf_"
OUTPUT_70_FILE_NAME = "data_70.csv"
OUTPUT_30_FILE_NAME = "data_30.csv"

def create_google_drive_service():
    """Authenticate and create a Google Drive service instance."""
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

def create_google_sheets_service():
    """Authenticate and create a Google Sheets service instance."""
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('sheets', 'v4', credentials=credentials)

@task
def load_data_from_drive():
    """Load data from Google Sheets and convert it into a CSV."""
    try:
        service = create_google_sheets_service()

        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=INPUT_FILE_ID, range="spotify_tracks")
            .execute()
        )
        values = result.get("values", [])
        rows = values[1:]
        columns = values[0]
        df = pd.DataFrame(rows, columns=columns)

        local_file_path = '/tmp/input_data.csv'
        df.to_csv(local_file_path, index=False)

        return df.to_dict()

    except HttpError as error:
        raise RuntimeError(f"An error occurred while accessing the Google Sheet: {error}")


@task
def split_data(data: dict):
    """Split data into 70-30 and save to temporary files."""
    df = pd.DataFrame.from_dict(data)

    train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)

    train_path = f"/tmp/{OUTPUT_70_FILE_NAME}"
    test_path = f"/tmp/{OUTPUT_30_FILE_NAME}"

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    return {"train_path": train_path, "test_path": test_path}


@task
def save_to_drive(paths: dict):
    """Upload split files back to Google Drive."""
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
            media = MediaFileUpload(local_path, mimetype='text/csv')
            service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        upload_file(paths["train_path"], OUTPUT_70_FILE_NAME)

        upload_file(paths["test_path"], OUTPUT_30_FILE_NAME)

    except HttpError as error:
        raise RuntimeError(f"An error occurred while uploading files: {error}")

@dag(
    dag_id="first_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def producer_dag():
    data = load_data_from_drive()
    paths = split_data(data)
    save_to_drive_task = save_to_drive(paths)

    trigger_second_dag = TriggerDagRunOperator(
        task_id='trigger_second_dag',
        trigger_dag_id='second_dag',
        conf={},
    )

    save_to_drive_task >> trigger_second_dag


producer_dag = producer_dag()
