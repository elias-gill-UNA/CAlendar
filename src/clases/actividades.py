from os import error
import backend.dataBase.activitiesManager as db

class Actividad:
    def __init__(self, identificador, nombre, duracion, dependencias, fechaInicioTemprano, fechaInicioTardio, finalizo):
        self.identificador = identificador
        self.nombre = nombre
        self.duracion = duracion
        self.dependencias = dependencias
        self.fechaInicioTemprano = fechaInicioTemprano
        self.fechaInicioTardio = fechaInicioTardio
        self.finalizo = finalizo # ENTERO    1: finalizado  0: aun no

# Retorna todas las actividades de la base de datos dentro de un array
def leerActividades(conexion):
    return db.getListaActividades(conexion) # y si, esto nomas es :)


#Asegurarte de actualizar la tabla al crear una actividad nueva
def crearActividad(conexion, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio):
    contadorDependencias = len(dependenciasAEnteros(decifrarDependenciasDelInput(dependenciasString)))
    nuevaActividad = Actividad(0, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio, 0)
    try: # comprueba si es posible crear la actividad
        db.anadirActividad(conexion, nuevaActividad, contadorDependencias)
        return nuevaActividad
    except ValueError:
        return ValueError


def editarActividad(conexion, id, nuevosDatos): # TODO  consultar a Ric que pedo
    # usar db.modificarActividad(conexion, actividadModificada). Pasarle la actividad ya modificada y la conexion
    # ATENCION: NO toquen el id por lo que mas quieran en sus vidas
    pass


#Eliminar actividad de la base de datos y sus relaciones
def eliminarActividad(conexion, actividadID):
    try: 
        db.eliminarActividad(conexion, actividadID)
        lista = db.getListaActividades(conexion)

        for actividad in lista: # por cada actividad 
            if actividadID in actividad.dependencias: # si una actividad contiene actividadID como dependencia
                index = actividad.dependencias.index(actividadID) # ver su posicion
                actividad.dependencias.pop(index) # eliminar
                db.modificarActividad(conexion, actividad.identificador, actividad) # actualizar la actividad
        return True
    except:
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
