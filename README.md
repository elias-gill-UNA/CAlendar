
# Poetry y como utilizar. 
Poetry no es nada mas que un gestor de paquetes muy simple y facil de usar (para el que conozca npm o cargo ya saben la onda).
Para la utilizacion de poetry usan los siguientes comandos en su terminal (y si, no hay de otra):
```
pip install poetry
```
Se colocan en la carpeta del proyecto y escriben:
```
poetry shell
```
Deberia de iniciar el entorno virtual, luego realizan:
```
poetry install
```
Y derian estar ready to go.
Y ya esta, ya tienen las dependencias necesarias para el proyecto con la version correspondiente.

# Version alternativa.
El proyecto tambien tiene el "depedencies.txt", el cual Pycharm lee y hace lo que tiene que hacer automaticamente.
En todo caso se deria de usar:
```
pip install -r requirement.txt
```

Ok esto esta siendo una mierda con este lenguaje de juguete. Para que les funcionen los import tienen que hacer asi.

Se colocan dentro de la carpeta src y hacen:
````
python ./setup.py sdist
````
Si la mierda funciona ahora hagan:
````
pip install ./dist/CAlendar-0.1.tar.gz
````

PERO QUE ASCOOOO

