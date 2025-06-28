# Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# # excepto que también sea divisible por 400.

"""NO FUNCIONA
def es_bisiesto (año):
    if año % 4 == 0:
        #es divisible por 4
        if año % 100 != 0:
            #es divisible por 4 pero no por 100
            return True
        else:
            # es divisible por 100
            if año % 400 == 0:
                return False
            else:
                return True
    else:
        #no es divisible por 4
        return False


assert es_bisiesto(2003) == False
assert es_bisiesto(2004) == True
assert es_bisiesto(1700) == False
assert es_bisiesto(1600) == True
"""
"-----------------------------------------------------------------------------"

def es_bisiesto_elegante (año):
    if año % 400 == 0:
        #es divisible por 400
        return True
    #no es divisible por 400
    if año % 100 == 0:
        #es divisible por 100
        return False
    #no es divisible por 400 ni por 100
    if año % 4 == 0:
        return True
    else:
        return False

assert es_bisiesto_elegante(2003) == False
assert es_bisiesto_elegante(2004) == True
assert es_bisiesto_elegante(1700) == False
assert es_bisiesto_elegante(1600) == True



"-----------------------------------------------------------------------------"
"EARLY RETURN"

def es_bisiesto_elegante_mejorado (año):
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    return año % 4 == 0


assert es_bisiesto_elegante_mejorado(2003) == False
assert es_bisiesto_elegante_mejorado(2004) == True
assert es_bisiesto_elegante_mejorado(1700) == False
assert es_bisiesto_elegante_mejorado(1600) == True

print("funciona :)")

# b) Dado un mes y un año, devolver la cantidad de días correspondientes.


def mes_año_a_dias (mes: str, año: int) -> int:
    if mes.lower() in ('enero', 'marzo', 'julio', 'agosto', 'octubre', 'diciembre'): # funcion lower convierte a minusculaz el string ingresado
        return 31
    if mes.lower() == "febrero":
        if es_bisiesto_elegante_mejorado(año):
            return 29
        return 28
    return 30

#c) Dada una fecha (día, mes, año), indicar si es válida o no.

def fecha_valida(dia: int, mes: int, año: int) -> bool:
   return 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 0

assert fecha_valida(1, 10, 1999) == True
assert fecha_valida (111, 10, 100) == False

# d) Dada una fecha, indicar los días que faltan hasta fin de mes.

def fin_de_mes (dia: int, mes: str, año: int) -> int:
    return mes_año_a_dias(mes, año) - dia

# e) Dada una fecha, indicar los días que faltan hasta fin de año.

def dias_fin_de_año(dia: int, mes: str, año: int) -> int:
    suma_meses = 0
    for i in ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'):
        if mes == i:
            return 365 - (dia + suma_meses)
        meses = mes_año_a_dias(i, año)
        suma_meses += meses

# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.


def dias_transcurridos(dia: int, mes: str, año: int) -> int:
    suma_meses = 0
    for i in ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'):
        if mes == i:
            return (dia + suma_meses)
        meses = mes_año_a_dias(i, año)
        suma_meses += meses

# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
# entre ambas, en años, meses y días.

def dos_fechas (dia1: int, mes1: int, año1: int, dia2: int, mes2: int, año2: int) :
    resta_dia = dia1 - dia2
    resta_meses = mes1 - mes2
    resta_años = año1 - año2
    if resta_dia < 0:
        resta_dia *= -1
    if resta_meses < 0:
        resta_meses *= -1
    if resta_años < 0:
        resta_años *= -1
    return f"Tiempo transcurrido: {resta_años} años, {resta_meses} meses y {resta_dia} días, entre las dos fechas"




def main():
   #print(mes_año_a_dias("FebRero", 2003))
   #print("faltan", fin_de_mes(20, "febrero", 2003), "dias para fin de mes")
   #print(dias_fin_de_año(2,'diciembre', 2004 ))
   print(dias_transcurridos(3,'febrero', 1999))
   print(dos_fechas( 20, 6, 2004, 2, 5, 2002))

main()