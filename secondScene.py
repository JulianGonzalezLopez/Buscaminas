import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from ThirdScene import ThirdScene
from Scene import Scene
from SceneLose import SceneLose

class SecondScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"images/segunda.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Esto...piensas que puedes ganarle al gran LORD [REDACTED]")
        bottomText.label.pack()
        buttonN = tkinter.Button(self.frame,text="Claro!", command= lambda: self.destroySelf(parent,ThirdScene(parent)))
        buttonN.pack()
