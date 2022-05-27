from camino_critico import *
from ...clases.clases_cam_critico import *

# crea el proyecto y cargar actividades
proyect = Proyecto()
objCrit = Criticos()
listaacts = []

# actividad 0
anteriores = []
actividad = Actividad("Inicio", 0, anteriores)
listaacts.append(actividad)

# actividad 1
anteriores = []
anteriores.append(listaacts[0])
actividad = Actividad("A", 5, anteriores)
listaacts.append(actividad)

# actividad 2
anteriores = []
anteriores.append(listaacts[0]) # dependencias supongo
actividad = Actividad("B", 1, anteriores)
listaacts.append(actividad)

# actividad 3
anteriores = []
anteriores.append(listaacts[1])
actividad = Actividad("C", 2, anteriores)
listaacts.append(actividad)

# actividad 4
anteriores = []
anteriores.append(listaacts[1])
actividad = Actividad("D", 3, anteriores)
listaacts.append(actividad)

# actividad 5
anteriores = []
anteriores.append(listaacts[1])
actividad = Actividad("E", 2, anteriores)
listaacts.append(actividad)

# actividad 6
anteriores = []
anteriores.append(listaacts[3])
actividad = Actividad("F", 3, anteriores)
listaacts.append(actividad)

# actividad 7
anteriores = []
anteriores.append(listaacts[4])
actividad = Actividad("G", 4, anteriores)
listaacts.append(actividad)

# actividad 8
anteriores = []
anteriores.append(listaacts[2])
anteriores.append(listaacts[5])
actividad = Actividad("H", 2, anteriores)
listaacts.append(actividad)

# actividad 9
anteriores = []
anteriores.append(listaacts[8])
actividad = Actividad("I", 1, anteriores)
listaacts.append(actividad)

# actividad 10
anteriores = []
anteriores.append(listaacts[6])
anteriores.append(listaacts[7])
anteriores.append(listaacts[9])
actividad = Actividad("J", 1, anteriores)
listaacts.append(actividad)

# actividad 11
anteriores = []
anteriores.append(listaacts[10])
actividad = Actividad("Fin", 0, anteriores)
listaacts.append(actividad)

caminoCritico(listaacts,proyect, objCrit)
cantidadCaminosCriticos(objCrit, listaacts[0])# siempre recibe como primer argumento la primera actividad
inicializarCritico(objCrit, listaacts)
cargarCriticos(objCrit, listaacts[0], 0)

print("Las actividades son: ", end='')
for i in objCrit.actividadesCriticas:
    print(i.nombre, end=', ')
print("\nCantidad de caminos:", objCrit.cantidadCritico)
print("....")

for j in range(objCrit.cantidadCritico):
    print("el camino critico numero "+str(j+1)+" es")
    for i in objCrit.caminosCriticos[j]:
        print(i.nombre)

