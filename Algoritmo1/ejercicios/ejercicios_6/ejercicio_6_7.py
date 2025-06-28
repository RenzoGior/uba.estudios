# Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
# es una subcadena de 'subcadena'.
def subcadena(s: str, subs: str) -> bool: 
    return subs in s or s in subs


assert subcadena('cadena', 'subcadena') == True
assert subcadena('1234', '5678' ) == False

# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
# debe devolver 'gnome'.
def orden_alfabetico(s: str, s2: str) -> str:
    l = [s, s2]
    l.sort()
    return l[0]


def main():
    subcadena('cadena', 'subcadena')
    print(orden_alfabetico('kde', 'gnome'))
main()