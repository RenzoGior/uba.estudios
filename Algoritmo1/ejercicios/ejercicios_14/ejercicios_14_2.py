# Escribir las clases Impresora y Oficina que permita modelar el funcionamiento
# de un conjunto de impresoras conectadas en red.
# Ejemplo:
# >>> o = Oficina()
# >>> o.agregar_impresora(Impresora('HP1234', 1))
# >>> o.agregar_impresora(Impresora('Epson666', 5))
# >>> o.impresora('HP1234').encolar('tp1.pdf')
# >>> o.impresora('Epson666').encolar('tp2.pdf')
# >>> o.impresora('HP1234').encolar('tp3.pdf')
# >>> o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
# >>> o.impresora('HP1234').imprimir()
# tp1.pdf impreso
# >>> o.impresora('HP1234').imprimir()
# No tengo tinta :(
# >>> o.impresora('HP1234').cargar_tinta()
# >>> o.impresora('HP1234').imprimir()
# tp3.pdf impreso

class Impresora:
    # Una impresora:
    # • Tiene un nombre, y una capacidad máxima de tinta.
    # • Permite encolar un documento para imprimir (recibiendo el nombre del documento).
    # • Permite imprimir el documento que está al frente de la cola.
    #   – Si no hay documentos encolados, se muestra un mensaje informándolo.
    #   – Si no hay tinta suficiente, se muestra un mensaje informándolo.
    #   – En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
    # • Permite cargar el cartucho de tinta
    def __init__(self, nombre, tinta = 0) -> None:
        self.items = []
        self.nombre = nombre
        self.tinta = tinta


    def encolar(self, x):
        self.items.append(x)
       
    def cargar_tinta(self):
        if self.tinta <= 5:
            self.tinta += 1
        else:
            print("no me entra mas tinta :(")

    def imprimir(self):
        if self.esta_vacia():
            print("no tengo nada que imprimir")
        elif self.tinta <= 0:
            print("no tengo tinta")
        else:
            imprimio = self.items.pop(0)
            self.tinta -= 1
            print(f"{imprimio} impreso")

    def esta_vacia(self):
        """Devuelve True si la cola esta vacía, False si no."""
        return len(self.items) == 0

class Oficina:
    # Una oficina:
    # • Permite agregar una impresora
    # • Permite obtener una impresora por nombre
    # • Permite quitar una impresora por nombre
    # • Permite obtener la impresora que tenga menos documentos encolados.
    def __init__(self) -> None:
        self.oficina = []

    def agregar_impresora(self, Impresora):
        nueva = "asd"
        self.oficina.append(Impresora)

    def obtener_impresora(self, nombre):
        for item in self.oficina:
            if nombre == item:
                print(f"{item}")
                break
        print(f"la impresora {nombre}, no existe")

    # def quitar_impresora(self, nombre):
    #     for item in self.oficina:
        

o = Oficina()
o.agregar_impresora(Impresora('HP1234', 1))
o.agregar_impresora(Impresora('Epson666', 5))
o.impresora('HP1234').encolar('tp1.pdf')
o.impresora('Epson666').encolar('tp2.pdf')
o.impresora('HP1234').encolar('tp3.pdf')
o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
o.impresora('HP1234').imprimir()
# tp1.pdf impreso
o.impresora('HP1234').imprimir()
# No tengo tinta :(
o.impresora('HP1234').cargar_tinta()
o.impresora('HP1234').imprimir()



