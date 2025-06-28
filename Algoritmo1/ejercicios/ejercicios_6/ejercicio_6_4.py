# Escribir una función que reciba una cadena que contiene un largo número en-
# tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe

# '1234567890', debe devolver '1.234.567.890'.

def num_entero(s: str) -> str:
    cadena_dada_vuelta = s[::-1]
    cadena = ""
    contador = 0
    for i in cadena_dada_vuelta:
        contador += 1
        if contador % 3 == 0:
            cadena += i
            cadena += "."
        else:
            cadena += i
    return  cadena[::-1]



def main():
    print(num_entero('123456789023122'))
main()

""" solucion al error, y ahorro de codigo, early return """

def num_entero(s: str) -> str:
    cadena_dada_vuelta = s[::-1]
    cadena = ""
    contador = 0
    for i in cadena_dada_vuelta:
        contador += 1
        cadena += i
        if contador % 3 == 0 and contador != len(s):
            cadena += "."
    return cadena[::-1]

def main():
    print(num_entero('123456789023122'))
main()