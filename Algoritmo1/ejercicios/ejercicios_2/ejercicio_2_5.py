def es_par(n):
    "funcion que verifica si un numero es par o inpar, si el resultado del numero dividido es 0 es par,(True) inpar(false)"
    return n % 2 == 0

es_par(11)

def es_par_inpar(m):
    "funcion que dado un numero m devuelve si es inpar es igual = 0, y si es par = 1"
    if m % 2 == 0:
        return 1
    else:
        return 0
es_par_inpar(5)

def digito_de_numero(digito):
    "funcion que dado un número entero devuelva el dígito de las unidades."
    return digito % 10

digito_de_numero(253)

def numero_multiplo_10(multiplo_10):
    "Escribir una función que dado un número devuelva el primer número múltiplo de 10 inferior a el"
    return multiplo_10 - digito_de_numero(multiplo_10)

numero_multiplo_10(153)

"""si hace falta probar con print, para testear"""