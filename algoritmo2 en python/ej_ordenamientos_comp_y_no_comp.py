# Realizar un seguimiento de ordenar el siguiente arreglo utilizando Inserción, Selección, MergeSort, QuickSort y HeapSort. 
# Contar la cantidad de operaciones (aproximadamente) para validar empíricamente la diferencia en el orden de cada uno,
# y poder comparar aquellos que sean iguales: [1, 7, 5, 8, 2, 4, 9, 6, 5].

#seguimiento de merge parte la lista apartir de un numero medio, te queda lista izq y lista der, asi hasta no poder dividir mas la lista
#  va comparado el izq con el derecho dependendiendo de cual es mas chico lo va mergiando las dos mitades, y asi mientras vuelve por la pila de
# recursividad  orden de complejidad O(n log n)

#seguimiento de quick sort, elije como pivote el primer elemento la lista,  crea dos lista de menores y mayores, compara el pivote con el resto
# de la lista, agregando a mayor o menor. y asi vuelve aplicar quick sort a la lista de mayores y menores nueva mente hasta que queden ordenados
# dependiendo de la version puede ser in place o no. orden de complejidad O(n log n)

#seguimiento de heapsort 
def merge_sort(lista):
    """ Ordena lista mediante el método mergesort.
        Pre: lista debe contener elementos comparables.
        Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    """ Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2."""

    i ,j = 0, 0
    resultado=[]

    while(i < len(lista1) and j < len(lista2)):
        if(lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

        #Agregarloquefalta
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado
    
lista = [1, 7, 5, 8, 2, 4, 9, 6, 5]
# print(f"merge sort: {merge_sort(lista)}")

def quick_sort(lista):
    """ Ordena la lista de forma recursiva.
        Pre: los elementos de la lista deben ser comparables.
        Devuelve: una nueva lista con los elementos ordenados."""
    if len(lista) < 2:
        return lista
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)
 
def _partition(lista):
 
    """ Pre: lista no vacía.
        Devuelve: tres listas: menores, medio y mayores."""
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores

def quick_sort2(lista):
    #version in place
    """ Ordena la lista de forma recursiva.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada."""
    _quick_sort2(lista, 0, len(lista)-1)

def _quick_sort2(lista,inicio,fin):
    """ Función quick_sortrecursiva.
        Pre: los índices inicio y fin indican sobre qué porción operar.
        Post: la lista estáo rdenada."""
    if inicio >= fin:
        return
    menores = _partition2(lista, inicio, fin)
    _quick_sort2(lista, inicio, menores-1)
    _quick_sort2(lista, menores+1, fin)

def _partition2(lista,inicio,fin):
    """ Función partición que trabaja sobre la misma lista.
        Pre: los índices inicio y fin indican sobre qué porción operar.
        Post: los menores están antes que el pivote, los mayores después.
        Devuelve: la posición en la que quedó ubicado el pivote."""
    pivote = lista[inicio]
    menores = inicio

    #Ubicar menores a la izquierda, mayores a la derecha
    for i in range(inicio+1, fin+1):
        if lista[i] < pivote:
            menores+=1
            if i != menores:
                _swap(lista, i, menores)
    #Ubicar el pivote alfinal de los menores
    if inicio != menores:
        _swap(lista,inicio,menores)
    return menores

def _swap(lista,i,j):
    """Intercambia los elementos i y j de lista."""
    lista[j], lista[i] = lista[i], lista[j]

    

def heapsort():
    """aplica heapify """
    # aplica heapify al arreglo combirtiendolo en un heap de maximos
    pass
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)



# Se tiene un arreglo de estructuras de la forma type Evento struct {anio long, evento string},
# que indica el año y evento de un hecho definido a lo largo de la historia de la Tierra. 
# Indicar y justificar cuál sería un algoritmo de ordenamiento apropiado para utilizar para ordenar dicho arreglo por año. 
# Indicar también, si en vez de ordenar por año se decide ordenar por evento (lexicográficamente). 
# Si se quiere ordenar por año y dentro de cada año, por evento: ¿Deben utilizarse para ambos campos el mismo algoritmo de ordenamiento? 
# ¿Que característica/s deben cumplir dicho o dichos algoritmos para que quede ordenado como se desea?
# ¿En qué orden deben aplicarse los ordenamientos?
"""se usaria radix sort, para los años y para los eventos para, se podrian usar como no el mismo algoritmo, para los eventos, primero se ordenaria
primero por evento, y luego por año"""
estruc = (1999, "boca campeon")


# Hacer el seguimiento de counting sort para ordenar por año las siguientes obras:

#     1988 - Crónicas del Ángel Gris
#     2000 - Los Días del Venado
#     1995 - Alta Fidelidad
#     1987 - Tokio Blues
#     2005 - En Picada
#     1995 - Crónica del Pájaro que Da Cuerda al Mundo
#     1995 - Ensayo Sobre la Ceguera
#     2005 - Los Hombres que No Amaban a las Mujeres

# ¿Cuál es el orden del algoritmo? ¿Qué sucede con el orden de los elementos de un mismo año, respecto al orden inicial, 
# luego de finalizado el algoritmo? Justificar brevemente.

"""primero se sacaria el rango, haciendo la fecha minima - la fecha maxima + 1, que daria 19. luego se sacaria la frecuencia, haciendo el año
a ordernar menos la fecha minima, daria un numero dentro de 19. hacemos eso si hay fechas repetidas se les suma 1 al, numero de la resta. los 
lugares vacios se le rellenarian con el ultimo numero mas chico cerca.
luego hariamos un arreglo con la cantidad de fechas iniciales, y recorreriamos el ultimo arreglo con las frecuencias para rellenar
(sacando su indice) el arreglo con las fechas iniciales. el orden de los elementos de un mismo año no cambian ya que es estable el alritmo
suponniendo que estan ordenados lexicograficcamente, quedarian igual.
en este caso el orden seria o(n) ya que es chico la cantidad de elementos a ordenar"""


# Realizar el seguimiento de ordenar por Radix Sort el siguiente arreglo de cadenas que representan versiones. 
# Cada versión tiene el formato a.b.c, donde cada valor a, b y c puede tener un valor entre 0 y 99. 
# Considerar que se quiere que quede ordenado primero por la primera componente (a), luego por la segunda (b) y finalmente por la tercera (c).
# Se puede asumir que a nunca será 0 salvo que el número sea efectivamente 0. Es decir, la notación es correcta.
# Tener en cuenta que, por ejemplo 1.1.3 < 1.1.20, 2.20.8 < 3.0.0.

# ["4.3.2", "5.1.2", "10.1.4", "2.1.20", "2.2.1", "4.2.3", "2.1.5", "8.1.2", "5.30.1", "10.0.23"]

"""usamos radix sort con bucket sort, empezando por c, por la cifra menos significativa que seria [c][1] si no tiene [c][0] asumimos que es 0
luego hacemos lo mismo con b, y por ultimo con a
    [   0    ][   1    ][    2     ][      3     ][     4    ][    5      ][6][7][8][9]
      2.1.20    2.2.1       4.3.2      4.2.3          10.1.4    2.1.5
                5.30.1      5.1.2      10.0.23
                            8.1.2
    ["2.1.20", 2.2.1, 5.30.1, 4.3.2, 5.1.2, 8.1.2, 4.2.3, 10.0.23, 10.1.4, 2.1.5]
    repetimos con [c][0]
    [2.2.1, 5.30.1, 4.3.2, 5.1.2, 8.1.2, 4.2.3, 10.1.4, 2.1.5, 2.1.20, 10.0.23]
    repetimos con [b][1]
    [   0    ][   1    ][    2     ][      3     ][     4    ][    5      ][6][7][8][9]
      5.30.1     5.1.2     2.2.1        4.3.2
     10.0.23     8.1.2      4.2.3
                10.1.4
                2.1.5
                2.1.20
    [5.30.1, 10.0.23, 5.1.2, 8.1.2, 10.1.4, 2.1.5, 2.1.20, 2.2.1, 4.2.3, 4.3.2  ]
    repetimos con [b][0]
    [10.0.23, 5.1.2, 8.1.2, 10.1.4, 2.1.5, 2.1.20, 2.2.1, 4.2.3, 4.3.2, 5.30.1]
    repetimos con [a][1]
    [   0    ][   1    ][    2     ][      3     ][     4    ][    5      ][6][7][       8      ][9]
    10.0.23               2.1.5                       4.2.3        5.1.2                   8.1.2
    10.1.4                2.1.20                    4.3.2,         5.30.1
                           2.2.1
    [10.0.23, 10.1.4, 2.1.5, 2.1.20, 2.2.1, 4.2.3, 4.3.2, 5.1.2, 5.30.1,  8.1.2]
    repetimos con [a][0]
    [2.1.5, 2.1.20, 2.2.1, 4.2.3, 4.3.2, 5.1.2, 5.30.1,  8.1.2, 10.0.23, 10.1.4]
 """

# indicar Verdadero o Falso, justificando de forma concisa en cualquier caso.

# a. Podríamos mejorar el orden de complejidad de QuickSort si contaramos con más información sobre cómo son los datos a ordenar.
"""falso, ya que el orden por comparacion nunca puede ser mejor que n log n"""
# b. No siempre conviene utilizar Counting Sort para ordenar un arreglo de números enteros.
"""verdadero, depende cuan distribuido esten esos numeros"""
# c. Que un algoritmo de ordenamientos sea estable implica que el algoritmo ordena sobre el arreglo original (sin utilizar otro adicional). 
# Por ejemplo, Counting Sort no es estable.
"""falso, eso seria in place."""


# Se quiere ordenar un arreglo de películas por su género. 
# No se conoce cuántos, ni cuáles son estos géneros, pero se sabe que son muy pocos comparando con la cantidad de películas a ordenar. 
# Diseñar un algoritmo que permita ordenar las películas en tiempo lineal de la cantidad de películas 
# y explique ćomo funcionaría sobre las siguientes películas:

# Donnie Darko (2001): Thriller psicológico
# Juno (2007): Coming of age
# The Shining (1980): Thriller psicológico
# Labyrinth (1986): Fantasía
# Ferris Bueller’s Day Off (1986): Coming of age
"peliculas = lista[(tuplas)]"
peliculas = [
    ("Donnie Darko (2001)", "Thriller psicológico"),
    ("Juno (2007)", "Coming of age"),
    ("The Shining (1980)", "Thriller psicológico"),
    ("Labyrinth (1986)", "Fantasía"),
    ("Ferris Bueller’s Day Off (1986)", "Coming of age"),
    ("shutter island", "Thriller psicológico"),]

def ordenar_peliculas_genero(peliculas):
    cubo = {}
    # buckets = []
    for pelicula in peliculas:
        nombre, genero = pelicula
        if genero not in cubo:
            cubo[genero] = []
        cubo[genero].append(pelicula)
    # print(cubo)
    resultado = []
    for genero in sorted(cubo.keys()):
        resultado.append(cubo[genero])
    return resultado
# print(ordenar_peliculas_genero(peliculas))
# ordenar_peliculas_genero(peliculas)
    
# Implementar un algoritmo que, dado un arreglo den números enteros cuyos valores van de 0 a K (constante conocida), 
# procese dichos números en tiempo  O(n + K)
# O(n+K), devuelva alguna estructura que permita consultar cuántos valores ingresados están en el intervalo (A, B), en tiempo O(1)
# O(1). Explicar cómo se usaría dicha estructura para poder realizar tales consultas.

def construir_estructura(arr, K):
    # Paso 1: Crear arreglo de conteo de tamaño K+1 inicializado en 0
    count = [0] * (K + 1)
    
    # Contar la frecuencia de cada número en el arreglo
    for num in arr:
        count[num] += 1
    
    # Paso 2: Convertir en suma de prefijos
    for i in range(1, K + 1):
        count[i] += count[i - 1]
    
    return count

def consultar_intervalo(count, A, B):
    # Consulta en O(1) para el intervalo (A, B)
    if A == 0:
        return count[B]
    return count[B] - count[A - 1]