package guia

import (
	"fmt"
	"slices"
	"tdas/pila"
	
)

// 1 (★) Implementar el TDA Fracción. Dicho TDA debe tener las siguientes primitivas, cuya documentación puede encontrarse aquí:
// CrearFraccion(numerador, denominador int) Fraccion
// Sumar(otra Fraccion) Fraccion
// Multiplicar(otra Fraccion) Fraccion
// ParteEntera() int
// Representacion() string
// Puede encontrarse la resolución de este ejercicio aquí.
type Fraccion struct {
	numerador   int
	denominador int
}

// type Fraccion[] interface {
// 	CrearFraccion(numerador, denominador int) Fraccion
// 	Sumar(otra Fraccion) Fraccion
// 	Multiplicar(otra Fraccion) Fraccion
// 	ParteEntera() int
// 	Representacion() string
// }

func CrearFraccion(numerador, denominador int) Fraccion {
	fraccion := new(Fraccion)
	fraccion.numerador = numerador
	fraccion.denominador = denominador
	return *fraccion
}

func (fraccion Fraccion) Sumar(otra Fraccion) Fraccion {
	nueva := new(Fraccion)
	nueva.numerador = fraccion.numerador + otra.numerador
	nueva.denominador = fraccion.denominador + otra.denominador // asi no se suman las fracciones
	return *nueva
}

func (fraccion Fraccion) Multiplicar(otra Fraccion) Fraccion {
	nueva := new(Fraccion)
	nueva.numerador = fraccion.numerador * otra.numerador
	nueva.denominador = fraccion.denominador * otra.denominador
	return *nueva
}

func (fraccion Fraccion) ParteEntera() int {
	return fraccion.numerador / fraccion.denominador
}

func (fraccion Fraccion) Representacion() string {
	if fraccion.denominador == 1 {
		return fmt.Sprintf("%d", fraccion.numerador)
	} else {
		return fmt.Sprintf("%d/%d", fraccion.numerador, fraccion.denominador)
	}
}

// 2 (★) Implementar el TDA NumeroComplejo. Dicho TDA debe tener las siguientes primitivas, cuya documentación puede encontrarse aquí:
// CrearComplejo(real float, img float) Complejo
// Multiplicar(otro Complejo)
// Sumar(otro Complejo)
// ParteReal() float
// ParteImaginaria() float
// Modulo() float
// Angulo() float
// 3 (★) Implementar una función que reciba un arreglo genérico e invierta su orden, utilizando los TDAs vistos.
// Indicar y justificar el orden de ejecución.

// 4(★★) Implementar en Go el TDA ComposiciónFunciones que emula la composición de funciones (i.e. f(g(h(x))).
// Se debe definir la estructura del TDA, y las siguientes primitivas:
// CrearComposicion() ComposicionFunciones
// AgregarFuncion(func (float64) float64)
// Aplicar(float64) float64
// Considerar que primero se irán agregando las funciones como se leen, pero tener en cuenta el correcto orden de aplicación.
// Por ejemplo: para emular f(g(x)), se debe hacer:
// composicion.AgregarFuncion(f)
// composicion.AgregarFuncion(g)
// composicion.Aplicar(x)
// Indicar el orden de las primitivas.

// 5(★★★) Dada una lista enlazada implementada con las siguientes estructuras:
type nodoLista[T any] struct {
	prox *nodoLista[T]
	dato T
}
type ListaEnlazada[T any] struct {
	prim *nodoLista[T]
}

// Escribir una primitiva de lista que devuelva el elemento que esté a
// k
// k posiciones del final (el ante-k-último), recorriendo la lista una sola vez y sin usar estructuras auxiliares. Considerar que
// k
// k es siempre menor al largo de la lista. Por ejemplo, si se recibe la lista [ 1, 5, 10, 3, 6, 8 ], y k = 4, debe devolver 10.
// Indicar el orden de complejidad de la primitiva.
func (lista ListaEnlazada[T]) AnteK(k int) T { // orden de complejidad O(n)
	separador := lista.prim
	actual := lista.prim
	for i := range k {
		separador = separador.prox
	}
	for separador != nil {
		actual = actual.prox
		separador = separador.prox
	}
	return actual.dato
}

// 6(★★★) Dada una pila de enteros, escribir una función que determine si sus elementos están ordenados de manera ascendente.
// Una pila de enteros está ordenada de manera ascendente si, en el sentido que va desde el tope de la pila hacia el resto de elementos,
// cada elemento es menor al elemento que le sigue. La pila debe quedar en el mismo estado que al invocarse la función.
// Indicar y justificar el orden del algoritmo propuesto.
func OrdenAscendente(pila pilaDinamica[int]) bool {
	desapilado := []int{}
	pilaTemporal := new(PilaDinamica[int]{})
	for !pila.EstaVacia() {
		valor := pila.Desapilar()
		desapilado = append(desapilado, valor)
		pilaTemporal.Apilar(valor)
	}
	for !pilaTemporal.EstaVacia() {
		pila.Apilar(pilaTemporal.Desapilar())
	}
	return slices.IsSorted(desapilado)
}

// 7(★★) Implementar la primitiva func (cola *colaEnlazada[T]) Multiprimeros(k int) []T que dada una cola y un número
// k
// k, devuelva los primeros
// k
// k elementos de la cola, en el mismo orden en el que habrían salido de la cola. En caso que la cola tenga menos de
// k
// k elementos. Si hay menos elementos que
// k
// k en la cola, devolver un slice del tamaño de la cola. Indicar y justificar el orden de ejecución del algoritmo.

// 8(★★) Implementar la función func Multiprimeros[T any](cola Cola[T], k int) []T con el mismo comportamiento de la primitiva anterior.

// 9(★★) Implementar en Go una primitiva func (lista *ListaEnlazada) Invertir() que invierta la lista, sin utilizar estructuras auxiliares.
// Indicar y justificar el orden de la primitiva.

// 10(★★) Se quiere implementar un TDA ColaAcotada sobre un arreglo. Dicho TDA tiene un espacio para
// k
// k elementos (que se recibe por parámetro al crear la estructura). Explicar cómo deberían implementarse
// las primitivas encolar y desencolar de tal manera que siempre sean operaciones de tiempo constante.

// 11(★★★★) Implementar una función que ordene de manera ascendente una pila de enteros sin conocer su estructura interna y utilizando
// como estructura auxiliar sólo otra pila auxiliar. Por ejemplo, la pila [ 4, 1, 5, 2, 3 ] debe quedar como [ 1, 2, 3, 4, 5 ]
// (siendo el último elemento el tope de la pila, en ambos casos). Indicar y justificar el orden de la función.
func OrdenarPilaAscendente(pila *pilaDinamica[T any]) pila {
	otra := new(pilaDinamica)
	for !pila.EstaVacia(){
		dato := pila.desapilar()
		for !otra.EstaVacia() && otra.VerTope() > dato{
			pila.apilar(otra.desapilar())
		}
		otra.apilar(dato)
	}
	for !otra.EstaVacia(){
		pila.apilar(otra.desapilar)
	}
	return pila
	// la complejidad seria O(Nal cuadrado) ya que en algunos caso tenemos que despilar la pila auxiliar y apilar en la primera pila 
	// para avanzar.
}

// 12(★★) Implementar una función func FiltrarCola[K any](cola Cola[K], filtro func(K) bool) ,
// que elimine los elementos encolados para los cuales la función filtro devuelve false.
// Aquellos elementos que no son eliminados deben permanecer en el mismo orden en el que estaban antes de invocar a la función.
// No es necesario destruir los elementos que sí fueron eliminados. Se pueden utilizar las estructuras auxiliares que se consideren
// necesarias y no está permitido acceder a la estructura interna de la cola (es una función). ¿Cuál es el orden del algoritmo implementado?

// 13(★★★) Sabiendo que la firma del iterador interno de la lista enlazada es:
//     Iterar(visitar func(K) bool)
// Se tiene una lista en donde todos los elementos son punteros a números enteros.
// Implementar una función SumaPares que reciba una lista y, utilizando el iterador interno (no el externo),
// calcule la suma de todos los números pares.

// 14(★★★★★) Diseñar un TDA PilaConMáximo, que tenga las mismas primitivas de la pila convencional,
// y además permita obtener el máximo de la pila. Todas las primitivas deben funcionar en
// O(1). Explicar cómo implementarías el TDA para que cumpla con todas las restricciones.

// 15(★★★) Implementar el TDA Mamushka (matrioshka, o muñeca rusa), teniendo en cuenta que una Mamushka puede tener otra Mamushka dentro de si misma. Las primitivas deben ser:

// CrearMamushka(tam int, color Color) Mamushka: Crea una mamushka con un tamaño y color definido.
// ObtenerColor() Color: Obtiene el color de la Mamushka.
// Guardar(Mamushka) bool: Intenta guardar la segunda mamushka en la primera. Si la primera ya tiene una mamushka guardada, entonces debe intentar guardar la mamushka a_guardar dentro de la mamushka que ya estaba guardada. La operación falla (y devuelve false) si en algún momento se intenta guardar una mamushka en otra de menor o igual tamaño. Por ejemplo: si tenemos una mamushka de tamaño 10 que dentro tiene una de tamaño 8, y se intenta guardar una de tamaño 5, ésta debe guardarse dentro de la de tamaño 8. Si, luego, se intentara guardar una de tamaño 6, la operación debe fallar dado que no se puede guardar una mamushka de tamaño 6 dentro de una de tamaño 5.
// ObtenerGuardada() Mamushka: Devuelve un puntero a la mamushka guardada. NULL en caso de no tener ninguna guardada. En el ejemplo anterior, si utilizaremos esta primitiva con la Mamushka de tamaño 10, nos devolvería la Mamushka de tamaño 8 que guardamos (y que dentro tiene la de tamaño 5).
// Definir la estructura (struct) del TDA, y escribir estas 5 primitivas. Indicar el orden de cada una de ellas.

// Nota: Color corresponde a un enumerado, que está definido en algún lugar.

// 16(★★★) Dadas dos pilas de enteros positivos (con posibles valores repetidos) cuyos elementos fueron ingresados de menor a mayor, 
// se pide implementar una función func MergePilas(pila1, pila2 Pila[int]) []int que devuelva un array ordenado de menor a mayor con 
// todos los valores de ambas pilas sin repeticiones. 
// Detallar y justificar la complejidad del algoritmo considerando que el tamaño de las pilas es N y M respectivamente.

// 17(★★) Escribir una primitiva para la pila (dinámica) cuya firma es func (pila pilaDinamica[T]) Transformar(aplicar func(T) T) Pila[T] que devuelva una nueva pila cuyos elementos sean los resultantes de aplicarle la función aplicar a cada elemento de la pila original. Los elementos en la nueva pila deben tener el orden que tenían en la pila original, y la pila original debe quedar en el mismo estado al inicial. Indicar y justificar la complejidad de la primitiva.

// Por ejemplo, para la pila de enteros [ 1, 2, 3, 6, 2 ] (tope es el número 2), y la función sumarUno (que devuelve la suma entre el número 1 y el número recibido), la pila resultante debe ser [ 2, 3, 4, 7, 3 ] (el tope es el número 3).

// 18(★★) Implementar una función recursiva que reciba una pila y devuelva, sin utilizar estructuras auxiliares, la cantidad de elementos de la misma. Al terminar la ejecución de la función la pila debe quedar en el mismo estado al original.

// 19(★★★) Implementar una función func balanceado(texto string) boolean, que retorne si texto esta balanceado o no. texto sólo puede contener los siguientes caracteres: [,],{,}(,). Indicar y justificar la complejidad de la función implementada. Un texto esta balanceado si cada agrupador abre y cierra en un orden correcto. Por ejemplo:
// balanceado("[{([])}]") => true
// balanceado("[{}") => false
// balanceado("[(])") => false
// balanceado("()[{}]") => true
// balanceado("()()(())") => true

// 20(★★) Carlos es nuevo en la empresa en la que trabajan Alan y Bárbara. Alan va a ser el mentor de Carlos, 
// quien debe implementar un nuevo TDA Gatito. Alan, revisando el trabajo que hizo Carlos, nota que este agregó una primitiva Redimensionar, 
// pública en la interfaz Gatito, para que la use Bárbara. Alan lo increpa a Carlos,
// preguntando para qué es dicha primitiva, y este le contesta “Tal como dice la documentación, es para que Bárbara me diga 
// cómo redimensionar el arreglo de pelos que tiene el gatito”. Alan, que conoce bien el temperamento de Bárbara, 
// decide evitar que echen a Carlos en su segunda semana de trabajo. En este ejercicio, te toca hacer de Alan.
// Escribir una explicación de por qué esto que está haciendo Carlos está mal. Considerá que Carlos es muy testarudo 
// (incluso, a pesar de su propio bien), así que tu argumentación deberá ser muy clara y contundente.
