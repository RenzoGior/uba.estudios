# Escribir una función que reciba una lista desordenada y un elemento, que:

# a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
# tidad de coincidencias encontradas.

def buscar_coincidencia (L: list, x: int) -> list: 
    cantidad = 0
    for i in L: 
        if x == i: 
            cantidad += 1
    return cantidad

# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
def primera_coincidencia (L: list, x: int) -> list:
    for i in L:
        if x == i:
            return L.index(i)

# c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
# por parámetro y devuelva una lista con las posiciones.
def coincidencias (L: list, x: int) -> list:
    posiciones = []
    for i, j in enumerate(L):
        if x == j:
           posiciones.append(i)
    return posiciones





def main():
    lista_desordenada = [1, 5, 2, 6, 5, 6, 7, 8, 9, 4, 2, 24, 23, 4, 111, 2, 1, 1, 6, 7,]
    elemento = 4
    assert buscar_coincidencia(lista_desordenada, elemento) == 2
    assert primera_coincidencia(lista_desordenada, elemento) == 9
    print(coincidencias(lista_desordenada, elemento))


main()
