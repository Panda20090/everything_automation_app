import dropbox

def upload_to_dropbox(local_file, dropbox_path, access_token):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path)
    return f"File {local_file} uploaded to Dropbox at {dropbox_path}."

def download_from_dropbox(dropbox_path, local_file, access_token):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file, 'wb') as f:
        metadata, res = dbx.files_download(path=dropbox_path)
        f.write(res.content)
    return f"File {dropbox_path} downloaded from Dropbox to {local_file}."
