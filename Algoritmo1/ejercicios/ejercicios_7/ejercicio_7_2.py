# Dominó.
# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

def domino_encanjan(t: tuple, t2: tuple) -> bool:
    return t[0] == t2[0] or t[1] == t2[0] or t[0] == t2[1] or t[1] == t2[1]


t = (3, 4)
t2 = (5, 4)
t3 = (0, 1)
t4 = (4, 2)

assert domino_encanjan(t , t2) == True
assert domino_encanjan(t3 , t4) == False
assert domino_encanjan(t , t4) == True
print('ok')

# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
# cadenas.

def domino_encajan_cadena(s: str, s2: str) -> bool:
    l = s.split("-")
    l2 = s2.split("-")
    return domino_encanjan(l, l2)
    


s = "3-4" 
s2 = "2-5"

def main():
    print(domino_encajan_cadena(s, s2))

main()