#NOTE  Poner los feriados en un objeto, la funcion itera sobre ellos
feriados = {
    "1": [1, 1, "Primero de enero"],
    "2": ["dia", "mes", "fiesta"],
    "3": ["dia", "mes", "fiesta"],
    # ..... 
}

def zeller(año,mes,dia):
    a=int((14-mes)/12)
    y=año-a
    m=mes+ 12*a - 2
    d=int((dia+y+int(y/4)-int(y/100)+int(y/400)+int((31*m)/12)) % 7)
    return d


# NOTE  Funcio que retorne {"feriado": True/False, "fiesta": "fiesta/fin de semana/trabaja"}
def feriado(año,mes,dia): 
    for key in feriados.keys(): # si es feriado
        if(dia, mes == key[0], key[1]):
            return {"res": True, "fiesta": "Primero de enero"}
    return finSemana(año,mes,dia) # si es que no retorna si es fin de semana o no

# muchas funciones al pedo
def finSemana(año,mes,fecha):
    d = zeller(año, mes, fecha)
    if d == 6 or d==0:
        return True
    else:
        return False


# NOTE  ESTE MODULO SOLO DEBE RETORNAR SI ES DIA LABORAL O NO


