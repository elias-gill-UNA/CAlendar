import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import backend.comprobaciones.verificarEntradas as verificarInput
import backend.dataBase.activitiesManager as activitiesManager
import backend.dataBase.proyectManager as proyectManager
import funcionesSobreObjetos.actividadFunciones as actividadFunciones
import funcionesSobreObjetos.proyectoFunciones as funcProyectos
from clases.actividades import Actividad
from clases.proyecto import Proyecto
from tkcalendar import *

from diagrama_de_gantt import AbrirDiagrama
from informes.camino_critico import funcionFinalYSuperpoderosa
from clases.clases_cam_critico import ObjetoCritico
conexion = None  # id del proyecto cuando se selecciona
objProyecto = 0  # objeto proyecto cuando se selecciona
listaActividades = 0  # lista de actividades del proyecto cuando se selecciona


def centrar_Ventana(root, num_Ventana):
    if num_Ventana == 0:
        ancho_ventana = 850
        alto_ventana = 550

    elif num_Ventana == 1:
        ancho_ventana = 1050
        alto_ventana = 500
    else:
        ancho_ventana = 400
        alto_ventana = 150
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    # La ventana no puede cambiar de tamaño
    root.resizable(False, False)


# 0 indica que viene de la ventana de Proyectos
# 1 indica que viene de la ventana de Actividades

def limpiar_Pantalla(framePrincipal, num_Ventana):
    global conexion
    if (num_Ventana != 2):
        framePrincipal.destroy()

    if num_Ventana == 0:
        ventana_Actividad(root)
    elif num_Ventana == 1:
        ventana_Proyecto(root)
    elif num_Ventana == 2:
        AbrirDiagrama(conexion)


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


def guardar_Actividad(framePrincipal, nombre, duracion, dependencia, tabla):
    if verificarInput.validar_Actividad(nombre, duracion):
        actividad = Actividad(nombre, duracion, dependencia)
        # Crea la actividad
        AC = actividadFunciones.crearActividad(conexion, actividad.nombre, actividad.duracion, actividad.dependencias)
        # Limpia la tabla
        for item in tabla.get_children():
            tabla.delete(item)
        # Vuelve a cargar los datos en la tabla agregandole la actividad creada
        cargar_Tabla_Actividad(tabla)


# Carga los proyectos en la tabla
def cargar_Tabla_Proyecto(tabla):
    proyectos = proyectManager.getProyectListsWithInfo()
    for i in proyectos:
        tabla.insert('', tk.END, text=i.identificador, values=(i.nombre, i.fechaInicio, i.descripcion))


# Carga las actividades en el proyecto
def cargar_Tabla_Actividad(tabla):
    global conexion
    if conexion != None:
        actividades = actividadFunciones.leerActividades(conexion)
        for i in actividades:
            tabla.insert("", tk.END, text=i.identificador, values=(i.nombre, i.duracion, i.dependencias))




# Cuando da click a el boton Abrir viene aca
def seleccionar_Proyecto(tabla, framePrincipal):
    try:
        global conexion
        global listaActividades
        global objProyecto
        id = tabla.item(tabla.selection())['text']
        # Si este tira error es porque no selecciono nada
        x = tabla.selection()[0]
        # abrir el proyecto recien creado y dar valor a las globales
        proyecto = funcProyectos.abrirProyecto(id)
        conexion = proyecto[0]
        objProyecto = proyecto[1]
        listaActividades = proyecto[2]
        limpiar_Pantalla(framePrincipal, 0)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione un Proyecto para abrir!")


def mostrar_Actividades_Criticas(objcritico):
    ventana= tk.Toplevel()
    ventana.title("Actividades Criticas")
    print(objcritico.cantidadCritico)



def iniciar_Camino_Critico():
    global conexion
    global objProyecto
    listaautoref=activitiesManager.getListaActividadesAutoreferenciada(conexion)
    listaFinal=[]
    objcritico= ObjetoCritico()
    funcionFinalYSuperpoderosa(conexion,listaautoref,listaFinal,objcritico,objProyecto)
    mostrar_Actividades_Criticas(objcritico)

class ventana_Proyecto(tk.Frame):
    # Crea la ventana principal
    def __init__(self, root):
        super().__init__(root)  # indica la ventana contenedora del frame principal
        self.root = root
        self.root.title("PROYECTOS")
        self.pack()
        self.__frame_Principal__()
        centrar_Ventana(root, 0)

    def __frame_Principal__(self):
        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=0)
        # Etiquetas
        lbl_titulo = tk.Label(frame1, text="\tCREAR PROYECTOS", font=("Courier", 20), anchor="center").grid(row=0,
                                                                                                            column=0)

        lbl_nombre = tk.Label(frame1, text="Nombre del Proyecto:", font=("Times New Roman", 12)).grid(row=1, column=0,
                                                                                                      sticky="w")
        contenedor_name = StringVar()
        nombre = tk.Entry(frame1, width=20, textvariable=contenedor_name)
        nombre.grid(row=1, column=1)

        fechaInicio = tk.StringVar()
        lbl_fechaInicio = tk.Label(frame1, text="Fecha de Inicio dd/mm/aa:", font=("Times New Roman", 12)).grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky="w")
        fechaI = DateEntry(frame1, selectmode="day", textvariable=fechaInicio, width=17)
        fechaI.grid(row=2, column=1)

        lbl_descripcion = tk.Label(frame1, text="Descripción:", font=("Times New Roman", 12)).grid(row=3, column=0,
                                                                                                   sticky="w")
        # Crea una caja de texto para la descripción
        descrip = Text(frame1, width=20, height=5)
        descrip.grid(row=3, column=1)

        # Crea un espacio entre frame y frame2
        lbl_lista = tk.Label(frame1, text="\n\t\tLISTA DE PROYECTOS CREADOS", anchor=CENTER,
                             font=("Courier", 12)).grid(row=4, column=0)

        frame2 = tk.Frame(self)
        frame2.grid(row=2, column=0)

        # Crea la tabla donde se vera la lista de Proyectos
        self.tabla = ttk.Treeview(frame2, height=10, columns=("#0", "#1", "#2"))
        self.tabla.place(x=90, y=180)
        self.tabla.grid(row=0, column=0)

        # Barra de desplazamiento
        barraDesplazamiento = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barraDesplazamiento.set)
        barraDesplazamiento.grid(row=0, column=2, sticky="nsew")

        # Tamaño de las columnas
        self.tabla.column("#0", width=40, anchor=CENTER)
        self.tabla.column("#1", width=200, anchor=SW)
        self.tabla.column("#2", width=200, anchor=CENTER)
        self.tabla.column("#3", width=200, anchor=SW)

        # Titulos
        self.tabla.heading("#0", text="Id", anchor=CENTER)
        self.tabla.heading("#1", text="Nombre del Proyecto", anchor=CENTER)
        self.tabla.heading("#2", text="Fecha Inicio Previsto", anchor=CENTER)
        self.tabla.heading("#3", text="Descripcion", anchor=CENTER)

        frame3 = tk.Frame(self)
        frame3.grid(row=3, column=0)

        # Crea espacios entre los botones
        tk.Label(frame3, text="\t\t").grid(row=0, column=1)
        tk.Label(frame3, text="\t\t").grid(row=0, column=3)
        tk.Label(frame3, text="\t\t").grid(row=0, column=5)

        # Botones
        btn_salir = tk.Button(frame3, text="Salir", command=quit).grid(row=0, column=0)

        btn_guardar_proyecto = tk.Button(frame3, text="Guardar proyecto",
                                         command=lambda: guardar_Proyecto(self.tabla, nombre.get(),
                                                                          descrip.get(1.0, "end"),
                                                                          fechaI.get_date())).grid(row=0, column=2,
                                                                                                   sticky="ns")

        btn_abrir = tk.Button(frame3, text="Abrir", command=lambda: seleccionar_Proyecto(self.tabla, self)).grid(row=0,
                                                                                                                 column=4,
                                                                                                                 sticky="ns")

        btn_elimi = tk.Button(frame3, text="Eliminar", command=lambda: eliminar_item(self.tabla)).grid(row=0, column=7)

        cargar_Tabla_Proyecto(self.tabla)

        # Elimina el proyecto seleccionado de la tabla y de la base de datos
        def eliminar_item(tabla):
            try:
                x = tabla.selection()[0]
                id = tabla.item(tabla.selection())['text']
                tabla.delete(x)
                proyectManager.eliminarProyecto(id)
            except IndexError:
                messagebox.showwarning("Mensaje", "Seleccione un Proyecto para eliminar!")


class ventana_Actividad(tk.Frame):
    def __init__(self, root):
        super().__init__(root)  # indica la ventana contenedora del frame principal
        self.root = root
        self.root.title("ACTIVIDADES")
        self.pack()  # ubica los elementos
        # Crea los frames a usar
        f1 = tk.Frame(self)
        f1.grid(row=1, column=0)
        f2 = tk.Frame(self)
        f2.grid(row=2, column=0)
        f3 = tk.Frame(self)
        f3.grid(row=3, column=0)

        # Titulo de la ventana
        lbl_titulo = tk.Label(self, text="CREAR O EDITAR ACTIVIDADES", font=("Courier", 20)).grid(row=0, column=0)

        self.__frame1__(f1)
        self.__frame2__(f2)
        self.__frame3__(f3)
        centrar_Ventana(root, 1)

    def __frame1__(self, frame):
        # Etiquetas
        lbl_nombre = tk.Label(frame, text="Nombre de la actividad:", font=("Times New Roman", 12)).grid(row=0, column=0,

                                                                                                        sticky="w")
        self.nombre = tk.Entry(frame, width=20)
        self.nombre.grid(row=0, column=1)

        lbl_dependencias = tk.Label(frame, text="Dependencias:", font=("Times New Roman", 12)).grid(row=0, column=2,
                                                                                                    sticky="w")
        self.dependencias = tk.Entry(frame, width=20)
        self.dependencias.grid(row=0, column=3)

        lbl_duracion = tk.Label(frame, text="Duración:", font=("Times New Roman", 12)).grid(row=0, column=4, sticky="w")
        self.duracion = tk.Entry(frame, width=20)
        self.duracion.grid(row=0, column=5)

        # Crea un espacio entre frame1 y frame2
        separador = tk.Label(frame, text="").grid(row=2, column=0)
        # Crea espacios entre los botones
        tk.Label(frame, text="\t\t").grid(row=5, column=1)
        tk.Label(frame, text="\t\t").grid(row=5, column=2)
        tk.Label(frame, text="\t\t").grid(row=5, column=3)

        # Botones
        btn_crear = tk.Button(frame, text="Crear Actividad",
                              command=lambda: guardar_Actividad(self, self.nombre.get(),
                                                                self.duracion.get(), self.dependencias.get(),
                                                                self.tabla)).grid(
            row=5, column=0)

        btn_eliminar = tk.Button(frame, text="Eliminar Actividad",
                                 command=lambda: self.eliminar_Actividad(self.tabla)).grid(row=5,
                                                                                           column=4)

    def __frame2__(self, frame):

        lbl_lista = tk.Label(frame, text="\nLISTA DE ACTIVIDADES DEL PROYECTO", font=("Courier", 12)).grid(
            row=0,
            column=0)
        # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
        self.tabla = ttk.Treeview(frame, height=10, columns=("#0", "#1", "2"))
        self.tabla.place(x=90, y=180)
        self.tabla.grid(row=1, column=0)

        # Barra de desplazamiento
        barraDesplazamiento = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barraDesplazamiento.set)
        barraDesplazamiento.grid(row=1, column=1, sticky="ns")

        # Tamaño de las columnas
        self.tabla.column("#0", width=40, anchor=CENTER)
        self.tabla.column("#1", width=200, anchor=CENTER)
        self.tabla.column("#2", width=100, anchor=CENTER)
        self.tabla.column("#3", width=200, anchor=CENTER)

        # Titulos
        self.tabla.heading("#0", text="Id")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Duración")
        self.tabla.heading("#3", text="Dependencia")

        cargar_Tabla_Actividad(self.tabla)

        cargar_Tabla_Actividad(self.tabla)
        # self.colocarActividadesEnTabla(tabla)
        def editar_Actividad(event):
            id = self.tabla.item(self.tabla.selection())['text']

            editar = Toplevel()
            centrar_Ventana(editar, 3)
            lbl_nombre = tk.Label(editar, text="Nombre de la actividad:", font=("Times New Roman", 12)).grid(row=0,
                                                                                                             column=0,

                                                                                                             sticky="w")
            nombre = tk.Entry(editar, width=20)
            nombre.grid(row=0, column=1)

            lbl_dependencias = tk.Label(editar, text="Dependencias:", font=("Times New Roman", 12)).grid(row=1,
                                                                                                         column=0,
                                                                                                         sticky="w")
            dependencias = tk.Entry(editar, width=20)
            dependencias.grid(row=1, column=1)

            lbl_duracion = tk.Label(editar, text="Duración:", font=("Times New Roman", 12)).grid(row=2, column=0,
                                                                                                 sticky="w")
            duracion = tk.Entry(editar, width=20)
            duracion.grid(row=2, column=1)

            btn_cancelar = tk.Button(editar, text="Cancelar", command=editar.destroy).grid(row=3, column=0)
            btn_guardar = tk.Button(editar, text="Guadar Cambios", command=lambda: guardar_Cambios(nombre.get(),
                                                                                                   duracion.get(),
                                                                                                   dependencias.get(),
                                                                                                   self.tabla, id,
                                                                                                   editar)).grid(
                row=3, column=1)

            editar.mainloop()

        def guardar_Cambios(nombre, duracion, dependencia, tabla, id, editar):
            global conexion
            if verificarInput.validar_Actividad(nombre, duracion):
                actividad = Actividad(nombre, duracion, dependencia)
                activitiesManager.modificarActividad(conexion, id, actividad)
                # Limpia la tabla
                for item in tabla.get_children():
                    tabla.delete(item)
                # Vuelve a cargar los datos en la tabla agregandole la actividad creada
                editar.destroy()
                cargar_Tabla_Actividad(tabla)

        self.tabla.bind("<Double-1>", editar_Actividad)

    def __frame3__(self, frame):
        # Crea espacios entre los botones
        tk.Label(frame, text="\t").grid(row=0, column=1)
        tk.Label(frame, text="\t").grid(row=0, column=3)
        tk.Label(frame, text="\t").grid(row=0, column=5)

        # Botones
        btn_newPro = tk.Button(frame, text="Nuevo Proyecto", command=lambda: limpiar_Pantalla(self, 1)).grid(row=0,
                                                                                                             column=0)

        btn_salir = tk.Button(frame, text="Salir", command=quit).grid(row=0, column=6)

        btn_gantt = tk.Button(frame, text="Diagram de Gantt", command=lambda: limpiar_Pantalla(self, 2)).grid(row=0,
                                                                                                              column=2)

        btn_Acti_critic = tk.Button(frame, text="Actividades Criticas", command=iniciar_Camino_Critico).grid(row=0,
                                                                                                             column=4)

    # Elimina el proyecto seleccionado de la tabla y de la base de datos
    def eliminar_Actividad(self, tabla):
        try:
            global conexion
            x = tabla.selection()[0]
            id = tabla.item(tabla.selection())['text']
            tabla.delete(x)
            actividadFunciones.eliminarActividad(conexion, id)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una Actividad para eliminar!")


root = tk.Tk()
ventana_Proyecto(root)
root.mainloop()
