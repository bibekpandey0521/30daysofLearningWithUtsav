### Binary Files
data = b'\x00\x01\x02\x03\x04'
# with open('example.bin','wb') as file:
#     file.write(data)


# with open('example.bin','rb') as file:
#     content = file.read()
#     print(content)


### Read the content from a source file and write to a destination text file
# Copying a file
with open('example.txt','r') as source_file:
    content = source_file.read()

with open('destination.txt','w') as destination_file:
    destination_file.write(content)    


