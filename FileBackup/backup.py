# pip install schedule
import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/Teodor/Pictures/Saved Pictures"
destination_dir = "C:/Users/Teodor/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        # Copy the entire folder to the destination
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        # Handle the case when the destination folder already exists
        print(f"Folder already exists in: {dest}")

# Schedule the folder copy operation every day at a specific time
schedule.every().day.at("12:17").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Run the scheduled tasks continuously
while True:
    schedule.run_pending()
    time.sleep(60)
