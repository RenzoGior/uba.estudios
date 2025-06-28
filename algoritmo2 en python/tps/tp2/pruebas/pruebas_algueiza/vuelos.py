import heapq
import csv

# Es necesario implementar una interfaz del programa, que leerá por entrada estándar los siguientes comandos:


"""
PENSAR SI HACERLO CON UN AVL O ABB, O COMO LO ESTABA HACIENDO. 
"""

class Vuelos:
    def __init__(self):
        self.lista_vuelos = [] 
        self.vuelos = {}

# agregar_archivo <nombre_archivo>: procesa de forma completa un archivo de .csv que contiene datos de vuelos.

# Agregar_archivo: El mantenimiento para actualizar los vuelos debe ser O(V log n) siendo V la cantidad de vuelos en el nuevo archivo y n la cantidad total de vuelos en el sistema.
    def agregar_archivo(self, nombre: str) -> None:
        try:
            with open(nombre,'r') as f:
                f_reader = csv.reader(f,delimiter=',')
                for line in f_reader:
                    if line[0] in self.vuelos:
                        self.vuelos[line[0]] = line[1:]
                        indice = self.lista_vuelos.index(line[0])  #otra solucion agregarle un indice cuando leemos la linea, para hacer mas eficiente
                        self.lista_vuelos.pop(indice, None)
                        self.lista_vuelos.append(line)
                    else:
                        self.vuelos[line[0]] = line[1:]  
                        self.lista_vuelos.append(line)
                self.lista_vuelos.sort(key=lambda x: x[6])
            print("OK")
        except Exception as e:
            print("Error inexperado:", e)

# ver_tablero <K cantidad vuelos> <modo: asc/desc> <desde> <hasta>: muestra los K vuelos ordenados por fecha de forma ascendente (asc) o descendente (desc),
# # cuya fecha de despegue esté dentro de el intervalo <desde> <hasta> (inclusive).

# Ver_tablero: debe ser O(v) en el peor caso (en el que se tenga que mostrar todos los vuelos del sistema), O(logv) en un caso promedio
# (en el caso en el que no se pidan mostrar demasiados visitantes). v es la cantidad de vuelos.
    def ver_tablero(self , cantidad: int, modo , desde: str, hasta: str) -> list:
        inicio, fin = buscar_limite_inferior(self.lista_vuelos, desde), buscar_limite_superior(self.lista_vuelos, hasta)
        vuelos = []
        for i in self.vuelos[inicio:fin]:
            if cantidad == 0:
                break
            vuelos.append(i)
            cantidad -= 1
        if modo == "desc":
            return vuelos[::-1]
        return vuelos
        
# info_vuelo <código vuelo>: muestra toda la información posible en sobre el vuelo que tiene el código pasado por parámetro.
# Info_vuelo: debe ser O(1).
    def info_vuelo(self, codigo: str) -> str:
        if codigo in self.vuelos:
            print(f"{self.vuelos[codigo]}")
        else:
            raise Exception("el codigo de vuelo no se encuentra")
    
# prioridad_vuelos <K cantidad vuelos>: muestra los códigos de los K vuelos que tienen mayor prioridad.
# Prioridad_vuelos: debe ser O(n+Klogn). Siendo K la cantidad de vuelos a mostrar y n la cantidad de vuelos en el sistema.
    def prioridad_vuelos(self, cantidad):
        copia = [(sublista[5], sublista[0]) for sublista in self.lista_vuelos[:]]
        return heapq.nlargest(cantidad, copia)

# siguiente_vuelo <aeropuerto origen> <aeropuerto destino> <fecha>: muestra la información del vuelo (tal cual en info_vuelo) 
# del próximo vuelo directo que conecte los aeropuertos de origen y destino, a partir de la fecha indicada (inclusive).
# Si no hay un siguiente vuelo cargado, imprimir No hay vuelo registrado desde <aeropuerto origen> hacia <aeropuerto destino> desde <fecha> (con los valores que correspondan).

# Siguiente_vuelo: debe ser O(log F conexion), siendo Fconexion la cantidad de fechas diferentes en las que se puede hacer dicho viaje 
# (si todos los vuelos de esa conexión son en fechas diferentes, sería lo mismo que la cantidad de vuelos que hacen dicha conexión). Considerar que F conexion 
# es mucho menor a la cantidad de vuelos totales y cantidad de fechas totales.
    def siguiente_vuelo(self, origen, destino, fecha):
        try:
            vuelo = busqueda_binaria(self.lista_vuelos, fecha) 
            if vuelo == -1: return Exception("no hay vuelos en esa fecha")
            if origen == vuelo[2] and destino == vuelo[3]:
                print(f"{vuelo[0]} {vuelo[1]} {vuelo[2]} {vuelo[3]} {vuelo[4]} {vuelo[5]} {vuelo[6]} {vuelo[7]} {vuelo[8]} {vuelo[9]}")
            print("OK")
        except Exception as e:
            print("Error inexperado:", e)
        
# borrar <desde> <hasta>: borra todos los vuelos cuya fecha de despegue estén dentro del intervalo <desde> <hasta> (inclusive).
# Borrar: debe ser O(Klogn) . Siendo K la cantidad de vuelos que hay en el rango de fechas ingresado y n la cantidad de vuelos en todo el sistema
    def borrar(self, desde, hasta):
        try:
            inicio, fin = buscar_limite_inferior(self.lista_vuelos, desde), buscar_limite_superior(self.lista_vuelos, hasta)
            vuelos_eliminar = self.lista_vuelos[inicio:fin]
            for vuelo in vuelos_eliminar:
                self.vuelos.pop(vuelo[0], None)
            self.lista_vuelos[inicio:fin] = []
            print(vuelos_eliminar)
            print("OK")
        except Exception as e:
            print("Error inexperado", e)

    # Si un comando es válido deberá imprimir OK por salida estándar después de ser ejecutado (esto incluso en el caso que no haya un siguiente vuelo en siguiente_vuelo). 
    # Si un comando no pertenece a los listados previamente o tiene un error, se imprime Error en comando <comando> por stderr y continua la ejecución.
    # El programa no tendrá un comando para terminar. Este finaliza cuando no quedan más líneas para procesar por entrada estándar. 
    # Al finalizar, es importante que se cierren correctamente todos los archivos procesados.

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio][6] == objetivo:
            return medio
        elif lista[medio][6] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def buscar_limite_inferior(arr, target):
    izquierda, derecha = 0, len(arr)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio][6] < target:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda

def buscar_limite_superior(arr, target):
    izquierda, derecha = 0, len(arr)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio][6] <= target:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda



# indice_inicio = buscar_limite_inferior(arr, inicio)
# indice_fin = buscar_limite_superior(arr, fin)
# arr =[]
# arr[indice_inicio:indice_fin]

# '2018-05-03T12:10:32'
# '2018-12-24T22:58:13'
# rango = busqueda_binaria_rango(archivo_ordenado,'2018-05-03T12:10:32', '2018-12-24T22:58:13')
# def asd(rango):
#     contador = 0
#     for i in rango:
#         contador +=1 
#         print(i, contador)
# asd(rango)

# def agregar_archivo(nombre: str) -> None:
#         with open(nombre,'r') as f:
#             contador = 0
#             f_reader = csv.reader(f,delimiter=',')
#             ordenados = []
#             for line in f_reader:
#                 ordenados.append(line)
#                 # print(line )
#                 contador += 1
#             ordenados.sort(key=lambda x: x[6])
#             # for i in ordenados:
#             #     print(i)
#             # print(ordenados, end="\n")
#             return ordenados
# archivo = "vuelos-algueiza-parte-05.csv"
# archivo_ordenado = agregar_archivo(archivo)