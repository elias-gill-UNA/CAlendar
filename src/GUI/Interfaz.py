import tkinter as tk
from tkinter import *
from tkinter import ttk

from matplotlib.pyplot import text


from tkcalendar import *
import funcionesSobreObjetos.proyectoFunciones as prFunctions
#import funcionesSobreObjetos.actividadFunciones as actFunctions
from funcionesSobreObjetos.actividadFunciones import *
from clases.proyecto import *
from backend.dataBase.proyectManager import *
import backend.comprobaciones.verificarEntradas as vrfInput
# 0 indica que viene de la ventana de Proyectos
# 1 indica que viene de la ventana de Actividades
def limpiar_Pantalla(framePrincipal, num_Ventana):
    framePrincipal.destroy()
    if num_Ventana == 0:
        ventana_Actividad(root)
    else:
        ventana_Proyecto(root)

def guardar_Proyecto(framePrincipal, DL, nombre, descripcion, fechaI, holgura):
    # Validar los datos
    if vrfInput.validar_Proyecto(DL, nombre, descripcion, fechaI, holgura):
        # Se crea el proyecto
        Pr=Proyecto(nombre,descripcion,fechaI,DL,holgura)
        print("Se creo el proyecto",crearProyecto(Pr))
        h = getProyectListsWithInfo()
        print(h)
        #print("id",Pr.identificador,"des:",Pr.descripcion,"nom:",Pr.nombre)


        #PR2=prFunctions.abrirProyecto(Pr.identificador)
        #print(PR2)
        #info=getProyectInfo(Pr.identificador,None)
        #print("Info",info)


        limpiar_Pantalla(framePrincipal, 0)


def guardar_Actividad(framePrincipal, nombre, duracion, dependencias, fechaInicio, fechaFinal):
    # Se crea la actividad

    # Falta validar los datos antes
    #actFunctions.crearActividad(nombre, duracion, dependencias, fechaInicio, fechaFinal)
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
        lbl_titulo = tk.Label(frame1, text="\tCREAR PROYECTOS", font=("Courier", 20), anchor="center")
        lbl_titulo.grid(row=0, column=0)

        lbl_nombre = tk.Label(frame1, text="Nombre del Proyecto:", font=("Times New Roman", 12))
        lbl_nombre.grid(row=1, column=0, sticky="w")
        nombre = tk.Entry(frame1, width=20)
        nombre.grid(row=1, column=1)

        lbl_Dl = tk.Label(frame1, text="Dias laborales:", font=("Times New Roman", 12))
        lbl_Dl.grid(row=2, column=0, sticky="w")
        DL = tk.Entry(frame1, width=20)
        DL.grid(row=2, column=1)

        fechaInicio = tk.StringVar()  # Guarda la fecha ingresada
        lbl_fechaInicio = tk.Label(frame1, text="Fecha de Inicio dd/mm/aa:", font=("Times New Roman", 12))
        lbl_fechaInicio.grid(row=3, column=0, sticky="w")
        fechaI = DateEntry(frame1, selectmode="day", textvariable=fechaInicio, width=17)
        fechaI.grid(row=3, column=1)

        lbl_descripcion = tk.Label(frame1, text="Descripción:", font=("Times New Roman", 12))
        lbl_descripcion.grid(row=5, column=0, sticky="w")
        # Crea una caja de texto para la descripción
        descrip = Text(frame1, width=20, height=5)
        descrip.grid(row=5, column=1)

        lbl_holgura = tk.Label(frame1, text="Holgura:", font=("Times New Roman", 12))
        lbl_holgura.grid(row=4, column=0, sticky="w")
        # Crea una caja de texto para el ID
        holgura = tk.Entry(frame1, width=20)
        holgura.grid(row=4,column=1)

        # Crea un espacio entre frame y frame2
        espacio = tk.Label(frame1, text="")
        espacio.grid(row=5, column=0)

        frame2 = tk.Frame(self)
        frame2.grid(row=2, column=0)

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

        frame3 = tk.Frame(self)
        frame3.grid(row=3, column=0)
        # Crea un espacio entre los botones
        espacio = tk.Label(frame3, text="")
        espacio.grid(row=0, column=1)
        espacio = tk.Label(frame3, text="\t\t\t\t")
        espacio.grid(row=0, column=4)

        # Botones
        btn_salir = tk.Button(frame3, text="Salir", command=quit)
        btn_salir.grid(row=0, column=2)

        btn_siguiente = tk.Button(frame3, text="Siguiente",
                                  command=lambda: guardar_Proyecto(self, DL.get(), nombre.get(),
                                                                   descrip.get(1.0, "end"),
                                                                   fechaI.get_date(),holgura.get()))
        btn_siguiente.grid(row=0, column=5, sticky="ns")


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
        lbl_titulo = tk.Label(self, text="CREAR O EDITAR ACTIVIDADES", font=("Courier", 20))
        lbl_titulo.grid(row=0, column=0)

        self.__frame1__(f1)
        self.__frame2__(f2)
        self.__frame3__(f3)

    def __frame1__(self, frame):
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
                              command=lambda: guardar_Actividad(self, self.nombre.get(),
                                                                self.duracion.get(), self.dependencias.get(),
                                                                self.fechaInicio.get(), self.fechaFinal.get()))
        btn_crear.grid(row=5, column=0)

        btn_editar = tk.Button(frame, text="Editar Actividad")
        btn_editar.grid(row=5, column=1)

        btn_eliminar = tk.Button(frame, text="Eliminar Actividad", command=lambda: self.eliminar(tabla))
        btn_eliminar.grid(row=5, column=2)

        btn_mostrar = tk.Button(frame, text="Actualizar Tabla")
        btn_mostrar.grid(row=5, column=3)

    def __frame2__(self, frame):
        global tabla

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

        self.colocarActividadesEnTabla(tabla)

    def __frame3__(self, frame):
        # Lista de opciones
        self.opcion = tk.StringVar()
        combo = ttk.Combobox(frame, values=["Diagrama de Gantt", "Mapa de Dependencias"], textvariable=self.opcion)
        combo.place(x=50, y=50)
        combo.grid(row=0, column=1)

        # Etiquetas
        lbl_opciones = tk.Label(frame, text="Opciones:")
        lbl_opciones.grid(row=0, column=0)

        # Botones
        # Tiene que ir a la funcion informe que esta en comprobaciones
        btn_siguiente = tk.Button(frame, text="Informe", command=self.__informe__)
        btn_siguiente.grid(row=0, column=2)

        # Crea un espacio entre los botones
        espacio = tk.Label(frame, text="\t\t\t\t")
        espacio.grid(row=0, column=3)

        btn_salir = tk.Button(frame, text="Salir", command=quit)
        btn_salir.grid(row=0, column=4)

        btn_newPro = tk.Button(frame, text="Nuevo Proyecto", command=lambda: limpiar_Pantalla(self, 1))
        btn_newPro.grid(row=0, column=0)

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
        '''actividades = leerActividades()
        # Llena la tabla de actividades
        for actividad in actividades:
            # Converite sus dependencias en formato string para poder visualizar
            stringDependencias = convertirArregloDependenciasAString(actividad.dependencias)
            tabla.insert('', END,
                         values=(actividad.identificador, actividad.nombre, actividad.duracion,
                                 stringDependencias, actividad.fechaInicioTemprano,
                                 actividad.fechaInicioTardio))'''
        pass

    # Actualiza la tabla
    def actualizar(self):
        pass

    # Elimina una actividad de la tabla
    def eliminar(self, tabla):
        curItem = tabla.focus()
        actividadEliminada = tabla.item(curItem)['values']
        print(actividadEliminada[0])
        eliminarActividad(actividadEliminada[0])

    # Editar alguna actividad
    def editar(self):
        pass


root = tk.Tk()
ventana_Proyecto(root)
root.mainloop()