from tkinter import *

root = Tk()

def OnClick():
    buttonMsg = Label(root, text=inputUsuario)
    buttonMsg.grid(row=3, column=0)

inputUsuario = Entry(root, width=50, borderwidth=20).grid(row=1, column=0)
myButton = Button(root, text="Archivos", command=OnClick).grid(row=2, column=0)

root.mainloop()