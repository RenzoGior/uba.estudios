# Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
# Escribir funciones que dada una cadena de caracteres:

# a) Imprima los dos primeros caracteres.
def imprime_perimeros2_c (s: str) -> None:
    print(s[0:2])

# b) Imprima los tres últimos caracteres.
def imprime_2ultimos_c(s: str) -> None:
    print(s[8:])

# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
def c_2_en_2(s: str) -> None:
    print(s[::2])

# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
def c_sentido_inverso(s: str) -> None:
    print(s[::-1])

# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
# 'reflejoojelfer'.
def c_sentido_sentidoinverso(s: str) -> None:
    print(s + s[::-1])



def main():
    imprime_perimeros2_c("caracteres")
    imprime_2ultimos_c("caracteres")
    c_2_en_2("recta")
    c_sentido_inverso('hola mundo!')
    c_sentido_sentidoinverso('reflejo')


main()