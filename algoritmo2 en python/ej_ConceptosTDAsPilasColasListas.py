from collections import deque
# 5. Dada una lista enlazada implementada con las siguientes estructuras:
#      type nodoLista[T any] struct {
#          prox *nodoLista[T]
#          dato T
#      }
#      type ListaEnlazada[T any] struct {
#          prim *nodoLista[T]
#      }
# Escribir una primitiva de lista que devuelva el elemento que esté a 
# k posiciones del final (el ante-k-último), recorriendo la lista una sola vez y sin usar estructuras auxiliares. 
# Considerar que k es siempre menor al largo de la lista. 
# Por ejemplo, si se recibe la lista [ 1, 5, 10, 3, 6, 8 ], y k = 4, debe devolver 10. Indicar el orden de complejidad de la primitiva.


class _Node:
    def __init__(self, dato: any, next=None) -> int:
        self.dato = dato
        self.next = next


class LinkedList:
    def __init__(self):
        self.prim = _Node

    def k_posiciones_final(self, k):
        #two pointers aproach
        rapido = self.prim
        lento = self.prim
        for _ in range(k - 1):
            rapido = rapido.next
            # print (f"{rapido.dato} adelantamiento")


        while rapido.next is not None:
            lento = lento.next
            rapido = rapido.next
            # print(lento.dato)
            # print(rapido.dato)        
            
        return lento.dato

lista = LinkedList()
    # Creamos la lista [1, 5, 10, 3, 6, 8]
lista.prim = _Node(1)
lista.prim.next = _Node(5)
lista.prim.next.next = _Node(10)
lista.prim.next.next.next = _Node(3)
lista.prim.next.next.next.next = _Node(6)
lista.prim.next.next.next.next.next = _Node(8)
lista.prim.next.next.next.next.next.next = _Node(22)
lista.prim.next.next.next.next.next.next.next = _Node(11)
    
    # Probamos con k = 4
resultado = lista.k_posiciones_final(7)
print(resultado)

# 6. Dada una pila de enteros, escribir una función que determine si sus elementos están ordenados de manera ascendente.
# Una pila de enteros está ordenada de manera ascendente si, en el sentido que va desde el tope de la pila hacia el resto de elementos,
# cada elemento es menor al elemento que le sigue. La pila debe quedar en el mismo estado que al invocarse la función. 
# Indicar y justificar el orden del algoritmo propuesto.

def pila_orden_acendente(pila) -> bool: #O(n) ya que desapilariamos la primer pila, que el desapilar es O(1), y la volveriamos a apilar
    if len(pila) <= 1:
        return True

    pila_aux = deque()
    anterior = pila.pop()
    es_ordenada = True
    pila_aux.append(anterior)

    while len(pila) > 0:
        actual = pila.pop()
        if anterior >= actual:
            es_ordenada = False
        pila_aux.append(actual) 
        anterior = actual

    while len(pila_aux) > 0:
        pila.append(pila_aux.pop())
    return es_ordenada


# 19. Implementar una función func balanceado(texto string) boolean, 
# que retorne si texto esta balanceado o no. texto sólo puede contener los siguientes caracteres: [,],{,}(,). 
# Indicar y justificar la complejidad de la función implementada. Un texto esta balanceado si cada agrupador abre y cierra en un orden correcto. 
# Por ejemplo:
 

def balanceado(texto: str) -> bool:
    if len(texto) % 2 != 0:
        return False
    pares = {')': '(', '}': '{', ']': '['}
    inicio = {"(","{","["}
    stack = deque() 
    for i in texto:
        if i in inicio:
            stack.append(i)
        elif i in pares:
            if not stack:
                return False
            ultimo_abierto = stack.pop()
            if ultimo_abierto != pares[i]:
                return False
    return len(stack) == 0

assert balanceado("[{([])}]") == True
assert balanceado("[{}") == False
assert balanceado("[(])") == False
assert balanceado("()[{}]") == True
assert balanceado("()()(())") == True 