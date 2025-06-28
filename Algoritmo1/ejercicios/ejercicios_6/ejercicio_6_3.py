# Modificar las funciones anteriores, para que reciban un parámetro que indique la
# cantidad máxima de reemplazos o inserciones a realizar.


# EARLY RETURN MEJORAR LOS IF EN FORMA DE FLECHA

# def separar_c (s: str, n: int) -> str:
#     contador = 0
#     cadena = ""
#     if contador < n:
#         cadena += s[::2]
#         contador += 1


def remplazar_espacios(s: str, n: int) -> str:
    espacio = " "
    cadena = ""
    contador = 0
    for i in s:
        if espacio == i and contador < n:
            cadena += "_"
            contador += 1
        else:
            cadena += i
        
    return cadena
    #return s[0:2] + "_" + s[3:10] + "_" + s[11:13] + "_" + s[14:]


def digitos_s(s: str, num: int) -> str:
    n = ("1","2","3","4","5","6","7","8","9","0")
    cadena = ""
    contador = 0
    for i in s:
        if i in n and contador < num:
            cadena += "X"
            contador += 1
        else:
            cadena += i
    return cadena

def insertar_caracter_3 (s: str, n: int) -> str:
    cadena = ""
    numero = 0
    contador = 0
    for i in s:
        numero += 1
        if numero % 3 == 0 and contador < n:
            cadena += i
            cadena += "."
            contador += 1
        else:
            cadena += i
    return cadena




   



def main():
    # separar_c('s,e,p,a,r,a,r', )
    print(remplazar_espacios("mi archivo  aca de esto de texto.txt", 5))
    print(digitos_s('su clave es: 1540', 2))
    print(insertar_caracter_3('2552552550', 1))

main()