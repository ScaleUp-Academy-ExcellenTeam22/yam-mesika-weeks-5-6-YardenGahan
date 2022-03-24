import os

"""
 This functions receives a path from the user, then prints all the 
 files names that starts with the word "deep"

 @param path - string which is path to location in the computer
"""


def print_files(path):
    dir_files_list = os.listdir(path)  # get a list of all files names in the wanted dir

    print([file_name for file_name in dir_files_list if file_name.startswith("deep")])


dir_path = input("Enter Directory path: ")  # take input from user
print_files(dir_path)
