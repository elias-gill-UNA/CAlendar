# from GUI.crear_proyectos import ir_Actividad
from clases.actividades import Actividad
from backend.dataBase import proyectManager
from backend.dataBase import activitiesManager
from backend.dataBase.dbFunctions import db_proyects

# Retorna todas las actividades de la base de datos dentro de un array
def leerActividades(conexion):
    return activitiesManager.getListaActividades(conexion) # y si, esto nomas es :)

def modificarActividad(conexion, id, nuevaActividad):
    if nuevaActividad.dependencias != '':
        deps = dependenciasAEnteros(decifrarDependenciasDelInput(nuevaActividad.dependencias))
    else:
        deps = False

    lista = activitiesManager.getListaActividades(conexion)
    if deps:
        for i in lista: # tirar error si una dependencia no existe
            if not i in deps:
                raise ValueError("La activida de la que dependencia no existe. No puedes asignar estas dependencias")

    try: # comprueba si es posible crear la actividad
        activitiesManager.modificarActividad(conexion, id, nuevaActividad)
        return True
    except ValueError:
        return ValueError
    


#Asegurarte de actualizar la tabla al crear una actividad nueva
def crearActividad(conexion, nombre, duracion, dependenciasString):
    if dependenciasString != '':
        deps = dependenciasAEnteros(decifrarDependenciasDelInput(dependenciasString))
    else:
        deps = False

    contadorDependencias = 0
    nuevaActividad = Actividad(nombre, duracion, dependenciasString)

    lista = activitiesManager.getListaActividades(conexion)
    if deps:
        for i in lista: # tirar error si una dependencia no existe
            if not i in deps:
                raise ValueError("La activida de la que depende no existe")

    try: # comprueba si es posible crear la actividad
        activitiesManager.anadirActividad(conexion, nuevaActividad, contadorDependencias)
        return nuevaActividad
    except ValueError:
        return ValueError


#Eliminar actividad de la base de datos y sus relaciones
def eliminarActividad(conexion, actividadID):
    try: 
        activitiesManager.eliminarActividad(conexion, actividadID)
        lista = activitiesManager.getListaActividades(conexion)

        # si una actividad contiene actividadID como dependencia entonces actualizarla
        for actividad in lista: 
            infoProyecto = proyectManager.getProyectInfo(None, conexion)
            if actividad.dependencias == '':
                break
            aux = dependenciasAEnteros(decifrarDependenciasDelInput(actividad.dependencias)) # dependencias a enteros
            if actividadID in aux:  
                index = aux.index(actividadID) 
                aux.pop(index) 
                actividad.dependencias = convertirArregloDependenciasAString(aux) # trasnformar dependencias nuevo a string 

                activitiesManager.modificarActividad(conexion, actividad.identificador, actividad) # actualizar la actividad
                db_proyects.actualizarParametro(conexion, 'depCount', infoProyecto.contadorConexiones - 1) 

        return True
    except ValueError:
        return ValueError


#  # Funciones de trasnformacion de dependencias #  # 
def decifrarDependenciasDelInput(dependenciasString):
    arregloDependencias = dependenciasString.split(",")
    return arregloDependencias

def dependenciasAEnteros(arregloDependencias):
    arregloEnteros = []
    for dependencia in arregloDependencias:
        arregloEnteros.append(int(dependencia))
    return arregloEnteros

#Esta funcion se usar para el display de dependencias en el GUI
def convertirArregloDependenciasAString(arregloDependencias):
    dependenciasString = ''
    for dependencia in arregloDependencias:
        dependenciasString += dependencia + ', '
    return  dependenciasString
