import os
from datetime import datetime, timedelta

def clean_up_folder(folder_path, days_to_keep):
    min_date = datetime.now() - timedelta(days=days_to_keep)

    for root, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            modified_time = os.path.getmtime(file_path)
            last_modified_date = datetime.fromtimestamp(modified_time)

            if last_modified_date < min_date:
                print(f"Deleting old file: {file_path}")
                os.remove(file_path)

if __name__ == "__main__":
    folder_to_clean = '/path/to/folder'
    days_to_keep_files = 30
    clean_up_folder(folder_to_clean, days_to_keep_files)




