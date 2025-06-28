# Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
# de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def cp ():
    with open("hola.txt") as archivo:
        copiado = archivo.read()

    with open("vacio.txt", "w") as archivo_copia:
        archivo_copia.write(copiado)

cp()