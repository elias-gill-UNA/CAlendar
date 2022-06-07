import tkinter as tk
from tkinter import *
from tkinter import messagebox
from clases.actividades import Actividad
import funcionesSobreObjetos.actividadFunciones as actividadFunciones
import backend.comprobaciones.verificarEntradas as verificarInput

from GUI.centrar_ventana import *

def guardar_Actividad(conexion, nombre, duracion, dependencia, tabla):
    try:
        if verificarInput.validar_Actividad(nombre, duracion):
            actividad = Actividad(nombre, duracion, dependencia)
            # Crea la actividad
            AC = actividadFunciones.crearActividad(
                conexion, actividad.nombre, actividad.duracion, actividad.dependencias)
            # Limpia la tabla
            for item in tabla.get_children():
                tabla.delete(item)
            # Vuelve a cargar los datos en la tabla agregandole la actividad creada
            cargar_Tabla_Actividad(conexion, tabla)
    except ValueError as Error:
        messagebox.showwarning("Advertencia", str(Error))

# Carga las actividades en el proyecto
def cargar_Tabla_Actividad(conexion, tabla):

    # Limpia la tabla
    for item in tabla.get_children():
        tabla.delete(item)

    if conexion != None:
        actividades = actividadFunciones.leerActividades(conexion)
        for i in actividades:
            tabla.insert("", tk.END, text=i.identificador,
                         values=(i.nombre, i.duracion, i.dependencias))


