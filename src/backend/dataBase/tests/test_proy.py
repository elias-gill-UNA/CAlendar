from clases.actividades import Actividad
from clases.proyecto import *
from backend.dataBase import proyectManager

from pprint import pprint


# crear y abrir el proyecto
# proyecto = Proyecto('Este tiene que ser el numero 4', 'si se puede', 'asldk', 1, 0)
# proyectManager.crearProyecto(proyecto)
conexion = proyectManager.abrirProyecto(2)
# proyectManager.modificarNombre(conexion, 'este es el 3')
proyectManager.modificarNombre(conexion, 'Este es el numero 9123847')
info = proyectManager.getProyectInfo(None, conexion)

# print(listaActs)
pprint(vars(info))

proyectManager.cerrarProyecto(conexion)
