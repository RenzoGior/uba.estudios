
def palo_a_indice(palo):
	if palo == "Picas":
		return 0
	elif palo == "Corazones":
		return 1
	elif palo == "Trebol":
		return 2
	elif palo == "Diamantes":
		return 3

def numero_a_indice(numero):
	# Si bien dice 'numero', puede ser una letra como A, J, Q, K
	if numero == "A":
		return 0
	elif numero == "J":
		return 10
	elif numero == "Q":
		return 11
	elif numero == "K":
		return 12
	else:
		return int(numero) - 1

def ordenar_counting(coleccion, cantidad, indexador):
	'''
	Devuelve un arrelgo/lista ordenada de los elementos de la coleccion, por el criterio que se indique
	Coleccion es una lista (o bien, un iterable).
	Cantidad es la cantidad de valores que puede llegar a tomar cada carta
	indexador es una funcion que asinga el indice a cada carta (indexador: Carta -> [0; cantidad-1])
	'''
	separados = []
	for i in range(cantidad):
		separados.append([])

	for elem in coleccion:
		separados[indexador(elem)].append(elem)

	ordenadas = []
	for de_mismo_indice in separados:
		ordenadas.extend(de_mismo_indice)
	return ordenadas

def ordenar_cartas_radix(cartas):
	parcial = ordenar_counting(cartas, 13, lambda carta: numero_a_indice(carta[1]))
	ordenadas = ordenar_counting(parcial, 4, lambda carta: palo_a_indice(carta[0]))
	return ordenadas

def main():
	# Uso mismo ejemplo que las diapositivas
	mazo = [
		("Picas", "8"),
		("Trebol", "7"),
		("Corazones", "3"),
		("Trebol", "8"),
		("Picas", "7"),
		("Corazones", "A"),
		("Trebol", "7"),
		("Diamantes", "3"),
		("Picas", "Q"),
		("Diamantes", "2"),
		("Diamantes", "A"),
		("Corazones", "2"),
		("Corazones", "8"),
		("Diamantes", "J")
	]
	ordenadas = ordenar_cartas_radix(mazo)
	print("Cartas ordenadas: " + str(ordenadas))

if __name__ == "__main__":
	main()


