try:
    with open("sample.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

print("\n")
try:
    with open("non_existent_file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")


