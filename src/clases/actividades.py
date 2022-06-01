from os import error
from backend.dataBase import proyectManager
import backend.dataBase.activitiesManager as activitiesManager
import backend.dataBase.dbFunctions.db_proyects as db_proyects

class Actividad:
    def __init__(self, identificador, nombre, duracion, dependencias, fechaInicioTemprano, fechaInicioTardio, finalizo):
        self.identificador = identificador
        self.nombre = nombre
        self.duracion = duracion
        self.dependencias = dependencias
        self.fechaInicioTemprano = fechaInicioTemprano
        self.fechaInicioTardio = fechaInicioTardio
        self.finalizado = finalizo # ENTERO    1: finalizado  0: aun no

# Retorna todas las actividades de la base de datos dentro de un array
def leerActividades(conexion):
    return activitiesManager.getListaActividades(conexion) # y si, esto nomas es :)


#Asegurarte de actualizar la tabla al crear una actividad nueva
def crearActividad(conexion, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio):
    contadorDependencias = len(dependenciasAEnteros(decifrarDependenciasDelInput(dependenciasString)))
    nuevaActividad = Actividad(0, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio, 0)
    try: # comprueba si es posible crear la actividad
        activitiesManager.anadirActividad(conexion, nuevaActividad, contadorDependencias)
        return nuevaActividad
    except ValueError:
        return ValueError


def editarActividad(conexion, id, nuevosDatos): 
    # TODO  consultar a Ric que pedo
    # usar db.modificarActividad(conexion, actividadModificada). Pasarle la actividad ya modificada y la conexion
    # ATENCION: NO toquen el id por lo que mas quieran en sus vidas
    pass


#Eliminar actividad de la base de datos y sus relaciones
def eliminarActividad(conexion, actividadID):
    try: 
        activitiesManager.eliminarActividad(conexion, actividadID)
        lista = activitiesManager.getListaActividades(conexion)
        infoProyecto = proyectManager.getProyectInfo(None, conexion)

        for actividad in lista: # por cada actividad 
            aux = dependenciasAEnteros(decifrarDependenciasDelInput(actividad.dependencias)) # dependencias de actividad
            if actividadID in aux: # si una actividad contiene actividadID como dependencia
                index = aux.index(actividadID) # ver su posicion
                aux.pop(index) # eliminar
                actividad.dependencias = convertirArregloDependenciasAString(aux) # trasnformar de nuevo a string 

                activitiesManager.modificarActividad(conexion, actividad.identificador, actividad) # actualizar la actividad
                db_proyects.actualizarParametro(conexion, 'depCount', infoProyecto.contadorConexiones - 1) # act. el contador
                print(infoProyecto.contadorConexiones)
                
        return True
    except ValueError:
        return ValueError


#  # Funciones de trasnformacion de dependencias #  # 
def decifrarDependenciasDelInput(dependenciasString):
    arregloDependencias = dependenciasString.split(",")
    return arregloDependencias;

def dependenciasAEnteros(arregloDependencias):
    arregloEnteros = []
    for dependencia in arregloDependencias:
        arregloEnteros.append(int(dependencia))
    return arregloEnteros;

#Esta funcion se usar para el display de dependencias en el GUI
def convertirArregloDependenciasAString(arregloDependencias):
    dependenciasString = ''
    for dependencia in arregloDependencias:
        dependenciasString += dependencia + ', '
    return  dependenciasString
