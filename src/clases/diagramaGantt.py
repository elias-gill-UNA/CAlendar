nombres=["a","b","c","d","e","f","g","h","i"]
duracion=[5,2,4,5,5,5,2,3,5]
dependencias=[["-"],["a"],["a"],["b"],["b"],["c"],["e","f"],["d"],["g","h"]]
columnas=21
filas=len(nombres)
matriz=[]
for i in range(filas):
    matriz.append([0]*columnas)
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
def diagramaGantt(nombres,dependencias,duracion,matriz,columnas):
    for i in range(len(nombres)):
        if dependencias[i][0]!="-":
            contador=calcularPosi(matriz,dependencias[i],nombres,columnas)
            contador=contador+1
        else:
            contador=0
        for j in range(duracion[i]):
            matriz[i][contador]=1
            contador=contador+1
diagramaGantt(nombres,dependencias,duracion,matriz,columnas)
for i in range(filas):
    print(matriz[i])