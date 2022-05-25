# Vista general
Para el manejo de actividades del proyecto se dispone del modulo __src/backend/dataBase/activitiesManager.py__.

El modulo cuenta con las funciones que se requeriran para el manejo, creacion, eliminacion y modificacion de actividades dentro del proyecto. Para ello se requiere de una __conexion__ al proyecto.

Todas las funciones hacen uso de los errors de python, por ende se require el uso de _try except_ para las llamadas.

## Funciones disponibles

	nuevaActividad (conexion, nuevaActividad)
Recibe la conexion al proyecto y el objeto actividad que se quiere crear. Si el numero de actividades es igual a 99 crea un erro. Operacion correcta retorna true.
El ID es asignado por la base de datos.

	eliminarActividad (conexion, idACtividad)
Recibe conexion y un ID. Error cuando la actividad con id=id no existe. Operacion correcta retorna true.

	modificarActividad (conexion, id, actividad)
Recibe conexion, id y un objeto actividad con la nueva informacion. Retorna true. Si id no existe lanza error.

	getInfoActividad (conexion, id)
	return data = [id, nombre,  duracion,fechaPrevista, fechaTardia, finalizado]
Retorna la informacion de la actividad en un array. Si el id no existe lanza error.

	getListaActividades (conexion)
	return data = [[id, nombre, fecha...], [id, nombre, fecha...]]
Retorna la lista de todas las actividades con su informacion. Retorna array de actividades, cada actividad cuenta con el formato de _getInfoActividad()_. 
