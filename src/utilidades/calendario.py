
def zeller(año,mes,dia): # determina que dia cae una fecha especifica
    a=int((14-mes)/12)
    y=año-a
    m=mes+ 12*a - 2
    d=int((dia+y+int(y/4)-int(y/100)+int(y/400)+int((31*m)/12)) % 7)
    return d


feriados = { # [dia, mes, descripcion] lista de feriados nacionales
    "1":[1,1,"Año nuevo"],
    "2":[1,3,"Dia de los heroes"],
    "3":[1,5,"Dia del trabajador"],
    "4":[14,5,"Dia de la Patria"],
    "5":[15,5,"Dia de la Madre"],
    "6":[12,6,"Paz del Chaco"],
    "7":[15,8,"Fundacion de Asuncion"],
    "8":[29,9,"Batalla de Boqueron"],
    "9":[8,12,"Dia de la Virgen de Caacupe"],
    "10":[25,12,"Navidad"]
    }


def fin_semana(año, mes, dia): # determina si un dia cae fin de semana
    d = zeller(año, mes, dia)
    if d == 6 or d == 0:
        return True, "Fin de semana"
    else:
        return False, "Dia normal"

def feriado(año,mes,dia): # retorna si es dia laboral, feriado o fin de semana 
    for key in feriados.keys(): # si es feriado
        if(dia==feriados[key][0] and mes == feriados[key][1]):
            return True, feriados[key][2]
    return fin_semana(año,mes,dia)

# formato de return (true/false, 'Descripcion del dia'), guardar como    var [2] = feriado(dia, ano, mes)
# true: feriado/finde  false: dia normal
