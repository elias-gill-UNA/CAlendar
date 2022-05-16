def dias(fechaInicial,fechaFinal,duracion):
    suma1=0
    suma2=0
    contador=0
    contadorBisiesto=0
    fechaInicial=fechaInicial.split("/")
    fechaFinal=fechaFinal.split("/")
    for i in range(len(fechaInicial)):
        fechaInicial[i]=int(fechaInicial[i])
    for i in range(len(fechaFinal)):
        fechaFinal[i]=int(fechaFinal[i])
    for i in range(1,fechaInicial[2]+1):
        if i%4==0 and (i%400==0 or i%100!=0):
            contadorBisiesto=contadorBisiesto+1
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if fechaInicial[2]%4==0 and (fechaInicial[2]%400==0 or fechaInicial[2]%100!=0):
        meses[1]=29
        for i in range(fechaInicial[1]):
            suma1=suma1+meses[i]
            contador=contador+1
    else:
        for i in range(fechaInicial[1]):
            suma1=suma1+meses[i]
            contador=contador+1
    dias1=((fechaInicial[2]-1-contadorBisiesto)*365)+(contadorBisiesto*366)+(suma1-(meses[contador-1]- fechaInicial[0]))
    contadorBisiesto=0
    for i in range(1,fechaFinal[2]+1):
        if i%4==0 and (i%400==0 or i%100!=0):
            contadorBisiesto=contadorBisiesto+1
    contador=0
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if fechaFinal[2]% 4 == 0 and (fechaFinal[2]% 400 == 0 or fechaFinal[2] % 100 != 0):
        meses[1]=29
        for i in range(fechaFinal[1]):
            suma2=suma2+meses[i]
            contador=contador+1
    else:
        for i in range(fechaFinal[1]):
            suma2=suma2+meses[i]
            contador=contador+1
    dias2=((fechaFinal[2]-1-contadorBisiesto)*365)+(contadorBisiesto*366)+(suma2-(meses[contador-1]- fechaFinal[0]))
    diferencia=abs(dias2-dias1)
    if duracion<=diferencia:
        return True
    else:
        return False
print(dias("12/01/2021","14/01/2021",5))