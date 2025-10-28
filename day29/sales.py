## Working With Sales Data
import sqlite3

## Connect to an SQLite database

connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

## Create a table for sales data

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id  INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT                                            
)
''')

# Insert data into the sales table
sales_data = [
    ('2025-01-01','Product1',100,'North'),
    ('2025-01-02','Product2',200,'South'),
    ('2025-01-03','Product1',150,'East'),
    ('2025-01-04','Product3',250,'West'),
    ('2025-01-05','Product2',300,'North')
]

cursor.executemany('''
    Insert into sales(date,product,sales,region)
                   values(?,?,?,?)
''',sales_data)
connection.commit()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows  = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

## Close the connection
connection.close()    