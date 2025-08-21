import scala.collection.immutable.Map
import scala.io.Source

case class ArbolXML(nodo: String, dato: String, hijos: List[ArbolXML], atributos: Map[String, String])

def xmlValidator(xml: String): Boolean = {
  val source = scala.io.Source.fromFile(xml)
  val lineas = source.getLines().toList
  val pila = List()
  val validado = validator(lineas, pila)  // devuelve una pila vacia, y un boolean
  source.close()
  return validado(1)
}

def validator(lineas: List[String], pila: List[String]): (List[String], Boolean) = lineas match {
  case Nil if pila.isEmpty => (List(), true)
  case Nil if pila.nonEmpty => (List(),false)
  case nodo :: resto if nodo.stripIndent().startsWith("</") => validator(resto, pila.init) //falta validar si el tope de la pila, es el mismo
  case nodo :: resto if nodo.stripIndent().startsWith("<") => validator(resto, pila :+ nodo)
  case _ :: resto => validator(resto, pila)
}

def parserXml(xml: String): ArbolXML = {
  val source = scala.io.Source.fromFile(xml)
  val lineas = source.getLines().toList
  val pila = List()
  val arbol = parser(lineas, pila) //devuelve un arbol
  source.close()
  return arbol
}

def parser(lineas: List[String], pila: List[ArbolXML]): ArbolXML = lineas match {
  case Nil => pila.head

  case nodo :: resto if nodo.stripIndent().startsWith("</") =>
    val cabeza = pila.head
    pila.tail match {
      case padre :: tail =>
        val padre2 = padre.copy(hijos = padre.hijos :+ cabeza)
        parser(resto, padre2 :: tail)
      case Nil =>
        parser(resto, List(cabeza))
    }

  case nodo :: resto if nodo.stripIndent().startsWith("<") && !nodo.stripIndent().startsWith(("</")) =>
    val cabeza = nodo.stripIndent().drop(1).dropRight(1)
    val partes = cabeza.split("\\s+").toList
    val nombreNodo = partes.head
    val atribu = partes.tail.map { atribu =>
      val Array(k, v) = atribu.split("=")
      k -> v
    }.toMap
    parser(resto, ArbolXML(nombreNodo, "", Nil, atribu) :: pila)

  case nodo :: resto =>
    val cabeza = pila.head.copy(dato = (pila.head.dato + nodo.trim).trim)
    parser(resto, cabeza :: pila.tail)

}




//throw new NoSuchElementException("no hay hijos")



def recorrerArbolXML(arbol: ArbolXML): Unit = {
  println(s"Nodo: ${arbol.nodo}, Dato: ${arbol.dato.trim}, Atributos: ${arbol.atributos}")
  arbol.hijos.foreach(recorrerArbolXML)
}

//def recorrerArbolXML(arbol: ArbolXML):  Unit = arbol match {
//  case ArbolXML(nodo, dato, Nil, atributos) =>
//    println(s"Nodo: ${arbol.nodo}, Dato: ${arbol.dato}, Atributos: ${arbol.atributos}")
//  case ArbolXML(nodo, dato, head :: Nil, atributos) =>
//    println(s"Nodo: ${arbol.nodo}, Dato: ${arbol.dato}, Atributos: ${arbol.atributos}")
//    recorrerArbolXML(head)
//  case ArbolXML(nodo, dato, head :: tail, atributos) =>
//    println(s"Nodo: ${arbol.nodo}, Dato: ${arbol.dato}, Atributos: ${arbol.atributos}")
//    recorrerArbolXML(head)
//    recorrerArbolXML(ArbolXML(nodo, dato, tail, atributos))
//}

//def paths(path: String):



object main extends App{
//  println(parserXml("C:\\Users\\renzo\\OneDrive\\Documentos\\GitHub\\uba.estudios\\algoritmo3 - paradigmas\\TP1-pxslt\\src\\main\\scala\\archivo.xml"))
  recorrerArbolXML(parserXml("C:\\Users\\renzo\\OneDrive\\Documentos\\GitHub\\uba.estudios\\algoritmo3 - paradigmas\\TP1-pxslt\\src\\main\\scala\\archivo.xml"))
}
