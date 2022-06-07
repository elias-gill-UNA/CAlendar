import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import *
import utilidades.calendario as calendar

def feriados(conexion):
    def cargar_tabla(tabla):
        for item in tabla.get_children():
            tabla.delete(item)
        feriados= calendar.getListaFeriados(conexion)
        for feriado in feriados:
            tabla.insert("", tk.END, text=feriado.identificador, values=(
                    str(feriado.dia)+"/"+str(feriado.mes), feriado.descripcion))   
    
    ventana=tk.Tk()
    tabla= ttk.Treeview(ventana, height=10, columns=("#0","1"))
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    tabla.place(x=90, y=180)
    tabla.grid(row=3, column=0)

    # Barra de desplazamiento
    barraDesplazamiento = ttk.Scrollbar(
        ventana, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscrollcommand=barraDesplazamiento.set)
    barraDesplazamiento.grid(row=3, column=1, sticky="ns")

    # Tamaño de las columnas
    tabla.column("#0", width=50, anchor=CENTER)
    tabla.column("#1", width=150, anchor=CENTER)
    tabla.column("#2", width=150, anchor=CENTER)

    # Titulos
    tabla.heading("#0", text="Id",anchor=CENTER)
    tabla.heading("#1", text="Fecha",anchor=CENTER)
    tabla.heading("#2", text="Acontecimiento",anchor=SW)
    cargar_tabla(tabla)

    fecha=tk.StringVar()
    lbl_fecha = tk.Label(ventana, text="Fecha", font=("Times New Roman", 12)).grid(row=0,column=0,sticky="w")
    fecha = DateEntry(ventana, selectmode="day",textvariable=fecha, width=17)
    fecha.grid(row=0, column=1)

    descri = tk.Label(ventana, text="Descripción:", font=("Times New Roman", 12)).grid(row=1, column=0,sticky="w")
    descri = tk.Entry(ventana, width=20)
    descri.grid(row=1, column=1)

    # Botones
    tk.Button(ventana, text="Eliminar",command=lambda: eliminar_Feriado(tabla)).grid(row=2, column=0)
    tk.Button(ventana, text="Agregar",command=lambda: crear_Feriado(fecha.get(),descri.get(),tabla)).grid(row=2, column=1)

    def crear_Feriado(fecha,descripcion,tabla):
        if descripcion!="":
            calendar.anadirFeriado(conexion,fecha,descripcion)
            cargar_tabla(tabla)
    
    def eliminar_Feriado(tabla):
        try:
            x = tabla.selection()[0]
            id = tabla.item(tabla.selection())['text']
            tabla.delete(x)
            calendar.eliminarFeriado(conexion, id)
            cargar_tabla(tabla)
        except IndexError:
            messagebox.showwarning(
                "Advertencia", "Seleccione una Actividad para eliminar!")


