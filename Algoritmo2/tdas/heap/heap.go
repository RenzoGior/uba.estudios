package cola_prioridad

const (
	CAPACIDAD_INICIAL            = 5
	_FACTOR_REDIMENSION_AGRANDAR = 2
	_FACTOR_REDIMENSION_ACHICAR  = 2
)

type colaConPrioridad[T any] struct {
	datos []T
	cant  int
	cmp   fcmpHeap[T]
}

type fcmpHeap[T any] func(T, T) int

func CrearHeap[T any](funcion_cmp func(T, T) int) ColaPrioridad[T] {
	nuevo := new(colaConPrioridad[T])
	nuevo.datos = make([]T, 5)
	nuevo.cant = 0
	nuevo.cmp = funcion_cmp
	return nuevo
}

func (heap colaConPrioridad[T]) EstaVacia() bool {
	return heap.cant == 0
}

func (heap colaConPrioridad[T]) VerMax() T {
	if heap.EstaVacia() {
		panic("La cola esta vacia")
	}
	return heap.datos[0]
}

func (heap colaConPrioridad[T]) Cantidad() int {
	return heap.cant
}

func (heap *colaConPrioridad[T]) redimensionarHeap(nueva_cap int) {
	if nueva_cap == 0 {
		nueva_cap = 2
	}
	nuevo := make([]T, nueva_cap)
	copy(nuevo, heap.datos)
	heap.datos = nuevo
}

func calcularPosicionPadre(pos_hijo int) int {
	return (pos_hijo - 1) / 2
}

func calcularPosicionesHijos(pos_padre int) (int, int) {
	return pos_padre*2 + 1, pos_padre*2 + 2
}

func upHeap[T any](arr []T, pos_hijo int, cmp func(T, T) int) {
	if pos_hijo == 0 {
		return
	}
	pos_padre := calcularPosicionPadre(pos_hijo)
	if cmp(arr[pos_padre], arr[pos_hijo]) < 0 {
		arr[pos_padre], arr[pos_hijo] = arr[pos_hijo], arr[pos_padre]
		upHeap(arr, pos_padre, cmp)
	}
}

func maximo[T any](arr []T, tam, pos_padre, hijo_izq, hijo_der int, cmp func(T, T) int) int {
	mayor := pos_padre
	if hijo_izq < tam && cmp(arr[mayor], arr[hijo_izq]) < 0 {
		mayor = hijo_izq
	}
	if hijo_der < tam && cmp(arr[mayor], arr[hijo_der]) < 0 {
		mayor = hijo_der
	}
	return mayor
}

func downHeap[T any](arr []T, tam, pos_padre int, cmp func(T, T) int) {
	if pos_padre >= tam {
		return
	}
	hijo_izq, hijo_der := calcularPosicionesHijos(pos_padre)
	mayor := maximo(arr, tam, pos_padre, hijo_izq, hijo_der, cmp)
	if mayor != pos_padre {
		arr[pos_padre], arr[mayor] = arr[mayor], arr[pos_padre]
		downHeap(arr, tam, mayor, cmp)
	}
}

func heapify[T any](arr []T, tam int, cmp func(T, T) int) {
	for i := tam - 1; i >= 0; i-- {
		downHeap(arr, tam, i, cmp)
	}
}
func (heap *colaConPrioridad[T]) Encolar(elemento T) {
	if heap.cant == cap(heap.datos) {
		heap.redimensionarHeap(cap(heap.datos) * _FACTOR_REDIMENSION_AGRANDAR)
	}
	heap.datos[heap.cant] = elemento
	upHeap(heap.datos, heap.cant, heap.cmp)
	heap.cant++
}

func (heap *colaConPrioridad[T]) Desencolar() T {
	if heap.EstaVacia() {
		panic("La cola esta vacia")
	}
	if heap.cant*4 <= cap(heap.datos) && cap(heap.datos) > CAPACIDAD_INICIAL {
		heap.redimensionarHeap(cap(heap.datos) / _FACTOR_REDIMENSION_ACHICAR)
	}
	heap.datos[0], heap.datos[heap.cant-1] = heap.datos[heap.cant-1], heap.datos[0]
	borrado := heap.datos[heap.cant-1]
	heap.cant--
	downHeap(heap.datos, heap.cant, 0, heap.cmp)
	return borrado
}

func CrearHeapArr[T any](arreglo []T, funcion_cmp func(T, T) int) ColaPrioridad[T] {
	nuevo := new(colaConPrioridad[T])
	nuevoArr := make([]T, len(arreglo))
	copy(nuevoArr, arreglo)
	heapify(nuevoArr, len(nuevoArr), funcion_cmp)
	nuevo.datos = nuevoArr
	nuevo.cant = len(nuevoArr)
	nuevo.cmp = funcion_cmp
	return nuevo
}

func HeapSort[T any](elementos []T, funcion_cmp func(T, T) int) {
	heapify(elementos, len(elementos), funcion_cmp)
	for i := len(elementos) - 1; i > 0; i-- {
		elementos[0], elementos[i] = elementos[i], elementos[0]
		downHeap(elementos, i, 0, funcion_cmp)
	}
}
