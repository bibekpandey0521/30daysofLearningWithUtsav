import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

## Update the data in the table
cursor.execute(''' 
UPDATE employees 
Set age = 34
where name = "Ram"               
''')
connection.commit()

## Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

for row in rows:
    print(row)