# Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
# imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc() -> None :
    
    
    with open("hola.txt") as archivo:
        contador_palabra = 0
        contador_caracter = 0
        for contador_lineas, linea in enumerate(archivo):
            palabra = linea.split(" ")
            for cantidad in palabra:
                contador_palabra += 1
            for caracter in linea:
                contador_caracter += 1
        contador_lineas += 1
        """ ejemplo chatgpt pero no funciona"""
        # contenido = archivo.read()
        # lineas = contenido.count('\n') + 1  # Contar líneas
        # palabras = len(contenido.split())   # Contar palabras
        # caracteres = len(contenido)         # Contar caracteres

        # print(f"Líneas: {lineas}")
        # print(f"Palabras: {palabras}")
        # print(f"Caracteres: {caracteres}")
        """tampoco funciona el otro ejemplo, pero buena solucion usar la funcion len"""
        # lineas = 0
        # palabras = 0
        # caracteres = 0

        # for linea in archivo:
        #         lineas += 1
        #         palabras += len(linea.split())
        #         caracteres += len(linea)
        # print(f"Líneas: {lineas}")
        # print(f"Palabras: {palabras}")
        # print(f"Caracteres: {caracteres}")
        print(f"el archivo tiene: {contador_lineas} lineas, {contador_palabra} palabras y {contador_caracter} caracteres")

wc()