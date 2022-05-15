from tkinter import *

myMenu = 0

def Inicializar(mainRoot):
    root = mainRoot
    myMenu = Menu(root)
    root.config(menu=myMenu)

#Commandos Click
def NuevoArchivo():
    pass

def AbrirArchivo():
    pass

def GuardarArchivo():
    pass

#Crear un item de menu

archivosMenu = Menu(myMenu)
myMenu.add_cascade(label="Archivo", menu=archivosMenu)

archivosMenu.add_command(label="Nuevo Archivo", command=NuevoArchivo)
archivosMenu.add_separator()
archivosMenu.add_command(label="Abrir Archivo", command=AbrirArchivo)
archivosMenu.add_separator()
archivosMenu.add_command(label="Guardar Archivo", command=GuardarArchivo)