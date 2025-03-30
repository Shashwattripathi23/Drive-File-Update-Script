# Google Drive File Update Script

## Description
A Python script to automatically update any file on Google Drive while keeping the same shared link. This ensures that the latest version is always accessible without changing the file ID.

## Features
✅ Works with any file type (PDF, DOCX, images, etc.).  
✅ Uses Google Drive API for seamless file replacement.  
✅ Keeps the same shared link, making updates invisible to users.  
✅ Securely stores file credentials in a `keys.py` file (ignored by Git).  

## Setup Instructions

### 1. Enable Google Drive API
- Go to [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Google Drive API** for your project.
- Create a **Service Account** and download the JSON key.

### 2. Share the Target File with the Service Account
- Right-click the file in Google Drive → **Share**.
- Add the **service account email** (found in the JSON key).
- Give it **Editor** permissions.

### 3. Create a `keys.py` File (Ignored in Git)
Inside your project folder, create a `keys.py` file and add:

```python
SERVICE_ACCOUNT_FILE = "your-service-account.json"  # Path to the JSON key
FILE_ID = "your_google_drive_file_id"  # Get this from the Drive link
RESUME_FILE_PATH = "path_to_your_file"  # Local file path
```

⚠️ **Important:**  
- Do **not** commit `keys.py` to Git. Add it to `.gitignore` to keep credentials safe.
- Example `.gitignore` entry:
  ```
  keys.py
  your-service-account.json
  ```

### 4. Install Dependencies
Run the following command to install required dependencies:

```sh
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

### 5. Run the Script
Execute the script using:

```sh
python script.py
```

