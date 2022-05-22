from tkinter import *

def inputUsuario(root, width, row, column):
    return Entry(root, width=width, borderwidth=2).grid(row=row, column=column)

def nuevo_texto(root, text, row, column):
    return Label(root, text=text).grid(row=row, column=column)

