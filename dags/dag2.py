from airflow.decorators import task, dag
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import io

SERVICE_ACCOUNT_FILE = '/opt/airflow/data/creds.json'
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    "https://www.googleapis.com/auth/spreadsheets"
]

CLEAN_DATA_PATH = "cleaned_data.csv"
OUTPUT_FOLDER_ID = "1Y4ZjDn5cJDPDxNve0_vV3d32YU-rUhf_"
INPUT_FILE_NAME = "data_70.csv"


def create_google_drive_service():
    """Authenticate and create a Google Drive service instance."""
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)


@task
def download_file_from_drive():
    """Download the 'data_70.csv' file from Google Drive."""
    try:
        service = create_google_drive_service()

        query = f"'{OUTPUT_FOLDER_ID}' in parents and name='{INPUT_FILE_NAME}'"
        results = service.files().list(q=query, fields="files(id)").execute()
        files = results.get('files', [])

        if not files:
            raise FileNotFoundError(f"File {INPUT_FILE_NAME} not found in Google Drive")

        file_id = files[0]['id']

        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        fh.seek(0)
        df = pd.read_csv(fh)
        return df

    except HttpError as error:
        raise RuntimeError(f"An error occurred while accessing the Google Drive file: {error}")


@task
def clean_data(df: pd.DataFrame):
    """Clean data by handling missing values, duplicates, and scaling features."""
    df.dropna(inplace=True)

    df.drop_duplicates(inplace=True)

    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    min_max_scaler = MinMaxScaler()
    df[numeric_cols] = min_max_scaler.fit_transform(df[numeric_cols])

    return df


@task
def save_to_drive(df: pd.DataFrame):
    """Upload the cleaned and processed data to Google Drive, overwrite if exists."""
    try:
        service = create_google_drive_service()

        local_file_path = "/tmp/" + CLEAN_DATA_PATH
        df.to_csv(local_file_path, index=False)

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

        upload_file(local_file_path, CLEAN_DATA_PATH)

    except HttpError as error:
        raise RuntimeError(f"An error occurred while uploading files: {error}")


@dag(
    dag_id="second_dag",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def data_cleaning_dag():
    """Fetch the 'data_70.csv' file, clean it, and save processed data to Google Sheets/Drive."""
    df = download_file_from_drive()
    cleaned_df = clean_data(df)
    save_to_drive(cleaned_df)


data_cleaning_dag = data_cleaning_dag()
