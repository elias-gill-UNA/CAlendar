import tkinter as tk
from tkinter import *


# Crea los nodos
def crearFrame(ventana,actividad):
    # Crea un cuadro
    frame = tk.Frame()

    # Aca tendria que variar las posiciones
    frame.grid(row=actividad[3], column=actividad[4])

    frame.config(relief="ridge")  # relieve del frame hundido
    frame.config(bd=10)  # tamaño del borde en píxeles
    lbl_nombre = tk.Label(frame, text="Nombre de la actividad:", font=("Times New Roman", 12))
    lbl_nombre.grid(row=0, column=0, sticky="w")
    lbl_nombre = tk.Label(frame, text=actividad[0], font=("Times New Roman", 12))
    lbl_nombre.grid(row=0, column=1, sticky="w")

    lbl_fechaInicio = tk.Label(frame, text="Fecha de Inicio", font=("Times New Roman", 12))
    lbl_fechaInicio.grid(row=1, column=0, sticky="w")
    lbl_fechaInicio = tk.Label(frame, text=actividad[2],font=("Times New Roman", 12))
    lbl_fechaInicio.grid(row=1, column=1, sticky="w")

    lbl_duracion = tk.Label(frame, text="Duración:", font=("Times New Roman", 12))
    lbl_duracion.grid(row=2, column=0, sticky="w")
    lbl_duracion = tk.Label(frame, text=actividad[1], font=("Times New Roman", 12))
    lbl_duracion.grid(row=2, column=1, sticky="w")

# Crear ventana
root = tk.Tk()
# Podriamos guardar la actividad en una lista
# el 0,0 seria las posiciones que debe tener (nose como hacer)
actividad=["Acti1","dur","FI",0,0]
# Titulo de la ventana
root.title("Visualizar Actividades")
# Tamaño de la ventana
root.geometry("850x500")

crearFrame(root,actividad)
root.mainloop()

