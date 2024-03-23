import csv
import sqlite3

# connectiong to database
connection = sqlite3.connect('roster.db')

'''Creating a cursor object to execute
SQL queries on a database table'''
cursor = connection.cursor()

assignments = []
students = []
houses = []

# opening the students csv file
# reading the contents of the file
with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        houses.append([i[2], i[3]])
        students.append([i[1]])
        assignments.append([i[1], i[2]])

# creating a new list to put none reapeating values in
slim_houses = []
for i in houses:
    if i not in slim_houses:
        slim_houses.append(i)

# SQL query to insert data into tables
insert_students = 'INSERT INTO students (student_name) VALUES (?)'
insert_houses = ('INSERT INTO house (house, head) VALUES (?, ?)')
insert_assignments = ('INSERT INTO assignments (student_name, house) VALUES (?, ?)')

# importing contents of file into tables
cursor.executemany (insert_students, students[1:])
cursor.executemany(insert_houses, slim_houses[1:])
cursor.executemany(insert_assignments, assignments[1:])

'''SQL quey to retrieve all data from tables to verify data
of file has been successfully inserted into tabkle'''
select_students = 'SELECT * FROM students'
select_houses = 'SELECT * FROM house'
select_assignments = 'SELECT * FROM assignments'

studs = cursor.execute(select_students).fetchall()
hous = cursor.execute(select_houses).fetchall()
assigns = cursor.execute(select_assignments).fetchall()

# print tables
for s in studs:
    print(s)

for h in hous:
    print(h)

for a in assigns:
    print(a)

# commiting the changes
connection.commit()

# closing the databadse connection
connection.close()

