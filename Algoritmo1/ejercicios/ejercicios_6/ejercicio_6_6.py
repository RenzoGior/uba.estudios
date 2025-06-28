# Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms'.
def letras_consonate(s: str) -> str:
    vocales = ("a", "e", "i", "o", "u")
    s2 = ""
    for i in s:
        if not i in vocales:
            s2 += i
    return s2

# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.
def letras_vocales(s: str) -> str:
    vocales = ("a", "e", "i", "o", "u", " ")
    s2 = ""
    for i in s:
        if i in vocales:
            s2 += i
    return s2

# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.
def remplazar_vocal_siguiente(s: str) -> str: 
    vocal_siguiente = ""
    for i in s:
        if i == "a" or i == "A":
            vocal_siguiente += "e"
        elif i == "e" or i == "E":
            vocal_siguiente += "i"
        elif i == "i" or i == "I":
            vocal_siguiente += "o"
        elif i == "o" or i == "O":
            vocal_siguiente += "u"
        elif i == "u" or i == "U":
            vocal_siguiente += "a"
        else:
            vocal_siguiente += i
    return vocal_siguiente


# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
# líndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def palidromo(s: str) -> str:
    sin_espacios = ""
    sin_espacios_al_revez = ""
    for i in s:
        if i != " ":
            sin_espacios += i
    for it in s[::-1]:
        if it != " ":
            sin_espacios_al_revez += it
    return sin_espacios == sin_espacios_al_revez 

assert palidromo('anita lava la tina') == True
assert palidromo('esto no es un palidromo') == False
assert palidromo('arriba la birra') == True



def main():
    print(letras_consonate('algoritmos'))
    print(letras_vocales('sin consonantes'))
    palidromo('anita lava la tina')
    print(remplazar_vocal_siguiente('vestuario'))


main()