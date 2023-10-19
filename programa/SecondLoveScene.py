import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from Scene import Scene

class SecondLoveScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/mate1.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Muchas gracias, necesitaba esto")
        bottomText.label.pack()
        button = tkinter.Button(self.frame,text="Reiniciar", command= lambda: self.terminar(parent))
        button.pack()
