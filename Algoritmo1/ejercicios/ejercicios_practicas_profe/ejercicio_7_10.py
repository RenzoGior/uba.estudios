    # Funcion para sumar dos matrices

# 2 3 4     1 1 1     6 4 5
# 5 4 3  +  1 1 1  =  6 5 4
# 1 2 3     1 1 1     2 3 4



def generar_matriz_nula(n, m):
    resultado = []
    for fil in range(n): #len(matriz_1)
        # hago espacio para la nueva fila
        fila_nueva = []

        # lleno la fila con lo que corresponde
        for col in range(m): #len(matriz_1[0])
            fila_nueva.append(0)
            #fila_nueva.append(matriz_1[f][c] + matriz_2[f][c])

        # agrego la fila a la matriz
        resultado.append(fila_nueva)
    return resultado

def generar_matriz_nula_v2(n, m):
    return [[0] * m] * n
 

def sumar_matrices(matriz_1, matriz_2):
    n_filas = len(matriz_1)
    n_cols = len(matriz_1[0])

    resultado = generar_matriz_nula(n_filas, n_cols)
    for f in range(n_filas):
        for c in range(n_cols):
            resultado[f][c] = matriz_1[f][c] + matriz_2[f][c]

    return resultado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

matriz_a = [
    [1, 2],
    [3, 4]
    ]

matriz_b = [
    [5, 6],
    [4, 6]
    ]

matriz_resultado = [
    [6, 8],
    [7, 10]
]

print('OK')
assert sumar_matrices(matriz_a, matriz_b) == matriz_resultado