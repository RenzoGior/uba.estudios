# Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
# en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
# segundos.

def listadetuplas_a_diccionario(L: list[tuple]) -> dict :
    diccionario = {} 
    for key, value in L:
        if not key in diccionario:
            diccionario[key] = [value]
        else:
            diccionario[key] += [value]
    return diccionario


def main():
    lista_de_tuplas = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
    print(listadetuplas_a_diccionario(lista_de_tuplas))
    
main()