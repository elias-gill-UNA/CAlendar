# --- Modulo en proceso ---
    #(id integer primary key, name TEXT, duracion INT, fechaPrevista TEXT, fechaTardia TEXT, finalizado INT) 

def nuevaActividad(conexion, actividad):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Actividades (nombre, duracion, dependencias) VALUES (?, ?, ?)",
              (actividad.nombre, actividad.duracion, actividad.dependencias)) # insertar nueva actividad
    conexion.commit() # guardar cambios
    cursor.close()
    return True

def eliminarActividad(conexion, id):
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM Actividades WHERE id={id}")
    conexion.commit() # guardar cambios
    cursor.close()
    return True

def getListaActividades(conexion): # retorna lista de actividades
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Actividades')
    data = cursor.fetchall()
    cursor.close()
    return data

def getInfoActividad(conexion, id): # si la actividad no existe retorna un array vacio
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM Actividades WHERE id={id}')
    data = cursor.fetchone()
    cursor.close()
    return data

def modificarActividad(conexion, id, actividad): # requiere conexion, nueva acti y id
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE Actividades SET nombre = ?, duracion = ?, dependencias = ? WHERE id={id}",
              (f"{actividad.nombre}", actividad.duracion, f"{actividad.dependencias}")) 
    conexion.commit() # guardar cambios
    cursor.close()
    return True


