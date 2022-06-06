from datetime import datetime
from tkinter import messagebox


# Cuando carga o edita una actividad debe validar aca
def validar_Actividad(nombre, duracion):
    valido = True
    # Valida el nombre
    if not 1 < len(nombre) <= 20:
        messagebox.showwarning("Mensaje", "Nombre de Actividad invalido")
        valido = False
    # Valida la duracion
    if not duracion.isdigit():
        messagebox.showwarning("Mensaje", "La duración ingresada no es válida")
        valido = False
    elif not 0 < int(duracion) <= 99:
        messagebox.showwarning("Mensaje", "La duración no puede superar 99 días")
        valido = False

    return valido


def validarInforme(opcion):
    if opcion == "":
        messagebox.showwarning("Error", "Elija una opción para continuar")
        return False
    return True


def validar_Proyecto(nombre, descripcion, fechaI):
    valido = True
    if not 1 < len(nombre) <= 30:
        messagebox.showwarning("Mensaje", "Nombre de Actividad invalido")
        valido = False
    if not 1 < len(descripcion) <= 60:
        messagebox.showwarning("Mensaje", "Descripcion invalido")
        valido = False
    if not validarFecha(fechaI):
        valido = False
    return valido

def validarFecha(fecha):
    try:
        bool(datetime.strptime(str(fecha), "%Y-%m-%d").date())
    except ValueError:
        messagebox.showwarning("Mensaje", "Fecha invalida")
        return False
    return True