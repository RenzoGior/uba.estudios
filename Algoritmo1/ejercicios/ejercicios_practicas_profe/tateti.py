"""
diseño

- quien juega primero? se puede elegir?|

 

presentacién (interacctén con el usuario):
- como interactuo con el juego?
    pedir_movimiento() -> coordenada x, coordenada y ,
    preguntar_juego_nuevo( )

- como se va a ver?
    nostrar_tablero(tablero) - muestra por terminal la partida

Logica:
- tablero? como lo represento?
    - matriz de 3x3
    - poner_x(coordenada x, coordenada y) / hay_x
    - poner_o(coordenada x, coordenada y) / hay_o
    - esta_vacia(coordenada x, coordenada y)
    - crear_tablero() -> matriz? representacion?

-como se si alguien gano?
    - buscar_ganador(tablero) -> "X", "O", " "


- turnos? como cambio de turno?
    - x= 0, pares, o = 1, impares
    - el turno es parte del estado del juego

- estado del juego: turno y el tablero

- como represento un juego tateti / una partida de tateti:
    - el tablero lo represento como matriz, y el turno lo obtengo
    contando cuantas fichas hay en el tablero - si es par, le toca a
    X, si es impar, le toca O
    - tupla (turno, tablero) -- turno es un entero y tablero es una
    matriz de 3x3

    - crear_juego() -> "juego de tateti"

def crear_juego():
    return (0, [" " * 3] * 3)

def poner_fichar(juego, fila, columna):
    turno, tablero = juego
    if turno % 2 == 0:
        tablero[fila][columna] = "X"
    else:
        tablero[fila][columna] = "0"
    
    return [turno + 1, tablero]

"""