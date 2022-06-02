from clases.actividades import Actividad
from clases.proyecto import *
from backend.dataBase import activitiesManager
from backend.dataBase import proyectManager

import pprint
# # anadir actividades
conexion = proyectManager.abrirProyecto(2)
actividad = Actividad(0, 'Esta esta modificada', 2, 'una dependencia', 'fecha 1', 'fecha 2', 0)

listaActs = activitiesManager.getListaActividades(conexion)

for i in range(1, 170):
    try:
        activitiesManager.eliminarActividad(conexion, i)
        print(i)
    except:
        print('algo paso')
        break

proyectManager.cerrarProyecto(conexion)
