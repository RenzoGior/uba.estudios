import math


def coordenadas_vector_r3 (x, y, z) -> tuple:
    "A) Escribir una función que reciba las coordenadas de un vector en R3 (x,y,z) y devuelva la norma del vector, "
    return (x, y, z)," -> ", math.sqrt(x ** 2 + y ** 2 + z ** 2)

# print(coordenadas_vector_r3(3, 2, -4))



def diferencia_vectores (x1, y1, z1, x2, y2, z2) -> tuple:
    "B) Escribir una función que reciba las coordenadas de dos vectores en R3 y devuelva las coordenadas del vector diferencia"
    return (x1, y1, z1, x2, y2, z2), " -> ", ((x1 - x2), (y1 - y2), (z1 - z2)) 

#print(diferencia_vectores(8, 7, -3, 5, 3, 2))


def producto_vectorial (x1, y1, z1, x2, y2, z2) -> tuple: #or list, 
    "c) Escribir una función que reciba las coordenadas de dos vectores en R3 y devuelva las coordenadas del producto vectorial"
    return (x1, y1, z1, "x", x2, y2, z2), "=", (y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2 )

#print(producto_vectorial(1, 4, -2, 3, -1, 0))


# def area_triangulo_vector (x1, y1, z1, x2, y2, z2, x3, y3, z3) -> tuple:
#     "Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de 3 puntos en R3 y devuelva el área del triángulo que conforman."
#     a1, b1, c1 = producto_vectorial2 (x1, y1, z1, x2, y2, z2) # desenpaqueta
#     a2, b2, c2 = producto_vectorial2 (x1, y1, z1, x3, y3, z3)
#     norma1 = coordenadas_vector_r3_2(a1, b1 , c1)
#     norma2 = coordenadas_vector_r3_2(a2, b2, c2)
    
#     return  (norma1 * norma2) / 2
def coordenadas_vector_r3_2 (x, y, z) -> tuple:
    "D) Escribir una función que reciba las coordenadas de un vector en R3 (x,y,z) y devuelva la norma del vector, "
    return math.sqrt((x ** 2) + (y ** 2) + (z ** 2))

def producto_vectorial2 (x1, y1, z1, x2, y2, z2) -> tuple: #or list, 
    "D)Escribir una función que reciba las coordenadas de dos vectores en R3 y devuelva las coordenadas del producto vectorial"
    return ((y1 * z2) - (z1 * y2), (z1 * x2) - (x1 * z2), (x1 * y2) - (y1 * x2) )


def area_triangulo_vector (x1, y1, z1, x2, y2, z2, x3, y3, z3) -> tuple:
    "D) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de 3 puntos en R3 y devuelva el área del triángulo que conforman."
    a1, b1, c1 =  (x2 - x1, y2 - y1, z2 - z1)     #desempaquetado
    a2, b2, c2 =  (x3 - x1, y3 - y1, z3 - z1)    
    a3, b3, c3 = producto_vectorial2 (a1, b1, c1, a2, b2, c2)
    
    return "area del triangulo: ",(x1, y1, z1, x2, y2, z2, x3, y3, z3), "-> "  ,coordenadas_vector_r3_2(a3, b3, c3)/2


#print(area_triangulo_vector (5, 8, -1, -2, 3, 4, -3, 3, 0))


def area_cuadrilatero (x1, y1, x2, y2, x3, y3, x4, y4):
    "E)  retomar en otro momento"
    return x1

area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5)