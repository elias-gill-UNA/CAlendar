class actividad:
    def __init__(self, identificador,nombre,duracion, dependencias,fechaInicioTemprano,fechaInicioTardio):
        self.identificador=identificador
        self.nombre=nombre
        self.duracion=duracion
        self.dependencias=dependencias
        self.fechaInicioTemprano=fechaInicioTemprano
        self.fechaInicioTardio=fechaInicioTardio
        self.finalizo=0#si finalizo es igual a 1, entonces la actividad fue terminada

#TODO Cambiar
#Retorna todas las actividades desde la base de datos en forma de arreglo
def leerActividades():
    actividades = []
    for i in range(0, 10):
        nuevaActividad = crearActividad('Titulo', 5, "5, 7, 9", "21/12/2020", "21/12/2022")
        actividades.append(nuevaActividad)

    return actividades

#Implementar base de datos
#Asegurarte de actualizar la tabla al crear una actividad nueva
def crearActividad(nombre, duracion, dependenciasString, fechaInicioTemprano, fechaInicioTardio):
    dependenciasArreglo = decifrarDependenciasDelInput(dependenciasString)
    dependenciasComoEnteros = dependenciasAEnteros(dependenciasArreglo)
    nuevaActividad = actividad(calcularIdentificadorNuevo(), nombre, duracion, dependenciasArreglo, fechaInicioTemprano, fechaInicioTardio)
    return nuevaActividad

def editarActividad():
    pass

#Eliminar actividad de la base de datos
#NOTE asegurar que elimines todas las dependencias referentes a esta actividad
def eliminarActividad(actividadID):
    print('eliminar actividad: ',actividadID)
    pass

#Conseguir desde la base de datos el identificador de la ultima actividad y sumarle 1
def calcularIdentificadorNuevo():
    return 1

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