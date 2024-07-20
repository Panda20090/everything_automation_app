import shutil
import os

def backup_database():
    source = 'data/data_automation.db'
    destination = 'backup/data_automation_backup.db'
    if not os.path.exists('backup'):
        os.makedirs('backup')
    shutil.copyfile(source, destination)
    return destination

def restore_database():
    source = 'backup/data_automation_backup.db'
    destination = 'data/data_automation.db'
    if os.path.exists(source):
        shutil.copyfile(source, destination)
        return destination
    else:
        return None
