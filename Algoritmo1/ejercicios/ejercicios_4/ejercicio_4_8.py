# Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
# y el programa le debe decir a qué signo corresponde.
"""
Aries: 21 de marzo al 20 de abril.                      Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.                     Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.                       Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.               Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.          Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.                  Piscis: 20 de febrero al 20 de marzo."""


# se pisan 
def astrologia (dia: int, mes: str) -> str:
    if (31 >= dia >= 21 or 20 >= dia >= 1) and (mes == "abril" or mes == "marzo"):
        return "Su signo es Aries" 
    elif (31 >= dia >= 21 or 21 >= dia >= 1) and (mes == "junio" or mes == "mayo"):
        return "Su signo es Geminis" 
    elif (31 >= dia >= 24 or 23 >= dia >= 1) and (mes == "agosto" or mes == "julio"):
        return "Su signo es Leo" 
    elif (30 >= dia >= 24 or 22 >= dia >= 1) and (mes == "octubre" or mes == "septiembre"):
        return "Su signo es Libra" 
    elif (30 >= dia >= 23 or 22 >= dia >= 1) and (mes == "noviembre" or mes == "diciembre"):
        return "Su signo es Sagitario" 
    elif (31 >= dia >= 21 or 19 >= dia >= 1) and (mes == "febrero" or mes == "enero"):
        return "Su signo es Acuario" 
    elif (30 >= dia >= 21 or 20 >= dia >= 1) and (mes == "mayo" or mes == "abril"):
        return "Su signo es Tauro" 
    elif (31 >= dia >= 21 or 23 >= dia >= 1) and (mes == "julio" or mes == "junio"):
        return "Su signo es Cancer" 
    elif (31 >= dia >= 21 or 23 >= dia >= 1) and (mes == "septiembre" or mes == "agosto"):
        return "Su signo es Virgo" 
    elif (31 >= dia >= 21 or 22 >= dia >= 1) and (mes == "noviembre" or mes == "octubre"):
        return "Su signo es Escorpio" 
    elif (31 >= dia >= 21 or 20 >= dia >= 1) and (mes == "enero" or mes == "diciembre"):
        return "Su signo es Capricornio" 
    elif (29 >= dia >= 21 or 20 >= dia >= 1) and (mes == "marzo" or mes == "febrero"):
        return "Su signo es Piscis" 
    return"ingrese una fecha valida"





def main():
    dias = int(input("ingrese su dia de cumpleaños: "))
    meses = str(input("ingrese su mes de cumpleaños: "))
    print(astrologia(dias, meses))


main()