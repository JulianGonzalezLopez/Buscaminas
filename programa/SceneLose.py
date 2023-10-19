import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from Scene import Scene

class SceneLose(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/lose.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Mal ahí :(")
        bottomText.label.pack()