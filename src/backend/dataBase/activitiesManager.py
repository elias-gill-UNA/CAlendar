import backend.dataBase.dbFunctions.db_activities as db
from clases.actividades import *
from backend.dataBase.proyectManager import getProyectInfo as proyect
from backend.dataBase.dbFunctions.db_proyects import actualizarParametro as actualizarContador 

def anadirActividad(conexion, nuevaActividad, numDeps):
    info = proyect(None, conexion)
    cont_actividades = info.contadorActividades
    cont_deps = info.contadorConexiones

    if cont_actividades == 99: # no mas de 99 actividades
        raise ValueError("Maximum number of activities reached")
    elif cont_deps + numDeps > 149:
        raise ValueError("Maximum number of dependencies reached")

    db.nuevaActividad(conexion, nuevaActividad)
    actualizarContador(conexion, 'actiCount', cont_actividades + 1) 
    actualizarContador(conexion, 'depCount', cont_deps + numDeps)  # actualizar el numero de relaciones y actividades
    return True


# eliminar las actividades
def eliminarActividad(conexion, idActividad):
    act = db.getInfoActividad(conexion, idActividad)
    if not len(act): # si no existe id
        raise ValueError("Activitie does not exist or empty")

    db.eliminarActividad(conexion, idActividad) # eliminar la actividad
    info = proyect(None, conexion) 

    actualizarContador(conexion, 'actiCount', info.contadorActividades - 1) # actualizar contadores
    actualizarContador(conexion, 'depCount', info.contadorConexiones - len(act[3]))
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


def getListaActividades(conexion): # retorna las dependencias como string
    # conseguir la lista
    aux = db.getListaActividades(conexion)
    actividades = []
    # cargar en objetos propios
    for i in aux: 
        activ = Actividad(i[0], i[1], i[2], i[3], i[4], i[5], i[6]) 
        actividades.append(activ)
    return actividades


# retorna un matriz con las dependencias autoreferenciadas en vez de id's
def getListaActividadesAutoreferenciada(conexion):
    lista = getListaActividades(conexion)

    # trasnformar las dependencias a una lista de enteros
    for i in lista:
        i.dependencias = dependenciasAEnteros(decifrarDependenciasDelInput(i.dependencias)) 

    # buscar entre las dependencias de cada actividad y reemplazar los id por las posiciones que ocupan en el array
    for actividad in lista: 
        for i, dependencia in actividad.dependencias:
            for index, aux in actividad:
                if dependencia == aux.identificador:
                    actividad.dependencia[i] = index # cambia por el indice en vez del id
        
    return lista

