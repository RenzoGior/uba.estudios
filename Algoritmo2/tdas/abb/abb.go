package diccionario

type nodoAbb[K comparable, V any] struct {
	izquierdo *nodoAbb[K, V]
	derecho   *nodoAbb[K, V]
	clave     K
	dato      V
}

type funcCmp[K comparable] func(K, K) int

type abb[K comparable, V any] struct {
	raiz     *nodoAbb[K, V]
	cantidad int
	cmp      funcCmp[K]
}

func CrearABB[K comparable, V any](funcion_cmp func(K, K) int) DiccinarioOrdenado[K, V] {
	ABB := new(abb[K, V])
	var raiz *nodoAbb[K, V]
	ABB.raiz = raiz
	ABB.cmp = funcion_cmp
	return ABB
}

func crearnodoabb[K comparable, V any](clave K, dato V) nodoAbb[K, V] {
	nuevonodo := new(nodoAbb[clave, dato])
	return nuevonodo
}

func (arbol *abb[K, V]) buscarClaveArbol(clave K, nodo, anterior *nodoAbb[K, V]) (*nodoAbb[K, V], *nodoAbb[K, V]) {
	if arbol.raiz == nil {
		return nodo, anterior
	}
	if arbol.cmp(nodo.clave, clave) < 0 {
		return arbol.buscarClaveArbol(clave, nodo.derecho, nodo)
	} else if arbol.cmp(nodo.clave, clave) > 0 {
		return arbol.buscarClaveArbol(clave, nodo.izquierdo, nodo)
	} else {
		return nodo, anterior
	}

}

// Pertenece determina si una clave ya se encuentra en el diccionario, o no
func (arbol *abb[K, V]) Pertenece(clave K) bool {
	nodo, _ := arbol.buscarClaveArbol(clave, arbol.raiz, nil)
	return nodo != nil
}

// Obtener devuelve el dato asociado a una clave. Si la clave no pertenece, debe entrar en pánico con mensaje 'La clave no pertenece al diccionario'
func (arbol *abb[K, V]) Obtener(clave K) V {
	buscar, _ := arbol.buscarClaveArbol(clave, arbol.raiz, nil)
	if buscar == nil {
		panic("la clave no pertenece al diccionario")
	}
	return buscar.dato

}

// Guardar guarda el par clave-dato en el Diccionario. Si la clave ya se encontraba, se actualiza el dato asociado
func (arbol *abb[K, V]) Guardar(clave K, dato V) {
	nuevo := crearnodoabb(clave, dato)
	// nuevo.clave, nuevo.dato := clave, dato

	nodo, padre := arbol.buscarClaveArbol(clave, arbol.raiz, nil)
	if nodo == nil {
		nodo.dato = dato
	} else {
		if padre == nil {
			arbol.raiz = &nuevo
		} else if arbol.cmp(padre.clave, clave) < 0 {
			padre.derecho = &nuevo
		} else {
			padre.izquierdo = &nuevo
		}
		arbol.cantidad++
	}
}

// Cantidad devuelve la cantidad de elementos dentro del diccionario
func (arbol *abb[K, V]) Cantidad() int {
	return arbol.cantidad
}

func (nodo *nodoAbb[K, V]) cantHijos() int {
	if nodo.izquierdo == nil && nodo.derecho == nil {
		return 0
	}
	if (nodo.izquierdo == nil && nodo.derecho != nil) || (nodo.izquierdo != nil && nodo.derecho == nil) {
		return 1
	}
	return 2
}

func (nodo *nodoAbb[K, V]) buscarReemplazante() *nodoAbb[K, V] {
	//mas grande del subarbol izquierdo
	if nodo.derecho == nil {
		return nodo
	}
	return nodo.derecho.buscarReemplazante()
}

// Borrar borra del Diccionario la clave indicada, devolviendo el dato que se encontraba asociado. Si la clave no pertenece al diccionario, debe entrar en pánico con un mensaje 'La clave no pertenece al diccionario'
func (ab *abb[K, V]) Borrar(clave K) V {
	nodo, padre := ab.buscarClaveArbol(clave, ab.raiz, nil)
	if nodo == nil {
		panic("La clave no pertenece al diccionario")
	}
	cant_hijos := nodo.cantHijos()
	borrado := nodo.dato

	if cant_hijos == 0 {
		if padre == nil {
			ab.raiz = nil
		} else if ab.cmp(nodo.clave, padre.clave) < 0 {
			padre.izquierdo = nil
		} else {
			padre.derecho = nil
		}
	} else if cant_hijos == 1 {
		if nodo.izquierdo != nil {
			if padre == nil {
				ab.raiz = nodo.izquierdo
			} else if ab.cmp(nodo.clave, padre.clave) < 0 {
				padre.izquierdo = nodo.izquierdo
			} else {
				padre.derecho = nodo.izquierdo
			}
		} else {
			if padre == nil {
				ab.raiz = nodo.derecho
			} else if ab.cmp(nodo.clave, padre.clave) < 0 {
				padre.izquierdo = nodo.derecho
			} else {
				padre.derecho = nodo.derecho
			}
		}
	} else {
		reemplazante := nodo.izquierdo.buscarReemplazante()
		claveRemplazante := reemplazante.clave
		valorReemplazante := ab.Borrar(reemplazante.clave)
		ab.cantidad++ //este llamado de Borrar reemplazante nos restó 1 en cantidad
		nodo.clave, nodo.dato = claveRemplazante, valorReemplazante
	}
	ab.cantidad--
	return borrado
}

// // Iterar itera internamente el diccionario, aplicando la función pasada por parámetro a todos los elementos del mismo
// Iterar(func(clave K, dato V) bool)
// // Iterador devuelve un IterDiccionario para este Diccionario
// Iterador() IterDiccionario[K, V]
