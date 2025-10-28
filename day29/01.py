import sqlite3
connection = sqlite3.connect('example.db')
print(connection)

cursor = connection.cursor()

# Create a Table
cursor.execute('''
Create Table If Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age integer,
    department text                    
     )
''')

## Commit the changes 
connection.commit()