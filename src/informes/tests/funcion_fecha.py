from datetime import date, datetime, timedelta
from clases.feriados import Feriado

feriados = []
x = [ 
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

for i in x: # cargar feriados en la db
    aux = Feriado(i[0], i[1], i[2])
    feriados.append(aux)

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

def diaLaboral(año, mes, dia): 
    for feriado in feriados:
        if(dia == feriado.dia and mes == feriado.mes):
            return False
    return __fin_semana(año,mes,dia)

def suma(fecha, cantidad):
    final = fecha
    contador = cantidad-1
    while(contador > 0):
        # pasar las fechas a formate datetime
        final = final.split("/")
        if diaLaboral(int(final[0]), int(final[1]), int(final[2])):
            contador -= 1

        fecha2 = timedelta(1) 
        aux = date(int(final[2]), int(final[1]), int(final[0]))

        # transformar el resultado
        resultado = aux+fecha2
        final = str(resultado)
        final = final.split("-")
        final= final[2] +"/"+ final[1] + "/" + final[0]
        
    return final

fecha = "29/04/2022"
print(suma(fecha, 3))
