# Escribir funciones que dada una cadena y un caracter:

# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'
def separar_c (s: str) -> str:
    return s[::2]

# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'
def remplazar_espacios(s: str) -> str:
    espacio = " "
    cadena = ""
    for i in s:
        if espacio == i:
            cadena += "_"
        else:
            cadena += i
    return cadena
    #return s[0:2] + "_" + s[3:10] + "_" + s[11:13] + "_" + s[14:]

# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'
def digitos_s(s: str) -> str:
    n = ("1","2","3","4","5","6","7","8","9","0")
    cadena = ""
    for i in s:
        if i in n:
            cadena += "X"
        else:
            cadena += i
    return cadena

# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'       
def insertar_caracter_3 (s: str) -> str:
    cadena = ""
    contador = 0
    for i in s:
        contador += 1
        if contador % 3 == 0:
            cadena += i
            cadena += "."
        else:
            cadena += i
    return cadena




   



def main():
    separar_c('s,e,p,a,r,a,r')
    remplazar_espacios("mi archivo  aca de esto de texto.txt")
    digitos_s('su clave es: 1540')
    insertar_caracter_3('2552552550')

main()