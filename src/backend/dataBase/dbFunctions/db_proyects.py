import sqlite3

def nuevoProyecto(proyecto, id): # nombre del proyecto
    conn = sqlite3.connect(f'../proyects/{id}.db') # crea la base de datos si no existe
    cursor = conn.cursor()

    # Crear las tablas necesarias para el proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Descripcion (id INT, name TEXT, desc TEXT, fecha TEXT, actiCount INT, depCount INT)") #  tabla de descripcion del proyecto
    cursor.execute("CREATE TABLE IF NOT EXISTS Actividades (id INT, name TEXT, duracion INT, fechaTemp TEXT, fechaTar Text, finalizado INT)") # tabla de actividades
    cursor.execute("CREATE TABLE IF NOT EXISTS Dependecias (id INT, idAntes TEXT, idDespues TEXT)") # tabla de Dependecias

    # Llenado de los campos de identificacion del proyecto
    cursor.execute("INSERT INTO Descripcion (id, name, desc, fecha, actiCount, depCount) VALUES (?, ?, ?, ?, ?, ?)", 
              (proyecto.identificador, proyecto.nombre, proyecto.descripcion, proyecto.inicioPrevisto, 0, 0))

    # Proyecto creado satisfactoriamente
    conn.commit()
    cursor.close()
    return True 

# retorna la tabla de informacion del proyecto
def getInfo(id):
    conn = sqlite3.connect(f'../proyects/{id}.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Descripcion')
    data = cursor.fetchall()
    cursor.close()
    return data
    

def abrirProyecto(id):
    pass



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

