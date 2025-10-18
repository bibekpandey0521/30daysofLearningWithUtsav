with open("journal.txt","w") as file:
    file.write("Day 1: Today I learned about writing files in Python. \n")


with open("journal.txt","a") as file:
    file.write("Day 2: I built a journal logger today! \n")


try:
    with open("/restricted/journal.txt",'w') as file:
        file.write("Test Entry")
except PermissionError:
    print("You do not have permission to write to the file.")        