class _Nodo:
    """modela un nodo de una lista enlazada."""
    def __init__(self, dato = None, prox = None) -> None: #recibe un dato y un nodo
        self.dato = dato
        self.prox = prox

    def __str__(self) -> str:
        return str(self.dato)

class ListaEnlazada:
    """Modela una lista enlazada."""
    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0

    def append(self, dato):
        """agrega un nuevo nodo al final de la lista"""
        nuevo = _Nodo(dato, None) #almacena el dato que se quiere guardar

        if self.prim is None:
            # caso borde: lista vacia
            self.prim = nuevo
        else:
            # caso feliz
            act = self.prim #garantizado que no es None
            while act.prox is not None:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo

        self.len += 1
            
    def __str__(self) -> str:
        # Ejercicio 13.1. Implementar el método __str__ de ListaEnlazada, para que se genere una
        # salida legible de lo que contiene la lista, similar a las listas de python.
        datos = []
        act = self.prim
        while act is not None:
            datos.append(act.dato)
            act = act.prox
        return str(datos)
    
    def extend(self, otra):
        # Ejercicio 13.2. Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
        # agregue a la lista actual los elementos que se encuentran en la lista recibida.
        
        ult = self.prim
        if ult is not None:
            while ult.prox is not None:
                ult = ult.prox

        act = otra.prim
        while act is not None:
            if ult is None:
                # la lista self es vacia
                self.prim = _Nodo(act.dato, None)
                ult = self.prim
            else:
                ult.prox = _Nodo(act.dato, None)
                ult = ult.prox
            self.len += 1
            act = act.prox

    def remove(self, dato):
        if self.prim is None:
            return
        ant = self.prim
        if ant.dato == dato:
            # caso borde el dato a eliminar es el primero
            self.prim = ant.prox

        while ant.prox is not None and ant.prox.dato != dato:
            ant = ant.prox

        if ant.prox is None:
            # llegamos al final de la lista y no encontramos el dato
            return
        # encontramos el dato
        ant.prox = ant.prox.prox
        self.len -= 1

    def remover_todos(self, elemento):
        # Ejercicio 13.3. Implementar el método remover_todos(elemento) de ListaEnlazada, que re-
        # cibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad
        # de elementos removidos. La lista debe ser recorrida una sola vez.
        if self.prim is None:
            # caso borde: lista vacia
            return
        else:
            # caso feliz
            act = self.prim #garantizado que no es None
            while act.prox is not None:
                if act.dato == elemento:
                    act.prox.prox # salta la referencia al siguiente nodo
                    self.len -= 1 # resta uno al atributo len
                act = act.prox

    def duplicar(self, elemento):
        # Ejercicio 13.4. Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
        # # elemento y duplica todas las apariciones del mismo. Ejemplo:
        # L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
        # L.duplicar(8) => L = 1 -> 5 -> 8 -> 8 -> 8 -> 8 -> 2 -> 8 -> 8
        pass
        
    def __len__(self):
        self.len