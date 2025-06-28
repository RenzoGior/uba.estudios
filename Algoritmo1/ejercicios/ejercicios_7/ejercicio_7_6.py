# Dada una lista de números enteros y un entero k, escribir una función que:
# a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
# k.
def num_enteros_k(L: list, k: int) -> list:
    menores = []
    mayores = []
    iguales = []
    for numero in L:
        if numero < k:
            menores.append(numero)
        elif numero > k:
            mayores.append(numero)
        else:
            iguales.append(numero)
    return menores, mayores, iguales




def main():
    L = [1, 2, 4, 42, 6, 24, 67, 23, 52, 2, 222, 2]
    print(num_enteros_k(L, 2))

main()