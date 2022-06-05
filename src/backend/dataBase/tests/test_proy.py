from clases.actividades import Actividad
from clases.proyecto import *
from backend.dataBase import proyectManager
# from pprint import pprint


# crear y abrir el proyecto
proyecto = Proyecto('nombre', 'alskdjaslkdj', '11/11/2121')
proyectManager.getProyectListsWithInfo()
proyectManager.crearProyecto(proyecto)

conexion = proyectManager.abrirProyecto(1)
# proyectManager.modificarNombre(conexion, 'este es el 3')
proyectManager.modificarNombre(conexion, 'Este es el numero 9123847')
info = proyectManager.getProyectInfo(None, conexion)

# print(listaActs)
print(info.nombre, info.descripcion)

proyectManager.cerrarProyecto(conexion)
