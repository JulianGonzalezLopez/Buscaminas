import tkinter
from tkinter import ttk
from FirstScene import *
from time import sleep



class App():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("500x500")
        self.buttonIniciar = tkinter.Button(self.window ,text="Iniciar", command= self.iniciar)
        self.buttonIniciar.pack()

    def iniciar(self):
        scene1 = FirstScene(self.window)
        scene1.frame.pack()
        self.buttonIniciar.pack_forget()

    def clear(self):
        lista = self.window.pack_slaves()
        print(lista)
        for l in lista:
            l.destroy()


    

if __name__ == "__main__":
    app = App() 
    app.window.mainloop()

    