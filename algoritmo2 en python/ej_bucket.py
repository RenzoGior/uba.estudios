
def indice_jugador(promedio):
	if promedio <= 0.03:
		return 0
	elif promedio <= 0.08:
		return 1
	elif promedio <= 0.15:
		return 2
	elif promedio <= 0.25:
		return 3
	else:
		return 4

def ordenar_bucket_jugadores(jugadores):
	buckets = []
	for i in range(5):
		buckets.append([])
	for jugador in jugadores:
		nombre, promedio = jugador
		buckets[indice_jugador(promedio)].append(jugador)
	buckets_ordenados = []
	for i in range(len(buckets)):
		buckets_ordenados.append(sorted(buckets[i], key=lambda jugador: jugador[1]))
	ordenados = []
	for bucket in buckets_ordenados:
		ordenados.extend(bucket)
	return buckets, buckets_ordenados, ordenados

def main():
	jugadores = [
		("Tagliafico", 0.04), 
		("Mercado", 0.07), 
		("Kannemann", 0.03), 
		("Pezzella", 0.05), 
		("Acuna", 0.1), 
		("Lisandro Martinez", 0.06), 
		("Montiel", 0.04), 
		("Saravia", 0), 
		("Foyth", 0.03), 
		("Paredes", 0.11), 
		("Pereyra", 0.09), 
		("Lanzini", 0.18), 
		("Correa", 0.18), 
		("Lo Celso", 0.14), 
		("Guido Rodriguez", 0.08), 
		("De Paul", 0.11), 
		("Marcone", 0), 
		("Blanco", 0), 
		("Pity Martinez que loco que estas", 0.17), 
		("Messi", 0.91), 
		("Benedetto", 0.42), 
		("Matias Suarez", 0.25), 
		("Dybala", 0.39), 
		("Lautaro Martinez", 0.4), 
		("Di Maria", 0.23), 
		("Zaracho", 0.1)
	]
	b, b_ord, ordenados = ordenar_bucket_jugadores(jugadores)
	print("Separacion en buckets: " + str(b))
	print()
	print("Cada bucket ordenado: " + str(b_ord))
	print()
	print("Jugadores Ordenados: " + str(ordenados))


if __name__ == "__main__":
	main()
