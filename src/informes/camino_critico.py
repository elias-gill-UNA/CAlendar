from clases import *
from datetime import date, datetime, timedelta
# carga o dibuja el camino critico y lo guarda en la matriz
def cargarCriticos(objCritico, inicio, indice):
    bandera = False
    for descendiente in inicio.siguientes:
        if descendiente in objCritico.actividadesCriticas: # si el descendiente es critico
            if bandera == True:
                # Copia el camino critico dentro del objCritico
                for k in objCritico.caminosCriticos[indice - 1]:
                    if k == aux: # solo ignora el error
                        break
                    if k.nombre != "Inicio": # nombre de la primera actividad
                        objCritico.caminosCriticos[indice].append(k)

            objCritico.caminosCriticos[indice].append(descendiente)
            cargarCriticos(objCritico, descendiente,indice)
            indice = indice+1
            bandera = True
            aux = descendiente


# funcion que prepara las matrices para los distintos caminos criticos
def inicializarCritico(objCritico, listaActividades):
    for i in range(objCritico.cantidadCritico):
        objCritico.caminosCriticos.append([listaActividades[0]]) # anade el inicio al nuevo CamCrit


# funcion principal que busca el camino critico
def caminoCritico(listaActividades, proyecto, objCritico):
    __inicializarLista(listaActividades)

    actividad = listaActividades[0] # actividad inicio
    actividad.inicioTemprano = 0
    cola = [actividad]

    while len(cola) > 0: # carga de inicios temprano, etc
        actividad = cola.pop(0)

        #1
        actividad.finTemprano = actividad.inicioTemprano + actividad.duracion#valor numerico
        actividad.fechaFinTemprano = suma(actividad.fechaInicioTemprano,actividad.duracion)#valor fecha
        # ya esta calculado el fin temprano
        if (proyecto.finTemprano < actividad.finTemprano):
            #2
            proyecto.finTemprano = actividad.finTemprano # valor
            proyecto.fechaFinTemprano = actividad.fechaFinTemprano # fecha

        for descendiente in actividad.siguientes:
            if descendiente.inicioTemprano < actividad.finTemprano: #comparar cadenas
                #3
                descendiente.inicioTemprano = actividad.finTemprano#valor
                descendiente.fechaInicioTemprano = actividad.fechaFinTemprano # fecha

            descendiente.anterioresPendientes -= 1
            if descendiente.anterioresPendientes == 0:
                cola.append(descendiente) # sigue operando con la cola
    #4
    proyecto.finTardio = proyecto.finTemprano + proyecto.holgura#valor
    proyecto.fechaFinTardio = suma(proyecto.fechaFinTemprano,proyecto.holgura) # fecha
    #5
    proyecto.inicioTardio = proyecto.finTardio # actualizar los tiempos de inicio y fin del proyecto
    proyecto.fechaInicioTardio = proyecto.fechaFinTardio #fecha

    actividad = listaActividades[-1] # quitar ultimo elemento
    #6
    actividad.finTardio = proyecto.finTardio # valor
    actividad.fechaFinTardio = proyecto.fechaFinTardio #fecha
    cola = [actividad] # algo

    while len(cola) > 0: # calcula las fechas tardias
        actividad = cola.pop(0)

        #7
        actividad.inicioTardio = actividad.finTardio - actividad.duracion # actualizar los tiempos de las actividades, es el valor numerico del de arriba
        actividad.fechaInicioTardio = resta(actividad.fechaFinTardio,actividad.duracion)#fecha
        actividad.holgura = actividad.inicioTardio - actividad.inicioTemprano

        if (actividad.holgura == proyecto.holgura):
            objCritico.actividadesCriticas.append(actividad) # si es una actividad critica entonces la anade a la lista 

        if (proyecto.inicioTardio > actividad.inicioTardio): # actualiza los tiempos de inicio tardio del proyecto
            #8
            proyecto.inicioTardio = actividad.inicioTardio # valor
            proyecto.fechaInicioTardio = actividad.fechaInicioTardio # fecha

        for antecesor in actividad.anteriores:
            if antecesor.finTardio == -1 or antecesor.finTardio > actividad.inicioTardio:
                #9
                antecesor.finTardio = actividad.inicioTardio # valor
                antecesor.fechaFinTardio = actividad.fechaInicioTardio # fecha
            antecesor.siguientesPendientes -= 1 
            if antecesor.siguientesPendientes == 0:
                cola.append(antecesor) # agrega algo en algun lugar


# determina la cantidad de caminos criticos que existen en el proyecto
def cantidadCaminosCriticos(objCritico, actvInicio):
    sumar = False
    for actividad in actvInicio.siguientes:

        if actividad in objCritico.actividadesCriticas and sumar: # si este si es mayor que 1 es porque hay mas de 1 
            objCritico.cantidadCritico = objCritico.cantidadCritico + 1
            cantidadCaminosCriticos(objCritico, actividad)

        # si esta actividad es critica y sumar == False
        if actividad in objCritico.actividadesCriticas and not sumar:
            cantidadCaminosCriticos(objCritico, actividad)
            sumar = True


# recibe la lista de actividades y la prepara para comenzar 
# WARNING : no volver a usar esta lista, porque esta funcion la modifica
# NOTE: PASAR UNA LISTA DE ACTIVIDADES AUXILIAR O VOLVER A PEDIR DEL BACKEND UNA NUEVA
def __inicializarLista(listaActividades):
    for actividad in listaActividades:
        #actividad.siguientes = []

        if len(actividad.anteriores) == 0 and actividad.nombre != "Inicio" and actividad.nombre != "Fin":
            actividad.anteriores.append(listaActividades[0])
        
        actividad.anterioresPendientes = len(actividad.anteriores)
        actividad.inicioTemprano = -1
        actividad.inicioTardio = -1
        actividad.finTemprano = -1
        actividad.finTardio = -1
        actividad.holgura = -1

    for actividad in listaActividades:
        for anterior in actividad.anteriores:
            anterior.siguientes.append(actividad)

    for actividad in listaActividades:
        if len(actividad.siguientes) == 0 and actividad.nombre!="Inicio" and actividad.nombre!="Fin":
            actividad.siguientes.append(listaActividades[len(listaActividades)-1])
            listaActividades[len(listaActividades)-1].anteriores.append(actividad)
    
    for actividad in listaActividades:
        actividad.siguientesPendientes = len(actividad.siguientes)

def convertirLista(listaGeneral,listaacts):
    for i in listaGeneral: #inicializa cada actividad con antecedentes en vacio
        actividad = ActividadCaminoCritico(i.nombre,i.duracion,[])
        listaacts.append(actividad)

    for i in listaGeneral:
        for j in i.dependencias: #como cada actividad tiene sus antecedentes en forma del indice de esa actividad, hago appen de esa actividad en ese indice
            listaacts[listaGeneral.index(i)].anteriores.append(listaacts[j])

    anteriores = []
    actividad = ActividadCaminoCritico("Inicio", 0, anteriores)
    listaacts.insert(0,actividad) #inicio siempre al comienzo

    anteriores = [] #fin siempre al final
    actividad = ActividadCaminoCritico("Fin", 0, anteriores)
    listaacts.append(actividad)
def suma(fecha,cantidad):#actualizar
    fecha = fecha.split("/")
    
    sumando = timedelta(cantidad)
    
    aux = date(int(fecha[2]),int(fecha[1]),int(fecha[0]))
    
    resultado = aux+sumando
    
    final = str(resultado)
    
    final = final.split("-")
    
    final= final[2] +"/"+ final[1] + "/" + final[0]
    
    return final

def resta(fecha,cantidad):#actualizar
    fecha = fecha.split("/")
    
    restando = timedelta(cantidad)
    
    aux = date(int(fecha[2]),int(fecha[1]),int(fecha[0]))
    
    resultado = aux-restando
    
    final = str(resultado)
    
    final = final.split("-")
    
    final= final[2] +"/"+ final[1] + "/" + final[0]
    
    return final

def zeller(año,mes,dia): # determina que dia cae una fecha especifica, domingo cero, y sabado es 6
    a=int((14-mes)/12)
    y=año-a
    m=mes+ 12*a - 2
    d=int((dia+y+int(y/4)-int(y/100)+int(y/400)+int((31*m)/12)) % 7)
    return d
def caminoCriticoCopia(listaActividades, proyecto,objCritico):
    __inicializarLista(listaActividades)

    actividad = listaActividades[0] # actividad inicio
    actividad.inicioTemprano = 0
    cola = [actividad]

    while len(cola) > 0: # carga de inicios temprano, etc
        actividad = cola.pop(0)

        #1
        actividad.finTemprano = actividad.inicioTemprano + actividad.duracion#valor numerico
        #actividad.fechaFinTemprano = suma(actividad.fechaInicioTemprano,actividad.duracion)#valor fecha
        # ya esta calculado el fin temprano

        if (proyecto.finTemprano < actividad.finTemprano):
            #2
            proyecto.finTemprano = actividad.finTemprano # valor
            #proyecto.fechaFinTemprano = actividad.fechaFinTemprano # fecha

        for descendiente in actividad.siguientes:
            if descendiente.inicioTemprano < actividad.finTemprano: #comparar cadenas
                #3
                descendiente.inicioTemprano = actividad.finTemprano#valor
                #descendiente.fechaInicioTemprano = actividad.fechaFinTemprano # fecha

            descendiente.anterioresPendientes -= 1
            if descendiente.anterioresPendientes == 0:
                cola.append(descendiente) # sigue operando con la cola
    #4
    proyecto.finTardio = proyecto.finTemprano + proyecto.holgura#valor
    #proyecto.fechaFinTardio = suma(proyecto.fechaFinTemprano,proyecto.holgura) # fecha
    #5
    proyecto.inicioTardio = proyecto.finTardio # actualizar los tiempos de inicio y fin del proyecto
    #proyecto.fechaInicioTardio = proyecto.fechaFinTardio #fecha

    actividad = listaActividades[-1] # quitar ultimo elemento
    #6
    actividad.finTardio = proyecto.finTardio # valor
    #actividad.fechaFinTardio = proyecto.fechaFinTardio #fecha
    cola = [actividad] # algo

    while len(cola) > 0: # calcula las fechas tardias
        actividad = cola.pop(0)

        #7
        actividad.inicioTardio = actividad.finTardio - actividad.duracion # actualizar los tiempos de las actividades, es el valor numerico del de arriba
        #actividad.fechaInicioTardio = resta(actividad.fechaFinTardio,actividad.duracion)#fecha
        actividad.holgura = actividad.inicioTardio - actividad.inicioTemprano

        if (actividad.holgura == proyecto.holgura):
            objCritico.actividadesCriticas.append(actividad) # si es una actividad critica entonces la anade a la lista 

        if (proyecto.inicioTardio > actividad.inicioTardio): # actualiza los tiempos de inicio tardio del proyecto
            #8
            proyecto.inicioTardio = actividad.inicioTardio # valor
            #proyecto.fechaInicioTardio = actividad.fechaInicioTardio # fecha

        for antecesor in actividad.anteriores:
            if antecesor.finTardio == -1 or antecesor.finTardio > actividad.inicioTardio:
                #9
                antecesor.finTardio = actividad.inicioTardio # valor
                #antecesor.fechaFinTardio = actividad.fechaInicioTardio # fecha
            antecesor.siguientesPendientes -= 1 
            if antecesor.siguientesPendientes == 0:
                cola.append(antecesor) # agrega algo en algun lugar
def inicializarFechaInicio(listaActividades,listaCopia,proyect):
    contador=0
    for actividad in listaCopia:
        listaActividades[contador].fechaInicioTemprano=suma(proyect.fechaInicioTemprano,actividad.inicioTemprano)
        contador=contador+1