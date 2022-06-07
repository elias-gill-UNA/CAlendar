import funcionesSobreObjetos.actividadFunciones as actividadFunciones
import backend.comprobaciones.verificarEntradas as verificarInput
from clases.actividades import Actividad
from tkinter import messagebox
import tkinter as tk
def guardar_Actividad(nombre, duracion, dependencia, tabla):
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
            cargar_Tabla_Actividad(tabla)
    except ValueError as Error:
        messagebox.showwarning("Advertencia", str(Error))

# Carga las actividades en el proyecto
def cargar_Tabla_Actividad(tabla):
    global conexion

    # Limpia la tabla
    for item in tabla.get_children():
        tabla.delete(item)

    if conexion != None:
        actividades = actividadFunciones.leerActividades(conexion)
        for i in actividades:
            tabla.insert("", tk.END, text=i.identificador,
                         values=(i.nombre, i.duracion, i.dependencias))