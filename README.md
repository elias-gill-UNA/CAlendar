# Instalacion de dependencias.
El proyecto tiene declaradas las dependencias dentro de "depedencies.txt", el cual Pycharm lee y hace lo que tiene que hacer automaticamente.
Para hacerlo manualmente (de preferencia) deben realizar el siguiente comando dentro de la carpeta principal del
proyecto
```
pip install -r requirement.txt
```
Luego proseguir con el siguiente apartado.
# Solucionar los problemas de import.
Ok esto esta siendo una mierda con este lenguaje de juguete. Para que les funcionen los import tienen que hacer asi.

Se colocan dentro de la carpeta __src__ y hacen:
````
python ./setup.py sdist
````
Si la mierda funciona ahora hagan:
````
pip install ./dist/CAlendar-0.1.tar.gz
````
PERO QUE ASCOOOO. 

## Ojo, agregando nuevos paquetes:
Si es que crean nuevas subcarpetas (es decir, nuevos paquetes) tienen que crear un archivo
`__init__.py` dentro de esa carpeta (dejar vacio el archivo) y actualizar el archivo setup.py
