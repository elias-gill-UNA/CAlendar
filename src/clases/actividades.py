class Actividad:
    def __init__(self, identificador, nombre, duracion, dependencias, fechaInicioTemprano, fechaInicioTardio, finalizo):
        self.identificador = identificador
        self.nombre = nombre
        self.duracion = duracion
        self.dependencias = dependencias
        self.fechaInicioTemprano = fechaInicioTemprano
        self.fechaInicioTardio = fechaInicioTardio
        self.finalizado = finalizo # ENTERO    1: finalizado  0: aun no
