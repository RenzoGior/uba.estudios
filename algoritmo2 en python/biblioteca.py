import heapq
import grafo
from collections import deque

def camino_minimo_dijkstra(g, origen, destino):
    distancia = {}
    padre = {}
    for v in g.obtener_vertices():
       distancia[v] = float("inf")
    distancia[origen] = 0
    padre[origen] = None
    heap = []
    heapq.heappush(heap,(0, origen))
    while len(heap) != 0:
       _, v = heapq.heappop(heap)
       if v == destino:
           return padre, distancia
       for w in g.adyacentes(v):
           if (distancia[v] + g.peso_arista(v,w) < distancia[w]):
               distancia[w] = distancia[v] + g.peso_arista(v,w)
               padre[w] = v
               heapq.heappush(heap,(distancia[w], w))
    return padre, distancia

def reconstruir_camino(padres, destino):
    recorrido = []
    while destino is not None:
        recorrido.append(destino)
        destino = padres[destino]
    return recorrido[::-1]

def camino_minimo_bfs(g, origen):
    padre = {}
    visitados = set()
    orden = {}
    padre[origen] = None
    orden[origen] = 0
    visitados.add(origen)
    bfs(g, origen, padre, visitados, orden)
    return padre, orden

def bfs(g, inicial, padre, visitados, orden):
    cola = deque()
    cola.append(inicial)
    while len(cola) != 0:
        v = cola.popleft()
        for w in g.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padre[w] = v
                orden[w] = orden[v]+1
                cola.append(w)

def centralidad(g):
    cent = {}
    for v in g.obtener_vertices():
        cent[v] = 0
    for v in g.obtener_vertices():
        padre, distancia = camino_minimo_dijkstra(g, v, None)
        cent_aux = {}
        for w in g.obtener_vertices():
            cent_aux[w] = 0
        vertices_ordenados = ordenar_vertices(distancia)
        for w in vertices_ordenados:
            if padre[w] == None:
                continue
            cent_aux[padre[w]] += 1 + cent_aux[w]
        for w in g.obtener_vertices():
            if w == v:
                continue
            cent[w] += cent_aux[w]
    return cent

def ordenar_vertices(distancia):
    vertices_ordenados = sorted(distancia.keys(), key=lambda v:distancia[v], reverse=True)
    for indice, vertice in enumerate(vertices_ordenados):
        if distancia[vertice] == float("inf"):
            vertices_ordenados.pop(indice)
    return vertices_ordenados 

def orden_topologico_dfs(g):
    visitados = set()
    pila = deque()
    for v in g.obtener_vertices():
        if v not in visitados:
            visitados.add(v)
            _dfs(g, v, visitados, pila)
    res = []
    while len(pila) != 0:
        res.append(pila.pop())
    return res

def _dfs(g, v, visitados, pila):
    for w in g.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _dfs(g, w, visitados, pila)
    pila.append(v)

def mst_prim(g):
    v = g.vertice_aleatorio()
    visitados = set()
    visitados.add(v)
    q = []
    for w in g.adyacentes(v):
        heapq.heappush(q, (g.peso_arista(v,w),v,w))
    arbol = grafo.Grafo(es_dirigido=False, vertices=g.obtener_vertices())
    while len(q) != 0:
        peso,v,w = heapq.heappop(q)
        if w in visitados:
            continue
        arbol.agregar_arista(v,w,peso)
        visitados.add(w)
        for x in g.adyacentes(w):
            if x not in visitados:
                heapq.heappush(q,(g.peso_arista(w,x),w,x))
    return arbol

def camino_minimo(grafo, origen):
    distancia, padre, visitado = {}, {}, {}
    for v in grafo:
        distancia[v] = float('inf')
    distancia[origen] = 0
    padre[origen] = None
    visitado[origen] = True
    q = deque()
    q.append(origen)
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if (v not in visitado):
                distancia[w] += distancia[v] + 1
                padre[w] = v
                visitado[w] = True
                q.append(w)
    return padre, distancia

def reconstruir_camino(padres, destino):
    recorrido = []
    while destino is not None:
        recorrido.append(destino)
        destino = padres[destino]
    if len(recorrido) > 6:
        return False
    return recorrido[::-1]




PAISES = ["ARG", "BRA", "URU", "CHI", "PER", "PAR", "BOL", "ECU", "VEN", "COL", "SUR", "GUY", "GUF", "POL", "ALE", "FRA", "AUS"]
g = grafo.Grafo(False, PAISES)
print(f"{g} \n vertices solos")
g.agregar_arista("ARG", "URU")
print(f"{g},\n 1 arista")
g.agregar_arista("ARG", "CHI")
print(f"{g},\n 2 arista")
g.agregar_arista("ARG", "BOL")
print(f"{g},\n 3 arista")
g.agregar_arista("ARG", "BRA")
print(f"{g},\n 4 arista")
g.agregar_arista("ARG", "PAR")
print(f"{g},\n 5 arista")
g.agregar_arista("BRA", "URU")
print(f"{g},\n 6 arista")
g.agregar_arista("BRA", "PAR")
print(f"{g},\n 7 arista")
g.agregar_arista("BRA", "BOL")
print(f"{g},\n 8 arista")
g.agregar_arista("BRA", "SUR")
print(f"{g},\n 9 arista")
g.agregar_arista("BRA", "GUF")
g.agregar_arista("BRA", "GUY")
g.agregar_arista("BRA", "VEN")
g.agregar_arista("BRA", "COL")
g.agregar_arista("BRA", "PER")
g.agregar_arista("CHI", "BOL")
g.agregar_arista("CHI", "PER")
g.agregar_arista("PAR", "BOL")
g.agregar_arista("PER", "BOL")
g.agregar_arista("ECU", "PER")
g.agregar_arista("ECU", "COL")
g.agregar_arista("COL", "PER")
g.agregar_arista("COL", "VEN")
g.agregar_arista("VEN", "GUY")
g.agregar_arista("SUR", "GUY")
g.agregar_arista("SUR", "GUF")
g.agregar_arista("POL", "ALE")
g.agregar_arista("ALE", "FRA")
