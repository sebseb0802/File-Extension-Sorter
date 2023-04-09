import os
import shutil

directory = os.path.join("C:", os.sep, "Users", "S.Pabst", "Documents")

file_extensions = {
    "png": "Photos",
    "jpg": "Photos",
    "jpeg": "Photos",
    "wav": "Music",
    "mov": "Videos",
    "txt": "Text Files"
}

"""for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    if os.path.isfile(f):
        print(f)"""
        
for filename in os.listdir(directory):
    for k, v in file_extensions.items():
        if filename.endswith(k):
            shutil.move(directory, f"\\{v}\\{filename}")