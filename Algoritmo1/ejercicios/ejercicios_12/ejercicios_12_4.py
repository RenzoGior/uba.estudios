# Escribir una clase Caja para representar cuánto dinero hay en una caja de un
# negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
# de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
# 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
# >>> c = Caja({500: 6, 300: 7, 2: 4})
# ValueError: Denominación "300" no permitida
# >>> c = Caja({500: 6, 100: 7, 2: 4})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
# >>> c.agregar({250: 2})
# ValueError: Denominación "250" no permitida
# >>> c.agregar({50: 2, 2: 1})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
# >>> c.quitar({50: 3, 100: 1})
# ValueError: No hay suficientes billetes de denominación "50"
# >>> c.quitar({50: 2, 100: 1})
# 200
# >>> str(c)
# 'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'
            # "1": 0, 
            # "2": 0, 
            # "5": 0, 
            # "10": 0, 
            # "20": 0, 
            # "50": 0, 
            # "100": 0, 
            # "200": 0, 
            # "500": 0, 
            # "1000": 0,

def billetes_validos(D: dict):
        validos = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000] 
        for valor in D.keys():
            if valor not in validos:
                raise ValueError("Denominación no permitida")



class Caja:

    def __init__(self, billetes = None) -> None:
        """"""
        if billetes is None: #si no se pasa dicccionario por atributo se crea
            billetes = {}  
        self.billete = billetes
        billetes_validos(self.billete) # chequea que los billetes pasados sean validos
            
            
    def agregar(self, billetes): 
        for valor, cantidad in billetes.items(): #desenpaqueta el diccionario
            billetes_validos(self.billete) # chequea que los billetes pasados sean validos
            if valor in self.billete:
                self.billete[valor] += cantidad
            else:
                self.billete[valor] = cantidad

    def quitar(self, billetes): 
        for valor, cantidad in billetes.items():
            billetes_validos(self.billete) # chequea que los billetes pasados sean validos
            if valor in self.billete:
                if self.billete[valor] < cantidad:
                    raise ValueError(f"No hay suficientes billetes de denominación {valor}")
                else:
                    self.billete[valor] -= cantidad
            else:
                raise ValueError(f"No hay billetes de denominación {valor}")


    def __str__(self):
        suma = 0
        for billete, cantidad in self.billete.items(): #desempaqueta las claves del diccionario, y las multiplica
            suma += billete * cantidad
        return (f"Caja {self.billete}, total: {suma} pesos")



c = Caja({500: 6, 100: 7, 2: 4})
print(str(c))



c.agregar({50: 2, 2: 1})
print(str(c))
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'


c.quitar({50: 2, 100: 1})

print(str(c))
