# a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
# asignan en el constructor, y se imprimen como X/Y en el método __str__.
class Fraccion:

    def __init__(self, dividendo, divisor) -> None:
        self.dividendo = dividendo
        self.divisor = divisor

# b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
# con la suma de ambas.
    
    def __add__(self, otro):
        if self.divisor == otro.divisor:
            return Fraccion(self.dividendo + otro.dividendo, self.divisor)
        return Fraccion(self.dividendo + otro.dividendo, self.divisor + otro.divisor)

# c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
# con el producto de ambas.
    
    def __mul__(self, otro):
        return Fraccion(self.dividendo * otro.dividendo, self.divisor * otro.divisor)

# d) Crear un método simplificar que modifica la fracción actual de forma que los valores
# del dividendo y divisor sean los menores posibles.
    
    def simplificar(self):
        return


    def __str__(self):
        return f"{(self.dividendo)}/{(self.divisor)}"