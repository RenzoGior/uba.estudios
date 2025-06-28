# Ejercicio 7.9. Escribir una función empaquetar para una lista, donde epaquetar significa indicar
# la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
# ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
# , (1, 2), (3, 2)].

def empaquetar(L: list) -> tuple:
        
    empaquetado = []
    valor_actual = L[0]
    cantidad = 1

    for i in range(1, len(L)):
        if L[i] == valor_actual:
            cantidad += 1
        else:
            empaquetado.append((valor_actual, cantidad))
            valor_actual = L[i]
            cantidad = 1

    empaquetado.append((valor_actual, cantidad))
    return empaquetado




def main(): 
    print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))
main()