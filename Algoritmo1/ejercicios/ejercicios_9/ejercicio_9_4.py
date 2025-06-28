# Escribir una función que reciba un texto y para cada caracter presente en el texto
# devuelva la cadena más larga en la que se encuentra ese caracter.

def cadena_mas_larga(s: str):
    apariciones = {}
    palabras = s.split()
    
    for palabra in palabras:
            for caracter in palabra:
                return
    return s 

    """resolver con len"""
   

def main():
    texto_ejemplo = "esto es un ejemplo de texto"
    x = cadena_mas_larga(texto_ejemplo)
    print(x)

main()