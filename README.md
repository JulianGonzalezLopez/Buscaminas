# Buscaminas con Interfaz en Python

Este proyecto es una implementación simple del juego Buscaminas con una interfaz gráfica desarrollada en Python y la biblioteca Tkinter. El juego consta de tres partes principales: la aplicación de la interfaz gráfica, la lógica del juego Buscaminas y una interfaz de usuario para el juego.

## Dependencias
Para correr este proyecto necesitaras los siguientes programas / librerias instalados:
- Python (Fue desarrollado con la version 3.12)
- Libreria PIL / Pillow
- SQLite3 (Viene por defecto en la standard library desde la versión 2.5)

## Manual de usuario
1. Descargar e instalar Python desde https://www.python.org/downloads/
2. Poner los ejecutables de python en el path https://www.youtube.com/watch?v=5YKZ03ZcvLo
3. Instalar pillow mediante PIP usando el comando "pip install pillow"
4. Clonar este repositorio mediante el comando "git clone https://github.com/JulianGonzalezLopez/Buscaminas.git" o descargando el .ZIP
5. Abrir la carpeta en Visual Studio Code
6. Desde la terminal, ir a la carpeta programa mediante el comando "cd programa"
7. Desde la terminal, ejecutar el programa escribiendo "python app.py"

## Clases

### Clase `App` (App.py)

La clase `App` se encarga de gestionar la interfaz gráfica del juego y las narrativas. A continuación, se describen sus funciones:

- `__init__(self)`: Constructor de la clase. Inicializa la ventana y otras variables importantes.

- `primeraEscena(self)`: Muestra la primera escena del juego con una imagen de introducción y un campo para ingresar el nombre del jugador.

- `segundaEscena(self)`: Muestra la segunda escena del juego con una pregunta al jugador.

- `primeraEscenaGoodEnding(self)`: Muestra la primera escena de un final bueno.

- `segundaEscenaGoodEnding(self)`: Muestra la segunda escena de un final bueno.

- `primerEscenaBadEnding(self)`: Muestra la primera escena de un final malo.

- `segundaEscenaBadEnding(self)`: Muestra la segunda escena de un final malo del juego y configura el juego Buscaminas.

- `clear(self)`: Limpia la ventana de la interfaz gráfica al eliminar todos los elementos en pantalla.

- `reiniciar(self)`: Reinicia el juego a la pantalla de inicio.

- `crear_tablero_buscaminas(self)`: Crea una instancia del juego Buscaminas y configura el tablero.

- `configurar_tablero_buscaminas(self)`: Configura la interfaz gráfica del juego Buscaminas.

- `terceraEscenaBadEnding(self)`: Muestra la tercera escena de un final malo.

- `reiniciar_juego(self)`: Reinicia el juego después de perder o ganar.

- `start(self)`: Inicia la ventana del juego Buscaminas.

- `primeraEscenaLoveEnding(self)`: Muestra la primera escena de un final amoroso.

- `segundaEscenaLoveEnding(self)`: Muestra la segunda escena de un final amoroso.

- `terceraEscenaLoveEnding(self)`: Muestra la tercera escena de un final amoroso.

- `escenaBadLoveEnding(self)`: Muestra el final malo de la ruta amorosa.

- `cuartaEscenaLoveEnding(self)`: Muestra la cuarta escena de un final amoroso.

### Clase `Buscaminas` (Buscaminas.py)

La clase `Buscaminas` contiene la lógica del juego Buscaminas. A continuación, se describen sus funciones:

- `__init__(self, filas, columnas, num_minas)`: Constructor de la clase. Inicializa el juego con el número de filas, columnas y minas especificadas.

- `colocar_minas(self)`: Coloca minas en el tablero de juego de manera aleatoria.

  - **Comportamiento**:

    - Inicia un bucle que se ejecutará un número de veces igual a la cantidad de minas que deben colocarse.
    - Genera aleatoriamente una fila y columna dentro de los límites del tablero.
    - Verifica si la casilla generada ya contiene una mina. Si es así, se vuelve a generar una ubicación aleatoria.
    - Coloca una mina en la casilla asignando el valor `-1` en el tablero, donde `-1` representa la presencia de una mina.

- `inicializar_tablero(self)`: Inicializa el tablero del juego Buscaminas y calcula los números de minas adyacentes a cada casilla.

  - **Comportamiento**:

    - Llama a la función `colocar_minas()` para distribuir minas en el tablero de forma aleatoria.
    - Recorre cada casilla en el tablero y establece los siguientes valores:
      - Si la casilla no contiene una mina (su valor no es `-1`), se establece su valor en el tablero a `0`. Esto indica que no hay minas adyacentes.
    - Todas las casillas se marcan como "cubiertas" al establecer `True` en la matriz `self.cubiertas`. Esto significa que todas las casillas están ocultas al comienzo del juego.

- `contar_minas_cercanas(self, fila, columna)`: Cuenta el número de minas adyacentes a una casilla dada.

  - **Parámetros**:

    - `self`: La instancia actual de la clase `Buscaminas`.
    - `fila`: La fila de la casilla para la que se desea contar las minas adyacentes.
    - `columna`: La columna de la casilla para la que se desea contar las minas adyacentes.

  - **Comportamiento**:
    - Inicializa una variable `minas_cercanas` a 0 para llevar un conteo de las minas cercanas.
    - Utiliza dos bucles anidados para explorar las casillas adyacentes a la casilla especificada. Esto se hace iterando en `i` y `j` en un rango que va desde -1 hasta 1. Esto permite explorar las 8 casillas alrededor de la casilla central.
    - Verifica si las casillas adyacentes son válidas (dentro de los límites del tablero) y si contienen una mina (su valor es `-1`). Si se cumple ambas condiciones, incrementa `minas_cercanas` en 1 para contar la mina adyacente.
    - Devuelve el valor de `minas_cercanas`, que representa la cantidad de minas adyacentes a la casilla dada.

- `explore_casillas_adyacentes(self, fila, columna)`: Explora las casillas adyacentes a una casilla sin minas y descubre casillas vacías.

  - **Parámetros**:

    - `self`: La instancia actual de la clase `Buscaminas`.
    - `fila`: La fila de la casilla que se desea explorar.
    - `columna`: La columna de la casilla que se desea explorar.

  - **Comportamiento**:
    - Utiliza dos bucles anidados para recorrer las casillas adyacentes a la casilla especificada. Esto se hace iterando en `i` y `j` en un rango que va desde -1 hasta 1, lo que permite explorar las 8 casillas alrededor de la casilla central.
    - Verifica si las casillas adyacentes son válidas (dentro de los límites del tablero).
    - Si la casilla adyacente no contiene una mina (su valor no es `-1`), establece su valor en el tablero como `0`. Esto indica que la casilla está vacía y no tiene minas adyacentes.
    - Marca la casilla como "descubierta" al establecer `False` en la matriz `self.cubiertas`. Esto permite mostrar la casilla abierta en la interfaz del juego.

### Clase `BuscaminasUI` (BuscaminasUI.py)

La clase `BuscaminasUI` se encarga de gestionar la interfaz de usuario del juego Buscaminas. A continuación, se describen sus funciones:

- `__init__(self, root, buscaminas, app_instance)`: Constructor de la clase. Inicializa la interfaz de usuario para el juego Buscaminas y la asocia con la ventana principal de la aplicación.

- `configurar_interfaz(self)`: Configura los botones que representan las casillas en el tablero del juego.

  - **Comportamiento**:
    - Itera a través de cada fila y columna en el tablero del juego Buscaminas.
    - Crea un botón de interfaz de usuario (`tk.Button`) para cada casilla en el tablero.
    - Configura el botón con las siguientes propiedades:
      - `text`: Establece el texto en el botón como un espacio en blanco, lo que indica que la casilla está oculta.
      - `width`: Establece el ancho del botón en 2 caracteres.
      - `height`: Establece la altura del botón en 1 caracter.
      - `command`: Asocia una función de manejo de clic (`self.clic_en_casilla(f, c)`) que se ejecutará cuando el jugador interactúe con el botón. Esto permite al jugador revelar o marcar casillas al hacer clic en ellas.
    - Coloca los botones en la interfaz gráfica usando la función `grid` de Tkinter, que los organiza en filas y columnas dentro de un marco (`frame`).

- `clic_en_casilla(self, fila, columna)`: Maneja la acción de hacer clic en una casilla en el juego Buscaminas.

  - **Parámetros**:

    - `self`: La instancia actual de la clase `BuscaminasUI`.
    - `fila`: La fila de la casilla en la que el jugador ha hecho clic.
    - `columna`: La columna de la casilla en la que el jugador ha hecho clic.

  - **Comportamiento**:
    - Verifica el contenido de la casilla en el tablero del juego (`self.buscaminas.tablero`) en la posición especificada por `(fila, columna)`:
      - Si la casilla contiene una mina (su valor es `-1`), se llama a la función `mostrar_minas_al_perder()` para finalizar el juego, mostrando todas las minas y finalizando la partida.
      - Si la casilla no contiene una mina, se realiza lo siguiente:
        - Se marca la casilla como "descubierta" al establecer `False` en la matriz `self.buscaminas.cubiertas`. Esto revela la casilla en el tablero.
        - Se deshabilita el botón correspondiente a la casilla al establecer su estado como "disabled". Esto evita que el jugador haga clic nuevamente en esa casilla.
        - Se cuenta el número de minas adyacentes a la casilla con la función `contar_minas_cercanas(fila, columna)` y se almacena en la variable `minas_cercanas`.
        - Si no hay minas cercanas (`minas_cercanas` es igual a 0), se exploran las casillas adyacentes a la casilla actual usando la función `explore_casillas_adyacentes(fila, columna)`.
        - Si hay minas cercanas (`minas_cercanas` es mayor que 0), se muestra el número de minas cercanas en la casilla al establecer el texto del botón.

- `descubrir_casilla(self, fila, columna)`: Deshabilita un botón de casilla.

  - **Parámetros**:

    - `self`: La instancia actual de la clase `BuscaminasUI`.
    - `fila`: La fila de la casilla que se desea marcar como "descubierta".
    - `columna`: La columna de la casilla que se desea marcar como "descubierta".

  - **Comportamiento**:
    - Accede al botón correspondiente a la casilla especificada en la matriz de botones `self.botones` utilizando las coordenadas `(fila, columna)`.
    - Establece el estado del botón como "disabled". Esto significa que el jugador no puede hacer clic nuevamente en esa casilla, lo que indica que la casilla ya ha sido revelada.

- `mostrar_minas_al_perder(self)`: Muestra las minas y termina el juego al perder en el juego Buscaminas.

  - **Parámetros**:

    - `self`: La instancia actual de la clase `BuscaminasUI`.

  - **Comportamiento**:
    - Itera a través de todas las casillas en el tablero del juego Buscaminas.
    - Si una casilla contiene una mina (su valor es `-1`), se actualiza el texto del botón correspondiente con el emoji "💥", que representa una mina explotada.
    - A continuación, deshabilita todos los botones en el tablero al establecer su estado como "disabled". Esto evita que el jugador interactúe con las casillas una vez que el juego ha terminado.
    - Finalmente, activa la tercera escena del juego llamando a la función `terceraEscenaBadEnding()` de la aplicación (`self.app`), que indica un resultado negativo en el juego.

- `reiniciar_juego(self)`: Reinicia el juego después de perder o ganar en el juego Buscaminas.

  - **Comportamiento**:
    - Limpia el tablero actual del juego Buscaminas al realizar las siguientes acciones:
      - Coloca las minas nuevamente en el tablero mediante la función `colocar_minas()` del objeto Buscaminas (`self.buscaminas`).
      - Inicializa el tablero del juego llamando a la función `inicializar_tablero()` del objeto Buscaminas (`self.buscaminas`).
    - Limpia la interfaz gráfica al eliminar todos los botones que representan las casillas del juego. Esto se hace mediante un bucle que recorre todos los botones en la matriz `self.botones`.
    - Limpia la lista de botones `self.botones`.
    - Configura nuevamente la interfaz del juego mediante la función `configurar_interfaz()` para que el jugador pueda comenzar una nueva partida.
    - Actualiza la ventana principal (`self.root`) para que refleje los cambios en la interfaz.
    - Inicia el juego nuevamente llamando a la función `start()` para que el jugador pueda interactuar con el tablero y jugar.

- `start(self)`: Inicia la ventana del juego Buscaminas.

## Uso

Para jugar al Buscaminas, navegá en la terminal hasta la carpeta programa con el comando `cd programa` y ejecutra el comando `python App.py`. ¡Divertite jugando!
