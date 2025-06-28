 # Vectores
 # a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
def producto_escalar(v1: tuple, v2: tuple) -> int:
    return v1[0] * v2[0] + v1[1] * v2 [1] + v1[2] * v2[2] 


# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
def vector_ortogonales(v1: tuple, v2: tuple) -> bool :
    return producto_escalar(v1, v2) == 0


# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
def vetores_paralelos(v1: tuple, v2: tuple) -> bool:
    return 

# d) Escribir una función que reciba un vector y devuelva su norma.





def main():
    v1 = (3, 0, 1)
    v2 = (1, -5, -3)
    print(producto_escalar(v1, v2))
    print(vector_ortogonales(v1, v2))

main()