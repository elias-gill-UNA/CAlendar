import backend.comprobaciones.verificarEntradas as verificarInput
import backend.dataBase.proyectManager as proyectManager
from clases.proyecto import Proyecto
import tkinter as tk
import funcionesSobreObjetos.proyectoFunciones as funcProyectos
from tkinter import messagebox
import Interfaz as In
def guardar_Proyecto(tabla, nombre, descrip, fechaI):
    # Valida los datos antes de crear el Proyecto
    if verificarInput.validar_Proyecto(nombre, descrip, fechaI):
        Pr = Proyecto(nombre, descrip, fechaI)
        # Crea el proyecto
        id = proyectManager.crearProyecto(Pr)
        # Elimina los datos de la tabla
        for item in tabla.get_children():
            tabla.delete(item)
        # Vuelve a cargar los datos en la tabla agregandole el nuevo proyecto creado
        cargar_Tabla_Proyecto(tabla)

# Carga los proyectos en la tabla
def cargar_Tabla_Proyecto(tabla):
    proyectos = proyectManager.getProyectListsWithInfo()
    for i in proyectos:
        tabla.insert('', tk.END, text=i.identificador, values=(
            i.nombre, i.fechaInicio, i.descripcion))

# Cuando da click a el boton Abrir viene aca
def seleccionar_Proyecto(tabla, framePrincipal):
    try:
        global conexion
        global listActividades
        global objProyecto
        id = tabla.item(tabla.selection())['text']
        # Si este tira error es porque no selecciono nada
        x = tabla.selection()[0]
        # abrir el proyecto recien creado y dar valor a las globales
        proyecto = funcProyectos.abrirProyecto(id)
        conexion = proyecto[0]
        objProyecto = proyecto[1]
        listActividades = proyecto[2]
        In.limpiar_Pantalla(framePrincipal, 0)
    except IndexError:
        messagebox.showwarning(
            "Advertencia", "Seleccione un Proyecto para abrir!")

