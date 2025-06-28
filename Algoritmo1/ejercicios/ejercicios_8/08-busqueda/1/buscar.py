def buscar(secuencia, elemento):
    """
    Devuelve el índice del elemento en la secuencia,
    o -1 si no está.
    """
    for i, elem in enumerate(secuencia):
        if elem == elemento:
            return i
    return -1


assert buscar([1, 3, 5], 3) == 1
assert buscar([1, 3, 5], 4) == -1
