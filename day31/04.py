### using the os module
import os
cwd = os.getcwd()
print(f"Current working directory is {cwd}")

## create a new directory
new_directory = "package"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' create")