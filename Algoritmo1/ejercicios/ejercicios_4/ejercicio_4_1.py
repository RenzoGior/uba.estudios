def numero_par(x) -> int:
    "funcion que calcula si un numero es par o inpar"
    if x % 2 == 0:
        print( "el numero es par")
    else:
        print ("el numero es inpar")




def es_primo(num, n=2) -> int:
    "funcion que calcula si un numero es primo"
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False

def main():
    numero_par(555)
    es_primo(85)


main()