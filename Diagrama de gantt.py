import matplotlib.pyplot as plt # instalar : pip install matplotlib
import numpy as np

# Datos
horizonte = 365  # Simula 1 año
ndatos = 4  # Cantidad de actividades
altura = 10  # Altura de las barras
actividades = ["Acti 1", "Acti 2", "Acti 3", "Acti 4"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre"]

# Crea el diagrama
figura, eje = plt.subplots()  # Retorna una figura y un eje

# Etiquetas
eje.set_title("Actividades del Proyecto")
eje.set_xlabel("Tiempo")
eje.set_ylabel("Actividades")
eje.set_yticks(np.arange(altura / 2, altura * ndatos - altura / 2 + altura, altura))
actividades.reverse()
eje.set_yticklabels(actividades)
eje.set_xticks(np.arange(0, 350, 30))
eje.set_xticklabels(meses, fontsize=7, rotation=15)

# Limite de los ejes
eje.set_xlim(0, horizonte)
eje.set_ylim(0, ndatos * altura)

# Se agrega Grillas a los dos ejes
#   Lineas verticales
eje.set_xticks(range(0, horizonte, 5), minor=True)
eje.grid(True, axis="x", which="both")
#   Lineas horizontales
eje.set_yticks(range(altura, ndatos * altura, altura), minor=True)
eje.grid(True, axis="y", which="minor")


def agregar_actividaes(inicio, duracion, color,numActividad):
    eje.broken_barh([(inicio, duracion)], (altura * numActividad, altura), facecolors=(color))


# duaracion: cuantos dias se establecio para esa actividad
agregar_actividaes(5, 26, "orange",3)
agregar_actividaes(20, 120, "blue",2)
agregar_actividaes(50, 80, "red",1)
agregar_actividaes(100, 260, "yellow",0)
plt.show()  # Muestra la figura
