package cola

type nodoCola[T any] struct {
	dato T
	prox *nodoCola[T]
}

type colaEnlazada[T any] struct {
	primero *nodoCola[T]
	ultimo  *nodoCola[T]
}

func crearNodo[T any](dato T) *nodoCola[T] {
	nodo := new(nodoCola[T])
	nodo.dato = dato
	return nodo
}

func CrearColaEnlazada[T any]() Cola[T] {
	return new(colaEnlazada[T])
}

func (cola colaEnlazada[T]) validarColaNoVacia() {
	if cola.EstaVacia() {
		panic("la cola esta vacia")
	}
}

func (cola colaEnlazada[T]) EstaVacia() bool {
	return cola.primero == nil
}

func (cola colaEnlazada[T]) VerPrimero() T {
	cola.validarColaNoVacia()
	return cola.primero.dato
}

func (cola *colaEnlazada[T]) Encolar(valor T) {
	nodo := crearNodo(valor)
	if cola.EstaVacia() {
		cola.primero = nodo
	} else {
		cola.ultimo.prox = nodo
	}
	cola.ultimo = nodo

}
func (cola *colaEnlazada[T]) Desencolar() T {
	cola.validarColaNoVacia()
	valor := cola.primero.dato
	if cola.primero.prox == nil {
		cola.primero = nil
		cola.ultimo = nil

	} else {
		cola.primero = cola.primero.prox
	}
	return valor

}
