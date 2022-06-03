from datetime import datetime
from tkinter import messagebox


# Cuando carga o edita una actividad debe validar aca
def validar_Actividad(nombre, duracion, identificador, fechaInicio):
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


def validar_Proyecto(DL, nombre, descripcion, fechaI, holgura):
    valido = True
    if not DL.isdigit():
        messagebox.showwarning("Mensaje", "Cantidad de dias laborales invalidos")
        valido = False
    elif  int(DL)<=0 or int(DL)>7:
        messagebox.showwarning("Mensaje", "Cantidad de dias laborales invalidos")
        valido = False
    if not 1 < len(nombre) <= 30:
        messagebox.showwarning("Mensaje", "Nombre de Actividad invalido")
        valido = False
    if not 1 < len(descripcion) <= 60:
        messagebox.showwarning("Mensaje", "Descripcion invalido")
        valido = False
    if not holgura.isdigit():
        messagebox.showwarning("Mensaje", "Holgura invalida")
        valido = False
    '''elif not 0 < int(holgura) > 7:
        messagebox.showwarning("Mensaje", "Cantidad de dias laborales invalidos")
        valido = False'''
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