# Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
# se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
# no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.

def busqueda_binaria (L: list, s: str) :
    izq = 0
    der = len(L) - 1
    while izq <= der:
        medio = (izq + der) // 2
        print(f"{medio:>5} {L[medio]}")
        if L[medio] == s:
            return medio
        if L[medio] > s:
            der = medio - 1
        else:
            izq = medio + 1
    L.insert(izq, s)
    return izq


  
   



def main():
    elemento = 4
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18]
    print(busqueda_binaria(lista_ordenada, elemento))    
    



main()