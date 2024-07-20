from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_gdrive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def backup_to_gdrive(local_file, drive_folder_id):
    drive = authenticate_gdrive()
    file_name = local_file.split('/')[-1]
    gfile = drive.CreateFile({'parents': [{'id': drive_folder_id}]})
    gfile.SetContentFile(local_file)
    gfile.Upload()
    return f"Uploaded {local_file} to Google Drive."

def download_from_gdrive(file_id, local_path):
    drive = authenticate_gdrive()
    gfile = drive.CreateFile({'id': file_id})
    gfile.GetContentFile(local_path)
    return f"Downloaded {file_id} to {local_path}."
