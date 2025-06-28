package diccionario

type DiccionarioOrdenado[K comparable, V any] interface {
	Diccionario[K, V]

	// IterarRango itera sólo incluyendo a los elementos que se encuentren comprendidos en el rango indicado,
	// incluyéndolos en caso de encontrarse
	IterarRango(desde *K, hasta *K, visitar func(clave K, dato V) bool)

	// IteradorRango crea un IterDiccionario que sólo itere por las claves que se encuentren en el rango indicado
	IteradorRango(desde *K, hasta *K) IterDiccionario[K, V]
}

type IterDiccionario[K comparable, V any] interface {
	// HaySiguiente devuelve si hay más datos para ver. Esto es, si en el lugar donde se encuentra parado el iterador hay un elemento.
	HaySiguiente() bool

	// VerActual devuelve la clave y el dato del elemento actual en el que se encuentra posicionado el iterador. Si no HaySiguiente, debe entrar en pánico con el mensaje 'El iterador termino de iterar'
	VerActual() (K, V)

	// Siguiente si HaySiguiente avanza al siguiente elemento en el diccionario. Si no HaySiguiente, entonces debe entrar en pánico con mensaje 'El iterador termino de iterar'
	Siguiente()
}
