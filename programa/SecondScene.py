import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from Scene import Scene
from FirstLoveScene import FirstLoveScene
from FirstSadScene import FirstSadScene

class SecondScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"../images/riendo.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Esto...¿Piensas que puedes ganarle al gran Lord Freezer?")
        bottomText.label.pack()
        buttonN = tkinter.Button(self.frame,text="Si, he venido a rescatar al cabeza de rodilla", command= lambda: self.destroySelf(parent,FirstSadScene(parent)))
        buttonN.pack()
        buttonY = tkinter.Button(self.frame,text="No, vine por vos", command= lambda: self.destroySelf(parent,FirstLoveScene(parent)))
        buttonY.pack()
                
