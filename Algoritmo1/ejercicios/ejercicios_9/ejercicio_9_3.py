# Continuación de la agenda.
# Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
# el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena ”*”, para salir del programa.

def leer_centinela() -> str:
    return input("Ingrese el nombre  (* para terminar): ")

def agregar_numero() -> int:
    return int(input("Ingrese el numero "))


def main() -> str:
    agenda = {
        "Juan": "123456789",
        "María": "987654321",
        "Pedro": "555555555"
    }
    nombre = leer_centinela()
    while nombre != "*" :
        if nombre in agenda:
            print(f"{nombre} se encuentra en la agenda y su numero es {agenda[nombre]} ")
        else:
            print(f"{nombre} agrege su numero ")
            agenda[nombre] = agregar_numero()
        nombre = leer_centinela()

main()