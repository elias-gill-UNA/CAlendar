import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import backend.dataBase.activitiesManager as activitiesManager
import backend.dataBase.proyectManager as proyectManager

from informes.camino_critico import funcionFinalYSuperpoderosa
from clases.clases_cam_critico import ObjetoCritico
from GUI.centrar_ventana import centrar_Ventana


def mostrar_Actividades_Criticas(objcritico, listaActvsconFecha, objProyecto):
    ventana = tk.Toplevel()
    ventana.title("Actividades Críticas")
    centrar_Ventana(ventana, 3)
    frame = tk.Frame(ventana)
    tk.Label(ventana, text="Cantidad de Caminos Críticos:"+" "+str(objcritico.cantidadCritico),font=("Courier", 14)).grid(row=0, column=0)
    
    frame.grid(row=1, column=0)

    inicio = datetime.strptime(objProyecto.fechaInicio, "%Y-%m-%d")
    fin = datetime.strptime(objProyecto.fechaFinTemprano, "%Y-%m-%d")
    diferencia = fin-inicio
    
    tk.Label(frame, text="Duración del Proyecto (en días laborales): "+ str(objProyecto.finTemprano)).grid(row=0, column=0)
    tk.Label(frame, text="Fecha de Inicio del Proyecto: "+ str(objProyecto.fechaInicio)).grid(row=1, column=0)
    tk.Label(frame, text="Fecha de Finalización prevista: "+ str(objProyecto.fechaFinTardio)).grid(row=2, column=0)
    tk.Label(frame, text="Duración (contando días no laborales): "+ str(diferencia)).grid(row=3, column=0)


    lbl_critico = tk.Label(
        frame, text="\nLista de actividades del Camino Crítico").grid(row=4, column=0)

    # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
    tabla1 = ttk.Treeview(frame, height=10, columns=("#0", "#1", "#2"))
    tabla1.place(x=90, y=180)
    tabla1.grid(row=5, column=0)

    # Barra de desplazamiento
    barraDesplazamiento = ttk.Scrollbar(
        frame, orient=tk.VERTICAL, command=tabla1.yview)
    tabla1.configure(yscrollcommand=barraDesplazamiento.set)
    barraDesplazamiento.grid(row=5, column=1, sticky="ns")

    # Tamaño de las columnas
    tabla1.column("#0", width=50, anchor=CENTER)
    tabla1.column("#1", width=250, anchor=CENTER)
    tabla1.column("#2", width=250, anchor=CENTER)
    tabla1.column("#3", width=250, anchor=CENTER)

    # Titulos
    tabla1.heading("#0", text="Id")
    tabla1.heading("#1", text="Nombre")
    tabla1.heading("#2", text="Fecha Inicio")
    tabla1.heading("#3", text="Fecha Fin")

    for item in tabla1.get_children():
        tabla1.delete(item)
    for acti in objcritico.actividadesCriticas:
        if acti.nombre != "Fin" and acti.nombre != "Inicio":
            tabla1.insert("", tk.END, text=acti.identificador, values=(
                acti.nombre, acti.fechaInicioTemprano, acti.fechaFinTemprano))
    
    tk.Label(
        frame, text="Caminos Críticos").grid(row=4, column=2)
    
    tabla2 = ttk.Treeview(frame, height=10, columns=())

    tabla2.place(x=90, y=180)
    tabla2.grid(row=5, column=2)

    # Barra de desplazamiento
    barraDesplazamiento = ttk.Scrollbar(
        frame, orient=tk.VERTICAL, command=tabla2.yview)
    tabla2.configure(yscrollcommand=barraDesplazamiento.set)
    barraDesplazamiento.grid(row=5, column=3, sticky="ns")

    # Tamaño de las columnas
    tabla2.column("#0", width=150, anchor=CENTER)

    # Titulos
    tabla2.heading("#0", text="Caminos")

    for camino in objcritico.caminosCriticos:
        for actividad in camino:
            if actividad.identificador == 0:
                tabla2.insert("", tk.END, text="----")
            else:
                tabla2.insert("", tk.END, text=actividad.nombre)
    
    frame2= tk.Frame(ventana)
    frame2.grid(row=2, column=0)
    tk.Label(frame2, text="\nLista de Actividades").grid(row=0, column=0)
    # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
    tabla3 = ttk.Treeview(frame2, height=10, columns=("#0", "#1", "#2"))
    tabla3.place(x=90, y=180)
    tabla3.grid(row=1, column=0)

    # Barra de desplazamiento
    barraDesplazamiento = ttk.Scrollbar(
        frame2, orient=tk.VERTICAL, command=tabla1.yview)
    tabla3.configure(yscrollcommand=barraDesplazamiento.set)
    barraDesplazamiento.grid(row=1, column=1, sticky="ns")

    # Tamaño de las columnas
    tabla3.column("#0", width=50, anchor=CENTER)
    tabla3.column("#1", width=250, anchor=CENTER)
    tabla3.column("#2", width=250, anchor=CENTER)
    tabla3.column("#3", width=250, anchor=CENTER)

    # Titulos
    tabla3.heading("#0", text="Id")
    tabla3.heading("#1", text="Nombre")
    tabla3.heading("#2", text="Fecha Inicio")
    tabla3.heading("#3", text="Fecha Fin")

    for item in tabla3.get_children():
        tabla3.delete(item)
    for acti in listaActvsconFecha:
        if acti.nombre != "Fin" and acti.nombre != "Inicio":
            tabla3.insert("", tk.END, text=acti.identificador, values=(
                acti.nombre, acti.fechaInicioTemprano, acti.fechaFinTemprano))
    
    ventana.mainloop()


def iniciar_Camino_Critico(conexion):
    listaautoref = activitiesManager.getListaActividadesAutoreferenciada(conexion)
    listaActvsconFecha = []
    objcritico = ObjetoCritico()
    objProyecto = proyectManager.getProyectInfo(None, conexion)

    funcionFinalYSuperpoderosa(
        conexion, listaautoref, listaActvsconFecha, objcritico, objProyecto)
    mostrar_Actividades_Criticas(objcritico, listaActvsconFecha, objProyecto)

