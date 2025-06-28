from grafo import Grafo 
from collections import deque
import random
# (★) a. Dibujar un grafo no dirigido que:
# Tenga 6 vértices
# Tenga un ciclo que incluya 4 de dichos vértices
# Sea conexo
# Haya un vértice de grado 1
# Haya un vértice de grado 4
# b. Escribir la representación de matriz de incidencia y matriz de adyacencia del grafo resultante del punto anterior.
"""          
      A ---- B    
      |      |
      |      |     
      D------C-----E
             |
             |
             F

matriz de incidencia            matriz de adyacencia    
    A  B  C  D  E  F                A  B  C  D  E  F
a1  1  1  0  0  0  0            A   0  1  0  1  0  0
a2  1  0  0  1  0  0            B   1  0  1  0  0  0
a3  0  1  1  0  0  0            C   0  1  0  1  1  1
a4  0  0  1  1  0  0            D   1  0  1  0  0  0
a5  0  0  1  0  1  0            E   0  0  1  0  0  0
a6  0  0  1  0  0  1            F   0  0  1  0  0  0
"""
# a. Dibujar un grafo dirigido que:
# Tenga 7 vértices
# Tenga un ciclo que incluya 3 de dichos vértices
# Tenga un ciclo que incluya 2 de dichos vértices
# Haya un vértice de grado de entrada 0
# Haya un vértice de grado de salida 4
# b. Escribir la representación de matriz de incidencia y matriz de adyacencia del grafo resultante del punto anterior.
"""
A ------ B <-------> C
              \        /
                \    /
                  \/
          F------ D ------ E
                  |
                  |
                  G
   matriz de incidencia               matriz de adyacencia    
    A  B  C  D  E  F  G                A  B  C  D  E  F  G
a1 -1  1  0  0  0  0  0             A  0  1  0  0  0  0  0
a2  0 -1  1  0  0  0  0             B  0  0  1  0  0  0  0
a3  0  1 -1  0  0  0  0             C  0  1  0  1  0  0  0
a4  0  0 -1  1  0  0  0             D  0  1  0  0  1  1  1
a5  0  1  0 -1  0  0  0             E  0  0  0  0  0  0  0
a6  0  0  0 -1  1  0  0             F  0  0  0  0  0  0  0
a7  0  0  0 -1  0  1  0             G  0  0  0  0  0  0  0
a8  0  0  0 -1  0  0  1
"""
#  Implementar una función que determine el:
# a. El grado de todos los vértices de un grafo no dirigido.
def grado_vertice(grafo):
    grado = {}
    for vertice in grafo:
        grado[vertice] = len(grafo.adyacentes(vertice)) 
    return grado


# b. El grado de salida de todos los vértices de un grafo dirigido.
# c. El grado de entrada de todos los vértices de un grafo dirigido.
def grados_vertices(grafo):
    salida = {}
    entrada = {}
    for vertice in grafo:
        salida[vertice] = len(grafo.adyacentes(vertice))
        for adyacente in grafo.adyacentes(vertice):
            entrada[adyacente] = entrada.get(adyacente, 0) +1
    return salida, entrada

# Implementar un algoritmo que determine si un grafo no dirigido es conexo o no. 
# Indicar la complejidad del algoritmo si el grafo está implementado con una matriz de adyacencia.

def grafo_conexo(grafo):
    visitados = set()
    q = deque()
    origen = random.choice(grafo.keys())
    visitados.add(origen)
    q.append(origen)
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                q.append(w)
    return len(grafo) == len(visitados)

#  Implementar un algoritmo que, dado un grafo dirigido, nos devuelva un ciclo dentro del mismo, si es que lo tiene. Indicar el orden del algoritmo.

"""Antes que nada, debemos entender que el ejercicio en sí es el mismo, se trate de un grafo dirigido o uno no dirigido. 
La única diferencia se encuentra en que un ciclo por definción necesita contar con al menos dos aristas. 
Esta definición en sí no nos importaría mucho en el caso de un grafo dirigido, pero si en el de uno no dirigido. 
Si no lo tuviéramos en cuenta, todo grafo no dirigido, con al menos una arista, va a tener un ciclo, lo cual no es cierto.
Para resolver este problema, podemos pensar en simplemente recorrer el grafo no dirigido, sea con un recorrido BFS o DFS. 
Una vez que nos topemos con un vértice ya visitado, ahí tenemos un posible ciclo. Esto es, si estoy viendo los adyacentes a un vértice dado,
 y dicho vértice está visitado, uno se apresuraría a decir que ahí se cierra un ciclo. Esto es cierto, salvo un caso: 
 que dicho vértice visitado sea el antecesor a nuestro vértice en el recorrido (BFS o DFS). Recordar que se trata de un grafo no dirigido, 
 por ende si v tiene de adyacente a w, entonces también vale la recíproca, y no por ello se crea un ciclo. El problema se da con la arista de la que vengo. 
 Básicamente, deberíamos obviar al vértice del que vengo en el recorrido, que justamente es el padre. Si nosotros ya tenemos que padre[W] = V, 
 entonces simplemente tenemos que saltearnos a V cuando veamos a los adyacentes ya visitados.

Lo resolvemos con ambos recorridos. Por DFS:"""
def obtener_ciclo_dfs(grafo):
    visitados = {}
    padre = {}
    for v in grafo:
        if v not in visitados:
            ciclo = dfs_ciclo(grafo, v, visitados, padre)
            if ciclo is not None:
                return ciclo
    return None

def dfs_ciclo(grafo, v, visitados, padre):
    visitados[v] = True
    for w in grafo.adyacentes(v):
        if w in visitados:
            # Si w fue visitado y es padre de v, entonces es la arista de donde
            # vengo (no es ciclo).
            # Si no es su padre, esta arista (v, w) cierra un ciclo que empieza
            # en w.
            if w != padre[v]:
                return reconstruir_ciclo(padre, w, v)
        else:
            padre[w] = v
            ciclo = dfs_ciclo(grafo, w, visitados, padre)
        if ciclo is not None:
            return ciclo
  # Si llegamos hasta acá es porque no encontramos ningún ciclo.
    return None

def reconstruir_ciclo(padre, inicio, fin):
    v = fin
    camino = []
    while v != inicio:
        camino.append(v)
        v = padre[v]
    camino.append(inicio)
    return camino[::-1]

"""Por BFS, la solución sería similar, pero tenemos que tener noción de la distancia/orden. Esto es porque podríamos terminar sin encontrar un ciclo correctamente.
 Por ejemplo, si tenemos un grafo con 4 vértices en forma de cuadrado (aristas A-B, B-C, C-D, D-A), y empezamos a hacer el recorrido desde A, 
 eventualmente en el BFS vamos a encontrar el ciclo (ej, al ver desde C para ir a D), pero al reconstruir el camino probablemente falle. 
 Es necesario modificar el algoritmo para reconstruir el camino:
"""
def obtener_ciclo_bfs(grafo):
    visitados = {}
    for v in grafo:
        if v not in visitados:
            ciclo = bfs_ciclo(grafo, v, visitados)
        if ciclo is not None:
            return ciclo
    return None

def bfs_ciclo(grafo, v, visitados):
    q = deque()
    q.append(v)
    visitados[v] = True
    padre = {}  # Para poder reconstruir el ciclo
    orden = {}
    padre[v] = None
    orden[v] = 0

    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w in visitados:
                # Si w fue visitado y es padre de v, entonces es la arista
                # de donde vengo (no es ciclo).
                # Si no es su padre, esta arista (v, w) cierra un ciclo que
                # empieza en w.
                if w != padre[v]:
                    return reconstruir_ciclo(padre, orden, w, v)
        else:
            q.append(w)
            visitados[v] = True
            padre[w] = v
            orden[w] = orden[v] + 1
    # Si llegamos hasta acá es porque no encontramos ningún ciclo.
    return None
  
def reconstruir_camino(padre, orden, v1, v2):
    ciclo = []
    if orden[v1] != orden[v2]: # no puede haber más que 1 de diferencia
        if orden[v1] > orden[v2]:
             ciclo.append(v1)
             v1 = padre[v1]
        else:
             ciclo.append(v2)
             v2 = padre[v2]
    while v1 != v2:
        ciclo.append(v1)
        ciclo.append(v2)
        v1 = padre[v1]
        v2 = padre[v2]
    ciclo.append(v1)
    return ciclo

"""Ahora bien, para ver el orden, podemos ver que en el caso feliz, vamos a encontrar un ciclo muy rapido. Pero claramente eso no nos cambia mucho. 
Pensemos el caso de, a lo sumo, encontrar el ciclo muy tarde en el recorrido (también veremos el caso de no haber ciclo). En ese caso, 
en cualquiera de los dos recorridos vamos a pasar por cada vértice una vez, y solo una vez (a fin de cuentas, no volvemos a estar sobre un vértice ya visitado). 
Por cada vértice vemos sus aristas. Recordar que es muy importante no caer en la tentación de decir que entonces el algoritmo es O(VxE), porque si bien es cierto, 
es una muy mala cota. Por cada vértice pasamos por sus aristas, que distan de ser las totales del grafo. Si por cada vértice vemos sus aristas (y no las de todo el grafo),
 en total estamos viendo todas las aristas del grafo, dos veces (una por cada extremo). Entonces, el orden será O(V+2E)=O(V+E). 
 Todo esto, considerando que la implementación es con listas de adyacencias (implementadas con diccionarios, 
 o bien siendo los vértices valores numéricos para indexar en un arreglo). Si fuera otra la implementación, obtener los adyacentes a un vértice dado nos costará más O(V),
   en el caso de una matriz de adyacencia, u O(E) en el caso de una matriz de incidencia).
Haciendo un poco más de análisis: ¿es acaso el caso de no tener ciclos nuestro peor caso? Supongamos que el grafo es conexo, por simplifcación. 
Si el grafo no tiene ciclos, y es conexo, necesariamente se trata de un árbol. Para este caso, |E|=|V|-1, por ende nuestro orden a fin de cuentas terminaría siendo O(V). 
¿Esto implica que entonces nuestro algoritmo es en realidad O(V)? No, significa que ese, que a priori podíamos pensar que era nuestro peor caso, en realidad no lo es. 
Nuestro peor caso implica que haya un ciclo, pero tener la mala suerte de tardar en encontrarlo. Ya sea porque el vértice en el que se empieza el recorrido está lejos del ciclo,
 o por el orden aleatorio de las cosas."""

#  Un árbol es un grafo no dirigido que cumple con las siguientes propiedades:

# a. ∥E∥=∥V∥-1

# b. Es acíclico

# c. Es conexo

# Por teorema, si un grafo cumple dos de estas tres condiciones, será árbol (y por consiguiente, cumplirá la tercera). Haciendo uso de ésto (y únicamente de ésto),
# se pide implementar una función que reciba un grafo no dirigido y determine si se trata de un árbol, o no. Indicar el orden de la función implementada.

def grafo_es_arbol(grafo):
    #chequear las funciones de arriba, si es conexo o si tiene ciclos,
    return obtener_ciclo_bfs(grafo) is None and grafo_conexo(grafo)
        
"""el orden de la funcion seria O(V + E), ya que las dos funciones de obtener ciclo y grafo conexo, son O(V + E) entonces se simplifica y seria O(V+E)"""


# Proponer una función para calcular el grafo traspuesto GT de un grafo dirigido G. El grafo traspuesto GT posee los mismos vértices que G,
# pero con todas sus aristas invertidas (por cada arista (v, w) en G, existe una arista (w, v) en GT). Indicar la complejidad para un grafo implementado con:

# a. lista de adyancencias

# b. matriz de adyacencias

def traspuesto(grafo):
    g_t = Grafo(es_dirigido=True)
    for v in grafo:
        g_t.agregar_vertice(v)
    for v in grafo:
        for w in grafo.adyacentes(v):
            g_t.agregar_arista(w, v)
    return g_t

# La teoría de los 6 grados de separación dice que cualquiera en la Tierra puede estar conectado a cualquier otra persona del planeta 
# a través de una cadena de conocidos que no tiene más de cinco intermediarios (conectando a ambas personas con solo seis enlaces). 
# Suponiendo que se tiene un grafo G en el que cada vértice es una persona y cada arista conecta gente que se conoce (el grafo es no dirigido):

# a. Implementar un algoritmo para comprobar si se cumple tal teoría para todo el conjunto de personas representadas en el grafo G. Indicar el orden del algoritmo.

# b. Suponiendo que en el grafo G no habrán altas ni bajas de vértices, pero podrían haberla de aristas (la gente se va conociendo), 
# explicar las ventajas y desventajas que tendría implementar al grafo G con una matriz de adyacencia.

def grados_6_separacion_conocidos(grafo):
    for v in grafo:
        _, distancia = camino_minimo(grafo, v)
        for d in distancia.values:
            if d > 6 or d == float('inf'):
                return False
    return True

def camino_minimo(grafo, origen):
    distancia = {}
    visitado = set()
    for v in grafo:
        distancia[v] = float('inf')
    distancia[origen] = 0
    visitado.add(origen)
    q = deque()
    q.append(origen)
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if (w not in visitado):
                distancia[w] = distancia[v] + 1
                visitado.add(w) 
                q.append(w)
    return distancia

"""el orden del algoritmo seria O(n2)

B. una desventaja seria el uso de memoria seria O(n2), y en el peor de los casos seria tambien en tiempo O(n2)

"""

# Matías está en Barcelona y quiere recorrer un museo. Su idea es hacer un recorrido bastante lógico: empezar en una sala (al azar), 
# luego ir a una adyacente a ésta, luego a una adyancente a la segunda (si no fue visitada aún), y así hasta recorrer todas las salas. 
# Cuando no tiene más salas adyacentes para visitar (porque ya fueron todas visitadas), simplemente vuelve por donde vino buscando otras salas adyacentes. 
# Teniendo un grafo no dirigido, que representa el mapa del museo (donde los vértices son salas, y las aristas (v, w) indican que las salas v y w se encuentran conectadas),
# implementar un algoritmo que nos devuelva una lista con un recorrido posible de la idea de Matías para visitar las salas del museo. 
# Indicar el recorrido utilizado y el orden del algoritmo. Justificar.
def _dfs(grafo, visitados, vertice):
    visitados.add(vertice)
    #mati_disfruta_esta_sala(vertice)  funcion que simula que resuelve la funcion
    for ady in grafo.adyacentes(vertice):
        if ady not in visitados:
            _dfs(grafo, visitados, ady)

def dfs_generalizado(grafo):
    visitados = set()
    for vertice in grafo:
        if vertice not in visitados:
            _dfs(grafo, visitados, vertice)

# Escribir una función es_bipartito(grafo) que dado un grafo no dirigido devuelva true o false de acuerdo a si es bipartito o no. 
# Indicar y justificar el orden del algoritmo. ¿Qué tipo de recorrido utiliza?
def es_bipartito (grafo, vertice_inicial):
    colores = {}
    cola = deque()
    cola.append(vertice_inicial)
    colores[vertice_inicial] = 0 # definimos colores 0 y 1
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w in colores:
                if colores[w] == colores[v]: return False
            else:
                colores[w] = 1 - colores[v]
                cola.append(w)
    return True

def es_bipartito_generalizado(grafo):
	colores = { }
	for vertice in grafo:
		if vertice not in colores:
			if not es_bipartito(grafo, vertice, colores):
				return False
	return True

# Implementar un algoritmo que reciba un grafo dirigido, un vértice V y un número N, y devuelva una lista con todos los vértices que se encuentren
# a exactamente N aristas de distancia del vértice V. Indicar el tipo de recorrido utilizado y el orden del algoritmo. Justificar.

def vertices_a_distancia_n(grafo, v, n):
    if n == 0:
        return [v]
    visitados = set()
    visitados.add(v)
    orden = {v: 0}
    resultado = []
    q = deque()
    q.append(v)
    while q:
        u = q.popleft()
        if orden[u] > n:
            continue
        for w in grafo.adyacentes(u):
            if w not in visitados:
                visitados.add(w)
                orden[w] = orden [u] + 1
                if orden[w] == n:
                    resultado.append(w)
                q.append(w)
    return resultado

#  a. Dada la siguiente matriz de adyacencias, escribir la representación del grafo como una lista de adyacencias:
# |   | A | B | C | D | E | F |
# |---|---|---|---|---|---|---|
# | A | 0 | 7 | 5 | 0 | 3 | 8 |
# | B | 7 | 0 | 0 | 0 | 1 | 3 |
# | C | 5 | 0 | 0 | 5 | 3 | 2 |
# | D | 0 | 0 | 5 | 0 | 2 | 0 |
# | E | 3 | 1 | 3 | 2 | 0 | 0 |
# | F | 8 | 3 | 2 | 0 | 0 | 0 |
def traducc_matriz_a_lista(grafo: list[list[int]]) -> list[deque]:
    n = len(grafo)  # Número de nodos
    lista_adyacencias = [deque() for _ in range(n)]  # Lista de deques, uno por nodo
    
    # Recorrer la matriz de adyacencias
    for i in range(n):
        for j in range(n):
            if grafo[i][j] > 0:  # Si hay una arista (peso > 0)
                lista_adyacencias[i].append((j, grafo[i][j]))  # Agregar (nodo, peso)
    
    return lista_adyacencias
# b. ¿Qué complejidad tiene hacer esta traducción?
"""O(V + E)"""

# c. ¿Qué ventajas y desventajas encuentra en cada representación? Explicar teniendo en cuenta cuestiones de espacio y tiempo según las operaciones que admite un grafo y 
# considerar que las listas de adyacencias es un diccionario de listas.
""" Matriz adyacencia
O(V2) memoria
O(V) (redim) agregar vertice
O(1) agregar arista
O(1) Ver si A → B
O(V2) Sacar vértice
O(1) Sacar arista
Lista adyacencia
O(V + E) memoria
-OLL(V) -ODL(1) agregar vertice
O(V) agregar arista
O(V)  Ver si A → B
O(V+E) Sacar vértice
O(V) Sacar arista
"""

#  Un autor decidió escribir un libro con varias tramas que se puede leer de forma no lineal. Es decir, por ejemplo, después del capítulo 1 puede leer el 2 o el 73; 
# pero la historia no tiene sentido si se abordan estos últimos antes que el 1.

# Siendo un aficionado de la computación, el autor ahora necesita un orden para publicar su obra, y decidió modelar este problema como un grafo dirigido, 
# en dónde los capítulos son los vértices y sus dependencias las aristas. Así existen, por ejemplo, las aristas (v1, v2) y (v1, v73).

# Escribir un algoritmo que devuelva un orden en el que se puede leer la historia sin obviar ningún capítulo. Indicar la complejidad del algoritmo.

def topologico_grados(grafo):
    _, g_ent = grados_vertices(grafo)
    q = deque()
    resultado = []
    for v in grafo: # O(V)
        if g_ent[v] == 0:
            q.append(v)

    while q:
        v = q.popleft()
        resultado.append(v)
        for w in grafo.adyacentes(v):
            g_ent[w] -= 1
            if g_ent[w] == 0:
                q.append(w)
    return resultado


# Dado un número inicial X se pueden realizar dos tipos de operaciones sobre el número:
# Multiplicar por 2
# Restarle 1.
# Implementar un algoritmo que encuentra la menor cantidad de operaciones a realizar para convertir el número X en el número Y, 
# con tan solo las operaciones mencionadas arriba (podemos aplicarlas la cantidad de veces que querramos).

def convertir_x_y_menor(x, y):
    padres = {x: None}
    visitados = set()
    visitados.add(x)
    q = deque()
    q.append(x)
    while q:
        v = q.popleft()
        if v == y:
            return padres
        if (2 * v) not in visitados:
            visitados.add(2*v)
            padres[2*v] = v
            q.append(2 * v)
        if (v - 1) not in visitados:
            visitados.add(v-1)
            padres[v-1] = v
            q.append(v - 1)
    return None

# recorrido_padres = convertir_x_y_menor(4, 17)
# v = 17
# while v is not None:
#     print(v)
#     v = recorrido_padres[v]


# Se tiene un arreglo de palabras de un lenguaje alienigena. Dicho arreglo se encuentra ordenado para dicho idioma (no conocemos el orden de su abecedario).
# Implementar un algoritmo que reciba dicho arreglo y determine un orden posible para las letras del abecedario en dicho idioma. Por ejemplo:
# {"caa", "acbd", "acba", "bac", "bad"} --> ['c', 'd', 'a', 'b']
def idioma_alien(palabras):
    grafo = grafo_desde_palabras(palabras)
    grados = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            grados[w] = grados.get(w, 0) + 1

    cola = deque()
    for v in grafo:
        if v not in grados:
            cola.append(v)
    
    result = []
    while len(cola) > 0:
        v = cola.popleft()
        result.append(v)
        for ady in grafo.adyacentes(v):
            grados[ady] = grados[ady] - 1
            if grados[ady] == 0:
                cola.append(ady)
    
    return result

def grafo_desde_palabras(palabras):
    grafo = Grafo(es_dirigido=True)
    for i in range(len(palabras) - 1):
        p1 = palabras[i]
        p2 = palabras[i+1]
        
        for letra in p1: grafo.agregar_vertice(letra)
        
        for j in range(len(p1)):
            if p1[j] != p2[j]:
                grafo.agregar_vertice(p2[j])
                grafo.agregar_arista(p1[j], p2[j], 9)
                break     
    return grafo

# Implementar un algoritmo que reciba un grafo dirigido y nos devuelva la cantidad de componentes débilmente conexas de este. 
# Indicar y justificar la complejidad del algoritmo implementado.

def dfs_comps(grafo, v, visitados, componente):
    visitados.add(v)
    componente.append(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs_comps(grafo, w, visitados, componente)

def contar_componetes_conexas(grafo):
    visitados = set()
    comps = 0
    resultado = []
    for v in grafo:
        if v not in visitados:
            nueva_componente = []
            resultado.append(nueva_componente)
            comps += 1
            dfs_comps(grafo, v, visitados, nueva_componente)
    return resultado

# Contamos con un grafo dirigido que modela un ecosistema. En dicho grafo, cada vértice es una especie, y cada arista (v, w) indica que v es depredador natural de w.
# Considerando la horrible tendencia del ser humano por llevar a la extinción especies, algo que nos puede interesar es saber si existe alguna especie que, si llegara a desaparecer,
# rompería todo el ecosistema: quienes la depredan no tienen un sustituto (y, por ende, pueden desaparecer también) y/o quienes eran depredados por esta ya no tienen amenazas,
# por lo que crecerán descontroladamente.
# Implementar un algoritmo que reciba un grafo de dichas características y devuelva una lista de todas las especies que cumplan lo antes mencionado. 
# Indicar y justificar la complejidad del algoritmo implementado.

def especies_isdispensables(grafo):
    g_sal, g_ent = grados_vertices(grafo)
    especies = {}
    for v in grafo: # O(V)
        for w in grafo.adyacentes(v):
            if g_sal[v] == 1:
                especies.add(w)
            if g_ent[w] == 1:
                especies.add(v)
    return especies

    

# El diámetro de una red es el máximo de las distancias mínimas entre todos los vértices de la misma. Implementar un algoritmo que permita obtener el diámetro de una red, 
# para el caso de un grafo no dirigido y no pesado. Indicar el orden del algoritmo propuesto.

def asddsalkl():
    pass

# a. Obtener una representación del camino mínimo desde el vértice A en el siguiente grafo (representado con una matriz de adyacencias), 
# hacia todos los demás vértices, utilizando el algoritmo de Dijkstra:

# |   | A | B | C | D | E | F |
# |---|---|---|---|---|---|---|
# | A | 0 | 7 | 5 | 0 | 3 | 8 |
# | B | 7 | 0 | 0 | 0 | 1 | 3 |
# | C | 5 | 0 | 0 | 5 | 3 | 2 |
# | D | 0 | 0 | 5 | 0 | 2 | 0 |
# | E | 3 | 1 | 3 | 2 | 0 | 0 |
# | F | 8 | 3 | 2 | 0 | 0 | 0 |

# b. ¿Qué condiciones debe cumplir el grafo para poder aplicar el algoritmo de Dijkstra? ¿Qué característica tiene el grafo si al finalizar la ejecución del algoritmo,
# uno o más vértices quedan a distancia infinita?
"""A para B = A, E, B
A para C = A, C
A para D = A, E, D
A para E = A, E
A para F = A, C , F

las condiciones para poder usar el algoritmo de dijkstra son que tiene que ser un grafo pesado, y los pesos no tienen que ser negativos ya que si los pesos son negativos
el alroitmo entraria en bucle.
si al finalizar si uno o mas vertice tiene distancia infinita, quiere decir que no se puede llegar de A a ese vertice, y el grafo no es conexo
"""

# a. Obtener una representación del camino mínimo desde el vértice A en el siguiente grafo (representado con una matriz de adyacencias), hacia todos los demás vértices, 
# utilizando el algoritmo de Bellman-Ford.
"""mirar grafo guia"""
# grafo bf 
# b. Volver a realizar, suponiendo que la arista de B a A ahora tiene un peso de 1.
""" se itera (V) veces.
  primera iteracion          segunda iteracion    
a.   padre  |  dist             padre  |  dist
   A: B     | A: 5            A: B     | A: 5 
   B: F     | B: -2           B: F     | B: -2
   C: A     | C: -1           C: A     | C: -1
   D: A     | D: -4           D: A     | D: -4
   E: G     | E: 1            E: G     | E: 1
   F: D     | F: -3           F: D     | F: -3
   G: C     | G: -2           G: C     | G: -2
   H: D     | H: 4            H: D     | H: 4

B.  padre  |  dist
   A:  B    | A: -1
   B:  F   | B: -2
   C:  G    | C: -3
   D:  a    | D: -4
   E: g     | E: -2
   F:  D    | F: -3
   G:  A    | G: -5
   H:  C   | H: 2
"""

# Obtener el Árbol de Tendido Mínimo del siguiente grafo:
# a. Utilizando el Algoritmo de Kruskal.
# b. Utilizando el Algoritmo de Prim.
"""mirar grafo guia"""
# grafo mst
"""
PRIM SIRVE PARA CUANDO HAY UNA COMPONENTE CONEXA
PRIM: F - B, B - A, A - E, E - G, E - C, C - H, H - I, H - D
KRUSKAL SIRVE PARA CUANDO HAY MAS DE UNA COMPONENTE CONEXA
KRUSKAL: F-B, B-A, A-E , C-E, C-H , E-G, H-I, D-H, D-F

"""
# Dadas las matrices de adyacencia M1, M2 y M3, responder las siguientes preguntas (recomendamos pasar los grafos a una representación visual para mayor facilidad):
# a. ¿Puede ser el grafo definido por M2 un árbol de tendido mínimo de M1? Justificar.
# b. Realizar un seguimiento de aplicar el algoritmo de Kruskal para obtener un árbol de tendido mínimo del grafo definido por M3.

# | M1 | A | B | C | D | E | F | G |
# |----|---|---|---|---|---|---|---|
# | A  | 0 | 3 | 4 | 0 | 0 | 0 | 0 |
# | B  | 3 | 0 | 5 | 3 | 3 | 0 | 0 |
# | C  | 4 | 5 | 0 | 2 | 0 | 0 | 6 |
# | D  | 0 | 3 | 2 | 0 | 4 | 2 | 1 |
# | E  | 0 | 3 | 0 | 4 | 0 | 6 | 0 |
# | F  | 0 | 0 | 0 | 2 | 6 | 0 | 0 |
# | G  | 0 | 0 | 6 | 1 | 0 | 0 | 0 |

# | M2 | A | B | C | D | E | F | G |
# |----|---|---|---|---|---|---|---|
# | A  | 0 | 3 | 4 | 0 | 0 | 0 | 0 |
# | B  | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
# | C  | 4 | 0 | 0 | 2 | 0 | 0 | 6 |
# | D  | 0 | 0 | 2 | 0 | 0 | 2 | 0 |
# | E  | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
# | F  | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
# | G  | 0 | 0 | 6 | 0 | 0 | 0 | 0 |
"""
M2, no puede ser arbol de tendido, ya que tiene una arista de A-C, teniendo un recorrido mas corto por C-D, y el arbol de tendido minimo de M1
es: C-D, D-H, D-F, D-B, B-A, B-E, C-G,
"""

# Responder las siguientes preguntas, justificando la respuesta:
# a. Al aplicar sobre un grafo el algoritmo de Dijkstra para encontrar caminos mínimos desde un vértice v cualquiera, se obtiene un árbol definido por el diccionario de padres 
# (que permite reconstruir dichos caminos mínimos). Dicho árbol, ¿es siempre de tendido mínimo?
"""si, pero de del vertice V a otro vertice, no de todo el grafo"""

# b. Al obtener un árbol de tendido mínimo de un grafo, se asegura que la suma de los pesos de las aristas sean mínimos. 
# ¿Es posible utilizar el árbol de tendido mínimo para encontrar el camíno mínimo entre dos pares de vértices cualesquiera?
"""no es posible"""

# c. Si un grafo es no pesado, ¿Se puede utilizar el Algoritmo de Dijkstra para obtener los caminos mínimos en dicho grafo?
"""no, ya que al encolar las aristas al heap de dijkstra seria inutil, te conviene utilizar bfs, o dfs"""

# Implementar un algoritmo que, dado un grafo dirigido, un vértice s y otro t determine la cantidad mínima de aristas que deberían cambiar de sentido en el
# grafo para que exista un camino de s a t.
def cantidad_minima_inversiones(grafo, s, t):
    pesado = Grafo()
    for v in grafo:
        if not v in pesado:
            pesado.add(v)
        for w in grafo.adyacentes(v):
            if not w in pesado:
                pesado.add(w)
                pesado.add(v, w, 0)
            if not grafo.contiene_arista(w, v):
                pesado.add(w, v, 1)

    return dijkstra(pesado, s, t)

def dijkstra(grafo, s, t):
    distancia = {}
    for v in grafo:
        distancia[v] = float("inf")
    distancia[s] = 0
    # q = Heap()
    q = deque()
    q.encolar(s, 0)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if distancia[v] + grafo.peso_arista(v, w) < distancia[w]:
                distancia[w] = distancia[v] + grafo.peso_arista(v, w)
                q.encolar(w, distancia[w])
    return distancia[t]


# Como todos sabemos, Taller de Programación I implica programar mucho. El equipo de Federico esta desarrollando un Age of Empires y le asignaron el modulo de movimientos.
# Dispone de un mapa, podríamos decir una grilla, donde se puede ver para cada celda su contenido (por ejemplo si está libre, si es agua, un árbol, etc). 
# Fede tiene que implementar un algoritmo que, a partir de una unidad (por ejemplo un soldado), en una celda en especifico encuentre el camino a una celda objetivo.
# Considerar que entre celdas puede haber diferencia de alturas por lo que puede costarle mas (o menos) a una unidad ir de una celda a otra. 
# Por supuesto que no puede ser cualquier camino, si no el que haga que la unidad llegue más rápido a su objetivo.

# a. Modelar el problema usando Grafos especificando de forma completa todos sus componentes.
""""""
# b. Implementar un algoritmo que a partir de una celda de origen y una de destino, retorne el camino que tiene que hacer la unidad, indicando y justificando la complejidad final.


# Daniel está a punto de casarse y tiene un problema: gastó casi todo su dinero en la luna de miel. Contrató un salón para la fiesta donde sólo hay 2 mesas (muy, muy grandes,
#  pero 2 en fin). Debe repartir a los $n$ invitados entre las dos mesas, y su esposo le indicó una condición: en cada mesa debe sentarse gente que se lleve bien entre todos ellos.
# Daniel cuenta con la información de quién se lleva bien con quién, y necesita poder determinar si hay alguna forma de separar en dos grupos de gente donde en cada grupo 
# todos se lleven bien entre sí.

# a. Modelar este problema utilizando grafos, indicando claramente qué son los vértices y qué las aristas.

# b. Implementar un algoritmo que reciba un grafo como el modelado en el punto (a) y devuelva ambos grupos de personas. Indicar y justificar la complejidad del algoritmo implementado.
"bipartito "
# IMPORTANTE: tener en cuenta que resolver el problema de forma directa puede ser difícil. Recomendamos plantearse el problema inverso:
# poder separar en dos grupos tal que en ningúno de los grupos haya un par que no se lleven bien.

""""""

#  Implementar un algoritmo que reciba un grafo no dirigido y determine la cantidad mínima de aristas que debería agregársele para que el grafo sea conexo. 
# Obviamente, si el grafo ya es conexo el algoritmo debe devolver 0. Indicar y justificar la complejidad del algoritmo implementado.
