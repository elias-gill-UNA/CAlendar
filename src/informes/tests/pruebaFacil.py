from clases.actividades import Actividad
from clases.clases_cam_critico import ObjetoCritico
from clases.proyecto import Proyecto
from backend.dataBase import proyectManager
from informes.camino_critico import funcionFinalYSuperpoderosa
from datetime import date

# crea el proyecto y cargar actividades
h = proyectManager.getProyectListsWithInfo()
proyectManager.crearProyecto(Proyecto("Nombre del proyecto", "ohala que funciones", "27/05/2022" ))
conexion = proyectManager.abrirProyecto(1)

objCrit = ObjetoCritico()
listaGeneral = []
proyect = Proyecto("Nombre del proyecto", "ohala que funciones", "27/05/2022")
listaCopia = []

#para probar nms
nombres=["A","B","C","D","E","F","G","H","I","J","K"]
duraciones=[7,15,7,1,30,5,30,1,1,1,1]

for i in range(len(nombres)):
    actividad=Actividad(nombres[i],duraciones[i],[])
    listaGeneral.append(actividad)

listaGeneral[1].dependencias=[0]
listaGeneral[2].dependencias=[0]
listaGeneral[3].dependencias=[2]
listaGeneral[4].dependencias=[1,3]
listaGeneral[5].dependencias=[4]
listaGeneral[6].dependencias=[5]
listaGeneral[7].dependencias=[0]
listaGeneral[8].dependencias=[4,7]
listaGeneral[9].dependencias=[6,8]
listaGeneral[10].dependencias=[6]

# super mega ultra funcion
funcionFinalYSuperpoderosa(conexion, listaGeneral, listaCopia, objCrit, proyect)

aux1 = proyect.fechaInicio.split("/")
fecha1 = date(2022, 5, 27)
fecha2 = date(2022, 9, 28)

print(fecha1 - fecha2)
print(proyect.finTemprano)
print(proyect.fechaInicioTardio)
