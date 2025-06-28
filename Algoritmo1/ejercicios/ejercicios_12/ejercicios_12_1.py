# a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
# instantes de tiempo (números enteros expresados en segundos), con la condición desde
# < hasta.

class Intervalo:
    """representa un intervalo entre dos intantes de tiempo, representados en segundos"""

    def __init__(self, desde: int, hasta: int) -> None:
        """constructor del tiempo, desde y hasta deben ser numeros enteros"""
        self.desde = desde
        self.hasta = hasta

# b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
        
    def duracion(self):
        """devuelve la duracion en segundos, """
        return self.hasta - self.desde

# c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
# tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
# es nula.
       
    def interseccion(self, otro):
        """duvuelve la interseccion entre dos intervalos"""
        return Intervalo(self.desde - otro.desde, self.hasta - otro.hasta)

# d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
# centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
# intervalo resultante de la unión entre ambos.

    def union(self, otro):
        return




    def __str__(self):
        return f"{abs(self.desde)}, {abs(self.hasta)}"
       
