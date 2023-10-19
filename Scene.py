import tkinter
from tkinter import ttk


class Scene():
    def __init__(self, parent):
        pass

    def destroySelf(self,parent,nextScene):
        lista = parent.pack_slaves()
        print(lista)
        for l in lista:
            l.destroy()
        nextScene.frame.pack()