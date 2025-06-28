import ejercicio_1_5

def preguntar_cantidad() -> int:
    return int(input ("de cuantos numeros desea realizar el factorial: "))

   
def preguntar_numero() -> int:
    return int(input ("ingrese el valor de los numeros: "))
  

def main(): 
    """funcion main, que invoca la funciones preguntar numero/cantidad, y realiza el factorial de los numeros dados. a ala vez importa el ejercicio 1_5 que calcula
    el factorial de un numero"""
    numeros = preguntar_cantidad()
    for i in range(numeros):
        i = preguntar_numero()
        print ("el factorial de ", i,"es: ", ejercicio_1_5.factorial(i))
    
main()