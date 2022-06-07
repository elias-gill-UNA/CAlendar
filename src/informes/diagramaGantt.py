from backend.dataBase import proyectManager
from clases.actividades import *;
import backend.dataBase.activitiesManager as actiManager
from clases.clases_cam_critico import ObjetoCritico
import informes.camino_critico as camCritico 

dependencias=[]
nombres=[]
duracion=[]
columnas=37 # en columnas va la duracion del proyecto
colores = ["blue","red"]
filas = 0
matriz=[]

class TareaEnFormatoGUI:
    def __init__(self, indiceInicio, duracion, color, arregloNro, nombre):
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

    dependencias=[]
    nombres=[]
    duracion=[]
    columnas=0
    filas = 0

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
    print("DURACION",columnas)
    filas = len(nombres)
    print("FILAS",filas)

def calcularPosi(matriz, dependencias, nombres, columnas):
    contador = 0
    definitivo = -1
    #print("len dependencias",len(dependencias))
    #print("len matriz[0]",len(matriz[0]))
    '''for f in range(0,len(nombres)):
        for c in range(0,columnas):
            print(matriz[f][c],end=" ")
        print("\n")'''
    for k in range(len(dependencias)):
        indice = nombres.index(dependencias[k])
        for j in range(columnas):
            if matriz[indice][j]==1:
                contador=j
        if(definitivo<contador):
            definitivo=contador
    #print("SEPARADOR")
    return definitivo

def DiagramaGantt(nombres, dependencias, duracion, columnas):
    # creacion de matriz
    global matriz
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)

    for i in range(len(nombres)):
        if dependencias[i][0]!="-":
            contador=calcularPosi(matriz,dependencias[i],nombres,columnas)
            contador=contador+1
        else:
            contador = 0
        for j in range(duracion[i]):
            # No pasar cantidad maxima de dias
            if (contador >= columnas):
                break
            matriz[i][contador] = 1
            contador = contador + 1


def ConseguirDataParaGUI(conexion):
    #Lista de actividades y duracion sin contar feriados
    global listaActividades
    listaActividades=[]
    listaActividades = actiManager.getListaActividadesAutoreferenciada(conexion)
    listaVacia = []
    objetoCritico = ObjetoCritico()
    proyecto = proyectManager.getProyectInfo(None, conexion)
    camCritico.funcionFinalYSuperpoderosa(conexion, listaActividades, listaVacia,objetoCritico, proyecto)

    prepararGantt(listaActividades, proyecto.finTemprano)
    DiagramaGantt(nombres,dependencias,duracion,columnas)

    arregloTareasGUI = []

    for i in range(0, len(nombres)):

        tareaEmpiezaIndice = 0

        # Calcula la posicion de inicio de la tarea en el grafico
        for j in range(0, columnas):
            if (matriz[i][j] == 1):
                break
            tareaEmpiezaIndice += 1
        
        color = 0


        for actividad in objetoCritico.actividadesCriticas:        
            if(listaActividades[i].identificador == actividad.identificador):
                color = 1
                break

        tareaGUI = TareaEnFormatoGUI(tareaEmpiezaIndice, duracion[i], colores[color], i, nombres[i])
        arregloTareasGUI.append(tareaGUI)

    return arregloTareasGUI

