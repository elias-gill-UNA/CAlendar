from clases.actividades import Actividad
from clases.clases_cam_critico import ObjetoCritico
from clases.proyecto import Proyecto
from backend.dataBase import proyectManager
from informes.camino_critico import funcionFinalYSuperpoderosa
from datetime import date, datetime, timedelta

# crea el proyecto y cargar actividades
conexion = proyectManager.abrirProyecto(1)

objCrit = ObjetoCritico()
listaGeneral = []
proyect = Proyecto("Nombre del proyecto", "ohala que funciones", "06/06/2022")
listaCopia = []

#para probar nms
nombres=["A","B","C","D","E"]
duraciones=[3,2,4,1,3]

for i in range(len(nombres)):
    actividad=Actividad(nombres[i],duraciones[i],[])
    listaGeneral.append(actividad)

listaGeneral[1].dependencias=[0]
listaGeneral[2].dependencias=[0]
listaGeneral[3].dependencias=[1]
listaGeneral[4].dependencias=[1]

# super mega ultra funcion
funcionFinalYSuperpoderosa(conexion, listaGeneral, listaCopia, objCrit, proyect)


print("Las actividades criticas son: ", end='')
for i in objCrit.actividadesCriticas:
    print(i.nombre, end=', ')
print("\nCantidad de caminos:", objCrit.cantidadCritico)

for j in range(objCrit.cantidadCritico):
    print("el camino critico numero "+str(j+1)+" es")
    for i in objCrit.caminosCriticos[j]:
        print(i.nombre)


print("DATOS DEL ACTIVIDADES")
for actividad in listaCopia:
    print("........")
    print("actividad con nombre "+str(actividad.nombre))
    print("su holgura es "+str(actividad.holgura))
    print("el inicio temprano de la actividad es "+str(actividad.fechaInicioTemprano))
    print("el inicio tardio de la actividad es "+str(actividad.fechaInicioTardio))
    print("el fin temprano de la actividad es "+str(actividad.fechaFinTemprano))#
    print("el fin tardio de la actividad es "+str(actividad.fechaFinTardio))
    print("........")
    print("........")


print("....")
print("DATOS DEL PROYECTO")
print("el inicio temprano es "+str(proyect.fechaInicio))
print("el inicio tardio es "+str(proyect.fechaInicioTardio))
print("el fin temprano es "+str(proyect.fechaFinTemprano))
print("el fin tardio es "+str(proyect.fechaFinTardio))
print("....")

aux1 = proyect.fechaInicioTardio.split("/")
fecha1 = date(int(aux1[2]),int(aux1[1]),int(aux1[0]))

aux2 = proyect.fechaFinTardio.split("/")
fecha2 = date(int(aux2[2]),int(aux2[1]),int(aux2[0]))
print(fecha2 - fecha1)

print(proyect.finTemprano)
