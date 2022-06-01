from clases.proyecto import *
from backend.dataBase import proyectManager
from backend.dataBase import activitiesManager
from pprint import pprint
from clases.actividades import *


# crear y abrir el proyecto
proyectManager.getProyectListsWithInfo()
proyecto = Proyecto('Este tiene que ser el numero 4', 'si se puede', 'asldk', 1, 0)
proyectManager.crearProyecto(proyecto)
conexion = proyectManager.abrirProyecto(1)

listaActs = activitiesManager.getListaActividades(conexion)

actividad = Actividad(0, 'Normal', 2, '5', 'fecha 1', 'fecha 2', 0)
for i in range(1, 5):
    try:
        activitiesManager.anadirActividad(conexion, actividad, 1)
    except:
        print('algo paso')
        break

actividad = Actividad(0, 'Esta es la que se debe modificar', 2, '1,2,3', 'fecha 1', 'fecha 2', 0)
activitiesManager.anadirActividad(conexion, actividad, 3)

try:
    eliminarActividad(conexion, 5)
except ValueError:
    print('Que lo que pasa')

list = activitiesManager.getListaActividades(conexion)
info = proyectManager.getProyectInfo(None, conexion)

pprint(vars(info))
print()
for i in list:
    pprint(vars(i))
    print()
proyectManager.cerrarProyecto(conexion)
