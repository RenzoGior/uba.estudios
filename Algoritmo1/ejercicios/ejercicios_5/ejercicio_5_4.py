# Utilizando la función randrange del módulo random, escribir un programa que
# obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
# si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
# correcto.
import random

def numero_aleatorio_secreto(k):
    aleatorio = random.randrange(1,10)
    while aleatorio != k:
        if aleatorio > k:
            print("el numero es mayor, siga adivinando: ")
        else:
            print("el numero es menor, siga adivinando: ")
        k = int(input("ingrese un numero entre 1 y 10: "))
    print("ganaste")

def main(): 
    numero_aleatorio_secreto(int(input("ingrese un numero entre 1 y 10: ")))
main()




