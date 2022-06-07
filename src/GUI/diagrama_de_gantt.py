from glob import glob
import matplotlib.pyplot as plt # instalar : pip install matplotlib
import numpy as np
from informes.diagramaGantt import ConseguirDataParaGUI
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Datos
horizonte = 365  # Simula 1 año
ndatos = 20  # Cantidad de actividades
altura = 10  # Altura de las barras
actividades = []
meses = ["0", "40", "70", "100", "130", "160", "190",
         "220", "250", "280", "310", "340"]

# Crea el diagrama


def CrearDiagrama(eje):
    # Etiquetas
    eje.set_title("Actividades del Proyecto")
    eje.set_yticks(np.arange(altura / 2, altura * ndatos - altura / 2 + altura, altura))
    # actividades.reverse()
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

def agregar_actividad(inicio, duracion, color,numActividad, eje):
    eje.broken_barh([(inicio, duracion)], (altura * numActividad, altura), facecolors=(color))

def AgregarActividades(conexion, eje):
    global ndatos
    global actividades
    actividades = []
    arregloGUI = ConseguirDataParaGUI(conexion)

    ndatos = len(arregloGUI)

    arregloGUI.reverse()

    for i in range(0, len(arregloGUI)):
        
        tareaGUI = arregloGUI[i]
        actividades.append(tareaGUI.nombre)
        # "len(arregloGUI) - tareaGUI.numActividad - 1" Invierte la tabla del lado correcto
        agregar_actividad(tareaGUI.indiceInicio, tareaGUI.duracion, tareaGUI.color, len(arregloGUI) - tareaGUI.numActividad - 1, eje)


# duaracion: cuantos dias se establecio para esa actividad
#Ej: agregar_actividad(20, 120, "blue",2)

def AbrirDiagrama(conexion):
    figura, eje = plt.subplots()  # Retorna una figura y un eje\
    
    global ndatos
    global actividades
    global horizonte
    global altura
    
    horizonte = 365  # Simula 1 año
    ndatos = 20  # Cantidad de actividades
    altura = 10  # Altura de las barras
    actividades = []
    
    AgregarActividades(conexion, eje)
    CrearDiagrama(eje)
    plt.show()

    
