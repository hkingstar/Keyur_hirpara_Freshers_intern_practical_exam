'''
5. Provide a program to create tables (Employee, Department, 
Project) in database Sqlite and insert the data.
• Make sure to add basic field, with employee to department and project relation. 
• Make sure maintain M2M relation between employee and project. 

'''

import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create the Employee table
cursor.execute("CREATE TABLE Employee (id INTEGER PRIMARY KEY, name TEXT, department_id INTEGER, FOREIGN KEY (department_id) REFERENCES Department(id))")

# Create the Department table
cursor.execute("CREATE TABLE Department (id INTEGER PRIMARY KEY, name TEXT)")

# Create the Project table
cursor.execute("CREATE TABLE Project (id INTEGER PRIMARY KEY, name TEXT)")

# Create the Employee_Project table to maintain the M2M relation between Employee and Project
cursor.execute("CREATE TABLE Employee_Project (employee_id INTEGER, project_id INTEGER, FOREIGN KEY (employee_id) REFERENCES Employee(id), FOREIGN KEY (project_id) REFERENCES Project(id))")

# Insert some data into the tables
cursor.execute("INSERT INTO Department (id, name) VALUES (1, 'IT')")
cursor.execute("INSERT INTO Department (id, name) VALUES (2, 'Marketing')")

cursor.execute("INSERT INTO Employee (id, name, department_id) VALUES (1, 'John', 1)")
cursor.execute("INSERT INTO Employee (id, name, department_id) VALUES (2, 'Jane', 1)")
cursor.execute("INSERT INTO Employee (id, name, department_id) VALUES (3, 'Bob', 2)")

cursor.execute("INSERT INTO Project (id, name) VALUES (1, 'Project A')")
cursor.execute("INSERT INTO Project (id, name) VALUES (2, 'Project B')")

cursor.execute("INSERT INTO Employee_Project (employee_id, project_id) VALUES (1, 1)")
cursor.execute("INSERT INTO Employee_Project (employee_id, project_id) VALUES (1, 2)")
cursor.execute("INSERT INTO Employee_Project (employee_id, project_id) VALUES (2, 1)")

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
