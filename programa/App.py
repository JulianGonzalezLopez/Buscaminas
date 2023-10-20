import tkinter
from tkinter import ttk
from BgImage import BgImage


class App():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("400x500")
        self.window.title("Freezer's choice")
        self.reiniciar()

    def primeraEscena(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/pensativo.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        
        bottomText = tkinter.Label(frame, text="Dime tu nombre, insecto")
        bottomText.pack()
        
        entry = ttk.Entry(frame)
        entry.pack()

        button = tkinter.Button(frame,text="Ingresar", command= lambda: self.segundaEscena())
        button.pack()

        frame.pack()

    def segundaEscena(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/riendo.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()

        bottomText =  tkinter.Label(frame, text="Esto...¿Piensas que puedes ganarle al gran Lord Freezer?")
        bottomText.pack()

        buttonBad = tkinter.Button(frame,text="Si, he venido a rescatar al cabeza de rodilla", command= lambda: self.primerEscenaBadEnding())
        buttonBad.pack()
        buttonGood = tkinter.Button(frame,text="No, vine por vos", command= lambda: self.primeraEscenaGoodEnding())
        buttonGood.pack()
                
        frame.pack()
    
    def primeraEscenaGoodEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/sonrojado.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = tkinter.Label(frame, text="¡Simio insolente! ¡¿Crees que podras amistarte con el GRAN LORD FREEZER?!")
        bottomText.pack()
        buttonBad = tkinter.Button(frame,text="Si, vamos a tomar unos mateicos", command= lambda: self.segundaEscenaGoodEnding())
        buttonBad.pack()
        buttonGood = tkinter.Button(frame,text="No, tienes razón, solo me interesa el cabeza de rodilla", command= lambda: self.primerEscenaBadEnding())
        buttonGood.pack()

        frame.pack()

    def segundaEscenaGoodEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/mate1.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = tkinter.Label(frame, text="Muchas gracias, necesitaba esto")
        bottomText.pack()
        button = tkinter.Button(frame,text="Reiniciar", command= lambda: self.reiniciar())
        button.pack()

        frame.pack()

    def primerEscenaBadEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/triste.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = tkinter.Label(frame, text="¿En serio solo te importa el pelado?")
        bottomText.pack()
        button = tkinter.Button(frame,text="Si...", command= lambda: self.segundaEscenaBadEnding())
        button.pack()

        frame.pack()

    def segundaEscenaBadEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window, bg="yellow")
        bImg = BgImage(frame,"../images/enojado.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.pack()
        bottomText = tkinter.Label(frame, text="Entonces...MUERE")
        bottomText.pack()
        frame.pack()   



    def clear(self):
        lista = self.window.pack_slaves()
        for l in lista:
            l.destroy()
    
    def reiniciar(self):
        self.clear()
        self.window.iconphoto(True, tkinter.PhotoImage(file="../images/intro.png"))
        bImg = BgImage(self.window,"../images/intro.png")
        self.aux = bImg.new_pic #Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        bImg.label.place(x=0, y=0)
        self.buttonIniciar = tkinter.Button(self.window ,text="Iniciar", command= lambda: self.primeraEscena())
        self.buttonIniciar.place(x=190, y=278)

if __name__ == "__main__":
    app = App() 
    app.window.mainloop()

    