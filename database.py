import sqlite3
connection = sqlite3.connect("student_details.db")
print("Database opened successfully")
cursor = connection.cursor()

connection.execute("create table Student_Info (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, father_name TEXT NOT NULL,mother_name TEXT NOT NULL,age TEXT NOT NULL,address TEXT NOT NULL, reg_date TEXT NOT NULL)")
print("Table created successfully")
connection.close()
