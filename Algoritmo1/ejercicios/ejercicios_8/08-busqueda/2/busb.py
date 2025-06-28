from passwords import passwords

def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        print(f"{medio:>5} {lista[medio]}")
        if lista[medio] == x:
            return medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1

p = 'python'
i = busqueda_binaria(passwords, p)

print(f"'{p}' está en la posición {i}")
