from clases.proyecto import *
from backend.dataBase import proyectManager
from backend.dataBase import activitiesManager
from pprint import pprint
from clases.actividades import *


# crear y abrir el proyecto
listaProyectos = proyectManager.getProyectListsWithInfo() # Crea la carpeta DB si no existe y/o ve la lista de proyectos

proyecto = Proyecto('Este tiene que ser el numero 4', 'si se puede', 'asldk', 1, 0)
proyectManager.crearProyecto(proyecto)

conexion = proyectManager.abrirProyecto(1)
listaActs = activitiesManager.getListaActividades(conexion)

# crear actividades dentro del proyecto
actividad = Actividad(0, 'Normal', 2, '', 'fecha 1', 'fecha 2', 0)
actividad = Actividad(0, 'Normal', 2, '1', 'fecha 1', 'fecha 2', 0)
# for i in range(1, 6):
try:
    crearActividad(conexion, 'Normal', 2, '1', 'fecha 1', 'fecha 2')
except ValueError as e:
    print(e)        

# una actividad especial para eliminar
actividad = Actividad(0, 'Esta es la que se debe modificar', 2, '1,2,3', 'fecha 1', 'fecha 2', 0)
activitiesManager.anadirActividad(conexion, actividad, 3)

info = proyectManager.getProyectInfo(None, conexion)
print()
pprint(vars(info))
print()

try: # eliminar esa una actividad especial
    eliminarActividad(conexion, 1)
    eliminarActividad(conexion, 10)
except ValueError:
    print(ValueError.args)

list = activitiesManager.getListaActividades(conexion)
info = proyectManager.getProyectInfo(None, conexion)

pprint(vars(info))
proyectManager.cerrarProyecto(conexion)

# for i in list:
#     pprint(vars(i))
#     print()
