import os
import glob
import datetime

def rename_files_with_number(directory):
    # Get all files in the directory
    file_list = glob.glob(os.path.join(directory, '*'))

    # Sort the file list in ascending order based on modification date
    file_list.sort(key=lambda x: os.path.getmtime(x))

    # Calculate the number of digits for zero-padding, based on the total number of files
    num_digits = len(str(len(file_list)))

    # Rename files
    for index, file_path in enumerate(file_list):
        # Get the file extension
        file_extension = os.path.splitext(file_path)[1]

        # Construct the new file name
        new_file_name = f"{str(index + 1).zfill(num_digits)}{os.path.basename(file_path)}"

        # Construct the new file path
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)

        print(f"Renamed: {file_path} --> {new_file_path}")

# Provide the directory path
directory_path = "/path/to/directory"

# Call the function to rename files
rename_files_with_number(directory_path)
