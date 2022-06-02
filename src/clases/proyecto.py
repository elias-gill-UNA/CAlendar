class Proyecto:
    def __init__(self,nombre, descripcion, inicioPrevisto, diasLaborales, holgura):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = inicioPrevisto
        self.holgura = holgura
        self.diasLaborales = diasLaborales # cantidad de dias de trabajo contando del lunes

        # valores cargados y actualizados por la base de datos
        self.identificador = 0 # esto se sobreescribe en la base de datos, dejar en 0 al crear proyecto
        self.contadorActividades = 0
        self.contadorConexiones = 0

        # valores asignados por el camino critico
        self.inicioTemprano = 0
        self.inicioTardio = -1
        self.finTemprano = -1
        self.finTardio = -1

    

