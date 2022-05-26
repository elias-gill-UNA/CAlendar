import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from src.clases.actividades import *

tabla = 0

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

        lbl_dependencias = tk.Label(frame, text="Dependencias:", font=("Times New Roman", 12))
        lbl_dependencias.grid(row=0, column=2, sticky="w")
        self.dependencias = tk.Entry(frame, width=20)
        self.dependencias.grid(row=0, column=3)

        self.fechaInicio = tk.StringVar()
        lbl_fechaInicio = tk.Label(frame, text="Fecha de Inicio:", font=("Times New Roman", 12))
        lbl_fechaInicio.grid(row=1, column=0, sticky="w")
        fechaI = DateEntry(frame, selectmode="day", textvariable=self.fechaInicio, width=17)
        fechaI.grid(row=1, column=1)

        self.fechaFinal = tk.StringVar()
        lbl_fechaFinal = tk.Label(frame, text="Fecha de Final:", font=("Times New Roman", 12))
        lbl_fechaFinal.grid(row=1, column=2, sticky="w")
        fechaF = DateEntry(frame, selectmode="day", textvariable=self.fechaFinal, width=17)
        fechaF.grid(row=1, column=3)

        lbl_duracion = tk.Label(frame, text="Duración:", font=("Times New Roman", 12))
        lbl_duracion.grid(row=1, column=4, sticky="w")
        self.duracion = tk.Entry(frame, width=20)
        self.duracion.grid(row=1, column=5)

        lbl_separador = tk.Label(frame, text="")
        lbl_separador.grid(row=2, column=0)

        # Botones
        btn_crear = tk.Button(frame, text="Crear Actividad",
        command= lambda: crearActividad(self.nombre.get(),
        self.duracion.get(), self.dependencias.get(), self.fechaInicio.get(), self.fechaFinal.get()))
        btn_crear.grid(row=5, column=0)

        btn_editar = tk.Button(frame, text="Editar Actividad", command=editarActividad)
        btn_editar.grid(row=5, column=1)

        btn_eliminar = tk.Button(frame, text="Eliminar Actividad", command= lambda: self.eliminar(tabla))
        btn_eliminar.grid(row=5, column=2)

        btn_mostrar = tk.Button(frame, text="Actualizar Tabla")
        btn_mostrar.grid(row=5, column=3)

    def frame2(self):
        global tabla

        # Crea un cuadro para la tabla
        frame = tk.Frame(self)
        frame.grid(row=2, column=0)

        # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
        tabla = ttk.Treeview(frame, height=10, columns=("#0", "#1", "#2", "#3", "#4", "#5"))
        tabla.place(x=90, y=180)
        tabla.grid(row=1, column=0)

        # Barra de desplazamiento
        barraDesplazamiento = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview())
        tabla.configure(yscrollcommand=barraDesplazamiento)
        barraDesplazamiento.grid(row=1, column=1, sticky="ns")

        # Tamaño de las columnas
        tabla.column("#0", width=40)
        tabla.column("#1", width=200)
        tabla.column("#2", width=100)
        tabla.column("#3", width=200)
        tabla.column("#4", width=200)
        tabla.column("#5", width=200)

        # Titulos
        tabla.heading("#0", text="Id")
        tabla.heading("#1", text="Titulo")
        tabla.heading("#2", text="Duración")
        tabla.heading("#3", text="Dependencias")
        tabla.heading("#4", text="Fecha Inicio Temprano")
        tabla.heading("#5", text="Fecha Inicio Tardio")

        self.colocarActividadesEnTabla(tabla)


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

    def colocarActividadesEnTabla(self, tabla):
        actividades = leerActividades()

        #Llena la tabla de actividades
        for actividad in actividades:
            # Converite sus dependencias en formato string para poder visualizar
            stringDependencias = convertirArregloDependenciasAString(actividad.dependencias)
            tabla.insert('', tk.END,
            values=(actividad.identificador,actividad.nombre, actividad.duracion,
                    stringDependencias, actividad.fechaInicioTemprano,
                    actividad.fechaInicioTardio))

    # Actualiza la tabla
    def actualizar(self):
        pass

    # Elimina una actividad de la tabla
    def eliminar(self, tabla):
        curItem = tabla.focus()
        actividadEliminada = tabla.item(curItem)['values']
        print(actividadEliminada[0])
        eliminarActividad(actividadEliminada[0])
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
