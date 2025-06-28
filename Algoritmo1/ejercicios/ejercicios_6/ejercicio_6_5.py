# Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
# devolver 'USB'.


def cadena_palabra(s: str) -> str:
    primera_letra = ""
    for i in s:
        if not i == i.lower():
            primera_letra += i
    return primera_letra

# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
# 'república argentina' debe devolver 'República Argentina'.

def primera_palabra_mayus(s: str) -> str:
    #usando la funcion title de python
    return s.title()

# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'

# def palabra_A (s: str) -> str:
#     palabras = s.split()  # Dividir la cadena en palabras
#     cadena_resultante = ""
#     for i in palabras:
#         i.upper()
#         if i.startswith("A"):
#             cadena_resultante += i
#     return cadena_resultante
	

def palabra_A2(s: str) -> str:
    l = s.split()
    palabras_con_a = ""
    # Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
    for palabra in l:
        if palabra.startswith("a") or palabra.startswith("A"):
            palabras_con_a += palabra + " "
    return palabras_con_a


def main():
    print(cadena_palabra('Universal Serial Bus'))
    print(primera_palabra_mayus('república argentina '))
    print(palabra_A2("Antes de ayer"))
 

main()