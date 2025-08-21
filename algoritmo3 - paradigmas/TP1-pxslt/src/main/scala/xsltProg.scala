import scala.io.StdIn

//hacer parser de xml

//hacer



object xsltProg {
  try {
    def main(args: List[String]): Unit = args match {
      case Nil => println("no se pasaron argumentos, ni parametros")
      case xslt :: xml :: parametros => println()
    }
  } catch {
    case e: Exception =>  println(s"Error: ${e}")
  }
}