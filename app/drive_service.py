from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import io

SERVICE_ACCOUNT_FILE = './creds.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
OUTPUT_FOLDER_ID = "1Y4ZjDn5cJDPDxNve0_vV3d32YU-rUhf_"

def create_google_drive_service():
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

def download_model_from_drive(model_path):
    """Download the linear_regression_model.pkl file from Google Drive."""
    try:
        service = create_google_drive_service()

        query = f"'{OUTPUT_FOLDER_ID}' in parents and name='model.pkl'"
        results = service.files().list(q=query, fields="files(id)").execute()
        files = results.get('files', [])

        if not files:
            raise FileNotFoundError("File model.pkl not found in Google Drive")

        file_id = files[0]['id']

        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)
        with open(model_path, "wb") as f:
            f.write(fh.read())

    except HttpError as error:
        raise RuntimeError(f"An error occurred while accessing the Google Drive file: {error}")