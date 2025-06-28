# Se cuenta con un sistema de versionado de software que identifica a cada versión con tres números mayores o iguales a cero, 
# (x, y, z) de la forma x.y.z. A mayor valor de x, más reciente es la versión.
# En caso de igualdad en x, el mayor valor de y determina la más reciente y, si el valor de y también coincide, el valor a considerar es el z.
# Se pide realizar una función que, dadas dos versiones representadas como cadenas de caracteres devuelva 1 
# si la primera versión recibida es mayor, 0 si son iguales y -1 si la segunda es mayor. Ejemplo:

# >>> comparar_versiones(“0.1.1”, “1.0.4”)
# -1
# >>> comparar_versiones(“1.10.4”, “1.2.4”)
# 1
# >>> comparar_versiones(“1.1.4”, “1.1.4”)
# 0

def comparar_versiones(programa1: str, programa2: str) -> int:
    return




comparar_versiones("0.1.1", "1.0.4")
comparar_versiones("1.10.4", "1.2.4")
comparar_versiones("1.1.4", "1.1.4")