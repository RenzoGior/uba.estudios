import  ejercicio_2_3


def tabla_conversion ( ):
    "un programa que usa la funcion de el ejercicio anterior, cambia grados farenheit a grados celcius"
    lista = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120]
    for i in lista:
        conversion = ejercicio_2_3.temperaturas(i)
        print (conversion)
    return "estas son las conversiones de temperatura de ferenheit a celcius "

print(tabla_conversion())



#lista = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120]

#lista = ejercicio_2_3.temperaturas(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120)
