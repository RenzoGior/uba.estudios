# Persistencia de un diccionario
# a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
# tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
# y el segundo como diccionario.

def cargar_datos(archivo: str) -> dict:
    diccionario ={}
    with open(archivo) as file:
        for linea in file:
            linea = linea.rstrip("\n")
            clave, valor = linea.split(': ')
            diccionario[clave] = valor
    return diccionario

# b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
# y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

def guardar_datos(diccionario: dict, nombre: str):
    with open(nombre, "w") as archivo:
            for i in diccionario:
                archivo.write(i)
                archivo.write(": ")
                archivo.write(diccionario[i])
                archivo.write("\n")
            
def main():
    nombre_archivo = "diccionario.txt"
    diccionario_copiar = "diccionario_copiar.txt"
    diccionario_guardar = cargar_datos(nombre_archivo)
    guardar_datos(diccionario_guardar, diccionario_copiar)

main()