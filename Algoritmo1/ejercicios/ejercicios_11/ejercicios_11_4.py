# Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
# las líneas del archivo que contienen la cadena recibida.

def grep (s: str, file) -> None:
    with open(file) as archivo:
        for i in archivo:
            if s in i:
                print(i, end="")

def main():
    cadena = "hola"
    archivo = "hola.txt"
    grep(cadena,archivo)

main()