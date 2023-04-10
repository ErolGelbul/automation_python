import os
import shutil

# Change the desktop_path to match the path to your desktop
desktop_path = "/path/to/your/desktop"

# List of extensions and their corresponding folder names
folders = {
    "mp4": "mp4",
    "mp3": "mp3",
    "pdf": "pdf",
    # Add more folders and extensions as needed
}


def move_file(file, ext):
    destination_folder = os.path.join(desktop_path, folders[ext])
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))


def organize_files():
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            file_ext = filename.split(".")[-1]
            if file_ext in folders:
                move_file(file_path, file_ext)


if __name__ == "__main__":
    organize_files()
