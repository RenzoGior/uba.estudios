from collections import deque


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

# Dado un árbol binario, escribir una primitiva recursiva que determine la altura del mismo. 
# Indicar y justificar el orden de la primitiva.

def altura(nodo): 
    if nodo == None: return -1
    altura_izq = altura(nodo.izq)
    altura_der = altura(nodo.der)
    return 1 + max(altura_izq, altura_der)

"""el orden de la de la primita es O(n) ya que revisa todo el arbol de manera recursiva"""

# Implementar una primitiva que devuelva la suma de todos los datos (números) de un árbol binario. 
# Indicar y justificar el orden de la primitiva.

def suma_total(nodo):
    if nodo == None: return 0
    # suma
    # suma_total(nodo.izq, suma + nodo.dato)
    # suma_total(nodo.der, suma + nodo.dato)
    return nodo.dato + suma_total(nodo.izq) + suma_total(nodo.der)

"""el orden de la primitiva es o(n) ya visita todos los nodos, haciendo operaciones que son o(1)"""


# Se tiene un AB con números enteros como datos, y se quiere reemplazar cada dato por el resultado de multiplicarlo con los datos de los hijos. 
# Hacer un seguimiento de hacer dicho procesamiento con un preorder, inorder o postorder. 
# A continuación se deja la implementación mediante cada recorrido:
"""arbol prueba
         2
       /   \
      3      4
    /  \
   5    6    
   """


# func datoONeutro(ab *arbol[int]) int {
#     if ab == nil {
#         return 1
#     } else {
#         return ab.dato
#     }
# }
    
""""""
# func MultiplicarConHijosPre(arbol *Arbol[int]) {
#     if arbol == nil {
#         return  
#     } 
#     valor_izq := datoONeutro(arbol.izq)
#     valor_der := datoONeutro(arbol.der)
#     arbol.dato *= valor_izq * valor_der
#     MultiplicarConHijosPre(arbol.izq)
#     MultiplicarConHijosPre(arbol.der)
# }

""" primer llamado pre, multiplico los hijos de la raiz(2) con la raiz y lo almaceno 2 * (3 * 4) = 24
         2 -> 24
       /   \
      3      4
    /  \
   5    6   
segundo llamado muplicarhhijospre(3) tiene 2 hijos si, entonces multiplico 3 * (5 * 6) = 90
            24
        /        \
    3 -> 90       4
    /  \
   5    6   
tercero 5 hago lo mismo como no tiene  hijo los multiplico 1
vuelvo en la llamada recursiva hacia el segundo llamado y voy para la derecha 6
cuarta 6, no tiene hijos lo multiplico por 1 queda igual
vuelvo hacia atras de nuevo la primera llamada voy hacia la derecha, 4
quinta 4 no tiene hijos multiplico por 1
vuelvo en la llamada y el arbol quedaria
        24
       /   \
     90      4
    /  \
   5    6   

"""
# func MultiplicarConHijosIn(arbol *Arbol[int]) {
#     if arbol == nil {
#         return  
#     } 
#     MultiplicarConHijosIn(arbol.izq)
#     valor_izq := datoONeutro(arbol.izq)
#     valor_der := datoONeutro(arbol.der)
#     arbol.dato *= valor_izq * valor_der
#     MultiplicarConHijosIn(arbol.der)
# }

"""primer llamado 2, tengo hijo izq, si entonces avanzo
segundo llamado 3, si entonces avanzo
tercer llamado 5, no tiene hijo izquiedo aplico las funciones del medio, 5 * 1* 1 = 5, no tiene hijo derecho
vuelvo al segundo llamado 3, aplico las funciones del medio 3 * (5 * 6 ) = 90, veo tiene hijo derecho si, llamo al 6
             2
          /     \
     3 -> 90     4
       /  \
      5    6   
cuarto llamado 6, me fijo tengo hijo izq no, hago las funciones del medio 6 * 1 * 1 = 6  me fijo tengo hijo derecho no,
vuelvo primer llamado hago funciones del medio 2 * 90 * 4 = 720 sigo y llamo al hijo derecho como tengo hago una llamada
        720
       /   \
     90     4
    /  \
   5    6    
quinta llamada 4, tengo hijo izq no, hago las funciones del medio. 4*1*1 tengo hijo derecho no, cierro la llamada, cierro la primera
tambien y termina el algoritmo
"""
# func MultiplicarConHijosPos(arbol *Arbol[int]) {
#     if arbol == nil {
#         return
#     } 
#     MultiplicarConHijosPos(arbol.izq)
#     MultiplicarConHijosPos(arbol.der)
#     valor_izq := datoONeutro(arbol.izq)
#     valor_der := datoONeutro(arbol.der)
#     arbol.dato *= valor_izq * valor_der
# }
"""
         2
       /   \
      3      4
    /  \
   5    6   
   primer llamado 2, tengo hijo izq si, segundo llamado 3, tengo hijo izq si, tercer llamado 5, tengo hijo izq no
   tengo hijo der no, multiplico 5 * 1* 1, cierro el llamado y vuelvo al segundo, tengo hijo der si cuarto llamado 6
   tengo hijo izq no, tengo hijo der no, multiplico 6 * 1 *1 cierro y vuelvo al segundo de nuevo, multiplico 3* 5*6 = 90
         2
       /   \
     90     4
    /  \
   5    6   

   cierro el segundo y vuelvo al primero, tengo hijo der si, quinto llamado 4, tengo hijo izq no, tengo hijo der no, multiplico
   4*1*1 cierro el llamado y vuelvo al primero
   y multiplico sus hijos 2* 90 * 4 = 720  cierro el primer llamado y termino el algoritmo."""

"""Preorder: Procesa la raíz antes que los hijos. El nodo 2 usa los valores originales de 3 y 4 (2 * 3 * 4 = 24).
Inorder y Postorder: Procesan los hijos antes que la raíz. El nodo 3 se actualiza a 90 antes de que el 2 lo use, dando 2 * 90 * 4 = 720.
Impacto: El orden afecta el resultado porque los valores de los hijos cambian antes de ser usados por los padres en inorder y postorder."""

# Dado un árbol binario, escriba una primitiva recursiva que cuente la cantidad de nodos que tienen exactamente dos hijos directos. 
# ¿Qué orden de complejidad tiene la función implementada?

def nodos_arbol(arbol):
    if arbol is None: return 0
    cuenta = 1 if (arbol.izq is not None and arbol.der is not None) else 0
    return cuenta + nodos_arbol(arbol.izq) + nodos_arbol(arbol.der)



# Escribir una primitiva con la firma func (arbol *Arbol) Invertir() que invierta el árbol binario pasado por parámetro, 
# de manera tal que los hijos izquierdos de cada nodo se conviertan en hijos derechos.

# La estructura Arbol respeta la siguiente definición:

#     type Arbol struct {
#         izq *Arbol
#         der *Arbol
#     }
"""
         2
       /   \
      3     4
    /  \
   5    6  
""" 
def invertir(arbol):
    if arbol is None: return
    arbol.izq, arbol.der = arbol.der, arbol.izq
    invertir(arbol.izq)
    invertir(arbol.der)
"""orden de complejidad o(n) ya que visita cada nodo una vez de manera recursiva, y el swap es o(1) ya que cambiar los punteros"""

# Suponer que se tiene un ABB A con una función de comparación cmp1 con n claves. También, se tiene otro ABB vacío B con función de comparación 
# cmp2 (con cmp1 y cmp2 diferentes).¿Es posible insertar en algún orden todas las claves de A en B de tal forma que ambos
# tengan exactamente la misma estructura? Si es posible, describir un algoritmo que permita lograr esto; si no lo es, razonar por qué. 
# (Considerar que la lógica a emplear debe funcionar para cualquier valor de n y cualquier estructura que tenga el ABB A.)

"""No es posible insertar las claves de A en B de manera que ambos árboles tengan exactamente la misma estructura para cualquier A, 
cualquier n, y cualquier cmp1≠cmp2.La estructura de un ABB depende de las comparaciones relativas entre claves, 
determinadas por la función de comparación.
"""

# Se tiene un AVL con números enteros como claves (su función de comparación simplemente compara dichos valores de la forma tradicional). 
# Su estado inicial puede reconstruirse a partir del preorder: 15 - 6 - 4 - 7 - 50 - 23. Hacer el seguimiento de las siguientes inserciones, 
# incluyendo rotaciones intermedias: 71 - 27 - 38 - 19 - 11 - 21 - 24.

"""    2(15)2
      /       \
  1(6)1       1(50)0
  /     \       /  
0(4)0  0(7)0  0(23)0

         2(15)2
      /         \
  1(6)1         1(50)1
  /     \       /      \
0(4)0  0(7)0  0(23)0  0(71)0
agregamos 71 no hay que balancear

         2(15)3
      /         \
  1(6)1         2(50)1
  /     \       /      \
0(4)0  0(7)0  1(23)0  0(71)0
                  \
                 0(27)0
agregamos 27 no hay que balancear 

         2(15)3
      /         \                       izq der x=27 y=23 z=50    el x pasa a ser hijo izq de z, y pasa a ser hijo izq de x,  
  1(6)1         3(50)1                                            el hijo izq de x pasa a ser hijo der de y, y el hijo der x queda igual
  /     \       /      \
0(4)0  0(7)0  (23)2  0(71)0
                  \
                 0(27)1
                     \
                    0(38)0
agregamos 38  hay que balancear
 
         2(15)3
      /         \
  1(6)1         3(50)1
  /     \       /      \             izq izq z=50 y= 27 x=23   Y pasa a ser padre x padre z, lo que esta ala der de Y pasa ala izq de z
0(4)0  0(7)0  2(27)1  0(71)0
             /    \
          1(23)0  0(38)0  
          /
       0(19)0
agregamos 19 hay que balancear 

               3(15)3
         /                   \
    1(6)2                    2(27)2                                          
  /     \                   /      \             
0(4)0  0(7)1            1(23)0   1(50)1
           \            /         /      \
          0(11)0      0(19)0     0(38)0    0(71)0  
agregamos 11 no hay que balancear

               3(15)4
           /               \
    1(6)2                    3(27)2           z=23 y=19  x=21            izq der     el x pasa a ser hijo izq de z, y pasa a ser hijo izq de x,    
  /     \                   /      \                                     el hijo izq de x pasa a ser hijo der de y, y el hijo der x queda igual
0(4)0  0(7)1            2(23)0   1(50)1
           \            /         /      \
          0(11)0      0(19)1     0(38)0    0(71)0  
                           \
                        0(21)0
agregamos 21 hay que balancear

               3(15)4
           /               \
    1(6)2                    3(27)2           z=23 y=19  x=21            izq izq        
  /     \                   /      \                                     
0(4)0  0(7)1            2(23)0   1(50)1
           \            /         /      \
          0(11)0      1(19)0     0(38)0    0(71)0  
                     /     
                  0(21)0
hay que balancear de nuevo

               3(15)3
           /               \
    1(6)2                      2(27)2              
  /     \                   /         \                                     
0(4)0  0(7)1            1(19)1        1(50)1
           \            /   \         /      \
          0(11)0     0(21)0 0(23)0 0(38)0    0(71)0  
arbol despues de balanceado                                       
"""

# Definimos como quiebre en un árbol binario cuando ocurre que:
# un hijo derecho tiene un solo hijo, y es el izquierdo
# un hijo izquierdo tiene un solo hijo, y es el derecho
# Implementar una primitiva para el árbol binario func (arbol Arbol) Quiebres() int que, dado un árbol binario, 
# nos devuelva la cantidad de quiebres que tiene. La primitiva no debe modificar el árbol. La estructura del tipo Arbol es:
#     type Arbol struct {
#         izq *Arbol
#         der *Arbol
#     }
# Indicar y justificar el orden de la primitiva, e indicar el tipo de recorrido implementado.

def quiebres(arbol):
    if arbol is None: return 0

    izq = quiebres(arbol.izq)
    der = quiebres(arbol.der)

    suma = izq + der
    if arbol.der is not None and arbol.der.izq is not None and arbol.der.der is None:
        suma += 1
    if arbol.izq is not None and arbol.izq.der is not None and arbol.izq.izq is None:
        suma += 1
    return suma
    
# Indicar si las siguientes afirmaciones son verdaderas o falsas. En caso de ser verdaderas, justificar, 
# en caso de ser falsas poner un contraejemplo:

# Si dos árboles binarios tienen el mismo recorrido inorder, entonces tienen la misma estructura.
"""falso, ya que es un arbol binario, no importa el orden si son mas chicos o mas grande arbol """

# Si dos árboles binarios tienen el mismo recorrido preorder, entonces tienen la misma estructura.
"""falso, ya que es un arbol binario, no importa el orden si son mas chicos o mas grande arbol """

# Si dos árboles binarios de búsqueda (e idéntica función de comparación) tienen el mismo recorrido preorder, 
# entonces tienen la misma estructura.
"""verdadero, ya que un arbol binario de busqueda si importa el orden los mas chicos siempre van a estar ala izquierda de los mas grandes"""

#  Determinar cómo es el Árbol cuyo pre order es EURMAONDVSZT, e in order es MRAUOZSVDNET, e indicar su recorrido post order.
"""el recorrido de este arbol post order es: M, A, R, Z, S, V, D, N; O, U, T, E """

# En un árbol binario, dado un nodo con dos hijos, explicar por qué su predecesor en el recorrido inorder no puede tener hijo derecho,
# y que su sucesor (también, en el recorrido inorder) no puede tener hijo izquierdo.
""" El predecesor de un nodo con dos hijos es el nodo más a la derecha del subárbol izquierdo,
 y no tiene hijo derecho porque sería visitado después, contradiciendo su posición como predecesor.
El sucesor de un nodo con dos hijos es el nodo más a la izquierda del subárbol derecho,
 y no tiene hijo izquierdo porque sería visitado antes, contradiciendo su posición como sucesor.
"""

#  Implementar una primitiva del ABB que dado un valor entero M, una clave inicial inicio y una clave final fin, 
# se devuelva una lista con todos los datos cuyas claves estén entre inicio y fin, que estén dentro de los primeros M niveles del árbol 
# (considerando a la raíz en nivel 1). Indicar y justificar la complejidad temporal.
# Por ejemplo, si tenemos el siguiente ABB con M = 3, inicio = 5 y fin = 15:
#       10
#     /    \
#    5      15                    Un resultado final serían los datos de las 
#   / \    /  \                   claves 10, 5, 8, 15, 12 (en cualquier orden).
#  3   8  12   20
#     /     \
#    7       14

def ejercicio17(arbol, m, inicio, fin):
    lista = deque()
    _ejercicio17(arbol, 1, m, inicio, fin, lista)
    return lista

def _ejercicio17(nodo, nivel, m, inicio, fin, lista):
    if nodo is None: return
    if nivel > m: return
    if nodo.clave >= inicio and nodo.clave <= fin:
        lista.append(nodo.clave)
    if nodo.clave > inicio:
      _ejercicio17(nodo.izq, nivel + 1, m, inicio, fin, lista)
    if nodo.clave < fin:
      _ejercicio17(nodo.der, nivel + 1, m, inicio, fin, lista)
"""orden de complejidad O(n) ya que se rrecorre el todo el arbol (en el peor de los casos)"""


