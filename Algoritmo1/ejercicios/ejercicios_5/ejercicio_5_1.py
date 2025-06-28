# Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-
# guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.


def leer_centinela() -> int:
    return int(input("Ingrese una nota (* para terminar): "))


def main() -> str:
    suma_nota = 0
    nota = leer_centinela()
    promedio = 1
    while nota != "*" :
        if nota <= 10:
            suma_nota = suma_nota + nota
            promedio_notas = suma_nota / promedio
            print(f"el promedio de las notas es: {promedio_notas} ")
            promedio += 1
        else:
            print("ingrese una nota valida")
        nota = leer_centinela()

main()