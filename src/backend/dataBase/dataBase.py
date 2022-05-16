import sqlite3
import os
import time
import random

def nuevoProyecto(proyecto, db): # nombre del proyecto
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, name TEXT, desc TEXT, fecha TEXT, actiCount INT, depCount INT)") # crea la descripcion del proyecto
    c.execute("CREATE TABLE IF NOT EXISTS Actividades (id INT, name TEXT, duracion INT, fechaTemp TEXT, fechaTar Text, finalizado INT)") # tabla de actividades
    c.execute("CREATE TABLE IF NOT EXISTS Dependecias (id INT, idAntes TEXT, idDespues TEXT)") # tabla de Dependecias

        # self.identificador=identificador
        # self.identificadorAntes=identificadorAntes
        # self.identificadorDespues=identificadorDespues






    # llenamos los campos de identificacion del proyecto
    c.execute("INSERT INTO Descripcion (id, name, desc, fecha, actiCount, depCount) VALUES (?, ?, ?, ?, ?, ?)", 
              (proyecto.identificador, proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto, 0, 0))
    return True 











def nuevaActividad(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, name TEXT, desc TEXT, fecha TEXT)") # crea la descripcion del proyecto

    # llenamos los campos de identificacio del proyecto
    c.execute("INSERT INTO tabla1 (id, name, desc, fecha) VALUES (?, ?, ?, ?)", 
              (proyecto.identificador, proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto))
    return True 
    




# for i in range(10):
#     dynamic_data_entry(i)
#     time.sleep(1)

# def dynamic_data_entry(i):
#     keyword = f'Numero {i}'
#     value = random.randrange(0,10)

#     c.execute("INSERT INTO tabla1 (palabraclave, valor) VALUES (?, ?)",
#               (keyword, value))
#     conn.commit()

# def read_from_db():
#     c.execute('SELECT * FROM tabla1')
#     data = c.fetchall()
#     print(data)
#     for row in data:
#         print(row)

# read_from_db()

    c.close
    conn.close()

