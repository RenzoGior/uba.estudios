# Ejercicio 7.8. Inversión de listas
# a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
# igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
# deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

def lista_invertida (L: list) -> list:
    return L[::-1]



def main():
    print(lista_invertida(['Di', 'buen', 'día', 'a', 'papa']))


main()