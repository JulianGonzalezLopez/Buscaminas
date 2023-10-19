import tkinter
import window

class Text():
    def __init__(self,parent,textContent):
        self.label = tkinter.Label(parent, text=textContent)
