## Delete the data from the table

import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
    Delete from employees
               where name = 'Ramesh'
    '''
)

## commit changes 
connection.commit()

## Query the data from the table
cursor.execute('Select * from  employees')
rows  = cursor.fetchall()

## print the querried data
for row in rows:
    print(row)