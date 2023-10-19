import tkinter
from tkinter import ttk
from firstScene import *
from time import sleep
class App():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("500x500")
        self.scene1 = FirstScene(self.window)
        self.scene1.frame.pack()

    def clear(self):
        print("fideos")
        lista = self.window.pack_slaves()
        print(lista)
        for l in lista:
            l.destroy()


if __name__ == "__main__":
    app = App() 
    app.window.mainloop()

    