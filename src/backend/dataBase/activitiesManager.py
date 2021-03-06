from backend.dataBase import proyectManager
import backend.dataBase.dbFunctions.db_activities as db
from clases.actividades import Actividad
from backend.dataBase.proyectManager import getProyectInfo as getInfoProyecto
from backend.dataBase.dbFunctions.db_proyects import actualizarParametro as actualizarContador 

def anadirActividad(conexion, nuevaActividad, numDeps):
    info = getInfoProyecto(None, conexion)
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
    act = getInfoActividad(conexion, idActividad)
    if not act: # si no existe id
        raise ValueError("Activitie does not exist or empty")

    db.eliminarActividad(conexion, idActividad) # eliminar la actividad
    info = getInfoProyecto(None, conexion) 

    cont_deps = len(act.dependencias.split(',')) # numero de dependencias
    actualizarContador(conexion, 'actiCount', info.contadorActividades - 1) # actualizar contadores
    actualizarContador(conexion, 'depCount', info.contadorConexiones - cont_deps)
    return True


# debe recibir un nuevo objeto actividad
def modificarActividad(conexion, id, actividadModificada): 
    actVieja = getInfoActividad(conexion, id)
    dpesProy = proyectManager.getProyectInfo(None, conexion).contadorConexiones
    if not actVieja: # si no existe ese ID
        raise ValueError("Activitie does not exist")

    # modificar la actividad
    contNUevasDeps = len(actividadModificada.dependencias.split())
    db.modificarActividad(conexion, id, actividadModificada) 

    #actualizar el contador de dependencias
    contadorNuevo = dpesProy - len(actVieja.dependencias) + contNUevasDeps
    actualizarContador(conexion, 'depCount', contadorNuevo)
    return True
    

def getInfoActividad(conexion, id):
    info = db.getInfoActividad(conexion, id) # busca en el proyecto esa actividad
    if not info: # no encontro la actividad
        raise ValueError("Activitie does not exist") 
    
    activ = Actividad(info[1], info[2], info[3]) 
    activ.identificador = info[0]
    return activ


def getListaActividades(conexion): # retorna las dependencias como string
    # conseguir la lista
    aux = db.getListaActividades(conexion)
    actividades = []
    # cargar en objetos propios
    for i in aux: 
        activ = Actividad(i[1], i[2], i[3]) 
        activ.identificador = i[0]
        actividades.append(activ)
        
    return actividades


def depesEnteros(deps):
    depes = deps.split(',')
    final = []
    for index, dep in enumerate(depes):
        if dep != "":
            final.append(int(dep))
    return final

# retorna un matriz con las dependencias autoreferenciadas en vez de id's
def getListaActividadesAutoreferenciada(conexion):
    lista = getListaActividades(conexion)

    # trasnformar las dependencias a una lista de enteros
    for i in lista:
        if i.dependencias != "": # si contiene dependencias
            i.dependencias = depesEnteros(i.dependencias)
        else:
            i.dependencias = []

    # buscar entre las dependencias de cada actividad y reemplazar los id por las posiciones que ocupan en el array
    for actividad in lista: 
        for i, dependencia in enumerate(actividad.dependencias):
            for index, aux in enumerate(lista):
                if dependencia == aux.identificador:
                    actividad.dependencias[i] = index # cambia por el indice en vez del id
        
    return lista

