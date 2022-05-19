import sqlite3
import os
import time
import random

def nuevaActividad(proyectId):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, name TEXT, desc TEXT, fecha TEXT)") # crea la descripcion del proyecto

    # llenamos los campos de identificacio del proyecto
    c.execute("INSERT INTO tabla1 (id, name, desc, fecha) VALUES (?, ?, ?, ?)", 
              (proyecto.identificador, proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto))
    return True 
