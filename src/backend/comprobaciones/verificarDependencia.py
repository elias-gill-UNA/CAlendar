from datetime import date
def separarFecha(fecha):
    fecha=fecha.split("/")
    for i in range(len(fecha)):
        fecha[i] = int(fecha[i])
    for i in range(len(fecha)):
        fecha[i] = int(fecha[i])
    return fecha

def verificarDependencia(fechaInicial,fechaFinal,duracion):#fechaInicial: es la actividad que no depende,
    # fechaFinal: es la actividad  que depende de la actividadInicial, duracion: duracion de la actividadInicial
    fechaInicial=separarFecha(fechaInicial)
    fechaFinal=separarFecha(fechaFinal)

    duracionInicial=date(fechaInicial[2],fechaInicial[1],fechaInicial[0])
    duracionFinal=date(fechaFinal[2],fechaFinal[1],fechaFinal[0])

    delta=duracionFinal-duracionInicial
    if delta.days>=duracion:
        return True
    else:
        return False