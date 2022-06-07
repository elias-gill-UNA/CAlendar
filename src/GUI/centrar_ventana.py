def centrar_Ventana(root, num_Ventana):
    ancho_ventana = 0
    alto_ventana = 0
    if num_Ventana == 0:
        ancho_ventana = 850
        alto_ventana = 550
    elif num_Ventana == 1:
        ancho_ventana = 1050
        alto_ventana = 500
    elif num_Ventana == 2:
        ancho_ventana = 400
        alto_ventana = 150
    elif num_Ventana == 3:
        ancho_ventana = 1200
        alto_ventana = 800
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    # La ventana no puede cambiar de tamaño
    root.resizable(False, False)


