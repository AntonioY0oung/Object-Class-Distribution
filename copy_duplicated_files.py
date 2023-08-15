import os
import json
import shutil

def find_and_replace_duplicated(old_folder, new_folder):
    old_files = os.listdir(old_folder)
    new_files = os.listdir(new_folder)

    duplicated_files = set(old_files) & set(new_files)

    for filename in duplicated_files:
        old_file_path = os.path.join(old_folder, filename)
        new_file_path = os.path.join(new_folder, filename)

        with open(old_file_path, 'r') as old_file:
            old_data = json.load(old_file)

        with open(new_file_path, 'w') as new_file:
            json.dump(old_data, new_file, indent=4)

if __name__ == "__main__":
    old_folder = "/Users/antonioyang/Documents/Python/copy_duplicated_file/old_file_annotated"
    new_folder = "/Users/antonioyang/Documents/Python/copy_duplicated_file/new_file_non-annotated"

    find_and_replace_duplicated(old_folder, new_folder)