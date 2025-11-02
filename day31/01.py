### Read a Whole File

# with open('example.txt','r') as file:
#     content = file.read()
#     print(content)


###  Read  a file line by line
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip()) ## sstrip() removes the new line character


# ## Writing a file(Overwriting)

# with open('example.txt','w')  as file:
#     file.write('Hello World!\n')
#     file.write('this is  a new line.')

## Write a file(without Overwriting)
# with open('example.txt','a') as file:
#     file.write("\nAppend operand taking place!\n")

### Writing a list of lines to a file
lines = ['First Line \n','Second Line \n','Third Line\n']
with open('example.txt','a') as file:
    file.writelines(lines)
    