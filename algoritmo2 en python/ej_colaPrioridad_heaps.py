import heapq

def calcular_posicion_padre(pos):
    return (pos - 1) / 2

def calcular_posicion_hijos(pos):
    return pos*2 + 1, pos*2 + 2
# Implementar en lenguaje Go una función recursiva con la firma func esHeap(arr []int). 
# Esta función debe devolver true o false de acuerdo a si el arreglo que recibe como parámetro cumple la propiedad de heap (de mínimos).

# Hacer el seguimiento de la función para el arreglo [ 1, 7, 2, 8, 7, 6, 3, 3, 9, 10 ].

arr = [ 1, 7, 2, 8, 7, 6, 3, 3, 9, 10]

def es_heap(arr, indice=0):
    if indice >= len(arr):
        return True
    hijo_izq, hijo_der = calcular_posicion_hijos(indice)
    if hijo_izq < len(arr) and arr[indice] > arr[hijo_izq]:
        return False
    if hijo_der < len(arr) and arr[indice] > arr[hijo_der]:
        return False
    return es_heap(arr, indice+1) 

# print(es_heap(arr))

# (★) Implementar una primitiva para el heap (de máximos) que obtenga los 3 elementos más grandes del heap en O(1).
"""no searia posible en 0(1) ya que el, al volver hacer upheap a los restantes en la cola de preoridad seria O(log N)"""

# Si en el ejercicio anterior en vez de quererse los 3 elementos más grandes, se quisieran los K elementos más grandes ¿cómo se debería proceder? 
# ¿Cuál terminaría siendo la complejidad del algoritmo?
"""seria peor ya que en el caso que el K se acerque a len(heap) la primitiva seria (N log N)"""

# En un heap de máximos ¿cuáles son las posibles posiciones del arreglo donde podría encontrarse el mínimo?
"""las posiciones posicible serian apartir de la mitad del arreglo hacia al final del arreglo"""

# Realizar el seguimiento del algoritmo heapsort para ordenar el siguiente arreglo: [ 4, 7, 8, 14, 10, 9, 16, 2, 3, 1 ].
"""primeros nos fijamos si cumple la siguientes funciones ¿Es un árbol binario? si ¿Es izquierdista? si ¿Es un heap de máximos ? no
entonces hacemos un heapify al array, Aplicamos downheap de las hojas hacia la raíz, el array hecho heapify quedaria
[16, 14, 9, 10, 7, 4, 8, 2, 3, 1] y ahora cumpliria las funciones y aplicamos heapsort. A partir del arreglo recibido, lo convierte en un heap.
Luego Itera sobre todo el heap: Va agarrando el primero del heap y lo swapea con el “utlimo relativo”
 (el “ultimo relativo” se va achicando desde lo ultimo del heap hasta el primero) Por cada iteración Aplica downheap al primero del heap
[16, 14, 9, 10, 7, 4, 8, 2, 3, 1] Va agarrando el primero del heap, lo swapea con el ultimo relativo
[1, 14, 9, 10, 7, 4, 8, 2, (3), 16] Actualizo ultimo relativo seria el 3
 Aplica downheap al primero del heap
 [1, 10, 9, 3, 7, 4, 8, (2), 14, 16]  Actualizo ultimo relativo seria el 2
 Aplica downheap al primero del heap
 [10, 7, 9, 3, 1, 4, 8, 2, 14, 16] swapea con el ultimo relativo
 [2, 7, 9, 3, 1, 4, (8), 10, 14, 16] actualizo ultimo relativo seria el 8
 Aplica downheap al primero del heap
 [9, 7, 8, 3, 1, 4, 2, 10, 14, 16] swapea con el ultimo relativo
 [8, 7, 3, 1, 4, (2), 9, 10, 14, 16] actualizo ultimo relativo seria el 2
 Aplica downheap al primero del heap
 queda igual swapeamos el ultimo relativo
 [2, 7, 3, 1, (4), 8, 9, 10, 14, 16] actualizo el ultimo relativo seria el 4
 aplico downheap al primero
 [7, 4, 3, 1, 2, 8, 9, 10, 14, 16]
 swapeamos el ultimo relativo
 [2, 4, 3, 1, 7, 8, 9, 10, 14, 16] y asi con el resto hasta que quede ordenado quedando
 el siguiente array
 [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
 """

# ¿Puede utilizarse un Heap para implementar el TDA cola (en el que se extraen los elementos en el orden en que fueron insertados)? 
# ¿Y para implementar el TDA pila?
"""si se puede en ambos casos, tenes que asignarles diferentes prioradades ala hora de insertarlos ala cola de prioridad en ambos casos
Definitivamente. Una Cola no es más que un arreglo con órden de elementos donde uno tiene más prioridad que otro (el primero que entró respecto del siguiente y así). 
Entonces como usamos un Heap para recrear el comportamiento de una Cola?
Hacemos una función de comparación que compare tiempo de entrada! Y listo, el tiempo más reciente es el de mayor prioridad
¡Es literalmente la misma idea! ¿Pero qué cambia acá?
El orden de prioridad, ahora los últimos en entrar tienen más prioridad.
Entonces, ¿cómo podemos hacerlo con toda esta idea que venimos armando?
Misma función de comparación, distinto tipo de Heap
"""

# Hacer el seguimiento de las siguientes operaciones sobre un heap (de mínimos),
# mostrando el estado de la estructura después de cada modificación:

# Crear un heap de mínimos desde el arreglo [8, 2, 1, 5, 10, 6, 14, 4].
[1, 2, 6, 4, 10, 8, 14, 5]

# Sobre el heap resultante del punto anterior, realizar las siguientes operaciones: 
# encolar(6), encolar(3), encolar(17), desencolar(), encolar(7), desencolar().
[3, 4, 6, 5, 7, 8, 14, 6, 10, 17]

# (★★★) ♠ Escribir una función en Go que, dado un arreglo de n cadenas y un entero positivo k, devuelva una lista con las 
# k cadenas más largas. Se espera que el orden del algoritmo sea O(n+klogn). Justificar el orden.

def k_cadenas_largas(arr, k):
    aux = []
    heapq.heapify(arr)
    if len(arr)< k:
        k = len(arr)
    for _ in range(k):
        aux.append(heapq.heappop(arr))
    return aux

# print(k_cadenas_largas(arr, 10))

#  Para implementar un TDA Cola de prioridad, nos proponen la siguiente solución: usar un arreglo desordenado (arr) 
# para insertar los datos, y una variable (maximo) para poder obtener el máximo en O(1). 
# Se mantiene actualizada la variable maximo cada vez que se encola o desencola. ¿Es una buena solución en el caso general?
# Justificar (recomendación: comparar contra la implementación de colas de prioridad vista en clase).

"""funcionaria si el heap que se quiere sea de maximos, pero si se quiere uno de minimos no se podria ya que no se sabria donde 
esta el minimo."""

# En clase vimos que se puede implementar un heap con un árbol izquierdista, o su representación equivalente en arreglo. 
# Esta última, siendo mucho más sencilla de implementar. ¿Por qué no implementamos también el Árbol Binario de Búsqueda con 
# una representación en arreglo, en vez de implementarlo con, valga la redundancia, árboles?

"""ya que romperia la funcion, arbol binario y al insertar seria o(n) en el peor de los caso, o peor aun , y ala hora de implementar el arbol
binario, la mantencion, y la eficiencia de la manera de arboles es la mejor"""

# ★★★★) ♠ Dado un arreglo de enteros y un número K, se desea que todos los elementos del arreglo sean mayores a K. 
# Aquellos números que sean menores o iguales a K deberían combinarse de la siguiente forma: buscar los dos números más chicos del vector, 
# sacarlos y generar uno nuevo de la forma Nuevo número = número-más-chico + 2 x segundo-más-chico. Por ejemplo, si K = 10 y 
# los números más chicos del arreglo son 3 y 4: 3 + 2 * 4 = 11. 
# Los números combinados pueden volver a ser combinados con otros en caso de ser necesario (en el ejemplo no lo es), 
# aplicando la misma lógica hasta que el número resultante sea mayor a K.

# Implementar una función que reciba un arreglo de enteros, su largo y un número K, y 
# devuelva una lista con los elementos que quedarían luego de aplicar las modificaciones.
# El arreglo original debe quedar en el estado original. El orden de la lista no es importante. 
# En caso de no poderse combinar todos los elementos para que todos los elementos sea mayores a K, devolver nil.
# Determinar y justificar la complejidad del algoritmo implementado.

# Ejemplo: Entrada: [11, 14, 8, 19, 42, 3, 1, 9]; K = 13:

# [11, 14, 8, 19, 42, 3, 1, 9] - (1,3)  -> 1 + 2*3 = 7
# [11, 14, 8, 19, 42, 9, 7]    - (7,8)  -> 7 + 8*2 = 23
# [11, 14, 19, 42, 9, 23]      - (9,11) -> 9 + 11*2 = 31
# [14, 19, 42, 23, 31]
# Notar que si el 9 no estuviera en el arreglo, no se podría resolver el problema (debemos devolver nil),
# ya que el 11 no podría combinarse con ningún otro número.
entrada = [11, 14, 8, 19, 42, 3, 1, 9]
largo = len(entrada)
k = 13

"""necesito heap de minimos """

def numeros_mayor_k(entrada, largo, k):
    copia = entrada[:]
    heapq.heapify(copia)
    while copia and copia[0] <= k: 
        min1 , min2 = heapq.heappop(copia), heapq.heappop(copia)
        nuevo_numero = min1 + 2 * min2
        heapq.heappush(copia, nuevo_numero)
    return list(copia)

# print(numeros_mayor_k(entrada, largo, k))