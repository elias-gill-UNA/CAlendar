from dbFunctions import db_activities as db
from proyectManager import getProyectInfo as proyect
from dbFunctions.db_proyects import actualizarContador 

def anadirActividad(conexion, nuevaActividad):
    info = proyect(None, conexion)
    if len(info[5]) == 99: # no mas de 99 actividades
        raise ValueError("Maximum number of activities reached")

    db.nuevaActividad(conexion, nuevaActividad)
    cont_actividades = info[5] # actualizar el contador en la DB
    actualizarContador(conexion, 'actiCount', cont_actividades + 1)
    return True

def eliminarActividad(conexion, id):
    if len(db.getInfoActividad(conexion, id)) == 0: # si no existe id
        raise ValueError("Activitie does not exist")

    db.eliminarActividad(conexion, id)
    cont_actividades = proyect(None, conexion)[5] # actualizar el contador en la DB
    actualizarContador(conexion, 'actiCount', cont_actividades - 1)
    return True

# debe recibir objeto actividad nuevo
def modificarActividad(conexion, actividadModificada): 
    if len(db.getInfoActividad(conexion, id)) == 0: # si no existe id
        raise ValueError("Activitie does not exist")

    db.actualizarActividad(conexion, actividadModificada)
    return True
    
def getInfoActividad(conexion, id):
    info = db.getInfoActividad(conexion, id)
    if len(info) == 0:
        raise ValueError("Activitie does not exist")
        
    return info
