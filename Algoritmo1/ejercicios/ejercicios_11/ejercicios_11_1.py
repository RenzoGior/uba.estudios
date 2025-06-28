# Escribir una función, llamada head que reciba un archivo y un número N e im-
# prima las primeras N líneas del archivo.

def head (x: int) -> None :
    with open("hola.txt") as archivo:
        contador = 0
        while contador < x:
            print(archivo.readline(), end="")
            contador += 1

head(4)