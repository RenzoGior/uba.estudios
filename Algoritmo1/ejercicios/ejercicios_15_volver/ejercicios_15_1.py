# Escribir una función recursiva que reciba un número positivo n y devuelva la
# cantidad de dígitos que tiene.

def contar_digitos(n):
    # Caso base: si n es menor que 10, tiene un solo dígito
    if n < 10:
        return 1
    else:
        # Llamada recursiva dividiendo el número por 10
        return 1 + contar_digitos(n // 10)
    

print(contar_digitos(100000))
