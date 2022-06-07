import backend.dataBase.dbFunctions.db_proyects as dataBase
import os
from clases.proyecto import Proyecto
from utilidades.calendario import cargarFeriadosNacionales
import shutil


path = os.path.expanduser("~") + '/CAlendar-database/proyects/'
# retorna la lista de todos los proyectos existentes
# Como cada proyecto se encuentra en su propio archivo idProyecto.db, entonces quitamos esa lista
def __getProyectsList(): 
    file_list = os.listdir(path)
    for index, item in enumerate(file_list): # Quitar la extension de archivo al id
        basename = os.path.basename(item)
        file_list[index] = os.path.splitext(basename)[0]
    
    return file_list # retorna la lista de id's del proyecto


def exportarProyecto(id):
    os.system(f'cp {path}/{id}.db ~/{id}.db')
    return True

# automatiza eleccion de ID para el proyecto
def __nuevoID():
    list = __getProyectsList();
    # el id es un entero 0 < n < 100, buscamos un nombre libre
    for i in range(1,999):
        if not str(i) in list:
            return str(i)


# Los proyectos se guardan en ../proyects/
def crearProyecto(nuevoProyecto):
    # comprobar si existen menos de 99 proyectos
    if os.listdir(path).__len__() == 999: 
        raise ValueError("Maximum number of projects reached")

    id = __nuevoID()
    dataBase.nuevoProyecto(nuevoProyecto, id) # crear y llena las tablas del proyecto
    cargarFeriadosNacionales(id)
    return id


def eliminarProyecto(id):
    # como cada proyecto tiene un .db distinto solo debemos eliminar ese archivo
    nombre = f'{path}{id}.db'
    if os.path.exists(nombre): # si el proyecto existe lo elimina
        os.remove(nombre) 
        return True
    raise ValueError("Proyect does not exist")


# acceder a la informacion general del proyecto
def getProyectInfo(id, conexion): 
    if not os.path.exists(f'{path}{id}.db') and not conexion: 
        raise ValueError("Proyect does not exist")

    # convertir la tupla a objeto proyecto
    info = dataBase.getInfo(id, conexion) 
    proyecto = Proyecto(info[0][1], info[0][2], info[0][3])
    proyecto.contadorActividades = info[0][4]
    proyecto.contadorConexiones = info[0][5]
    proyecto.identificador = info[0][0]
    return proyecto


# retorna un array con los proyectos existentes[id, [Descripcion, fecha ...]]
def getProyectListsWithInfo():
    if not os.path.isdir(path): # si la path a la base de datos no existe
        os.makedirs(path)

    list = __getProyectsList() 
    if len(list) == 0: # si la lista esta vacia
        return []

    matriz = []
    for id in list:
        proyecto = getProyectInfo(id, None)
        matriz.append(proyecto)
    return matriz 

def modificarDescripcion(conexion, nuevaDescripcion): # solo se pueden modificar proyectos activos
    dataBase.actualizarParametro(conexion, 'descripcion', f'"{nuevaDescripcion}"')
    return True

def modificarNombre(conexion, nuevoNombre): # solo se pueden modificar proyectos activos
    dataBase.actualizarParametro(conexion, 'nombre', f'"{nuevoNombre}"')
    return True


def cerrarProyecto(conexion): # pasarle la conexion
    dataBase.cerrarProyecto(conexion)
    return True

def abrirProyecto(id): # cargar todo el proyecto  
    if not os.path.exists(f'{path}{id}.db'): 
        raise ValueError("Proyect does not exist")
    return dataBase.abrirProyecto(id) # retorna la conexion al proyecto


