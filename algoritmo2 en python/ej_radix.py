
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

def ordenar_cartas_counting_numero(cartas):
	'''
	Devuelve un arrelgo/lista ordenada de cartas, por numero
	Cartas es una lista (o bien, un iterable) de tuplas (palo, numero)
	'''
	separados = []
	for i in range(13):
		separados.append([])

	for carta in cartas:
		palo, numero = carta
		separados[numero_a_indice(numero)].append(carta)

	ordenadas = []
	for de_mismo_num in separados:
		ordenadas.extend(de_mismo_num)
	return ordenadas

def ordenar_cartas_counting_palo(cartas):
	'''
	Devuelve un arrelgo/lista ordenada de cartas, por palo
	Cartas es una lista (o bien, un iterable) de tuplas (palo, numero)
	'''
	separados = []
	for i in range(4):
		separados.append([])

	for carta in cartas:
		palo, numero = carta
		separados[palo_a_indice(palo)].append(carta)

	ordenadas = []
	for de_mismo_num in separados:
		ordenadas.extend(de_mismo_num)
	return ordenadas

def ordenar_cartas_radix(cartas):
	parcial = ordenar_cartas_counting_numero(cartas)
	ordenados = ordenar_cartas_counting_palo(parcial)
	return ordenados

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


