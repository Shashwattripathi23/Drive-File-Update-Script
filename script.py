from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import keys

SERVICE_ACCOUNT = keys.SERVICE_ACCOUNT_FILE

FILE_ID = keys.FILE_NAME
RESUME_FILE_PATH = keys.FILE_PATH
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT, scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=creds)


media = MediaFileUpload(RESUME_FILE_PATH, mimetype="application/pdf", resumable=True)
drive_service.files().update(fileId=FILE_ID, media_body=media).execute()

print("Resume updated successfully!")