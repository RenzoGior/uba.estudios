
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

def ordenar_cartas_counting_completo(cartas):
	'''
	Devuelve un arrelgo/lista ordenada de cartas, por numero (como en el ejemplo
	de las diapositivas)
	Cartas es una lista (o bien, un iterable) de tuplas (palo, numero)
	'''
	frecuencias = []
	# inicializo todas las frecuencias en 0
	for i in range(13):
		frecuencias.append(0)

	# cuento la frecuencia de cada numero
	for carta in cartas:
		palo, numero = carta
		frecuencias[numero_a_indice(numero)] += 1

	# obtengo el arreglo de sumas acumuladas
	acum = []
	# pongo la primera posicion en 0
	acum.append(0)
	for i in range(1, 13):
		acum.append(acum[i - 1] + frecuencias[i - 1])

	# pongo las cartas en donde corresponde
	ordenadas = []
	for i in range(len(cartas)): 
		# inicializo, porque en Python no tengo un "arreglo" propiamente dicho
		# Este paso en C no sería necesario
		ordenadas.append(None)

	for carta in cartas:
		palo, numero = carta
		indice = acum[numero_a_indice(numero)]
		ordenadas[indice] = carta
		acum[numero_a_indice(numero)] += 1

	return frecuencias, acum, ordenadas

def ordenar_cartas_counting_simple(cartas):
	'''
	Devuelve un arrelgo/lista ordenada de cartas, por numero (como en el ejemplo
	de las diapositivas)
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
	return separados, ordenadas


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
	freq, acum, ordenadas = ordenar_cartas_counting_completo(mazo)
	print("Version completa:")
	print("\tFrecuencias: " + str(freq))
	print("\tAcumulado: " + str(acum))
	print("\tOrdenadas: " + str(ordenadas))
	print()
	sep, ordenadas = ordenar_cartas_counting_simple(mazo)
	print("Version Simple:")
	print("\tSeparadas: " + str(sep))
	print("\tOrdenadas: " + str(ordenadas))

if __name__ == "__main__":
	main()

