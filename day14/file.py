with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes1.txt","w") as file:
    file.write("\nThis is new note.\n")

with open("notes.txt","a") as file:
    file.write("\nThis is a new second note.\n")
        