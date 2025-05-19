# TRACK, BACKUP, ROLLBACK
import shutil
import os
from datetime import datetime

BACKUP_DIR = 'backups'

def backup_comfig(file_path):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.basename(file_path)
    backup_name = f'{timestamp}_{file_name}'
    backup_path = os.path.join(BACKUP_DIR, backup_name)


    shutil.copy(file_path, backup_path)
    return backup_path

def list_backups(file_name):
    if not os.path.exists(BACKUP_DIR):
        return []
    return [f for f in os.listdir(BACKUP_DIR) if file_name in f]

def rollback_config(file_path, backup_file):
    backup_path = os.path.join(BACKUP_DIR, backup_file)
    shutil.copy(backup_path, file_path)