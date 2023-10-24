import random


class Buscaminas:
    def __init__(self, filas, columnas, num_minas):
        self.filas = filas
        self.columnas = columnas
        self.num_minas = num_minas
        self.tablero = [[0] * columnas for _ in range(filas)]
        self.cubiertas = [[True] * columnas for _ in range(filas)]

    def colocar_minas(self):
        # Coloca las minas en el tablero de forma aleatoria
        for _ in range(self.num_minas):
            fila, columna = random.randint(
                0, self.filas - 1), random.randint(0, self.columnas - 1)
            while self.tablero[fila][columna] == -1:
                fila, columna = random.randint(
                    0, self.filas - 1), random.randint(0, self.columnas - 1)
            self.tablero[fila][columna] = -1  # -1 representa una mina

    def inicializar_tablero(self):
        # Inicializa el tablero con valores predeterminados y coloca minas
        self.colocar_minas()
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] != -1:
                    self.tablero[fila][columna] = 0
                self.cubiertas[fila][columna] = True

    def contar_minas_cercanas(self, fila, columna):
        minas_cercanas = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                    if self.tablero[fila + i][columna + j] == -1:
                        minas_cercanas += 1
        return minas_cercanas

    def explore_casillas_adyacentes(self, fila, columna):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                    if self.tablero[fila + i][columna + j] != -1:
                        self.tablero[fila + i][columna + j] = 0
                        self.cubiertas[fila + i][columna + j] = False
