
//Escribir una función entreNumeros(inicio: Int, fin: Int): List[Int] que retorne una lista que incluya todos los números enteros entre
//  inicio y fin incluyéndolos.
def entreNumeros(inicio: Int, fin: Int): List[Int] = {
  return List.range(inicio, fin + 1)
}

//Escribir una función repetidos(lista1: List[Int], lista2: List[Int]): List[Int] que retorne una nueva lista que contenga
//  los elementos que están presentes en ambas listas.
def repetidos(lista1: List[Int], lista2: List[Int]): List[Int] = {
  lista1.intersect(lista2)
}

//Escribir una función eliminarRepetidos(lista: List[Int]): List[Int] que retorne una nueva lista que contenga los mismos
//elementos que la original pero sin elementos repetidos.
def eliminarRepetidos (lista: List[Int]): List[Int] = {
  lista.distinct
}

//Escribir una función aplicar(lista: List[Int], f: (Int, Int) =¿Int): List[Int] que retorne una nueva lista que contenga
// los resultados de aplicar f a cada elemento de lista
def aplicar(lista: List[Int], f: (Int, Int) => Int): List[Int] = lista match {
  case Nil => List()
  case nodo::Nil => List()
  case nodo::resto  => f(nodo, resto.head) :: aplicar(resto, f)
}


// Escribir una función sumar(lista: List[Int]): Int que retorne la suma de todos los elementos de la lista.
def sumar(lista: List[Int]): Int = lista match {
  case Nil => 0
  case nodo::resto => nodo + sumar(resto)
}

//Indicar y justificar cuales de las siguientes funciones son impuras

//1.
//def f ( x : Int , y : Int ) : Int = {
//  x + y
//}

//es una funcion pura, ya que no tiene sideefect, y no accede a datos externos

//2.
//def fecha () : String = {
//  LocalDate.now.format(DateTimeFormatter.ofPattern ("yyyyMMdd "))
//}
//no es pura, no tiene sideefect, pero accede a datos externos

//3.
//def contar(l: List[Int], e: Int): Int = {
//  var cont = 0;
//  l.foreach(elemento => {
//    if(elemento == e) {
//      cont = cont + 1
//    }
//  })
//  cont
//}
//es una funcion pura, no tiene sideefect y trabaja dentro del scope

//4.
//import scala.collection.mutable.Map
//
//def actualizarAUno(mapa: Map[Int, Int]) = {
//  for (k, v) <- mapa do
//    mapa(k) = 1
//}
//es inpura ya que el map es mutable

//5.
//import scala.collection.mutable.Map
//
//def randomEntre(a: Int, b: Int): Int = {
//  val rand = new scala.util.Random
//  rand.between(a, b)
//}
//es inpura, ya que la funcion no es deterministica.

//6.
//def merge[A](list1: List[A], list2: List[A]): List[A] = {
//  list1 ::: list2
//}
//es una funcion pura

//7.
//import java.io.PrintWriter
//
//def guardarEnArchivo(texto: String, ruta: String): Unit = {
//  val escritor = new PrintWriter(ruta)
//  try {
//    escritor.write(texto)
//  } finally {
//    writer.close()
//  }
//}
//es una funcion inpura ya que accede a datos externos, y lo modifica


//Escribir una función contar(palabras: List[String]): Map[String, Int] retorne un mapa donde las claves sean las palabras
//  de la lista pasada por parámetro y los valores la cantidad de apariciones que tiene dicha palabra en la lista
def contar(palabras: List[String]): Map[String, Int] ={
  palabras
    .groupBy(palabra => palabra)
    .map((palabra,cantidad) => (palabra, cantidad.length))
}

//Escribir una función topK(numeros: List[Int], k: Int, f: (Int, Int) => Int): List[Int] que retorne una lista
//con los k elementos de números mas grandes según la función f. La respuesta debe estar ordenada según el criterio de la función f.
def topK(numeros: List[Int], k: Int, f: (Int, Int) => Int): List[Int] ={
  numeros
    .sortWith((a, b) => f(a, b) > 0)
    .take(k)
}


//Escribir una función que junte los números de una lista sin usar métodos de ordenamiento. Ej: (1, 2, 3,4, 1, 3) => (2, 1, 1, 3, 3, 4).
def jumtarNumeros(l: List[Int]) = {
  l
    .groupBy(x => x)
    .flatten((c, v) => v)
}

//Escribir una función que retorne el n-esimo número de la sucesión de Fibonacci a partir de un número n.
def fibo(n: Int): Int = n match{
  case 0 => 0
  case 1 => 1
  case _ => fibo(n - 1)  + fibo(n - 2)
}

////Generar la lista de los primeros mil números primos.
//def milNumerosPrimos(): List[int] = l match{
//
//}

//Escribir una función que reciba un string y retorne un booleano mostrando capicua o no.
def capicua(s: String): Boolean = s match{
  case _ if s.length < 2 => true
  case _ if s.head == s.last => capicua(s.substring(1, s.length - 1))
  case _ => false
}

//Escribir una función que retorne el máximo de una lista (no es valido usar la función reverse) utilizando match y luego sin utilizarlo.
def maximo(l: List[Int]): Int = l match{
  case Nil => 0
  case elemento :: Nil => elemento
  case elemento :: tail => elemento max maximo(tail)
}

def maximoSinMatch(l: List[Int]) = {
  l
    .sortBy(x => -x)
    .head
}

//Escribir una función que reciba un entero n y una lista l y retorne una lista con la diferencia de cada uno de la lista a n.
//  Solo debe tener en cuenta los números para los cuales la diferencia es mayor a 10, ignorar el resto.
def diferenciaLista(l: List[Int], n: Int) ={
  l
    .map(y => y - n)
    .filter(y => y > 10)
}



//Dado un texto, crear una función que tome el texto como entrada y devuelva un mapa que muestre la frecuencia de cada palabra en el texto.
//  Los espacios no deben ser considerados
def frecuenciaPalabras(s: String): Map[String, Int] = {
  s
    .toLowerCase
    .split("\\W+")
    .groupBy(palabra => palabra)
    .map((palabra,cantidad) => (palabra, cantidad.length))
}



//
//@Main
object main extends App {
//  val test = entreNumeros(2, 9)
  val lista1 = List(1,2,3,5,3)
  val lista2 = List(2,4,5,6,9)
  val lista3 = List("pala", "hora", "hora", "letra", "horario")
  val texto = "hola como estas me llamo "
  val suma = (a: Int, b: Int) => a + b
  val test2 = frecuenciaPalabras(texto)
  println(test2)
}