#Escribir un programa que tome una cantidad m de valores ingresados por el usuario
# a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
# resolvio de otra forma


def factorial(n) -> int:
    resultado = 1
    for i in range(1, n+1):  #(2, n+1)
        resultado = resultado * i
    return resultado

def main ():
    cantidad = int(input("ingrese cantidad de numeros: "))
    for i in range(1, cantidad + 1):
        numero = int(input("ingrese un numero: "))
        resultado = factorial(numero)
        print ("{}! = {}".format(numero, resultado))

main()