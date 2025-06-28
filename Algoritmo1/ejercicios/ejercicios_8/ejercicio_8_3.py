# Agenda simplificada
# Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
# telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
# la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
# Debe devolver una lista con todas las tuplas encontradas.

def agenda_simplificada(s: str, L: list) -> list:
    L.sort()
    encontradas = []
    columnas = len(L)
    for i in range(columnas):
        for n in L[i]:
            if s in n:
                encontradas.append(L[i])
    return encontradas



def main():
    agenda = [
        ("Juan Pérez", "123-456-7890"),
        ("María García", "234-567-8901"),
        ("Luis Martínez", "345-678-9012"),
        ("Ana López", "456-789-0123"),
        ("Pedro Sánchez", "567-890-1234"),
        ("Laura Rodríguez", "678-901-2345"),
        ("Carlos López", "789-012-3456"),
        ("Sofía Martín", "890-123-4567"),
        ("David García", "901-234-5678"),
        ("Marta Pérez", "012-345-6789")
    ]
    agenda_simplificada("Juan ", agenda)
    
main()