import ejercicio_2_5

def programa_par(n, m):
    n = int(input("ingrese un numero: "))
    m = int(input("ingrese otro numero: "))
    for numeros in range(n, m+1):
        if ejercicio_2_5.es_par(numeros): 
            print("el", numeros, "es par")
        else:
            print("el", numeros, "es inpar")
        

    
programa_par(1,0)