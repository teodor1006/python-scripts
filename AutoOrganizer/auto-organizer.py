import os
import shutil

# Specify the folder path to organize
folder = '/path/to/folder'

# Define file extensions corresponding to different categories
extensions = {
    'Images': ['jpg', 'png', 'jpeg', 'svg'],
    'Documents': ['doc', 'docx', 'pdf', 'xls', 'ppt', 'txt'],
    'Video': ['mov', 'mp4', 'avi', 'wmv'],
    'Audio': ['wav', 'mp3']
}

# Loop through each item in the specified folder
for item in os.listdir(folder):
    # Split the filename and extension
    filename, extension = os.path.splitext(item)

    # Check if the item has an extension
    if extension:
        # Loop through the defined extensions for each category
        for folder_name, ext_list in extensions.items():
            # Check if the current extension matches any in the list
            if extension[1:] in ext_list:
                # Create a path for the destination folder
                folder_path = os.path.join(folder, folder_name)
                # Create the destination folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Move the file to the corresponding folder
                shutil.move(os.path.join(folder, item), folder_path)   