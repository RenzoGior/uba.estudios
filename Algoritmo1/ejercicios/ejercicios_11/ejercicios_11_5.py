# Escribir una función, llamada rot13, que reciba un archivo de texto de origen
# y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
# en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
# prendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
# caracter.

def rot13(origen, destino) :
    """ejemplo de como usar rot 13 en python"""
    # rot13 = str.maketrans(
    #     'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    #     'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    # 'Hello World!'.translate(rot13)

    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    'Hello World!'.translate(rot13)

    with open(origen) as archivo:
        cifrar = archivo.read()
        codificar = cifrar.translate(rot13)

    with open(destino, "w") as cifrado:
        cifrado.write(codificar)
    



def main():
    origen = "origen.txt"
    destino = "cifrado.txt"
    rot13(origen, destino)


main()