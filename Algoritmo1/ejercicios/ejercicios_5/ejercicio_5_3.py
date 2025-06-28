import time 

# Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
# rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

def manejo_contraseña():
    contraseña = input("introduzca la contraseña: " )
    clave = ["elcuco", "señor", "1234"]
    while contraseña in clave:
        return("iniciando sesion...")
    
        

# b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
# tos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.

def cantidad_fija():
    intentos = 3
    i = 0
    while i < intentos:
        i += 1
        if manejo_contraseña():
            return "sesion iniciada"
        time.sleep(i)
        print("introduzca una contraseña correcta ")
        







def main():
    #manejo_contraseña()
    cantidad_fija()
    


main()
