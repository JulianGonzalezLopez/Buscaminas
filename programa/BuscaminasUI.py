import tkinter as tk


class BuscaminasUI:
    def __init__(self, root, buscaminas, app_instance):
        self.root = root
        self.buscaminas = buscaminas
        self.app = app_instance
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.botones = []  # Lista para almacenar los botones que representan las casillas

    def configurar_interfaz(self):
        # Configura los botones del tablero
        for fila in range(self.buscaminas.filas):
            fila_botones = []
            for columna in range(self.buscaminas.columnas):
                boton = tk.Button(self.frame, text=" ", width=2, height=1,
                                  command=lambda f=fila, c=columna: self.clic_en_casilla(f, c))
                boton.grid(row=fila, column=columna)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

    def clic_en_casilla(self, fila, columna):
        # La casilla tiene una mina, el juego termina
        if self.buscaminas.tablero[fila][columna] == -1:
            self.mostrar_minas_al_perder()

        # La casilla no tiene una mina, descubre la casilla
        else:
            self.buscaminas.cubiertas[fila][columna] = False
            self.botones[fila][columna]["state"] = "disabled"
            minas_cercanas = self.buscaminas.contar_minas_cercanas(
                fila, columna)
            # No hay minas cercanas, explorar casillas adyacentes
            if minas_cercanas == 0:
                self.buscaminas.explore_casillas_adyacentes(fila, columna)
            # Mostrar el número de minas cercanas en la casilla
            elif minas_cercanas > 0:
                self.botones[fila][columna]["text"] = str(minas_cercanas)

    def descubrir_casilla(self, fila, columna):
        self.botones[fila][columna]["state"] = "disabled"

    def mostrar_minas_al_perder(self):
        for fila in range(self.buscaminas.filas):
            for columna in range(self.buscaminas.columnas):
                if self.buscaminas.tablero[fila][columna] == -1:
                    # Muestra una mina en la casilla correspondiente
                    self.botones[fila][columna]["text"] = "💥"

        # Deshabilita todos los botones en el tablero
        for fila_botones in self.botones:
            for boton in fila_botones:
                boton.config(state="disabled")

        # Tercera escena
        self.app.terceraEscenaBadEnding()

    def reiniciar_juego(self):
        # Limpia el tablero del Buscaminas actual
        self.buscaminas.colocar_minas()
        self.buscaminas.inicializar_tablero()

        # Limpia los botones de la interfaz
        for fila_botones in self.botones:
            for boton in fila_botones:
                boton.destroy()
        self.botones.clear()

        # Configura nuevamente el tablero
        self.configurar_interfaz()
        self.root.update()
        self.start()

    def start(self):
        # Llama a esta función para mostrar la ventana del Buscaminas
        self.root.mainloop()
