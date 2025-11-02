### Writing and then reading a file

with open('example.txt','w+') as file:
    file.write("Hello World\n")
    file.write("This is a new line \n")

    ## Move the file cursor to the begining
    file.seek(0)

    ## Read the content of the file
    content = file.read()
    print(content)