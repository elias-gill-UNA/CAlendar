from backend.dataBase import proyectManager
import utilidades.calendario as cal

conexion = proyectManager.abrirProyecto(1)
feriados = cal.getListaFeriados(conexion)
for i in feriados:
    print(i.mes, i.dia, i.descripcion)
    print()

