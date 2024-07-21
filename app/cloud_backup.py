from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_gdrive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def backup_to_gdrive(local_file, drive_folder_id):
    drive = authenticate_gdrive()
    file_name = os.path.basename(local_file)
    gfile = drive.CreateFile({'parents': [{'id': drive_folder_id}], 'title': file_name})
    gfile.SetContentFile(local_file)
    gfile.Upload()
    return f"File {local_file} uploaded to Google Drive."

def download_from_gdrive(file_id, local_path):
    drive = authenticate_gdrive()
    gfile = drive.CreateFile({'id': file_id})
    gfile.GetContentFile(local_path)
    return f"File {file_id} downloaded from Google Drive to {local_path}."
