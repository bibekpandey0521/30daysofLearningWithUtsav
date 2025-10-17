with open("sample.txt","r") as file:
    content = file.read()
    print(content)
print("\n--- Strip ---")    
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())    

with open("sample.txt","r")  as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())       