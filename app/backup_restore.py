import shutil
import os

def backup_database():
    source = 'data/users.db'
    destination = 'data/backup/users_backup.db'
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copyfile(source, destination)
    return destination

def restore_database():
    source = 'data/backup/users_backup.db'
    destination = 'data/users.db'
    if os.path.exists(source):
        shutil.copyfile(source, destination)
        return source
    return None
