import math
base_rectangulo = 6
altura_rectangulo = 4 
x1 = 2
x2 = 8
y1 = 3
y2 = 6
radio_circulo = 5
radio_esfera = 10
cateto_a = 4
cateto_b = 6

def perimetro_de_rectangulo():
    "funcion para calcular el perimetro de un rectangulo"
    suma_lados = base_rectangulo * 2 + altura_rectangulo * 2
    return suma_lados

perimetro_de_rectangulo()
print ("el perimetro del rectangulo es ", perimetro_de_rectangulo())

def area_de_rectangulo():
    "funcion para calcular el area de un rectangulo"
    base_por_altura = base_rectangulo * altura_rectangulo
    return base_por_altura

area_de_rectangulo()
print ("el area del rectangulo es ", area_de_rectangulo())

def area_rectangulo_cordenadas(x1, x2, y1, y2):
    "calcula el area de un rectangulo dadas unas cordenadas en un eje x y"
    base = x1 - x2
    altura = y1 - y2 
    area = base * altura
    return area 

area_rectangulo_cordenadas(x1, x2, y1, y2)
print ("el area del rectangulo dada sus cordenadas es :", area_rectangulo_cordenadas(x1, x2, y1, y2))

def perimetro_circulo_radio ():
    "define el perimetro de un circulo dado su radio"
    perimetro = 2 * math.pi * radio_circulo 
    return perimetro

perimetro_circulo_radio ()
print ("el perimetro del circulo dado su radio es: ", perimetro_circulo_radio ())

def area_circulo_radio():
    "calcula el area de un circulo "
    area = math.pi * (radio_circulo ** 2)
    return area

area_circulo_radio()
print("el area del circulo dado su radio es: ", area_circulo_radio())


def volumen_esfera ():
    "calcula el volumen de una esfera"
    volumen = 4/3 * math.pi * radio_esfera ** 3
    return  volumen

volumen_esfera()
print("el volumen de la esfera es: ", volumen_esfera())


def catetos_triangulos ():
    "calcula la hipotenusa dado sus catetos"
    hipotenusa = math.sqrt (cateto_a ** 2 + cateto_b ** 2)
    return hipotenusa

catetos_triangulos()
print("la hipotenusa es: ", catetos_triangulos())