from clases.actividades import *;
import backend.dataBase.activitiesManager as actiManager
import camino_critico 

dependencias=[]
nombres=[]
duracion=[]
columnas=37 # en columnas va la duracion del proyecto
colores = ["red","green","yellow","pink","purple","orange","black","blue","orange"]
filas = 0
matriz=[]

##################Fake Data
listaGeneral=[]
names=["A","B","C","D","E","F","G","H"]
duraciones=[4,10,5,15,12,4,8,7]
for i in range(len(names)):
    actividad=Actividad(i,names[i],duraciones[i],[],"12/02/2021","13/02/2021",0)
    listaGeneral.append(actividad)
listaGeneral[2].dependencias=[0]#c
listaGeneral[3].dependencias=[1,2]#d
listaGeneral[4].dependencias=[1]#e
listaGeneral[5].dependencias=[3]#f
listaGeneral[6].dependencias=[4]#h
listaGeneral[7].dependencias=[5,6]#i
#######################################

class TareaEnFormatoGUI:
    def __init__(self, indiceInicio, duracion, color,arregloNro, nombre):
        self.indiceInicio = indiceInicio
        self.duracion = duracion
        self.color = color
        self.numActividad = arregloNro
        self.nombre = nombre

#recibe la lista de actividades desde la base de datos
# y carga cada lista vacia con sus valores(listaGeneral, duracionProyecto)
def prepararGantt(listaActividades, duracionProyectoSinFeriados):

    global nombres
    global dependencias
    global duracion
    global filas
    global columnas

    contador=0
    for actividad in listaActividades:
        nombres.append(actividad.nombre)
        duracion.append(actividad.duracion)
        if(len(actividad.dependencias)==0):
            dependencias.append("-")
        else:
            aux=[]
            for dependencia in actividad.dependencias:
                aux.append(listaActividades[dependencia].nombre)
            dependencias.append(aux)
        contador=contador+1

    columnas = duracionProyectoSinFeriados
    filas = len(nombres)

def calcularPosi(matriz,dependencias,nombres,columnas):
    contador=0
    definitivo=-1
    for k in range(len(dependencias)):
        indice=nombres.index(dependencias[k])
        for l in range(columnas):
            if matriz[indice][l]==1:
                contador=l
        if(definitivo<contador):
            definitivo=contador

    return definitivo

def DiagramaGantt(nombres,dependencias,duracion,matriz,columnas):
    #creacion de matriz
    for i in range(filas):
        matriz.append([0] * columnas)

    for i in range(len(nombres)):
        if dependencias[i][0]!="-":
            contador=calcularPosi(matriz,dependencias[i],nombres,columnas)
            contador=contador+1
        else:
            contador=0
        for j in range(duracion[i]):
            #No pasar cantidad maxima de dias
            if(contador >= columnas):
                break
            matriz[i][contador]=1
            contador=contador+1

def ConseguirDataParaGUI(conexion):
    #Lista de actividades y duracion sin contar feriados
    lista = actiManager.getListaActividadesAutoreferenciada(conexion)
    aux = lista
   # camino_critico.
    camino_critico.cantidadCaminosCriticos

    prepararGantt(lista, 37)
    DiagramaGantt(nombres,dependencias,duracion,matriz,columnas)

    arregloTareasGUI = []

    for i in range(filas):
       print(matriz[i])

    for i in range(0, len(nombres)):

        tareaEmpiezaIndice = 0;

        #Calcula la posicion de inicio de la tarea en el grafico
        for j in range(0, columnas):
            if(matriz[i][j] == 1):
                break;
            tareaEmpiezaIndice+=1;

        tareaGUI = TareaEnFormatoGUI(tareaEmpiezaIndice, duracion[i], colores[i], i, nombres[i]);
        arregloTareasGUI.append(tareaGUI);

    return arregloTareasGUI

