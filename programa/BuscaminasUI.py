import tkinter as tk
import pygame


class BuscaminasUI:
    def __init__(self, root, buscaminas, app_instance):
        self.root = root
        self.buscaminas = buscaminas
        self.app = app_instance
        self.puntos = 0
        self.puntaje = 0
        self.game_over = False
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
                boton.bind("<Button-3>", self.marcar_con_bandera)
                boton.grid(row=fila, column=columna)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

    """
    MODIFICACION PARA MOSTRAR MINAS EN EL TABLERO

    def configurar_interfaz(self):
    # Configura los botones del tablero
    for fila in range(self.buscaminas.filas):
        fila_botones = []
        for columna in range(self.buscaminas.columnas):
            if self.buscaminas.tablero[fila][columna] == -1:
                # Si hay una mina en esta casilla, muestra el emoji directamente
                boton = tk.Button(self.frame, text="💣", width=2, height=1)
            else:
                # Casilla sin mina, utiliza el comando clic_en_casilla
                boton = tk.Button(self.frame, text=" ", width=2, height=1,
                                  command=lambda f=fila, c=columna: self.clic_en_casilla(f, c))
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        self.botones.append(fila_botones)
        
        """

    def actuPuntaje(self, fila, columna):
        if self.buscaminas.tablero[fila][columna] != -1:
            self.puntos += 1
        # print("Puntaje:", self.puntos)    ## Mostrar contador en terminal
        return self.puntos

    def clic_en_casilla(self, fila, columna):
        if self.game_over:
            return
        # La casilla tiene una mina, el juego termina
        if self.buscaminas.tablero[fila][columna] == -1:
            self.game_over = True
            self.mostrar_minas_al_perder()
            self.puntaje = self.puntos
        # La casilla no tiene una mina, descubre la casilla
        else:
            self.buscaminas.cubiertas[fila][columna] = False
            self.actuPuntaje(fila, columna)
            self.botones[fila][columna]["state"] = "disabled"
            minas_cercanas = self.buscaminas.contar_minas_cercanas(
                fila, columna)
            # No hay minas cercanas, explorar casillas adyacentes
            if minas_cercanas == 0:
                self.buscaminas.explore_casillas_adyacentes(fila, columna)
                # Establecer el texto del botón en "0" cuando no hay minas cercanas
                self.botones[fila][columna]["text"] = "0"
            # Mostrar el número de minas cercanas en la casilla
            elif minas_cercanas > 0:
                self.botones[fila][columna]["text"] = str(minas_cercanas)
            # Llamar a verificar_victoria después de descubrir una casilla
            self.verificar_victoria()

    def descubrir_casilla(self, fila, columna):
        self.botones[fila][columna]["state"] = "disabled"

    def mostrar_minas_al_perder(self):
        for fila in range(self.buscaminas.filas):
            for columna in range(self.buscaminas.columnas):
                if self.buscaminas.tablero[fila][columna] == -1:
                    # Muestra una mina en la casilla correspondiente
                    self.botones[fila][columna]["text"] = '💣'
                    self.explosion = pygame.mixer.Sound(
                        '../sound/explosion.wav')
                    self.explosion.set_volume(0.25)
                    self.explosion.play()
        self.game_over = True

        # Deshabilita todos los botones en el tablero
        for fila_botones in self.botones:
            for boton in fila_botones:
                boton.config(state="disabled")

        # Creo un marco para el botón "Oh no..." porque sino se ve para el culo
        oh_no_frame = tk.Frame(self.root)
        oh_no_frame.pack()

        # Creo el botón y lo asocio al metodo de la clase app
        oh_no_button = tk.Button(
            oh_no_frame, text="Oh no...", command=self.app.crear_boton_oh_no)
        # Ajusto estilos
        oh_no_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def marcar_con_bandera(self, event):
        if self.game_over:
            return
        boton = event.widget  # Obtiene el widget (botón) que generó el evento

        if boton["state"] != "disabled" and boton["text"] == " ":
            boton["text"] = "🚩"
            self.verificar_victoria()
        elif boton["text"] == "🚩":
            boton["text"] = " "

    def verificar_victoria(self):
        todas_descubiertas = True
        for fila in range(self.buscaminas.filas):
            for columna in range(self.buscaminas.columnas):
                boton = self.botones[fila][columna]
                valor = self.buscaminas.tablero[fila][columna]
                texto = boton["text"]

                if valor != -1:
                    # Casilla sin mina, debe estar descubierta
                    if texto == " ":
                        todas_descubiertas = False
                        break

        if todas_descubiertas:
            # Crear un botón "Que fácil" y asociarlo a ruta final
            boton_facil = tk.Button(
                self.frame, text="Que fácil", command=self.app.primeraEndingWithKrilin)
            boton_facil.grid(row=self.buscaminas.filas, column=0,
                             columnspan=self.buscaminas.columnas, pady=(10, 0))
            self.puntaje = self.puntos
            self.game_over = True

    def obtener_fila_columna(self, boton):
        # Obtiene la información de la cuadrícula del botón
        info = boton.grid_info()
        fila = info["row"]
        columna = info["column"]
        return fila, columna

    def reiniciar_juego(self):
        if self.app and self.app.window and self.app.window.winfo_exists():
            # Limpia el tablero del Buscaminas actual
            self.buscaminas.colocar_minas()
            self.buscaminas.inicializar_tablero()

        if self.botones:
            # Limpia los botones de la interfaz
            for fila_botones in self.botones:
                for boton in fila_botones:
                    if boton.winfo_exists():  # Verifica si el botón aún existe
                        boton.destroy()
            self.botones.clear()

        # Configura nuevamente el tablero
        self.configurar_interfaz()
        self.root.update()  # Forzar la actualización de la interfaz
        self.start()

    def start(self):
        # Llama a esta función para mostrar la ventana del Buscaminas
        self.root.mainloop()
