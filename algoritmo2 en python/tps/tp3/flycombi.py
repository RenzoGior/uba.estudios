import biblioteca
import grafo
import sys
import heapq
from collections import deque


def ingresar_aeropuertos(ruta, grafo_dinero, grafo_tiempos, grafo_frecuencias, ciudades, coordenadas):
    with open(ruta) as archivo:
        for linea in archivo:
            linea = linea.rstrip().split(",")
            aeropuerto = linea[1]
            ciudad = linea[0]
            latitud, longitud = linea[2], linea[3]
            coordenadas[aeropuerto] = (latitud, longitud)
            grafo_dinero.agregar_vertice(aeropuerto)
            grafo_tiempos.agregar_vertice(aeropuerto)
            grafo_frecuencias.agregar_vertice(aeropuerto)
            if ciudad not in ciudades:
                ciudades[ciudad] = [aeropuerto]
            else:
                ciudades[ciudad].append(aeropuerto)

def ingresar_vuelos(ruta, grafo_dinero, grafo_tiempos, grafo_frecuencias):
    with open(ruta) as archivo:
        for linea in archivo:
            linea = linea.rstrip().split(",")
            origen, destino = linea[0], linea[1]
            tiempo, precio, frecuencia = linea[2], linea[3], linea[4]
            grafo_dinero.agregar_arista(origen, destino, int(precio))
            grafo_tiempos.agregar_arista(origen, destino, int(tiempo))
            grafo_frecuencias.agregar_arista(origen, destino, 1/(int(frecuencia)))

def camino_minimo(origen, destino, ciudades, g):
    camino_minimo = {}
    padres_camino_minimo = {}
    minimo = float("inf")
    for aeropuerto_origen in ciudades[origen]:
        for aeropuerto_destino in ciudades[destino]:
            padres, distancia = biblioteca.camino_minimo_dijkstra(g, aeropuerto_origen, aeropuerto_destino)
            if camino_minimo == {} or distancia[aeropuerto_destino] < minimo:
                camino_minimo = distancia
                padres_camino_minimo = padres
                minimo = distancia[aeropuerto_destino]
                destino_definitivo = aeropuerto_destino
    res = biblioteca.reconstruir_camino(padres_camino_minimo, destino_definitivo)
    return res

def camino_minimo_escalas(origen, destino, ciudades, g):
    camino_minimo = {}
    padres_camino_minimo = {}
    minimo = float("inf")
    for aeropuerto_origen in ciudades[origen]:
        for aeropuerto_destino in ciudades[destino]:
            padres, distancia = biblioteca.camino_minimo_bfs(g, aeropuerto_origen)
            if camino_minimo == {} or distancia[aeropuerto_destino] < minimo:
                camino_minimo = distancia
                padres_camino_minimo = padres
                minimo = distancia[aeropuerto_destino]
                destino_definitivo = aeropuerto_destino
    res = biblioteca.reconstruir_camino(padres_camino_minimo, destino_definitivo)
    return res

def obtener_centralidad(g, n):
    #Obtiene los n aeropuertos principales

    cent = biblioteca.centralidad(g)
    heap = []
    res = []

    for v,centralidad in cent.items():
        heapq.heappush(heap, (-centralidad,v))
        #Se guarda la centralidad en negativo ya que el heap de python es de minimos, y nosotros queremos los maximos

    i=0
    while len(heap) != 0 and i < n:
        _, v = heapq.heappop(heap)
        res.append(v)
        i+=1

    return res

def crear_itinerario(ruta):
    g = grafo.Grafo(True)
    with open(ruta) as archivo:
        primera_linea = archivo.readline()
        ciudades = primera_linea.rstrip().split(",")
        for ciudad in ciudades:
            g.agregar_vertice(ciudad)
        for linea in archivo:
            linea = linea.rstrip().split(",")
            ciudad1, ciudad2 = linea[0], linea[1]
            g.agregar_arista(ciudad1, ciudad2)
    return g

def crear_rutas(ruta, arbol, grafo_tiempos, grafo_frecuencias):
    visitados = set()
    with open(ruta, "w") as archivo:
        for v in arbol.obtener_vertices():
            for w in arbol.adyacentes(v):
                if w in visitados:
                    continue
                precio = arbol.peso_arista(v,w)
                tiempo = grafo_tiempos.peso_arista(v,w)
                frecuencia = grafo_frecuencias.peso_arista(v,w)
                frecuencia = int(frecuencia**(-1)) #se eleva a la -1 ya que se habia guardado como 1/frecuencia
                archivo.write(f"{v},{w},{tiempo},{precio},{frecuencia}\n")
            visitados.add(v) #Permite no agregar la arista de vuelta. (Si se agregó A -> B, no se agrega B -> A)

def crear_kml(ruta, camino, coordenadas):
    with open(ruta, "w") as archivo:
        archivo.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<kml xmlns="http://earth.google.com/kml/2.1">\n'
            '    <Document>\n'
            '        <name>Ruta del ultimo comando ejecutado</name>\n'
            "\n"
        )

        for aeropuerto in camino:
            latitud, longitud = coordenadas[aeropuerto]
            archivo.write('        <Placemark>\n')
            archivo.write(f'            <name>{aeropuerto}</name>\n')
            archivo.write('            <Point>\n')
            archivo.write(f'                <coordinates>{longitud}, {latitud}</coordinates>\n')
            archivo.write('            </Point>\n')
            archivo.write('        </Placemark>\n')
        archivo.write("\n")
        
        i = 0
        for aeropuerto in camino:
            if i > len(camino)-2:
                break
            aeropuerto1 = camino[i]
            aeropuerto2 = camino[i+1]
            latitud1, longitud1 = coordenadas[aeropuerto1]
            latitud2, longitud2 = coordenadas[aeropuerto2]
            archivo.write('        <Placemark>\n')
            archivo.write('            <LineString>\n')
            archivo.write(f'                <coordinates>{longitud1}, {latitud1} {longitud2}, {latitud2}</coordinates>\n')
            archivo.write('            </LineString>\n')
            archivo.write('        </Placemark>\n')
            i+=1
        
        archivo.write(
            '    </Document>\n'
            '</kml>\n'
        )



def main():
    argumentos = sys.argv
    argumentos = argumentos[1:]
    if len(argumentos) != 2:
        raise Exception("Parametros invalidos")
    aeropuertos = argumentos[0]
    vuelos = argumentos[1]

    pila = deque()

    grafo_dinero = grafo()
    grafo_tiempos =  grafo()
    grafo_frecuencias = grafo()

    ciudades = {} 
    coordenadas = {}

    ingresar_aeropuertos(aeropuertos, grafo_dinero, grafo_tiempos, grafo_frecuencias, ciudades, coordenadas)
    ingresar_vuelos(vuelos, grafo_dinero, grafo_tiempos, grafo_frecuencias)

    for linea in sys.stdin:
        comando, parametros = linea.strip(" ", 1)
        parametros = parametros.rstrip().split(",")


        if comando == "camino_mas":
            if len(parametros) != 3:
                print("Error de parametros")
                continue

            criterio, origen, destino = parametros[0], parametros[1], parametros[2]

            if criterio == "barato":
                g = grafo_dinero
            elif criterio == "rapido":
                g = grafo_tiempos
            else:
                print("Error de parametros")
                continue

            if origen not in ciudades or destino not in ciudades:
                print("Error de parametros")
                continue

            res = camino_minimo(origen, destino, ciudades, g)
            pila.append(res)
            print(" -> ".join(res))


        elif comando == "camnino_escalas":
            g = grafo_frecuencias
            if len(parametros) != 2:
                print("Error de parametros")
                continue

            origen, destino = parametros[0], parametros[1]
            g = grafo_dinero

            if origen not in ciudades or destino not in ciudades:
                print("Error de parametros")
                continue

            res = camino_minimo_escalas(origen, destino, ciudades, g)
            pila.append(res)
            print(" -> ".join(res))

        elif comando == "centralidad":
            if len(parametros) != 1:
                print("Error de parametros")
                continue

            n = parametros[0]
            if not n.isdigit():
                print("Error de parametros")
                continue
            
            n = int(n)
            g = grafo_frecuencias

            res = obtener_centralidad(g, n)
            print(", ".join(res))

        elif comando == "itenerario":
            if len(parametros) != 1:
                print("Error de parametros")

            ruta = parametros[0]
            grafo_ciudades = crear_itinerario(ruta)
            orden = biblioteca.orden_topologico_dfs(grafo_ciudades)
            print(", ".join(orden))

            for i in range(len(orden)-1):
                origen, destino = orden[i], orden[i+1]
                res = camino_minimo_escalas(origen, destino, ciudades, grafo_frecuencias)
                print(" -> ".join(res))

        elif comando == "nueva_aerolinea":
            if len(parametros) != 1:
                print("Error de parametros")
                continue
            ruta = parametros[0]
            arbol = biblioteca.mst_prim(grafo_dinero)
            crear_rutas(ruta, arbol, grafo_tiempos, grafo_frecuencias)
            print("OK")

        elif comando == "exportar_kml":
            if len(parametros) != 1:
                print("Error de parametros")
                continue
            ruta = parametros[0]
            if len(pila) == 0:
                print("No se ha ejecutado un comando anteriormente")
                continue
            camino = pila.pop()
            crear_kml(ruta, camino, coordenadas)
            print("OK")
    
main()