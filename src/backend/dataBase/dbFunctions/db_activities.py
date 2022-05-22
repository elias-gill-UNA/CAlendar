# --- Modulo en proceso ---

def nuevaActividad(conexion, actividad):
    conexion.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, name TEXT, desc TEXT, fecha TEXT)") # crea la descripcion del proyecto

#     c.execute("INSERT INTO tabla1 (palabraclave, valor) VALUES (?, ?)", (keyword, value))
#     conn.commit()

#     c.execute('SELECT * FROM tabla1')
#     data = c.fetchall()
    return True 


