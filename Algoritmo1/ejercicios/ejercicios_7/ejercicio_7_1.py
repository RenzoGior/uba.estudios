# Escribir una función que reciba una tupla de elementos e indique si se encuentran
# ordenados de menor a mayor o no.

def mayor_a_menor(t: tuple) -> bool:
    return sorted(t) == t


t = (2, 4, 1, 7, 2,)
t2 = sorted(t)

assert mayor_a_menor(t) == False
assert mayor_a_menor(t2) == True
print("ok")