from os import error
import backend.dataBase.activitiesManager as db
import backend.dataBase.dependecyManager as dps

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
    aux = db.getListaActividades(conexion)
    actividades = []
    # cargar en objetos propios
    for i in aux: 
        activ = Actividad(i[0], i[1], i[2], i[3], i[4], i[5], i[6]) 
        actividades.append(activ)

    return actividades

#Implementar base de datos
#Asegurarte de actualizar la tabla al crear una actividad nueva
def crearActividad(conexion, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio):
    contadorDependencias = len(dependenciasAEnteros(decifrarDependenciasDelInput(dependenciasString)))
    nuevaActividad = Actividad(0, nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio, 0)
    try: # comprueba si es posible crear la actividad
        db.anadirActividad(conexion, nuevaActividad, contadorDependencias)
        return nuevaActividad
    except ValueError:
        return ValueError

def editarActividad():
    # usar db.modificarActividad(conexion, actividadModificada). Pasarle la actividad ya modificada y la conexion
    # ATENCION: NO toquen el id por lo que mas quieran en sus vidas
    pass

#Eliminar actividad de la base de datos
#NOTE asegurar que elimines todas las dependencias referentes a esta actividad
def eliminarActividad(actividadID):
    print('eliminar actividad: ',actividadID)
    pass

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
