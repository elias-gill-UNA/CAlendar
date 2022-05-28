from dbFunctions import db_activities as db
from proyectManager import getProyectInfo as proyect
from dbFunctions.db_proyects import actualizarParametro as actualizarContador 
# TODO importar dependencias 

def anadirActividad(conexion, nuevaActividad, numDeps):
    info = proyect(None, conexion)
    cont_actividades = info[5] # actualizar el contador de actividades del proyecto
    cont_deps = info[6]
    if cont_actividades == 99: # no mas de 99 actividades, dos actividades fantasmas
        raise ValueError("Maximum number of activities reached")
    elif cont_deps + numDeps == 

    db.nuevaActividad(conexion, nuevaActividad)
    actualizarContador(conexion, 'actiCount', cont_actividades + 1) 
    return True

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
    if len(db.getInfoActividad(conexion, id)) == 0: # si no existe id
        raise ValueError("Activitie does not exist")

    db.modificarActividad(conexion, id, actividadModificada)
    return True
    
def getInfoActividad(conexion, id):
    info = db.getInfoActividad(conexion, id) # busca en el proyecto esa actividad
    if len(info) == 0: # si no encuentra retorna vacio
        raise ValueError("Activitie does not exist") 
        
    return info

def getListaActividades(conexion):
    # armar las actividades
    return db.getListaActividades(conexion)
