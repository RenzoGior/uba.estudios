# Dada una lista de números enteros, escribir una función que:
# a) Devuelva una lista con todos los que sean primos.
def es_primo(n: int) -> bool:
    for i in range(2, n):    
        if n % i == 0:                                                                                                 
            return False
    return True    

def cousins(L: list) -> str:
    primos = []
    for n in L:
        if es_primo(n):
            primos.append(n)
    return f"los numeros primos son {primos}"

# b) Devuelva la sumatoria y el promedio de los valores.
def sum_prom(L: list) -> int:
    suma = 0
    for i, n in enumerate(L):
        suma += n
    return f"la suma es: {suma}, y el promedio: {suma / (i + 1)}"

# c) Devuelva una lista con el factorial de cada uno de esos números.



def main():
    numeros_l = [1, 54, 6, 2, 6, 8, 9, 2, 22, 3, 4, 7]
    print(cousins(numeros_l))
    print(sum_prom(numeros_l))


main()