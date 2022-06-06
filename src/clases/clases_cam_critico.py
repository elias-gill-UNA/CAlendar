class ObjetoCritico:
    def __init__(self):
        self.cantidadCritico = 1 # numero de caminos criticos
        self.caminosCriticos = [] # los caminos en si
        self.actividadesCriticas=[]

class ActividadCaminoCritico:
    def __init__(self, nombre, duracion, anteriores):
        self.nombre = nombre
        self.duracion = duracion

        self.anteriores = anteriores
        self.siguientes = []

        self.anterioresPendientes = -1
        self.siguientesPendientes = -1

        self.inicioTemprano = -1
        self.inicioTardio = -1
        self.finTemprano = -1
        self.finTardio = -1
        self.holgura = -1

        self.fechaInicioTemprano = ''
        self.fechaInicioTardio = ''
        self.fechaFinTemprano = ''
        self.fechaFinTardio = ''

        self.identificador = 0


