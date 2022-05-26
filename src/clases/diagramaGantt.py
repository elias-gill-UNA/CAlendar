nombres=["a","b","c","d","e","f","g","h","i"]
duracion=[25,50,45,60,5,5,20,6,100]
dependencias=[["Inicio"],["a"],["a"],["b"],["b"],["c"],["e","f"],["d"],["g","h"]]
colores = ["red","green","yellow","pink","purple","orange","black","blue","orange"]
columnas=365
filas=len(nombres)
matriz=[]

class TareaEnFormatoGUI:
    def __init__(self, indiceInicio, duracion, color,arregloNro, nombre):
        self.indiceInicio = indiceInicio
        self.duracion = duracion
        self.color = color
        self.numActividad = arregloNro
        self.nombre = nombre


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
    #print(definitivo)
    return definitivo

def DiagramaGantt(nombres,dependencias,duracion,matriz,columnas):
    #creacion de matriz
    for i in range(filas):
        matriz.append([0] * columnas)

    for i in range(len(nombres)):
        if dependencias[i][0]!="Inicio":
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

def ConseguirDataParaGUI():

    DiagramaGantt(nombres, dependencias, duracion, matriz, columnas)

    arregloTareasGUI = []

    print(matriz[0][1])

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
