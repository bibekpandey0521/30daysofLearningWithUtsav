import os
dir_name  = "folder"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

path = 'example.txt'
if os.path.exists('example.txt'):
    print(f"The path '{path}' exists")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory")
else:
    print(f"The path '{path}' does not exists")    


## Get the absoulte path
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

path = 'example1.txt'
if os.path.exists(path):
    print(f"The path '{path}' exists")
else:
    print(f"The path '{path}' does not exixsts")    