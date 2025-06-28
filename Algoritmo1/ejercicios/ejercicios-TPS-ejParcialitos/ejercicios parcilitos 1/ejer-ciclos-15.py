# Escribir una función que realice lo siguiente: - Le pida al usuario que ingrese una contraseña. 
# Luego debe validar que la misma: 
# - Tenga al menos dos numeros, pero no tenga más números que letras
# (a-z, A-Z, no es necesario incluir letras acentuadas o especiales de otros idiomas que no sea el ingles). 
# - Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres. 
# - Si no ingresa una contraseña válida debe volver a preguntarle hasta quedarse sin intentos. 
# - Cuando sea válida, se deben devolver la cantidad de intentos restante. 
# Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1. 
# La cantidad de intentos es recibida por parametro.

def validar_contraseña(intentos: int) -> int:
    caracteres = ("!", "@", "~", "/", "#")
    numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    
    while intentos > 0:
        contra = input("ingrese una contraseña: ")
        longitud_caracteres = len(contra)
        cant_numeros = 0
        cant_caracteres_especiales = 0
        for i in contra:
            if i in numeros:  
                cant_numeros += 1
            elif i in caracteres:
                cant_caracteres_especiales += 1
        #achicar if maybe
        if 1 <= cant_caracteres_especiales <= 3 and (longitud_caracteres - cant_numeros - cant_caracteres_especiales) > cant_numeros and cant_numeros >= 2:
            return intentos - 3
        else:
            intentos -= 1
            print("La contraseña debe contener al menos: 2 numeros y menor cantidad de numeros que letra")
            print("entre 1 y 3 caracteres de los siguientes '!', '@', '~', '/', '#'")
            print(f"te quedan {intentos} intentos")
    return -1             

validar_contraseña(4)

