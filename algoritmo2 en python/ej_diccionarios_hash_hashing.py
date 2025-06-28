# Suponer que se tiene un hash cerrado que se redimensiona cuando el factor de carga llega a 0.75, 
# y que no se tienen en cuenta los elementos borrados a la hora de calcular el factor de carga.

# Describir, en términos generales, el peor escenario posible para esta implementación.

# Dado un hash de estas características, con capacidad inicial 100, 
# calcular el número máximo de casillas que podría llegar a visitar hash_obtener() 
# si la cantidad actual de elementos en el hash es 1, y no se realizó ningúna redimensión, 
# pero sí se insertaron y borraron elementos. (En otras palabras, poner una cota superior al caso peor de este hash.)

""" el peor caso seria que este lleno de borrados, y que cuando quieras agregar otro al hash no, termine o se rompa

el numero maximo seria infinito, o dependiendo de la implementacion por que si se quiere igresar un nuevo elemento que quede en la ultima
posicion daria una vuelta al comienzo pero si en todos lo demas casilleros estan ocupados ya sea por borrados o ocupados, no encontraria lugar."""

 
# ¿Para qué casos la función hash_obtener() tiene una complejidad peor que O(1)
# O(1)? Explicar tanto para el hash abierto, como el cerrado.

"""para todos los casos exepto cuando tenga que redimensionar el arreglo"""


# Justificar si la siguiente función de hashing es correcta o no:
# func calcularHash(string clave) int {
#     // rand.Intn(x) devuelve un numero entero entre 0 y x
#     return rand.Intn(10000)
# }

"""es incorrecta ya que siempre va a dar un numero random, y si lo guardamos en el diccionario nunca lo vamos a poder recuperar el valor"""

# a. Mostrar el resultado de las siguientes operaciones tanto para un hash cerrado como para un hash abierto, 
# ambos de capacidad 9 e inicialmente vacíos (los números son también el resultado de la función de hashing): 
# insertar 17, insertar 22, insertar 35, borrar 17, insertar 52, insertar 54.
"""[O, 35][O, 54][V][V][O,22][V][V][O, 52][B, 17] cerrado   17 % 9 = 8.donde 9 es el len del array, asi con todos los numeros  
35 % 9 = 8 entonces hacemos mas +1 pero como estamos al 
final va al primero, con el 54 pasa lo mismo entonces hacemos mas 1"""
"""[54][][][][22,][][][52,][35,] abierto, lo mismo que nada mas que crea una lista enlazada, cuando se agrega un nuevo al hash, 
y en esa lista nomas enlazada nomas hasta 3 y luege se redimenciona"""
# b. Tras estas inserciones ¿qué pasos hay que seguir para verificar si el 70 pertenece al hash?
"""aplicamos hash, nos fijamos en el numero que cae si esta ocupado o borrado el numero que cae, iteramos hasta que haya uno vacio
o se encuentre, en el caso de hash abierto nos fijamos el numero que cae, y iteramos en la lista esa hasta que sea null o lo encontremos"""
# c. Posteriormente se realizan más inserciones. ¿Cuándo redimensionaría cada hash? ¿Qué pasos hay que seguir para hacerlo?
"""en el hash cerrado, cada vez que agregamos uno 1, sumamos 1 a un contador, si el contador para el 70% del tamañao del array
se redimenciona, se hace un por 2 al tamaño del array, y se le vuelven a hacer hash a todos los elementos de la lista y lo aplicamos en el array
sacando los elementos borrados.
en un hash abierto pasa lo mismo sin los elementos borrados, se redimenciona cuando se ocupan el 70% del el array o ,cuando una de las listas
enlazadas dentro de el array es mayor a 3"""


# Implementar una función de orden O(n)
# O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces.
# Justificar el orden de la solución. Ejemplos:
arreglo1 = [1, 2, 1, 2, 3] #-> false
arreglo2 = [1, 1, 2, 3] #-> false
arreglo3 = [1, 2, 3, 1, 1, 1] #-> true
arreglo4 = [1] #-> true

def n_elemento_mas_mitad(array) -> bool:
    elementos = {}
    n = len(array)// 2
    for i in array:
        elementos[i] = elementos.get(i, 0) + 1
        if elementos[i] > n:
            return True
    return False

assert n_elemento_mas_mitad(arreglo1) == False
assert n_elemento_mas_mitad(arreglo2) == False
assert n_elemento_mas_mitad(arreglo3) == True
assert n_elemento_mas_mitad(arreglo4) == True


#  Asumiendo que se tiene disponible una implementación completa del TDA Hash,
# se desea implementar una función que decida si dos Hash dados representan o no el mismo Diccionario.
# Considere para la solución que es de interés la mejor eficiencia temporal posible. Indique, para su solución, eficiencia en tiempo y espacio.
# Nota: Dos tablas de hash representan el mismo diccionario si tienen la misma cantidad de elementos;
# todas las claves del primero están en el segundo; todas las del segundo, en el primero; y los datos asociados a cada una de esas 
# claves son iguales (se pueden comparar los valores con “==”).
"""eficiencia temporal O(n), en espacio es el tamaño de los dos diccionarios"""
def son_mismo_diccionario(diccionario1, diccionario2):
    if len(diccionario1) != len(diccionario2):
        return False
    for clave, valor in diccionario1.items():
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False
    return True


# Se tiene un hash que cuenta con una función de hashing que, recibida una clave, devuelve la posición de su inicial en el abecedario. 
# La capacidad inicial del hash es 26. Para los puntos B, C y D indicar y justificar si las afirmaciones son verdaderas o falsas.
# Se puede considerar que todas las claves serán palabras (sólo se usan letras para las claves).

# a. Mostrar cómo quedan un hash abierto y un hash cerrado (sólo el resultado final) tras guardar las siguientes claves: 
# Ambulancia (0), Gato (6), Manzana (12), Ananá (0), Girasol (6), Zapato (25), Zapallo (25), Manzana (12), Bolso (1). Aclaración: 
# No es necesario hacer una tabla de 26 posiciones, lo importante es que quede claro en cuál posición está cada elemento.
"""[ambulancia,anana,][bolso,] [gato,girasol] [manzana,] [zapato, zapallo]"""

# b. En un hash abierto con dicha función de hashing, se decide redimensionar cuando la cantidad alcanza la capacidad 
# (factor de carga = 1). El rendimiento de hash_obtener() es mejor en este caso respecto a si se redimensionara al alcanzar un factor de carga 2.
"""el rendimiento seria el mismo ya que el hash obtener() es o(1) para los dos casos"""

# c. En un hash cerrado con dicha función de hashing, si se insertan n + 1 claves diferentes (considerar que se haya redimensionado acordemente),
# n con la misma letra inicial, y 1 con otra distinta, en el primer caso Obtener() es O(n) y en el segundo siempre O(1).
"""falso"""
# d. En un hash abierto con dicha función de hashing, si se insertan n + 1 claves diferentes (considerar que se haya redimensionado acordemente),
# n con la misma letra inicial, y 1 con otra distinta, en el primer caso Obtener() es O(n) y en el segundo siempre O(1)
"""verdadero"""

# El Ing. Musumeci quiere implementar un hash abierto, pero en el que las listas de cada posición se encuentren ordenadas por clave 
# (se le pasa por parmámetro la función de comparación, por ejemplo strcmp). 
# Explicar cómo mejora o empeora respecto a la versión que vemos en clase para el caso de inserciones, borrados, búsquedas con éxito 
# (el elemento se encuentra en el hash) y sin éxito (no se encuentra)
"""el algoritmo empeoraria, ya que agregamos nuevos paso al insertar y borrar, en el mejor de los casos al ordenar por comparacion
seria n log n, lo cual empeoraria estos metodos de O(1), para busqueda de exito o no, no cambiaria """


