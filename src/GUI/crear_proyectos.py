import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from GUI.crear_edit_borrarActividades import *


def ir_Actividad(frame, frame2, frame3, ID, Nom, Des, Fech):
    #from src.GUI.crear_edit_borrarActividades import ventana_Acti
    # Crea un objeto de tipo proyecto
    #P = Pr.proyecto(ID, Nom, Des, Fech)
    # Aca tendria que guardar los datos ingresados en la Bd
    # .............
    # Limpia la ventana
    frame.destroy()
    frame2.destroy()
    frame3.destroy()
    # Pasa a la ventana para crear actividades
    #ventana_Acti(root)
    ventana_Acti(root)
    #ventana_Pro(root)

def ventana_Pro(root):
    # Crea la ventana principal

    root.title("PROYECTOS")

    frame = tk.Frame(root)
    frame.pack()

    # Tamaño de la ventana
    root.geometry("850x500")

    # Etiquetas
    lbl_titulo = tk.Label(frame, text="\tCREAR PROYECTOS", font=("Courier", 20), anchor="center")
    lbl_titulo.grid(row=0, column=0)

    lbl_nombre = tk.Label(frame, text="Nombre del Proyecto:", font=("Times New Roman", 12))
    lbl_nombre.grid(row=1, column=0, sticky="w")
    nombre = tk.Entry(frame, width=20)
    nombre.grid(row=1, column=1)

    lbl_ID = tk.Label(frame, text="Identificador:", font=("Times New Roman", 12))
    lbl_ID.grid(row=2, column=0, sticky="w")
    ID = tk.Entry(frame, width=20)
    ID.grid(row=2, column=1)

    fechaInicio = tk.StringVar()  # Guarda la fecha ingresada
    lbl_fechaInicio = tk.Label(frame, text="Fecha de Inicio dd/mm/aa:", font=("Times New Roman", 12))
    lbl_fechaInicio.grid(row=3, column=0, sticky="w")
    fechaI = DateEntry(frame, selectmode="day", textvariable=fechaInicio, width=17)
    fechaI.grid(row=3, column=1)

    lbl_descripcion = tk.Label(frame, text="Descripción:", font=("Times New Roman", 12))
    lbl_descripcion.grid(row=4, column=0, sticky="w")

    # Crea una caja de texto para la descripción
    descrip = Text(frame, width=20, height=5)
    descrip.grid(row=4, column=1)

    # Crea un espacio entre frame y frame2
    espacio = tk.Label(frame, text="")
    espacio.grid(row=5, column=0)

    frame2 = tk.Frame(root)
    frame2.pack()

    # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
    tabla = ttk.Treeview(frame2, height=10, columns=("#0", "#1", "#2"))
    tabla.place(x=90, y=180)
    tabla.grid(row=0, column=0)

    # Barra de desplazamiento
    barraDesplazamiento = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscrollcommand=barraDesplazamiento)
    barraDesplazamiento.grid(row=0, column=2, sticky="nsew")

    # Tamaño de las columnas
    tabla.column("#0", width=40)
    tabla.column("#1", width=200)
    tabla.column("#2", width=120)
    tabla.column("#3", width=200)

    # Titulos
    tabla.heading("#0", text="Id")
    tabla.heading("#1", text="Nombre del Proyecto")
    tabla.heading("#2", text="Fecha Inicio Previsto")
    tabla.heading("#3", text="Descripcion")

    frame3 = tk.Frame(root)
    frame3.pack()
    # Crea un espacio entre los botones
    espacio = tk.Label(frame3, text="")
    espacio.grid(row=0, column=1)
    espacio = tk.Label(frame3, text="\t\t\t\t")
    espacio.grid(row=0, column=4)

    # Botones
    btn_salir = tk.Button(frame3, text="Salir", command=quit)
    btn_salir.grid(row=0, column=2)

    btn_siguiente = tk.Button(frame3, text="Siguiente",
                              command=lambda: ir_Actividad(frame, frame2, frame3, ID.get(), nombre.get(),
                                                           descrip.get(1.0, "end"),
                                                           fechaI))
    btn_siguiente.grid(row=0, column=5, sticky="ns")




root = tk.Tk()
ventana_Pro(root)
root.mainloop()
