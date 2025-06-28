# Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
# el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
# número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
# pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe
# devolver.

def pedir_entero(mensaje: str, min: int, max: int) -> str:
    while True:
        valor = int(input(mensaje))
        if valor < min or valor > max:
            return valor
  

def main():
    z = pedir_entero("¿Cuál es tu número favorito? ", -50, 50)
    print(z)
main()