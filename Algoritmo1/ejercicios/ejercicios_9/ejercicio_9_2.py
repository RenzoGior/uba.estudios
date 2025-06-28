import random 

# Diccionarios usados para contar.
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

def cadena_a_diccionario(s: str) -> dict:
    diccionario = {}
    cadena_separada = s.split(" ")
    valor = 0
    for palabra in cadena_separada:
        if not palabra in diccionario:
            diccionario[palabra] = valor + 1
        else:
            diccionario[palabra] += 1
    return diccionario

# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
# dena de texto, y los devuelva en un diccionario.

def aparaciones_caracter(s: str) -> dict:
    diccionario = {}
    valor = 0
    for palabra in s:
        if not palabra in diccionario:
            diccionario[palabra] = valor + 1
        else:
            diccionario[palabra] += 1
    return diccionario

# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.

def iteraciones_dados (x: int) -> dict:
    diccionario = {}
    valor = 0
    for i in range(x):
        suma_dados = random.randint(1, 6) + random.randint(1, 6)
        if not suma_dados in diccionario:
            diccionario[suma_dados] = valor + 1
        else:
            diccionario[suma_dados] += 1
    return diccionario

def main():
    cadena = 'que lindo dia que hace hoy que que hoy lindo'
    iteraciones = 10
    print(cadena_a_diccionario(cadena))
    print(aparaciones_caracter(cadena))
    print(iteraciones_dados(iteraciones))


main()
