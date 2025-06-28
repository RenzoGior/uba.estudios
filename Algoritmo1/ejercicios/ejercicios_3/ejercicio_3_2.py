import ejercicio_3_1

def intervalos_horas_minutos_segundos() -> int:
    "le pide al usuario que ingrese hora, minutos, segundos. los transforma a segundos usando la funcion del ejercicio anterior"
    horas = int(input("ingrese las horas: "))
    minutos = int(input("ingrese los minutos: "))
    segundos = int(input("ingrese los segundos: "))
    return ejercicio_3_1.hora_minutos_a_segundos(horas, minutos, segundos) 


def main():
    "funcion main, que suma los dos intervalos ya convertidos a segundos, y el resultado lo transforma, a horas, minutos,segundos. usando la funcion del ejercicio anterior"
    intervalo1 = intervalos_horas_minutos_segundos()
    intervalo2 = intervalos_horas_minutos_segundos()
    suma_intervalos = intervalo1 + intervalo2
    print(ejercicio_3_1.minutos_segundos_a_horas(suma_intervalos))

     


main()