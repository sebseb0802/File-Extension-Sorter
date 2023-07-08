import os
import shutil

directory = input("Enter the entire path of the directory that you wish to get sorted: ")

file_extensions = {
    "png": "Photos",
    "jpg": "Photos",
    "jpeg": "Photos",
    "wav": "Music",
    "mov": "Videos",
    "txt": "Text Files"
}
        
for filename in os.listdir(directory):
    for k, v in file_extensions.items():
        if filename.endswith(k):
            destination_folder = os.path.join(directory, v)
            os.makedirs(destination_folder, exist_ok=True)  # Create the destination folder if it doesn't exist
            shutil.move(os.path.join(directory, filename), os.path.join(directory, v, filename))