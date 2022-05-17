import dataBase
import os

def crearProyecto(nuevoProyecto):
    if os.listdir('./proyects/').__len__() < 100: # si ya existen 99 proyectos
        return {"status": 'error', "msg": 'Maximum number of projects reached'}

    nombre = './proyects/'+nuevoProyecto.identificador+'db'
    if os.path.exists(nombre): # si ya existe ese id
        return {"status": False, "msg": 'The project already exists'}

    newProyect = open(nombre + '.db', 'w')
    newProyect.close() # crea el archivo '<proyecto>.db' si no esta creado
    dataBase.nuevoProyecto(nuevoProyecto, nombre) # crear el proyecto
    return {"status": True, "msg": 'Proyect has been created'}

def eliminarProyecto(idProyecto):
    nombre = './proyects/'+idProyecto+'db'
    if os.path.exists(nombre): # si el proyecto existe lo elimina
        os.remove(nombre) 
        return {"status": True, "msg": 'Proyect removed succesfully'}
    return {"status": False, "msg": 'Proyect does not exist'}

# def abrirProyecto(id): # cargar todo el proyecto TODO 
#     nombre = './proyects/'+id+'db'
#     if os.path.exists(nombre): # si el proyecto existe lo elimina
#         return {"status": True, "msg": }
#     return {"status": False, "msg": 'Proyect does not exist'}
    
def getInfoProyecto(id): # acceder solo la informacion general del proyecto
    # return <datos del proyecto (nombre, descrip, id...)>
    pass

def getProyectsList(): # vefile_path = os.path.splitext(file_path)[0]
    # Como cada proyecto se encuentra en su propio archivo idProyecto.db, entonces quitamos esa lista
    file_list = os.listdir('./proyects/')
    # Quitar la extension de archivo al id
    for index, item in enumerate(file_list):
        basename = os.path.basename(item)
        file_list[index] = os.path.splitext(basename)[0]
    
    return file_list

#def changeProyectValues():

#def closeProyect():
