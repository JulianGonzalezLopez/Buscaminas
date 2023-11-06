import tkinter
from tkinter import ttk, font
from BgImage import BgImage
from PopUpImage import PopUpImage
from Buscaminas import Buscaminas
from BuscaminasUI import BuscaminasUI
import sqlite3
# depurar


class App():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("405x580")
        self.window.title("Freezer's choice")
        self.window.resizable(False, False)

        self.defaultFont = font.nametofont("TkDefaultFont") 
  
        self.defaultFont.configure(family="A Goblin Appears!",size=8) 


        self.reiniciar()
        self.buscaminas_ui = None
        self.conexion = sqlite3.connect("bm.db")
        self.crear_db()
        self.entryNombre = 0  # Contiene el nombre en la funcion ingresarNombre
        self.usuario = ""
        self.auxPopUp = ""
        self.actualizacion = 0

    def create_popup(self, logro):

        # Se llama a la base de datos para saber que texto corresponde al popup
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre FROM Logros WHERE id = ?", (logro,))
        # Texto del logro
        res = cursor.fetchall()

        popup = tkinter.Toplevel(self.window)
        # Establece el tamaño de la ventana emergente
        popup.geometry("200x100")

        # Configura la ventana emergente sin borde
        popup.overrideredirect(True)
        popup.attributes('-topmost', 1)

        # Obtiene el tamaño de la pantalla
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calcula las coordenadas x e y para que la ventana sea visible en su totalidad
        popup_width = 200
        popup_height = 150

        x = screen_width - popup_width
        y = screen_height - popup_height

        if x < 0:
            x = 0
        if y < 0:
            y = 0

        # Posiciona la ventana emergente en la esquina inferior derecha
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        imagen_logro = PopUpImage(popup, f"../images/logro_{logro}.png")
        self.auxPopUp = imagen_logro.new_pic
        imagen_logro.label.pack()
        label = tkinter.Label(popup, text=res[0][0], wraplength=150)
        label.pack()
        # Se autodestruye pasados los 2000 milis
        popup.after(2000, popup.destroy)

    # Funciones para conexiones DB

    def crear_db(self):
        self.conexion.execute("PRAGMA foreign_keys = 1")
        try:
            self.conexion.execute(
                "CREATE TABLE Logros (id integer primary key autoincrement, nombre text, descripcion text)")
            self.conexion.execute(
                "CREATE TABLE Usuarios (id integer primary key autoincrement, nombre text, puntos integer)")
            self.conexion.execute(
                "CREATE TABLE Usuarios_Logros (nombreU text, idL integer)")
            self.cargar_db()
        except sqlite3.OperationalError:
            pass
        self.conexion.close()

    def cargar_db(self):
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        self.conexion.execute(
            "INSERT INTO Logros(nombre, descripcion) VALUES('La primera nunca se olvida', 'Logro obtenido por morir por primera vez')")
        self.conexion.execute(
            "INSERT INTO Logros(nombre, descripcion) VALUES('Leo Mateolis', 'Logro obtenido por tomarte unos mates con Freezer')")
        self.conexion.execute(
            "INSERT INTO Logros(nombre, descripcion) VALUES('Kinda gay', 'Logro obtenido por casarte con el emperador galactico')")
        self.conexion.execute(
            "INSERT INTO Logros(nombre, descripcion) VALUES('Pelado matero', 'Logro obtenido por reventarle la cabeza al pelado blanco y tomarte unos mates')")
        self.conexion.commit()
        self.conexion.close()

    def ingresarNombre(self):
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        cursor = self.conexion.cursor()
        texto = self.entryNombre.get()
        self.usuario = texto
        try:
            cursor.execute(
                "SELECT nombre FROM Usuarios WHERE nombre = ?", (texto,))
            res = cursor.fetchall()
            if (res != []):
                pass
            else:
                sql = "INSERT INTO Usuarios(nombre,puntos) values(?,?)"
                try:
                    self.conexion.execute(sql, (texto, 0))
                    self.conexion.commit()
                except sqlite3.OperationalError:
                    print("error")
        except:
            pass

        self.conexion.close()
        self.segundaEscena()
    # Funcion que toma el valor de puntos de la base de datos de usuarios y los actualiza

    def tomarPuntos(self):
        print("Pidiendo puntos del usuario")
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT puntos FROM Usuarios WHERE nombre = ?", (self.usuario,))
        res = cursor.fetchone()
        res = res[0]
        self.actualizacion = res + self.buscaminas_ui.puntaje
        print(res, "VALOR ACTUAL PUNTOS")
        cursor.execute("UPDATE Usuarios SET puntos = ? WHERE nombre = ?",
                       (self.actualizacion, self.usuario,))
        self.conexion.commit()
        self.conexion.close()
        # mensaje en consola para comprobar que se actualizaron los datos en la base
        print("Base de datos actualizada: Usuario: ",
              self.usuario, "Puntos: ", self.actualizacion)

    def revisarPosesionLogro(self, logro):
        print('Revisando si usuario : ' + self.usuario + ' posee este logro')
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT nombreU,idL FROM Usuarios_Logros WHERE nombreU = ? AND idL = ?", (self.usuario, logro,))
        res = cursor.fetchall()
        self.conexion.close()
        if (res != []):
            print("Ya se encuentra en posesion del mismo")
        else:
            self.relacionarUsuarioLogro(logro)

    def relacionarUsuarioLogro(self, logro):
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        self.conexion.execute(
            "INSERT INTO Usuarios_Logros(nombreU,idL) values(?,?)", (self.usuario, logro))
        self.conexion.commit()
        print("LOGRO OBTENIDO! " + str(logro))
        self.create_popup(logro)
        self.conexion.close()

    def retornarTopCinco(self):
        print("Pidiendo puntos del usuario")
        self.conexion = sqlite3.connect("bm.db")
        self.conexion.execute("PRAGMA foreign_keys = 1")
        cursor = self.conexion.cursor()
        cursor.execute('SELECT nombre, puntos FROM Usuarios Order By Puntos DESC LIMIT 5')
        res = cursor.fetchall()
        print(res)
        return res

    # Escenas buscaminas
    def primeraEscena(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/pensativo.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()

        bottomText = tkinter.Label(frame, text="Dime tu nombre, insecto")
        bottomText.pack()

        self.entryNombre = ttk.Entry(frame)
        self.entryNombre.pack()

        button = tkinter.Button(frame, text="Ingresar",
                                command=lambda: self.ingresarNombre())
        button.pack()

        frame.pack()
        

    def segundaEscena(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/riendo.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()

        bottomText = tkinter.Label(
            frame, text="Esto...¿Piensas que puedes ganarle al gran Lord Freezer?", wraplength=400)
        bottomText.pack()

        buttonBad = tkinter.Button(
            frame, text="Si, he venido a rescatar al cabeza de rodilla", wraplength=400, command=lambda: self.primerEscenaBadEnding())
        buttonBad.pack()
        buttonGood = tkinter.Button(
            frame, text="No, vine por vos", command=lambda: self.primeraEscenaGoodEnding())
        buttonGood.pack()

        frame.pack()


    def primeraEscenaGoodEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/sonrojado.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="¡Simio insolente! ¡¿Crees que podras amistarte con el GRAN LORD FREEZER?!", wraplength=400)
        bottomText.pack()
        buttonBad = tkinter.Button(
            frame, text="Si, vamos a tomar unos mateicos", command=lambda: self.segundaEscenaGoodEnding())
        buttonBad.pack()
        buttonGood = tkinter.Button(
            frame, text="No, tienes razón", command=lambda: self.primerEscenaBadEnding())
        buttonGood.pack()

        frame.pack()

    def segundaEscenaGoodEnding(self):
        self.clear()
        self.revisarPosesionLogro(2)
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/mate1.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="Muchas gracias, necesitaba esto")
        bottomText.pack()
        button = tkinter.Button(frame, text="Reiniciar",
                                command=lambda: self.reiniciar())
        button.pack()

        frame.pack()

    def primerEscenaBadEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/triste.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="¿En serio solo te importa el pelado?")
        bottomText.pack()
        button = tkinter.Button(frame, text="Si...",
                                command=lambda: self.segundaEscenaBadEnding())
        button.pack()

        frame.pack()

    def segundaEscenaBadEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/enojado.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(frame, text="Entonces...MUERE")
        bottomText.pack()
        frame.pack()

        # Creo e inicializo el tablero, actualizo la ventana para que ande.

        self.crear_tablero_buscaminas()
        self.configurar_tablero_buscaminas()
        self.window.update()
        self.buscaminas_ui.start()

    # Metodo para el boton de la segunda escena o no funciona como YO quiero
    def crear_boton_oh_no(self):
        self.tomarPuntos()
        print("vamo bocaaaa")  # depuracion
        self.terceraEscenaBadEnding()

    def clear(self):
        lista = self.window.pack_slaves()
        for l in lista:
            l.destroy()

    def reiniciar(self):
        self.clear()
        self.window.iconphoto(
            True, tkinter.PhotoImage(file="../images/intro.png"))
        bImg = BgImage(self.window, "../images/intro.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.place(x=0, y=0)
        self.buttonIniciar = tkinter.Button(
            self.window, text="Iniciar", command=lambda: self.primeraEscena())
        self.buttonIniciar.place(x=190, y=278)

    # Buscaminas

    def crear_tablero_buscaminas(self):
        # Crea una instancia de Buscaminas
        self.buscaminas = Buscaminas(
            filas=5, columnas=5, num_minas=3)
        self.buscaminas.colocar_minas()
        self.buscaminas.inicializar_tablero()

        # Pasa la instancia de App a BuscaminasUI
        self.buscaminas_ui = BuscaminasUI(self.window, self.buscaminas, self)

    def configurar_tablero_buscaminas(self):
        self.buscaminas_ui.configurar_interfaz()

    # Visual Novel

    def terceraEscenaBadEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/derrotaJugador.jpeg")
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="Tocaste al pelado, perdiste... el pelado es MÍO")
        bottomText.pack()

        # Reinicio buscaminas
        reiniciar_button = tkinter.Button(
            frame, text="Intentar salvar al pelado una vez más ", command=lambda: [self.segundaEscenaBadEnding(), self.buscaminas_ui.reiniciar_juego()])
        reiniciar_button.pack()

        # Me gustó
        love_ending_button = tkinter.Button(
            frame, text="Me gustó...", command=self.primeraEscenaLoveEnding)
        love_ending_button.pack()

        frame.pack()

    def primeraEscenaLoveEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/freezerBaka.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="¿E- esto... acaso crees que puedes hacer que")
        bottomText.pack()
        bottomText2 = tkinter.Label(
            frame, text="EL GRAN EMPERADOR DEL UNIVERSO LORD FREEZER se ")
        bottomText2.pack()
        bottomText3 = tkinter.Label(
            frame, text="interese por una miserable y estupida sabandija como tú?")
        bottomText3.pack()
        button = tkinter.Button(frame, text="Si...",
                                command=self.segundaEscenaLoveEnding)
        button.pack()
        frame.pack()

    def segundaEscenaLoveEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/freezerTentado.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="¿Ooh... miserable sabandija...")
        bottomText.pack()
        bottomText2 = tkinter.Label(
            frame, text="para ganar mi afecto se me ocurren ")
        bottomText2.pack()
        bottomText3 = tkinter.Label(
            frame, text="algunas opciones que podrías tratar de realizar")
        bottomText3.pack()
        button = tkinter.Button(frame, text="¿Cuáles?",
                                command=self.terceraEscenaLoveEnding)
        button.pack()
        frame.pack()

    def terceraEscenaLoveEnding(self):
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/riendo.png")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="MORIR, MORIR O MORIR, ¿CUÁL PREFIERES SABANDIJA? JAJAJAJA")
        bottomText.pack()
        button = tkinter.Button(
            frame, text="MORIR", command=self.escenaBadLoveEnding)
        button.pack()
        button = tkinter.Button(
            frame, text="Prefiero tu amor", command=self.cuartaEscenaLoveEnding)
        button.pack()
        frame.pack()

    def escenaBadLoveEnding(self):
        self.clear()
        self.revisarPosesionLogro(1)
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/badLoveEndingFreezer.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="¡MUERE INSECTO!")
        bottomText.pack()
        button = tkinter.Button(frame, text="Reiniciar",
                                command=lambda: self.reiniciar())
        button.pack()

        frame.pack()

    def cuartaEscenaLoveEnding(self):
        self.clear()
        self.revisarPosesionLogro(3)
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/freezerEnamorado.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="Oh... está bien, podremos gobernar juntos el universo a nuestro antojo,")
        bottomText.pack()
        bottomText2 = tkinter.Label(
            frame, text="ven conmigo.")
        bottomText2.pack()
        button = tkinter.Button(frame, text="Volver a jugar",
                                command=lambda: self.reiniciar())
        button.pack()

        frame.pack()

    def primeraEndingWithKrilin(self):
        self.clear()
        self.tomarPuntos()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/freezerKrilin.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="... Felicidades miserable sabandija, llevate al pelado.", wraplength=400)
        bottomText.pack()
        button = tkinter.Button(frame, text="Vamonos Krilin...",
                                command=self.segundaEndingWithKrilin)
        button.pack()
        frame.pack()

    def segundaEndingWithKrilin(self):
        self.revisarPosesionLogro(4)
        self.clear()
        frame = tkinter.Frame(self.window)
        bImg = BgImage(frame, "../images/jugadorKrilin.jpeg")
        # Si eliminamos esto deja de andar el programa por el recolector de basura y coso
        self.aux = bImg.new_pic
        bImg.label.pack()
        bottomText = tkinter.Label(
            frame, text="Fin.")
        bottomText.pack()
        button = tkinter.Button(frame, text="Volver a jugar",
                                command=lambda: self.reiniciar())
        button.pack()

        tree = ttk.Treeview(frame, columns=("Columna1", "Columna2"), show="headings")
        ttk.Style().configure("Treeview.Heading", font=("A Goblin Appears!", 8))
        tree.heading("Columna1", text="Usuario")
        tree.heading("Columna2", text="Puntos")

        tree.column("Columna1", anchor="center")
        tree.column("Columna2", anchor="center")
        tree.pack()

        topCinco  = self.retornarTopCinco()
        for nombre,valor in topCinco:
            tree.insert("", "end", values=(nombre,valor))

        frame.pack()


if __name__ == "__main__":
    app = App()
    app.window.mainloop()
