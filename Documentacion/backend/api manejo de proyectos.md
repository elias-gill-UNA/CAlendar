# API para el manejo de proyectos
##Vista general
Para el manejo, creacion de proyectos y la modificacion de su informacion general, el backend dispone del siguiente modulo src/backend/dataBase/proyectManager.py.
Todas las funciones retornan un "data", pero si existe un error entonces generan un error de python con "raise ValueError", por ello es requerido el uso de (try, except).

## Funciones principales
	abrirProyecto(id) 
Para abrir un proyecto nuevo. Recibe el ID del proyecto y retorna un objeto _**conexion**_, el cual es utilizado para la mayoria de funciones de la base de datos. Guardar dicho objeto en una variable.

	cerrarProyecto(conexion)
Requiere una conexion el objeto __conexion__ antes proporcionado. Cierra la conexion con el proyecto. No retorna valores utilizables

	getProyectInfo(id, conexion)
	return data = [nombre, descripcion, fechaInicio, cont_actividades, conta_dependecias]
Se utiliza para leer la informacion general del proyecto (numero de actividades, nombre, fecha de inicio ...) pero no asi datos mas epecificos como la lista de actividades, para ello existen otros modulos.
Se requiere de un **ID** o de una **conexion** para llamar a esta funcion. SOLO utilizar UNO de ellos, el otro sin uso debera enviarse como _"None"_. 
    
    
	getProyectListWithInfo()
	return data = [id, [nombre, descripcion, fechaInicio, cont_actividades, conta_dependecias]]
	
Retorna matriz con la lista de id's de proyectos existentes y su informacion general dentro de otro array.


	crearProyecto(proyecto)
Funcion que crea un nuevo proyecto dentro de la base de datos. Recibe un objeto proyecto con los datos del proyecto y lo crea dentro de la base de datos. No retorna valores utilizables.


	eliminarProyecto(id)
Funcion que elimina un proyecto de la lista  de proyectos. Recibe el id del proyecto a eliminar. No retorna valores utilizables.

	modificarDescripcion(conexion, nuevaDescripcion)
	modificarNombre(conexion, nuevoNombre)
Funciones para modificar la descripcion y el nombre del proyecto. Se debe contar con una conexion para modificar el proyecto. No retornan valores utilizables.

	
	
 
## Funciones incaccesibles (privadas)
	getProyectList()
Esta funcion retorna la lista de proyectos que existen, pero solo el ID de cada proyecto, ningun otro tipo de informacion extra. 

	nuevoID() 
Retorna el primer ID disponible para el proyecto, sin mucha utilidad fuera del backend.