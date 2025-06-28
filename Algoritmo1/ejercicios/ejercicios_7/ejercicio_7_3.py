# Campaña electoral
# a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
# el mensaje Estimado <nombre>, vote por mí.
def vota_por_mi (t: tuple) -> None:
    for i in t:
        print(f"Estimado/a {i}, vote por mi")

tupla = ("Ricardo", "Jaimito", "Matias", "Arjona", "Estefania", "Barbara" )

# b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
# cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
# de la posición p.

def vota_por (t: tuple, p: int, n: int) -> None:
    cont = 1
    for i in range(p, len(t)):
        if cont <= n:
            print(f"Estimado/a {t[i]}, vote por mi")
        cont += 1

# c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
# para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

def vota_genero(t: tuple, p: int, n: int) -> None:
    cont = 1
    for i in range(p, len(t)):
        if cont <= n:
            if t[i][1] == "masculino":
                print(f"Estimado {t[i][0]}, vote por mi")
            else:
                print(f"Estimada {t[i][0]}, vote por mi")
        cont += 1

t = (("Ricardo", "masculino"), ("Jaimito", "masculino"), ("Matias", "masculino"), ("Arjona", "masculino"), ("Estefania","femenina"), ("Barbara", "femenina"))

def main():
    #vota_por_mi(tupla)
    #vota_por(tupla, 0, 4)
    vota_genero(t, 2, 6)

main()