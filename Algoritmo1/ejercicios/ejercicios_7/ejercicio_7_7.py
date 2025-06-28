# Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
# cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
# nombre, luego la inicial con un punto, y luego el apellido.
def nombres_completos(L: list) -> list:

    
    Lista_ordenada = []
    for i in range(len(L[0])):
        apellido, nombre, inicial_segundo_nombre = L
        Lista_ordenada.append(nombre[i])
        Lista_ordenada.append(inicial_segundo_nombre[i] + ".")
        Lista_ordenada.append(apellido[i])
        " ".join(Lista_ordenada)
    return Lista_ordenada


def main():
    apellidos = ("Giordanino", "Sanchez", "Muñoz")
    nombre = ("Renzo", "Lana", "Santiago")
    inicial_segundo_nombre = ("J", "F", "G")
    l_de_t = [(apellidos), (nombre), (inicial_segundo_nombre)]
    print(nombres_completos(l_de_t))

main()