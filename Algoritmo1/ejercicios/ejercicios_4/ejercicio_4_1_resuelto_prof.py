# Ejercicio 4.1. Escribir dos funciones que resuelvan los siguientes problemas:
# a) Dado un número entero n, indicar si es par o no.
# b) Dado un número entero n, indicar si es primo o no.

def es_par(n: int) -> bool:
    return n % 2 == 0


def es_par2(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False


print(es_par(2))
print(es_par(3))

"b)"

def es_primo(n: int) -> bool:
    for i in range(2, n):  # es mejor por que el algoritmo no divide todos los numeros, va hasta la mitad (2, (n // 2) + 1)   1,2,4,5,10 20 divisores
        if n % i == 0:                                                                                              #   1, 2, 5, 10     
            return False
    return True    


print(es_primo(7))