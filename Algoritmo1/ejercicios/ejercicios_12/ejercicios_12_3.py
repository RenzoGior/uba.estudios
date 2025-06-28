# a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
# sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]

class Vector:
    
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

# b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
# cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
# misma cantidad de elementos debe levantar una excepción.
        
    def __add__ (self, otro):
        try:
            if len(self) == len(otro):
                return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z )
        except:
            print("no tienen la misma cantidad de elementos")

    def __len__(self):
        return len(self)

# c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
# los elementos multiplicados por ese número.
            
    def __mul__(self, n):
        return Vector(self.x * n, self.y * n, self.z * n)
        
    def __str__(self) -> str:
        print(f"[{self.x},{self.y},{self.z}]")