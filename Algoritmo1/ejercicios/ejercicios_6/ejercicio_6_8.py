# Ejercicio 6.8. Escribir una función que reciba una cadena de unos y ceros (es decir, un número
# en representación binaria) y devuelva el valor decimal correspondiente.

def binarios_a_decimal(s: str) -> int:
    potencia = 0
    n = 0
    for i in s[::-1]:
        suma = int(i) * (2 ** potencia)
        potencia += 1
        n += suma
    return n


def main():
    binarios_a_decimal("1100011")
main()