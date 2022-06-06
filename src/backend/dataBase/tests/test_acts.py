from clases.actividades import Actividad
from clases.proyecto import *
from backend.dataBase import activitiesManager
from backend.dataBase import proyectManager
from funcionesSobreObjetos.actividadFunciones import modificarActividad, crearActividad

# # anadir actividades
conexion = proyectManager.abrirProyecto(2)
actividad = Actividad('Poronga', 10, '')

listaActs = activitiesManager.getListaActividades(conexion)
crearActividad(conexion, 'Poronga', 10, '')

for i in range(1, 17):
    try:
        crearActividad(conexion, 'Poronga', 10, '1')
        print(i)
    except ValueError as e:
        print(str(e))
        break


try:
    print(modificarActividad(conexion, 2, actividad))
except ValueError as e:
    print(str(e))

proyectManager.cerrarProyecto(conexion)
