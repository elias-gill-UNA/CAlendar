# si no existe retorna un array vacio
def getFeriado(conexion, id): 
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM Feriados WHERE id={id}')
    data = conexion.fetchone()
    cursor.close()
    return data

# retorna lista de feriados
def getListaFeriados(conexion): 
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Feriados')
    data = cursor.fetchall()
    cursor.close()
    return data

def eliminarFeriado(conexion, id):
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM Feriados WHERE id={id}")
    conexion.commit() # guardar cambios
    cursor.close()
    return True

def nuevoFeriado(conexion, feriado):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Feriados (dia, mes, descripcion) VALUES (?, ?, ?)",
              (feriado.dia, feriado.mes, feriado.descripcion)) # insertar nueva actividad
    conexion.commit() # guardar cambios
    cursor.close()
    return True
