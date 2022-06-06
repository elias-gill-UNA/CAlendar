from backend.dataBase.dbFunctions import db_feriados, db_proyects
from clases.feriados import Feriado
from datetime import date

# retorna si es dia laboral, feriado o fin de semana 
def diaLaboral(feriados, año, mes, dia): 
    for feriado in feriados:
        if(dia == feriado.dia and mes == feriado.mes):
            return False
    return __fin_semana(año,mes,dia)

# determina si un dia cae fin de semana
def __fin_semana(año, mes, dia): 
    d = zeller(año, mes, dia)
    if d == 6 or d == 0:
        return False
    else:
        return True

# determina que dia cae una fecha especifica
def zeller(ano,mes,dia): 
    d = date(dia, mes, ano)
    a = d.weekday()
    if (a == 5 or a == 6):
        return False
    return True

# cargar los feriados nacionales
def cargarFeriadosNacionales(id):
    conexion = db_proyects.abrirProyecto(id)
    feriados = [ 
        [1,1,"Año nuevo"],
        [1,3,"Dia de los heroes"],
        [1,5,"Dia del trabajador"],
        [14,5,"Dia de la Patria"],
        [15,5,"Dia de la Madre"],
        [12,6,"Paz del Chaco"],
        [15,8,"Fundacion de Asuncion"],
        [29,9,"Batalla de Boqueron"],
        [8,12,"Dia de la Virgen de Caacupe"],
        [25,12,"Navidad"] 
    ]
    for i in feriados: # cargar feriados en la db
        aux = Feriado(i[0], i[1], i[2])
        db_feriados.nuevoFeriado(conexion, aux)

    db_proyects.cerrarProyecto(conexion)
    return True


##############################################################
#  funciones sobre los dias feriados en conjunto con la DB  #
##############################################################

def anadirFeriado(conexion, dia, mes, descripcion):
    feriado = Feriado(dia, mes, descripcion)
    db_feriados.nuevoFeriado(conexion, feriado)
    return getListaFeriados(conexion)

def leerFeriado(conexion, id):
    info = db_feriados.getFeriado(conexion, id)
    feriado = Feriado(info[1], info[2], info[3])
    feriado.identificador = info[0]
    return feriado

def getListaFeriados(conexion):
    aux = db_feriados.getListaFeriados(conexion)
    feriados = []
    # cargar en objetos propios
    for i in aux: 
        feriado = Feriado(i[1], i[2], i[3]) 
        feriado.identificador = i[0]
        feriados.append(feriado)
    return feriados

# elimina el feriado si es que existe
def eliminarFeriado(conexion, id):
    if leerFeriado(conexion, id):
        db_feriados.eliminarFeriado(conexion, id)
        return True
    raise ValueError("El feriado no existe")





