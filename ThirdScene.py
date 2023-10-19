import tkinter
from tkinter import ttk
from BgImage import BgImage
from Text import Text
from SceneLose import SceneLose
from Scene import Scene
from SceneMine import SceneMine

class ThirdScene(Scene):
    def __init__(self, parent):
        self.frame = tkinter.Frame(parent, bg="yellow")
        bImg = BgImage(self.frame,"images/tercera.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = Text(self.frame, "Me has hecho reir, insecto ¡笑 笑 笑 笑!")
        bottomText.label.pack()
        Text(self.frame, "Está bien, te permitiré rescatar al tobogan de piojos si logras pasar este desafio!").label.pack()
        #EN BUTTONN DEBERIA IR EL FRAME DEL BUSCAMINAS
        #buttonN = tkinter.Button(self.frame,text="Continuar", command= lambda: self.destroySelf(parent,SceneMine(parent)))
        #buttonN.pack()
