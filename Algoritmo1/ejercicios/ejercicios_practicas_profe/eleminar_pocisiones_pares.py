
def eliminar_posiciones_pares(L: list) -> None:
    """
    Elimina de L los elementos que están en
    indices pares.
    """
    i = len(L) -1 
    while i >= 0:
        if i % 2 == 0:
            L. pop(i)
        i -= 1

L = ["e", "e", "C", "d", "e", "e", "e"]
eliminar_posiciones_pares(L)
assert L == ["e", "d", "e"]
print("todo bien :)")
