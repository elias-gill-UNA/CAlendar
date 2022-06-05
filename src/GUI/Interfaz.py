import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import backend.comprobaciones.verificarEntradas as vp
import backend.comprobaciones.verificarEntradas as va
from backend.dataBase.activitiesManager import getInfoActividad
from backend.dataBase.activitiesManager import *

from backend.dataBase.proyectManager import *
from funcionesSobreObjetos.actividadFunciones import *
from tkcalendar import *

conexion = 0  # id del proyecto cuando se selecciona
descripcion = 0  # descripcion del proyecto cuando se selecciona
listaActividades = 0  # lista de actividades del proyecto cuando se selecciona


# 0 indica que viene de la ventana de Proyectos
# 1 indica que viene de la ventana de Actividades

def limpiar_Pantalla(framePrincipal, num_Ventana):
    framePrincipal.destroy()
    if num_Ventana == 0:
        ventana_Actividad(root)
    else:
        ventana_Proyecto(root)


def guardar_Proyecto(tabla, nombre, descrip, fechaI):
    # global conexion
    # global listaActividades
    # global descripcion
    # Valida los datos antes de crear el Proyecto
    if vp.validar_Proyecto(nombre, descrip, fechaI):
        Pr = Proyecto(nombre, descrip, fechaI)
        # Mejor si crear proyecto no retorna nada (Preguntar a Elias)
        # Crea el proyecto
        id = proyectManager.crearProyecto(Pr)
        # Retorna todos los proyectos guardados
        # Elimina los datos de la tabla
        for item in tabla.get_children():
            tabla.delete(item)
        # Vuelve a cargar los datos en la tabla agregandole el nuevo proyecto creado
        cargar_Tabla(tabla)

        # abrir proyecto
        # conexion = abrirProyecto(id)
        # conexion = proyecto[0]
        # descripcion = proyecto[1]
        # listaActividades = proyecto[2]

def cargar_tabla_Actividad(tabla,conexion):
    activities=activitiesManager.getListaActividades(conexion)
    for i in activities:
        tabla.insert('',tk.END,text=idem,values=(i.nombre,i.fechaInicio,i.descripcion))
def cargar_Tabla(tabla):
    proyectos = proyectManager.getProyectListsWithInfo()
    for i in proyectos:
        tabla.insert('', tk.END, text=i.identificador, values=(i.nombre, i.fechaInicio, i.descripcion))


# Cuando da click a el boton Abrir viene aca
def seleccionar_id(tabla, framePrincipal):
    global conexion
    global listaActividades
    global descripcion
    id = tabla.item(tabla.selection())['text']
    # abre el proyecto seleccionado o el recien creado?
    # abrir el proyecto recien creado y dar valor a las globales
    conexion = abrirProyecto(id)
    # conexion = proyecto[0]
    # descripcion = proyecto[1]
    # listaActividades = proyecto[2]
    limpiar_Pantalla(framePrincipal, 0)


def guardar_Actividad(framePrincipal,tabla, nombre, duracion, dependencias, fechaInicio, fechaFinal):
    # Se crea la actividad
    global idem
    idem=-1
    idem=idem+1
    #seleccionar_id(tabla,framePrincipal)
    #getInfoActividad(id,conexion)
    #id = tabla.item(tabla.selection())['text']
    #antes se necesita el id
    
    if va.validar_Actividad(nombre,duracion,idem,fechaInicio):
        Ac=Actividad(idem,nombre,duracion,dependencias,fechaFinal)
        #conexion=abrirconexion(id)
        actis=leerActividades(conexion)

        for item in tabla.get_children():
            tabla.delete(item)
        # Vuelve a cargar los datos en la tabla agregandole el nuevo proyecto creado
        cargar_tabla_Actividad(tabla,conexion)
    


    # Falta validar los datos antes
    # actFunctions.crearActividad(nombre, duracion, dependencias, fechaInicio, fechaFinal)
    # if vp.validar_Proyecto()

    limpiar_Pantalla(framePrincipal, 1)


class ventana_Proyecto(tk.Frame):
    # Crea la ventana principal
    def __init__(self, root):
        super().__init__(root)  # indica la ventana contenedora del frame principal
        self.root = root
        self.root.title("PROYECTOS")
        self.root.geometry("850x500")
        self.pack()
        self.__frame_Principal__()

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
        espacio = tk.Label(frame1, text="\t\tLISTA DE PROYECTOS CREADOS", anchor=CENTER, font=("Times New Roman", 12))
        espacio.grid(row=4, column=0)

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

        btn_abrir = tk.Button(frame3, text="Abrir", command=lambda: seleccionar_id(self.tabla, self)).grid(row=0,
                                                                                                           column=4,
                                                                                                           sticky="ns")

        btn_elimi = tk.Button(frame3, text="Eliminar", command=lambda: eliminar_item(self.tabla)).grid(row=0, column=7)

        cargar_Tabla(self.tabla)

        # Elimina el proyecto seleccionado de la tabla y de la base de datos
        def eliminar_item(tabla):
            try:
                x = tabla.selection()[0]
                id = tabla.item(tabla.selection())['text']
                tabla.delete(x)
                eliminarProyecto(id)
            except IndexError:
                messagebox.showwarning("Mensaje", "Seleccione un Proyecto para eliminar!")


tabla = 0


class ventana_Actividad(tk.Frame):
    def __init__(self, root):
        super().__init__(root)  # indica la ventana contenedora del frame principal
        self.root = root
        self.root.title("ACTIVIDADES")
        self.root.geometry("1050x500")
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

        self.fechaInicio = tk.StringVar()
        lbl_fechaInicio = tk.Label(frame, text="Fecha de Inicio:", font=("Times New Roman", 12)).grid(row=1, column=0,
                                                                                                      sticky="w")
        fechaI = DateEntry(frame, selectmode="day", textvariable=self.fechaInicio, width=17)
        fechaI.grid(row=1, column=1)

        self.fechaFinal = tk.StringVar()
        lbl_fechaFinal = tk.Label(frame, text="Fecha de Final:", font=("Times New Roman", 12)).grid(row=1, column=2,
                                                                                                    sticky="w")
        fechaF = DateEntry(frame, selectmode="day", textvariable=self.fechaFinal, width=17)
        fechaF.grid(row=1, column=3)

        lbl_duracion = tk.Label(frame, text="Duración:", font=("Times New Roman", 12)).grid(row=1, column=4, sticky="w")
        self.duracion = tk.Entry(frame, width=20)
        self.duracion.grid(row=1, column=5)

        # Crea un espacio entre frame1 y frame2
        separador = tk.Label(frame, text="").grid(row=2, column=0)
        # Crea espacios entre los botones
        tk.Label(frame, text="\t\t").grid(row=5, column=1)
        tk.Label(frame, text="\t\t").grid(row=5, column=3)
        tk.Label(frame, text="\t\t").grid(row=5, column=5)

        # Botones
        btn_crear = tk.Button(frame, text="Crear Actividad",
                              command=lambda: guardar_Actividad(self,tabla, self.nombre.get(),
                                                                self.duracion.get(), self.dependencias.get(),
                                                                self.fechaInicio.get(), self.fechaFinal.get())).grid(
            row=5, column=0)

        btn_editar = tk.Button(frame, text="Editar Actividad").grid(row=5, column=2)

        btn_eliminar = tk.Button(frame, text="Eliminar Actividad", command=lambda: self.eliminar(tabla)).grid(row=5,
                                                                                                              column=4)

        btn_mostrar = tk.Button(frame, text="Actualizar Tabla").grid(row=5, column=6)

    def __frame2__(self, frame):
        global tabla
        separador = tk.Label(frame, text="LISTA DE ACTIVIDADES DEL PROYECTO", font=("Times New Roman", 12)).grid(row=0,
                                                                                                                column=0)
        # Crea la tabla     ID / Nombre / Fecha Inicio  /  Duracion
        tabla = ttk.Treeview(frame, height=10, columns=("#0", "#1", "#2", "#3", "#4"))
        tabla.place(x=90, y=180)
        tabla.grid(row=1, column=0)

        # Barra de desplazamiento
        barraDesplazamiento = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview())
        tabla.configure(yscrollcommand=barraDesplazamiento)
        barraDesplazamiento.grid(row=1, column=1, sticky="ns")

        # Tamaño de las columnas
        tabla.column("#0", width=40, anchor=CENTER)
        tabla.column("#1", width=200, anchor=CENTER)
        tabla.column("#2", width=100, anchor=CENTER)
        tabla.column("#3", width=200, anchor=CENTER)
        tabla.column("#4", width=200, anchor=CENTER)
        tabla.column("#5", width=200, anchor=CENTER)

        # Titulos
        tabla.heading("#0", text="Id")
        tabla.heading("#1", text="Titulo")
        tabla.heading("#2", text="Duración")
        tabla.heading("#3", text="Dependencias")
        tabla.heading("#4", text="Fecha Inicio Temprano")
        tabla.heading("#5", text="Fecha Inicio Tardio")

        # self.colocarActividadesEnTabla(tabla)

    def __frame3__(self, frame):
        # Lista de opciones
        self.opcion = tk.StringVar()
        combo = ttk.Combobox(frame, values=["Diagrama de Gantt", "Mapa de Dependencias"], textvariable=self.opcion)
        combo.place(x=50, y=50)
        combo.grid(row=0, column=3)

        # Etiquetas
        lbl_opciones = tk.Label(frame, text="Opciones:").grid(row=0, column=2)

        # Crea espacios entre los botones
        tk.Label(frame, text="\t").grid(row=0, column=1)
        tk.Label(frame, text="\t\t").grid(row=0, column=5)

        # Botones
        # Tiene que ir a la funcion informe que esta en comprobaciones
        btn_newPro = tk.Button(frame, text="Nuevo Proyecto", command=lambda: limpiar_Pantalla(self, 1)).grid(row=0,
                                                                                                             column=0)

        btn_informe = tk.Button(frame, text="Informe", command=self.__informe__).grid(row=0, column=4)

        btn_salir = tk.Button(frame, text="Salir", command=quit).grid(row=0, column=6)

    # Muestra el informe seleccionado
    def __informe__(self):
        opcion = self.opcion.get()
        # hay que enviar esta opcion a la funcion de validacion
        if True:
            if opcion == "Diagrama de Gantt":
                # Mostrar diagrama
                pass
            elif opcion == "Mapa de Dependencias":
                # Mostrar mapa
                pass
            else:
                # Mostrar camino crítico
                pass

    def colocarActividadesEnTabla(self, tabla):
        global listaActividades
        # Llena la tabla de actividades
        for actividad in listaActividades:  # ignorar error
            # Converite sus dependencias en formato string para poder visualizar
            stringDependencias = convertirArregloDependenciasAString(actividad.dependencias)
            tabla.insert('', END,
                         values=(actividad.identificador, actividad.nombre, actividad.duracion,
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
        eliminarActividad(conexion, actividadEliminada[0])

    # Editar alguna actividad
    def editar(self):
        pass


root = tk.Tk()
ventana_Proyecto(root)
root.mainloop()
