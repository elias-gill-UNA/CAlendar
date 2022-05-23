import sqlite3

def nuevoProyecto(proyecto, id): # nombre del proyecto
    conn = sqlite3.connect(f'../proyects/{id}.db') # crea la base de datos 
    cursor = conn.cursor()

    # Crear las tablas necesarias para el proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Descripcion (nombre TEXT, descripcion TEXT, fechaInicio TEXT, actiCount INT, depCount INT)") #  tabla de descripcion del proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Actividades (id integer primary key, nombre TEXT, duracion INT, fechaPrevista TEXT, fechaTardia TEXT, finalizado INT)") # tabla de actividades
    cursor.execute("CREATE TABLE IF NOT EXISTS Dependencias (id INT, idAntes TEXT, idDespues TEXT)") # tabla de Dependecias

    # Llenado de los campos de identificacion del proyecto
    cursor.execute("INSERT INTO Descripcion (nombre, descripcion, fechaInicio, actiCount, depCount) VALUES (?, ?, ?, ?, ?)", 
              (proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto, 0, 0))

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
        
    conn = sqlite3.connect(f'../proyects/{id}.db') # si es que no 
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Descripcion')
    data = cursor.fetchall()
    conn.close()
    return data

def modificarValor(conexion, parametro, valor):
    cursor = conexion.cursor
    cursor.execute(f"UPDATE Descripcion SET {parametro} = {valor}") # cambiar el valor en alguna tabla
    conexion.commit()
    cursor.close()
    return True

def abrirProyecto(id):
    conn = sqlite3.connect(f'../proyects/{id}.db') # abre el proyecto
    return conn # retorna la conexion al proyecto

def cerrarProyecto(conexion):
    conexion.close()
    return True


