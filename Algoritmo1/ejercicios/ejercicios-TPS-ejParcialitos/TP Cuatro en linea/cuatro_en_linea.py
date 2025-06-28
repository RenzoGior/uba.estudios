# Se busca realizar una implementación del 4 en línea que se pueda jugar de a dos jugadores humanos, desde la terminal,
# permitiendo tableros de cualquier dimensión NxM, con N y M mayores o iguales a cuatro y menores a diez.

from typing import List


def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """
    # n_columnas > 3
    # n_filas > 3
    tablero = []
    for filas in range(n_filas):
        fila_nueva = []
        for columnas in range(n_columnas):
            fila_nueva.append(" ")
            # lleno la fila con lo que corresponde
        tablero.append(fila_nueva)
        # agrego la fila a la matriz
    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    suma = 0
    cantidad_de_filas = len(tablero) 
    cantidad_de_columnas = len(tablero[0])
    for fila in range(cantidad_de_filas):
        for columna in range(cantidad_de_columnas):
            if tablero[fila][columna] == "X" or tablero[fila][columna] == "O":
                suma += 1
    return suma % 2 == 0




def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """
    # len de tablero [::-1] recoriendo el tablero para atras
    cantidad_de_columnas = len(tablero) - 1
    # cantidad_de_filas = len(tablero[0])
    for i in range(-1, -cantidad_de_columnas,-1):
        # for j in cantidad_de_filas:
            if es_turno_de_x :
                tablero[i].pop(columna)
                tablero[i].insert(columna, "X")
                return es_turno_de_x(tablero)   
            else:
                tablero[i].pop(columna)
                tablero[i].insert(columna, "O")
                return es_turno_de_x(tablero)   
            




def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """


def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O', 'O', 'X', 'X', 'X', 'O'],
        ]
    """