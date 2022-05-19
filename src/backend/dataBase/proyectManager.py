import dbFunctions.db_proyects as dataBase
import os

# TODO  Cambiar los return y comenzar la documentacion

# retorna la lista de todos los proyectos existentes
def getProyectsList(): 
    # Como cada proyecto se encuentra en su propio archivo idProyecto.db, entonces quitamos esa lista
    file_list = os.listdir('./proyects/')
    # Quitar la extension de archivo al id
    for index, item in enumerate(file_list):
        basename = os.path.basename(item)
        file_list[index] = os.path.splitext(basename)[0]
    
    return file_list


# automatiza eleccion de ID para el proyecto
def nuevoID():
    list = getProyectsList();
    # el id es un entero 0 < n < 100, buscamos un nombre libre
    for i in range(1, 100):
        aproval = True
        for k in list:
            if i == int(k):
                aproval = False
        if aproval:
            i = str(i)
            return i


# los proyectos se guardan en ../proyects/
def crearProyecto(nuevoProyecto):
    # comprobar si existen menos de 99 proyectos
    if os.listdir('./proyects/').__len__() < 99: 
        return {"status": False, "data": 'Maximum number of projects reached'}

    id = nuevoID()
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
def getProyectInfo(id): 




def proyectListsWithInfo():
    list = getProyectsList()
    matriz = []
    for i in list:
        proyecto = [i, getProyectInfo(i)]
        matriz.append(proyecto)
    return matriz
        


def modificarDescripcion(id, proyect):
    pass


def cerrarProyecto(id):
    return True


def abrirProyecto(id): # cargar todo el proyecto TODO 
    pass


