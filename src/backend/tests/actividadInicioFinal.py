#aplicar este codigo luego de inicializar el proyecto, se le puede meter dentro de la funcion tambien
def conectar_Actividades(lista_Actividades):
    for actividad in lista_Actividades:#para hacer que las actividades sin antecedentes tengan como antecedentes a la actividad imaginaria "inicio"
        if len(actividad.anteriores) == 0 and actividad.nombre!="Inicio" and actividad.nombre!="Fin":
            #print(actividad.nombre)
            actividad.anteriores.append(lista_Actividades[0])
            lista_Actividades[0].siguientes.append(actividad)

        if len(actividad.siguientes) == 0 and actividad.nombre!="Inicio" and actividad.nombre!="Fin":#para hacer que las actividades sin descendientes sean antecedentes a la actividad imaginaria "fin"
            lista_Actividades[len(lista_Actividades)-1].anteriores.append(actividad)