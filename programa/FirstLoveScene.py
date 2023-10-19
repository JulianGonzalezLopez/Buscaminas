import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from Scene import Scene
from SecondLoveScene import SecondLoveScene
from FirstSadScene import FirstSadScene 

class FirstLoveScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/sonrojado.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "¡Simio insolente! ¡¿Crees que podras amistarte con el GRAN LORD FREEZER?!")
        bottomText.label.pack()
        buttonN = tkinter.Button(self.frame,text="Si, vamos a tomar unos mateicos", command= lambda: self.destroySelf(parent,SecondLoveScene(parent)))
        buttonN.pack()
        buttonY = tkinter.Button(self.frame,text="No, tienes razón, solo interesa el cabeza de rodilla", command= lambda: self.destroySelf(parent,FirstSadScene(parent)))
        buttonY.pack()
