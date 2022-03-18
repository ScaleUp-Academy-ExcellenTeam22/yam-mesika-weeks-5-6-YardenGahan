import os

# input: path to a directory.
# output: files names starts with "deep"

dir_path = input("Enter Directory path: ")  # take input from user

dir_files_list = os.listdir(dir_path)  # get a list of all files names in the wanted dir

# print the file name if it starts with "deep"
for file_name in dir_files_list:
    if file_name.startswith("deep"):
        print(file_name)
