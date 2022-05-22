import dbFunctions.db_proyects as dataBase
import os

# retorna la lista de todos los proyectos existentes
# Como cada proyecto se encuentra en su propio archivo idProyecto.db, entonces quitamos esa lista
def __getProyectsList(): 
    file_list = os.listdir('./proyects/')
    for index, item in enumerate(file_list): # Quitar la extension de archivo al id
        basename = os.path.basename(item)
        file_list[index] = os.path.splitext(basename)[0]
    
    return file_list # retorna la lista de id's del proyecto


# automatiza eleccion de ID para el proyecto
def __nuevoID():
    list = __getProyectsList();
    # el id es un entero 0 < n < 100, buscamos un nombre libre
    for i in range(1, 100):
        aproval = True
        for k in list:
            if i == int(k):
                aproval = False
        if aproval:
            i = str(i)
            return i


# Los proyectos se guardan en ../proyects/
def crearProyecto(nuevoProyecto):
    # comprobar si existen menos de 99 proyectos
    if os.listdir('./proyects/').__len__() < 99: 
        return {"status": False, "data": 'Maximum number of projects reached'}

    id = __nuevoID()
    dataBase.nuevoProyecto(nuevoProyecto, id) # crear y llena las tablas del proyecto
    return {"status": True, "data": 'Proyect has been created'}


def eliminarProyecto(idProyecto):
    # como cada proyecto tiene un .db distinto solo debemos eliminar ese archivo
    nombre = './proyects/'+idProyecto+'db'
    if os.path.exists(nombre): # si el proyecto existe lo elimina
        os.remove(nombre) 
        return {"status": True, "data": 'Proyect removed succesfully'}
    return {"status": False, "data": 'Proyect does not exist'}


# acceder solo la informacion general del proyecto
def getProyectInfo(id, conexion): 
    if conexion: # si ya existe conexion
        return {"status": True, "data": dataBase.getInfo(id, conexion)}

    if not os.path.exists('./proyects/'+id+'.db'): # si el proyecto no existe 
        return {"status": False, "data": 'Proyect does not exist'}

    return {"status": True, "data": dataBase.getInfo(id, conexion)} # entonces si existe id


def getProyectListsWithInfo():
    list = __getProyectsList()
    matriz = []
    for i in list:
        proyecto = [i, dataBase.getInfo(i, None)]
        matriz.append(proyecto)
    return matriz # retorna un array [id, [Descripcion, fecha ...]]
        

def modificarDescripcion(conexion, nuevaDescripcion): # solo se pueden modificar proyectos activos
    dataBase.modificarValor(conexion, 'Descripcion', 'desc', nuevaDescripcion, "")
    return {"status": True, "data": 'Succesfull'}

def modificarNombre(conexion, nuevoNombre): # solo se pueden modificar proyectos activos
    dataBase.modificarValor(conexion, 'Descripcion', 'name', nuevoNombre, "")
    return {"status": True, "data": 'Succesfull'}

def cerrarProyecto(conexion): # pasarle la conexion
    dataBase.cerrarProyecto(conexion)
    return True


def abrirProyecto(id): # cargar todo el proyecto  
    if not os.path.exists('./proyects/'+id+'.db'): # si el proyecto existe 
        return {"status": False, "data": 'Proyect does no exist'}
    return {"status": True, "data":dataBase.abrirProyecto(id) } # retorna la conexion al proyecto


