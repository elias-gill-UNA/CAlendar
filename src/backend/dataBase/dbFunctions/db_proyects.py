import sqlite3
import os
path = os.path.expanduser("~") + '/CAlendar-database/proyects/'

def nuevoProyecto(proyecto, id): # nombre del proyecto
    conn = sqlite3.connect(f'{path}{id}.db') # crea la base de datos 
    cursor = conn.cursor()

    # Crear las tablas necesarias para el proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, nombre TEXT, descripcion TEXT, fechaInicio TEXT, actiCount INT, depCount INT, diasLaborales INT, holgura INT)") #  tabla de descripcion del proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Actividades (id INTEGER PRIMARY KEY, nombre TEXT, duracion INT, dependencias TEXT, fechaPrevista TEXT, fechaTardia TEXT, finalizado INT)") # tabla de actividades
    cursor.execute("CREATE TABLE IF NOT EXISTS Feriados (Fecha TEXT)") # tabla de Dependecias

    # Llenado de los campos de identificacion del proyecto
    cursor.execute("INSERT INTO Descripcion (id, nombre, descripcion, fechaInicio, actiCount, depCount, diasLaborales, holgura) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
              (id, proyecto.nombre, proyecto.descripcion, proyecto.fechaInicio, 0, 0, proyecto.diasLaborales, proyecto.holgura))

    # Proyecto creado satisfactoriamente
    conn.commit()
    conn.close()
    return True 

# retorna la tabla de informacion del proyecto
def getInfo(id, conexion):
    if(conexion): # si se tiene una conexion establecida
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Descripcion')
        data = cursor.fetchall()
        cursor.close()
        return data
        
    conn = sqlite3.connect(f'{path}{id}.db') # si es que no 
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Descripcion')
    data = cursor.fetchall()
    conn.close()
    return data

# actualiza un parametro concreto de la info del proyecto
def actualizarParametro(conexion, parametro, valor): 
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE Descripcion SET {parametro} = {valor}") 
    conexion.commit()
    cursor.close()
    return True

# retorna una conexion al proyecto
def abrirProyecto(id):
    conn = sqlite3.connect(f'{path}{id}.db') # conexion
    return conn 

# cierra la conexion
def cerrarProyecto(conexion):
    conexion.close()
    return True


