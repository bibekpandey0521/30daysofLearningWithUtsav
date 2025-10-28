import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute(''' 
SELECT * FROM employees               
''')

## Insert the data in sqlite table
cursor.execute('''
Insert Into employees(name,age,department)
Values('Ram',32,'Math Teacher')
''')

cursor.execute(''' 
Insert Into employees(name,age,department)
VALUES('Ramesh',35,'Finance')               
''')
cursor.execute(''' 
Insert Into employees(name,age,department)
VALUES('Charlie',35,'Civil')               
''')

## commit changes
connection.commit()

## Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

## print the queried data

for row in rows:
    print(row)

## Update the data in the table
cursor.execute(''' 
UPDATE employees 
Set age = 34
where name = "Ram"               
''')
connection.commit()



