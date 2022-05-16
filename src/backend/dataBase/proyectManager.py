import dataBase
import os


def newProyect(nuevoProyecto):
    nombre = nuevoProyecto.identificador+'db'
    if os.path.exists(nombre):
        return {"status": 'error', "msg": 'The project already exists'}
    newProyect = open(nombre + '.db', 'w')
    newProyect.close() # crea el archivo '<proyecto>.db' si no esta creado
    dataBase.nuevoProyecto(nuevoProyecto, nombre)
    return {"status": 'succesfull', "msg": 'Proyect has been created'}

def deleteProyect(proyecto):
    nombre = proyecto.identificador+'db'
    if os.path.exists(nombre):
        os.remove("demofile.txt") 
        return {"status": 'succesfull', "msg": 'Added new activity'}
    return {"status": 'error', "msg": 'Proyect does not exist'}

def openProyect():
    pass
    

    

    

#def deleteProyect():

#def changeProyectValues():

#def getProyectInfo():

#def openProyect():

#def closeProyect():
