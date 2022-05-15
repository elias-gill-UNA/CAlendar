from tkinter import *
from navbar import Inicializar

root = Tk()

Inicializar(root)

def OnClick():
    buttonMsg = Label(root, text="ABRIR ARCHIVO!")
    buttonMsg.grid(row=3, column=0)

myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I Like Donuts!")
myButton = Button(root, text="Archivos", command=OnClick)
myButton.grid(row=2, column=0)

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()