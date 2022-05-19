import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from tkcalendar import *



class form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__inicializarGUI__()

    def __inicializarGUI__(self):
        self.title("")

        # Etiquetas
        lbl_titulo = tk.Label(self, text="CREAR ACTIVIDAD", font=("Courier", 20))
        lbl_titulo.grid(row=0, column=1)
        self.minsize(400, 200)
        self.maxsize(400, 200)
        frmPrincipal = tk.Frame(self, bd=7, relief="groove")
        frmPrincipal.grid(row=1, column=1, padx=5, pady=10)

        lbl_nombre = tk.Label(frmPrincipal, text="Nombre de la actividad:", font=("Times New Roman", 12))
        lbl_nombre.grid(row=0, column=0, sticky="w")
        self.nombre = tk.Entry(frmPrincipal, width=20)
        self.nombre.grid(row=0, column=1)

        lbl_duracion = tk.Label(frmPrincipal, text="Duración:", font=("Times New Roman", 12))
        lbl_duracion.grid(row=1, column=0, sticky="w")
        self.duracion = tk.Entry(frmPrincipal, width=20)
        self.duracion.grid(row=1, column=1)

        lbl_identificador = tk.Label(frmPrincipal, text="Identificador:", font=("Times New Roman", 12))
        lbl_identificador.grid(row=2, column=0, sticky="w")
        self.identificador = tk.Entry(frmPrincipal, width=20)
        self.identificador.grid(row=2, column=1)

        self.fechaInicio = tk.StringVar()
        lbl_fechaInicio = tk.Label(frmPrincipal, text="Fecha de Inicio dd/mm/aa:", font=("Times New Roman", 12))
        lbl_fechaInicio.grid(row=3, column=0, sticky="w")
        fechaI = DateEntry(frmPrincipal, selectmode="day", textvariable=self.fechaInicio, width=17)
        fechaI.grid(row=3, column=1)

        # Botones
        btn_guardar = tk.Button(frmPrincipal, text="Añadir", command=self.agregar)
        btn_guardar.grid(row=4, column=2)

        btn_salir = tk.Button(frmPrincipal, text="Salir", command=quit)
        btn_salir.grid(row=4, column=3)

        # Boton para dejar de cargar
        # btn_listo=tk.Button(frmPrincipal,text="Siguiente")
        # btn_listo.grid(row=4,column=1,sticky="e")
        # desoues de guardar la actividad hay que vaciar la lista

    def __validacion__(self, nombre, duracion, identificador, fechaInicio):
        valido = True
        if not 1 < len(nombre) <= 20:
            messagebox.showwarning("Mensaje", "Nombre de Actividad invalido")
            valido = False
        if not duracion.isdigit():
            messagebox.showwarning("Mensaje", "La duración ingresada no es válida")
            valido = False
        elif not 0 < int(duracion) <= 99:
            messagebox.showwarning("Mensaje", "La duración no puede superar 99 días")
            valido = False

        if not identificador.isdigit():
            messagebox.showwarning("Mensaje", "El identificador ingresado no es válido")
            valido = False
        elif not 0 <= int(identificador) <= 999:
            messagebox.showwarning("Mensaje", "El identificador  no puede superar 999 ")
            valido = False

        try:
            bool(datetime.strptime(fechaInicio, "%m/%d/%y"))
        except ValueError:
            messagebox.showwarning("Mensaje", "Fecha invalida")
            valido = False
        return valido

    def agregar(self):
        nombre = self.nombre.get()
        duracion = self.duracion.get()
        identificador = self.identificador.get()

        fechaInicio = self.fechaInicio.get()
        if self.__validacion__(nombre, duracion, identificador, fechaInicio):
            # guarda la actividad y despues limpia las cajas de texto
            #self.__limpiar__()
            pass

    def __limpiar__(self):
        self.nombre.delete(0, "end")
        self.duracion.delete(0, "end")
        self.identificador.delete(0, "end")


app = form()
app.mainloop()
