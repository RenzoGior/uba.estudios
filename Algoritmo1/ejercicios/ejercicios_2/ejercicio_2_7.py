
def triangular_formula(n):
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        print(f"{i} - {triangular_number}")


triangular_formula(5)


def triangular(n):
    triangular_number = 0
    for i in range(1, n + 1):
        triangular_number += i
        print(f"{i} - {triangular_number}")

n = int(input("Ingrese un número n: "))
triangular(n)

"""
la funcion que utiliza la ecuación realiza un cálculo único para obtener cada número triangular
esta funcion realiza menos operaciones.

En cambio, la funcion que utiliza el bucle debe realizar sumas repetidas en cada iteración del bucle, y la cantidad de sumas aumenta con el valor de n.

"""