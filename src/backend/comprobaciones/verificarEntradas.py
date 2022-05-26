from tkinter import messagebox
from datetime import datetime

# Cuando carga o edita una actividad debe validar aca
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

def validarInforme(opcion):

    if opcion == "":
        messagebox.showwarning("Error", "Elija una opción para continuar")
        return False
    return True



