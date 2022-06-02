import backend.dataBase.proyectManager as proyectManager
import backend.dataBase.activitiesManager as activitiesManager

def abrirProyecto(idProyecto):
    conexion = proyectManager.abrirProyecto(idProyecto)
    descripcion = proyectManager.getProyectInfo(None, conexion)
    listaActividades = activitiesManager.getListaActividades(conexion)
    proyecto = [conexion, descripcion, listaActividades] # este objeto es el que deberia de circular por el frontend
    return proyecto