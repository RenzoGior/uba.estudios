# Escribir una función que reciba por parámetro una dimensión n, e imprima la
# matriz identidad correspondiente a esa dimensión.


def matriz (n: int, e: int) -> None:
    for filas in range(1, n + 1):
        for columnas in range(1, e + 1):
            if (filas == columnas):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print(" ")
            



def main():
    matriz(5, 5)
 
main()



