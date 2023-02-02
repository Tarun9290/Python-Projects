#File Renamer

import os

def rename_files(folder_path, old_prefix, new_prefix):
    for filename in os.listdir(folder_path):
        if filename.startswith(old_prefix):
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, filename.replace(old_prefix, new_prefix, 1))
            os.rename(old_file_path, new_file_path)

folder_path = input("Enter the folder path: ")
old_prefix = input("Enter the old prefix: ")
new_prefix = input("Enter the new prefix: ")

rename_files(folder_path, old_prefix, new_prefix)
