#Question 1
import os

def list_directory_contents(path):
    try:
        print(os.listdir(path))
    except Exception as e:
        print(f"An error occurred: {e}")


path = input("What is the path that you are looking for? ")
list_directory_contents(path)

#Task 2
def report_file_sizes(directory):
    try:
        for file in os.listdir(directory):
            file_path= os.path.join(directory, file)
            if os.path.isfile(file_path):
                size = os.stat(file_path).st_size
                print(f"The size for file: {file} is: {size}.")
            else:
                print(f"{file} is not a file.")
    except Exception as e:
        print(f"Error occurred: {e}.")
directory = input("What is the path that you are looking for? ") 
report_file_sizes(directory)

import re
#Task 3
def get_file_extension(directory):
    try:
        extension_list=[]
        pattern = r"\.(.+)\b"
        for file in os.listdir(directory):
            extension = re.search(pattern, file, re.IGNORECASE)
            extension_list.append(extension.group(1))
        return extension_list                

    except Exception as e:
        print(f"Error occured with directory: {e}")

def extension_amounts(directory):
    extension_dict={}
    extension_list= get_file_extension(user_directory)
    for extension in extension_list:
        if extension not in extension_dict:
            extension_dict[extension]= 1
        else:
            extension_dict[extension] +=1

    return extension_dict

user_directory = input("Enter your directory. ")

extensions = extension_amounts(user_directory)

for extension, quantity in extensions.items():
    print(f"Extension: '{extension}' appears {quantity} time(s) in the directory.")