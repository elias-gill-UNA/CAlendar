class actividad:
    def __init__(self, identificador,nombre,duracion,fechaInicioTemprano,fechaInicioTardio):
        self.identificador=identificador
        self.nombre=nombre
        self.duracion=duracion
        self.fechaInicioTemprano=fechaInicioTemprano
        self.fechaInicioTardio=fechaInicioTardio
        self.finalizo=0#si finalizo es igual a 1, entonces la actividad fue terminada