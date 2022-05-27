class DescripcionProyecto:
    def __init__(self, nombre, descripcion, inicioPrevisto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = inicioPrevisto

class ValoresProyecto:
    def __init__(self):
        self.inicioTemprano = 0
        self.inicioTardio = -1
        self.finTemprano = -1
        self.finTardio = -1
        self.holgura = 0
