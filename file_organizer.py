import os
import shutil

# ===== SELECT FOLDER PATH =====
# Change this path to the folder you want to organize

path = r"C:\Users\Tyagi\Downloads"

# ===== FILE TYPE CATEGORIES =====

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Documents": [".docx", ".txt", ".pptx", ".xlsx"],
    "Programs": [".exe", ".msi"],
    "Zip_Files": [".zip", ".rar"]
}

# ===== GET ALL FILES =====

files = os.listdir(path)

# ===== ORGANIZE FILES =====

for file in files:

    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    moved = False

    # Check category
    for folder_name, extensions in file_types.items():

        if extension in extensions:

            folder_path = os.path.join(path, folder_name)

            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, file))

            print(f"{file} moved to {folder_name}")

            moved = True
            break

    # Files with unknown extension
    if not moved:

        other_folder = os.path.join(path, "Others")

        if not os.path.exists(other_folder):
            os.mkdir(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))

        print(f"{file} moved to Others")

print("\nFiles organized successfully!")