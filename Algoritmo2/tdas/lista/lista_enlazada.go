package lista

type nodoLista[T any] struct {
	dato      T
	siguiente *nodoLista[T]
}

func crearNodoLista[T any](valor T) *nodoLista[T] {
	nodo := new(nodoLista[T])
	nodo.dato = valor
	return nodo
}

type listaEnlazada[T any] struct {
	primero *nodoLista[T]
	ultimo  *nodoLista[T]
	largo   int
}

func CrearListaEnlazada[T any]() Lista[T] {
	lista := new(listaEnlazada[T])
	return lista
}

func (lista listaEnlazada[T]) validarListaNoVacia() {
	if lista.EstaVacia() {
		panic("la lista esta vacia")
	}
}

func (lista listaEnlazada[T]) EstaVacia() bool {
	return lista.largo == 0
}

func (lista *listaEnlazada[T]) InsertarPrimero(valor T) {
	nuevo := crearNodoLista(valor)
	if lista.EstaVacia() {
		lista.primero = nuevo
		lista.ultimo = nuevo
	} else {
		nuevo.siguiente = lista.primero
		lista.primero = nuevo
	}
	lista.largo++
}

func (lista *listaEnlazada[T]) InsertarUltimo(valor T) {
	nuevo := crearNodoLista(valor)
	if lista.EstaVacia() {
		lista.primero = nuevo
	} else {
		lista.ultimo.siguiente = nuevo
	}
	lista.ultimo = nuevo
	lista.largo++
}

func (lista *listaEnlazada[T]) BorrarPrimero() T {
	lista.validarListaNoVacia()
	borrado := lista.primero.dato
	lista.primero = lista.primero.siguiente
	if lista.primero == nil {
		lista.ultimo = nil
	}
	lista.largo--
	return borrado
}

func (lista listaEnlazada[T]) VerUltimo() T {
	lista.validarListaNoVacia()
	return lista.ultimo.dato
}

func (lista listaEnlazada[T]) VerPrimero() T {
	lista.validarListaNoVacia()
	return lista.primero.dato
}

func (lista listaEnlazada[T]) Largo() int {
	return lista.largo
}

func (lista *listaEnlazada[T]) Iterar(visitar func(T) bool) {
	actual := lista.primero
	for actual != nil && visitar(actual.dato) {
		actual = actual.siguiente
	}
}

func (lista *listaEnlazada[T]) Iterador() IteradorLista[T] {
	iterador := new(iterListaEnlazada[T])
	iterador.lista = lista
	iterador.actual = iterador.lista.primero
	return iterador
}

type iterListaEnlazada[T any] struct {
	actual   *nodoLista[T]
	anterior *nodoLista[T]
	lista    *listaEnlazada[T]
}

func (iter iterListaEnlazada[T]) VerActual() T {
	if iter.actual == nil {
		panic("el iterador termino.")
	}
	return iter.actual.dato
}

func (iter iterListaEnlazada[T]) HaySiguiente() bool {
	return iter.actual != nil
}

func (iter *iterListaEnlazada[T]) Siguiente() {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
	iter.anterior = iter.actual
	iter.actual = iter.actual.siguiente
}

func (iter *iterListaEnlazada[T]) Insertar(elem T) {
	nuevo := crearNodoLista(elem)
	if iter.anterior == nil && iter.actual == nil {
		iter.lista.primero = nuevo
		iter.lista.ultimo = nuevo
		iter.actual = iter.lista.primero
	} else if iter.anterior == nil {
		nuevo.siguiente = iter.actual
		iter.actual = nuevo
		iter.lista.primero = iter.actual
	} else {
		iter.anterior.siguiente = nuevo
		nuevo.siguiente = iter.actual
		iter.actual = nuevo
		if iter.actual.siguiente == nil {
			iter.lista.ultimo = iter.actual
		}
	}
	iter.lista.largo++
}

func (iter *iterListaEnlazada[T]) Borrar() T {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
	borrado := iter.actual.dato
	iter.lista.largo--
	if iter.anterior == nil {
		if iter.actual.siguiente != nil {
			iter.actual = iter.actual.siguiente
			iter.lista.primero = iter.actual
			return borrado
		} else {
			iter.actual = nil
			return borrado
		}
	}
	iter.anterior.siguiente = iter.actual.siguiente
	if iter.actual.siguiente == nil {
		iter.actual = nil
		iter.lista.ultimo = iter.anterior
		return borrado
	}
	iter.actual = iter.actual.siguiente
	return borrado
}
