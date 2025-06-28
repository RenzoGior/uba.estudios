"""
def mil_veces_parlabra (palabra):
    palabra = str(input("ingrese una palabra: "))
    for i in range(1001):
        i += 1 
        print(f"la ", palabra, "se imprimio " {i}, "veces ", end=" ")

mil_veces_parlabra()
"""

"CORRECCION CHATGPT,,"

def imprimir_palabra_multiples_veces(palabra, repeticiones):
    for i in range(repeticiones):
        print(palabra, end=" ")

# Solicitar la palabra al usuario
palabra_usuario = input("Ingresa una palabra: ")

# Imprimir la palabra 1000 veces en una única línea con espacios intermedios
imprimir_palabra_multiples_veces(palabra_usuario, 1000)