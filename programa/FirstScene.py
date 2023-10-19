import tkinter
from tkinter import ttk
from SecondScene import *
from BgImage import BgImage
from Text import Text
from Scene import Scene

class FirstScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/pensativo.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Dime tu nombre, insecto")
        bottomText.label.pack()
        #Seria al pedo abstraerlo de momento
        entry = ttk.Entry(self.frame)
        entry.pack()
        #De momento quedan como objetos locales
        button = tkinter.Button(self.frame,text="Ingresar", command= lambda: self.destroySelf(parent,SecondScene(parent)))
        button.pack()