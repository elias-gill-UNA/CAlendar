# API de llamadas a base de datos 
Se proporcionan modulos que gestionan el control a la base de datos integrada en el proyecto,
los cuales se encuentra dentro de src/backend/dataBase/ dentro del modulo "proyectManager"

##  crearProyecto(proyecto) 
Para crear nuevos proyectos, recibe un objeto de tipo proyecto y retorna un diccionario {
'status': True/False, "msg": 'mensaje acorde al error'
}

##  eliminarProyecto(proyecto) 
Para eliminar un proyecto existente. Recibe y retorna los mismos parametros que crearProyecto()

##  abrirProyecto(id) 
Para abrir un proyecto nuevo. Recibe el ID del proyecto. Retorna lo mismo que las anteriores funciones, pero en
caso de existir el proyecto, dentro "msg" encuentra un diccionario con los siguientes datos:
{ "datos", "actividades", "dependencias" } y en caso de no existir msg: 'mensaje de error'

##  getInfoProyecto(id)
    
##  getProyectsList()
Retorna una matriz con la lista de id's de proyectos existentes y su descripcion.
[id, descripcion]
 
