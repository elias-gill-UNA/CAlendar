import tkinter as tk
from tkinter import ttk


from tkcalendar import *



class Interfaz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  # indica la ventana contenedora del frame principal
        self.master = master
        self.pack()  # ubica los elementos
        self.frame1()
        self.frame2()
        self.frame3()
        lbl_titulo = tk.Label(self, text="CREAR O EDITAR ACTIVIDADES", font=("Courier", 20))
        lbl_titulo.grid(row=0, column=0)

    def frame1(self):
        # Crea un cuadro
        frame = tk.Frame(self)
        frame.grid(row=1, column=0)

        # Etiquetas
        lbl_nombre = tk.Label(frame, text="Nombre de la actividad:", font=("Times New Roman", 12))
        lbl_nombre.grid(row=0, column=0, sticky="w")
        self.nombre = tk.Entry(frame, width=20)
        self.nombre.grid(row=0, column=1)

        self.fechaInicio = tk.StringVar()
        lbl_fechaInicio = tk.Label(frame, text="Fecha de Inicio dd/mm/aa:", font=("Times New Roman", 12))
        lbl_fechaInicio.grid(row=1, column=0, sticky="w")
        fechaI = DateEntry(frame, selectmode="day", textvariable=self.fechaInicio, width=17)
        fechaI.grid(row=1, column=1)

        lbl_duracion = tk.Label(frame, text="Duración:", font=("Times New Roman", 12))
        lbl_duracion.grid(row=1, column=2, sticky="w")
        self.duracion = tk.Entry(frame, width=20)
        self.duracion.grid(row=1, column=3)

        lbl_separador = tk.Label(frame, text="")
        lbl_separador.grid(row=2, column=0)

        # Botones
        btn_crear = tk.Button(frame, text="Crear Actividad")
        btn_crear.grid(row=5, column=0)

        btn_editar = tk.Button(frame, text="Editar Actividad")
        btn_editar.grid(row=5, column=1)

        btn_eliminar = tk.Button(frame, text="Eliminar Actividad")
        btn_eliminar.grid(row=5, column=2)

        btn_mostrar = tk.Button(frame, text="Actualizar Tabla")
        btn_mostrar.grid(row=5, column=3)

    def frame2(self):
        # Crea un cuadro para la tabla
        frame = tk.Frame(self)
        frame.grid(row=2, column=0)

        # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
        tabla = ttk.Treeview(frame, height=10, columns=("#0", "#1", "#2"))
        tabla.place(x=90, y=180)
        tabla.grid(row=1, column=0)

        # Barra de desplazamiento
        barraDesplazamiento = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview())
        tabla.configure(yscrollcommand=barraDesplazamiento)
        barraDesplazamiento.grid(row=1, column=1, sticky="ns")

        # Tamaño de las columnas
        tabla.column("#0", width=50)
        tabla.column("#1", width=400)
        tabla.column("#2", width=90)
        tabla.column("#3", width=60)

        # Titulos
        tabla.heading("#0", text="Id")
        tabla.heading("#1", text="Nombre de la actividad")
        tabla.heading("#2", text="Fecha Inicio")
        tabla.heading("#3", text="Duración")


    def frame3(self):
        # Crea un cuadro
        frame = tk.Frame(self)
        frame.grid(row=3, column=0)

        # Botones
        # Tiene que ir a la funcion informe que esta en comprobaciones
        btn_siguiente = tk.Button(frame, text="Informe")
        btn_siguiente.grid(row=0, column=2)

        # Etiquetas
        lbl_opciones = tk.Label(frame, text="Opciones:")
        lbl_opciones.grid(row=0, column=0)

        # Lista de opciones
        self.opcion=tk.StringVar()
        combo = ttk.Combobox(frame, values=["Diagrama de Gantt", "Mapa de Dependencias"],textvariable=self.opcion)
        combo.place(x=50, y=50)
        combo.grid(row=0, column=1)
    # Actualiza la tabla
    def actualizar(self):
        pass

    # Elimina una actividad de la tabla
    def eliminar(self):

        pass

    # Editar alguna actividad
    def editar(self):
        pass




# Crea la ventana root: raiz o principal
root = tk.Tk()
# Tamaño de la ventana
root.geometry("850x500")
# Titulo de la ventana
root.title("ACTIVIDADES")

app = Interfaz(master=root)
app.mainloop()
