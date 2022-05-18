def calendario (año):
    for i in range(1,13) :
        print("mes:",nombre_mes(i))
        print("Dom Lun Mar Mie Jue Vie Sab ")
        z=zeller(año,i)
        print("z:",z)
        for k in range(0,z) :
            print("  ",end="")

        diasmes=calculardiasMes(año,i)

        for j in range(1, diasmes+1) :
            if (j%7==0 or j==30 or j==31):
                print(j)
            else:
                print(j,end="   ")

def calculardiasMes(año,mes):
    if (mes ==1 or mes== 3 or mes== 5 or mes ==7 or mes==8 or mes==10 or mes==12 ):
        return 31
    elif mes==2:
        if (añobisiesto(año)):

            return 29
        else:
            return 28

    elif (mes==4 or mes==6 or mes==9 or mes==11):
        return 30


def feriado(año,mes,dia):


    dia_correspondiente(zeller(año,mes,dia))

    if (dia==1 and mes==1):
        print("AÑO NUEVO")


    elif (dia == 1 and mes == 3):
        print("DIA DE LOS HEROES")


    elif (dia==1 and mes==5):
        print("DIA DEL TRABAJADOR")


    elif ((dia==14 and mes==5) or (dia==15 and mes==5)):
        print("DIA DE LA PATRIA")


    elif (dia==12 and mes==6):
        print("PAZ DEL CHACO")


    elif (dia==15 and mes==8):
        print("FUNDACION DE ASUNCION")


    elif (dia == 29 and mes == 9):
        print("BATALLA DE BOQUERON")


    elif (dia == 8 and mes == 12):
        print("DIA DE LA VIRGEN DE CAACUPE")


    elif (dia == 25 and mes == 12):
        print("NAVIDAD")



def fines_semana(año,mes,fecha):

    d=zeller(año,mes,fecha)

    if d==6:
        print("ES SABADO NO SE TRABAJA")
    else:
        print("ES DOMINGO NO SE TRABAJA")

"""
def dia_correspondiente(x):
    if(x==0):
        print("ES DOMINGO")
    elif x==1:
        print("ES LUNES")
    elif x==2:
        print("ES MARTES")
    elif x==3:
        print("ES MIERCOLES")
    elif x == 4:
        print("ES JUEVES")
    elif x == 5:
        print("ES VIERNES")
    elif x == 6:
        print("ES SABADO")

"""
def añobisiesto(año):
    if(año % 4 ==0 and año%100!=0 or año%400==0 ):
        return 1
    else:
        return 0

def nombre_mes(mes):

    if mes == 1:
        return "enero"
    elif mes == 2:
        return "Febrero"
    elif mes == 3:
        return "Marzo"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Mayo"
    elif mes == 6:
        return "Junio"

    elif mes == 7:
        return "Julio"

    elif mes == 8:
        return "Agosto"
    elif  mes == 9:
        return "Septiembre"
    elif mes == 10:
        return "Octubre"

    elif mes == 11:
        return "Noviembre"
    else:
        return "Diciembre"

