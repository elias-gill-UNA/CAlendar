import backend.dataBase.dbFunctions.db_activities as db
from clases.actividades import *
from backend.dataBase.proyectManager import getProyectInfo as proyect
from backend.dataBase.dbFunctions.db_proyects import actualizarParametro as actualizarContador 
# TODO importar dependencias 

def anadirActividad(conexion, nuevaActividad, numDeps):
    info = proyect(None, conexion)
    cont_actividades = info[5] 
    cont_deps = info[6]

    if cont_actividades == 99: # no mas de 99 actividades
        raise ValueError("Maximum number of activities reached")
    elif cont_deps + numDeps > 149:
        raise ValueError("Maximum number of dependencies reached")

    db.nuevaActividad(conexion, nuevaActividad)
    actualizarContador(conexion, 'actiCount', cont_actividades + 1) 
    actualizarContador(conexion, 'depCount', cont_deps + numDeps)  # actualizar el numero de relaciones y actividades
    return True


# eliminar las actividades
def eliminarActividad(conexion, id):
    act = db.getInfoActividad(conexion, id)
    if len(act) == 0: # si no existe id
        raise ValueError("Activitie does not exist")
    elif act.nombre == "Inicio" or act.nombre == "Final":
        raise ValueError("No puedes eliminar estas actividades")

    db.eliminarActividad(conexion, id)
    cont_actividades = proyect(None, conexion)[5] # actualizar el contador 
    actualizarContador(conexion, 'actiCount', cont_actividades - 1)
    return True


# debe recibir objeto actividad nuevo
def modificarActividad(conexion, id, actividadModificada): 
    if len(db.getInfoActividad(conexion, id)) == 0: # si no existe ese ID
        raise ValueError("Activitie does not exist")

    db.modificarActividad(conexion, id, actividadModificada) # modificar
    return True
    

def getInfoActividad(conexion, id):
    info = db.getInfoActividad(conexion, id) # busca en el proyecto esa actividad
    if len(info) == 0: # si no encuentra retorna vacio
        raise ValueError("Activitie does not exist") 
        
    return info


def getListaActividades(conexion):
    # conseguir la lista
    aux = db.getListaActividades(conexion)
    actividades = []
    # cargar en objetos propios
    for i in aux: 
        activ = Actividad(i[0], i[1], i[2], i[3], i[4], i[5], i[6]) 
        actividades.append(activ)
    return actividades
