# Escribir una función que reciba una lista de números no ordenada, que:
# a) Devuelva el valor máximo.
def valor_maximo(L: list) -> int:
    valor = 0
    for i in L:
        if i >= valor :
            valor = i
    return valor

# b) Devuelva una tupla que incluya el valor máximo y su posición.
def tupla_maximo(L: list) -> int:
    valor = 0
    indice = 0
    for i in L:
        if i >= valor :
            valor = i
            indice = L.index(i)
    return (indice, valor)



def main(): 
    lista_desordenada = [1, 5, 2, 6, 5, 6, 7, 8, 9, 4, 222, 24, 23, 4, 111, 2, 1, 1, 6, 7]
    valor_maximo(lista_desordenada)
    tupla_maximo(lista_desordenada)

main()
