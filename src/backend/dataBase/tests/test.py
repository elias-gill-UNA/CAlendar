from ....clases.actividades import Actividad
from ....clases.proyecto import *
from ....backend.dataBase import proyectManager
from ....backend.dataBase import activitiesManager

# crear y abrir el proyecto
proyecto = DescripcionProyecto('Verga', 'Mieeeeerda', '2002')
proyectManager.crearProyecto(proyecto)
lista = proyectManager.getProyectListsWithInfo()
conexion = proyectManager.abrirProyecto(lista[0])

# anadir actividades
actividad = Actividad(1, 2, 'algo', 'algo')
activitiesManager.anadirActividad(conexion, actividad)

listaActs = activitiesManager.getListaActividades(conexion)
print(listaActs)
