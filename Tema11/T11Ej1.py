import sqlite3

conn = sqlite3.connect('T11E1.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute("CREATE TABLE Alumnos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL)")

# Introducir datos
cursor.execute("INSERT INTO Alumnos VALUES (1,'Guiomar','Bobadilla')")
cursor.execute("INSERT INTO Alumnos VALUES (2,'Diana','Prince')")
cursor.execute("INSERT INTO Alumnos VALUES (3,'Wanda','Maximoff')")
cursor.execute("INSERT INTO Alumnos VALUES (4,'Thor','Odinson')")
cursor.execute("INSERT INTO Alumnos VALUES (5,'Harley','Quinn')")
cursor.execute("INSERT INTO Alumnos VALUES (6,'Natasha','Romanoff')")
cursor.execute("INSERT INTO Alumnos VALUES (7,'Bruce','Wayne')")
cursor.execute("INSERT INTO Alumnos VALUES (8,'Arthur','Curry')")
conn.commit()

# Hacer consulta
query = "SELECT * FROM Alumnos where nombre = 'Wanda'"
rows = cursor.execute(query)
data = rows.fetchall()
print("Resultado: ", data)

cursor.close()
conn.close()