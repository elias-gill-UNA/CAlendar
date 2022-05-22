import sqlite3

def nuevoProyecto(proyecto, id): # nombre del proyecto
    conn = sqlite3.connect(f'../proyects/{id}.db') # crea la base de datos 
    cursor = conn.cursor()

    # Crear las tablas necesarias para el proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Descripcion (name TEXT, desc TEXT, fechaInicio TEXT, actiCount INT, depCount INT)") #  tabla de descripcion del proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Actividades (id INT, name TEXT, duracion INT, fechaTemp TEXT, fechaTar Text, finalizado INT)") # tabla de actividades
    cursor.execute("CREATE TABLE IF NOT EXISTS Dependencias (id INT, idAntes TEXT, idDespues TEXT)") # tabla de Dependecias

    # Llenado de los campos de identificacion del proyecto
    cursor.execute("INSERT INTO Descripcion (name, desc, fechaInicio, actiCount, depCount) VALUES (?, ?, ?, ?, ?)", 
              (proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto, 0, 0))

    # Proyecto creado satisfactoriamente
    conn.commit()
    cursor.close()
    return True 

# retorna la tabla de informacion del proyecto
def getInfo(id, conexion):
    if(conexion): # si se tiene una conexion establecida
        conexion.execute('SELECT * FROM Descripcion')
        data = conexion.fetchall()
        return data
        
    conn = sqlite3.connect(f'../proyects/{id}.db') # si es que no 
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Descripcion')
    data = cursor.fetchall()
    cursor.close()
    return data

def modificarValor(conexion, tabla, parametro, valor, condicion):
    conexion.execute(f"UPDATE {tabla} SET {parametro} = {valor} {condicion}") # cambiar el valor en alguna tabla
    conexion.commit()
    return True

def abrirProyecto(id):
    conn = sqlite3.connect(f'../proyects/{id}.db') # abre el proyecto
    cursor = conn.cursor()
    return cursor # retorna la conexion al proyecto

def cerrarProyecto(cursor):
    cursor.close()
    return True


#     c.execute("INSERT INTO tabla1 (palabraclave, valor) VALUES (?, ?)", (keyword, value))
#     conn.commit()

#     c.execute('SELECT * FROM tabla1')
#     data = c.fetchall()

