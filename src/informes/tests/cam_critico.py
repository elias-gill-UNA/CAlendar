from clases.actividades import Actividad
from clases.clases_cam_critico import ObjetoCritico
from clases.proyecto import Proyecto
from backend.dataBase import proyectManager
from informes.camino_critico import funcionFinalYSuperpoderosa

# crea el proyecto y cargar actividades
proyectManager.crearProyecto(Proyecto("Nombre del proyecto", "ohala que funciones", "27/05/2022" ))
conexion = proyectManager.abrirProyecto(1)

objCrit = ObjetoCritico()
listaGeneral = []
listaacts = []
proyect = Proyecto("Nombre del proyecto", "ohala que funciones", "27/05/2022")
listaCopia = []

#para probar nms
nombres=["A","B","C","D","E","F","G","H","I","J","K"]
duraciones=[7,15,7,1,30,5,30,1,1,1,1]
for i in range(len(nombres)):
    actividad=Actividad(i,nombres[i],duraciones[i],[],0)
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


print("Las actividades criticas son: ", end='')
for i in objCrit.actividadesCriticas:
    print(i.nombre, end=', ')
print("\nCantidad de caminos:", objCrit.cantidadCritico)

for j in range(objCrit.cantidadCritico):
    print("el camino critico numero "+str(j+1)+" es")
    for i in objCrit.caminosCriticos[j]:
        print(i.nombre)

print("la duracion es "+str(proyect.finTardio-proyect.inicioTardio))


print("los datos del proyecto son ")
print("el inicio temprano es "+str(proyect.fechaInicioTemprano))
print("el inicio tardio es "+str(proyect.fechaInicioTardio))
print("el fin temprano es "+str(proyect.fechaFinTemprano))
print("el fin tardio es "+str(proyect.fechaFinTardio))
print("....")

for actividad in listaacts:
    print("actividad con nombre "+str(actividad.nombre))
    print("su holgura es "+str(actividad.holgura))
    print("el inicio temprano de la actividad es "+str(actividad.fechaInicioTemprano))
    print("el inicio tardio de la actividad es "+str(actividad.fechaInicioTardio))
    print("el fin temprano de la actividad es "+str(actividad.fechaFinTemprano))#
    print("el fin tardio de la actividad es "+str(actividad.fechaFinTardio))
    print("........")
