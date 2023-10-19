import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from SceneLose import SceneLose
from Scene import Scene

class FirstSadScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/triste.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "¿En serio solo te importa el pelado?")
        bottomText.label.pack()
        #buttonN = tkinter.Button(self.frame,text="Continuar", command= lambda: self.destroySelf(parent,SceneMine(parent)))
        #buttonN.pack()
