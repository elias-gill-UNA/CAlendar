# --- Modulo en proceso ---
    #(id integer primary key, name TEXT, duracion INT, fechaPrevista TEXT, fechaTardia TEXT, finalizado INT) 

def nuevaActividad(conexion, actividad):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Actividades (nombre, duracion, dependencias, fechaPrevista, fechaTardia, finalizado) VALUES (?, ?, ?, ?, ?)",
              (actividad.nombre, actividad.duracion, actividad.dependecias, actividad.fechaInicioTemprano, actividad.fechaInicioTardio,
               actividad.finalizado)) # insertar nueva actividad
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
    data = conexion.fetchall()
    cursor.close()
    return data

def getInfoActividad(conexion, id): # si la actividad no existe retorna un array vacio
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM Actividades WHERE id={id}')
    data = conexion.fetchone()
    cursor.close()
    return data

def modificarActividad(conexion, id,actividad): # requiere conexion, nueva acti y id
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE Actividades SET (nombre, duracion, fechaPrevista, fechaTardia, finalizado) VALUES (?, ?, ?, ?, ?) WEHRE id={id}",
              (actividad.nombre, actividad.duracion, actividad.fechaInicioTemprano, actividad.fechaInicioTardio,
               actividad.finalizado)) # insertar nueva actividad
    conexion.commit() # guardar cambios
    cursor.close()
    return True


