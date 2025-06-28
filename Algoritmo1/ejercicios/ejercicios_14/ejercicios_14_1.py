# Escribir una clase TorreDeControl que modele el trabajo de una torre de control de
# un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen
# prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al
# siguiente ejemplo:
# >>> torre = TorreDeControl()
# >>> torre.nuevo_arribo('AR156')
# >>> torre.nueva_partida('KLM1267')
# >>> torre.nuevo_arribo('AR32')
# >>> torre.ver_estado()
# Vuelos esperando para aterrizar: AR156, AR32
# Vuelos esperando para despegar: KLM1267
# >>> torre.asignar_pista()
# El vuelo AR156 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo AR32 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo KLM1267 despegó con éxito.
# >>> torre.asignar_pista()
# No hay vuelos en espera.




class TorreDeControl:
    def __init__(self) -> None:
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, avion):
        self.arribos.append(avion)

    def nueva_partida(self, avion):
        self.partidas.append(avion)

    def ver_estado(self):
        if not self.arribos and not self.partidas:
            print("No hay vuelos en espera")
        else:
            llegadas = str(self.arribos)
            salidas = str(self.partidas)
            print(f"Vuelos esperando para aterrizar: {llegadas}")
            print(f"Vuelos esperando para despegar: {salidas}")

    def asignar_pista(self):
        if not self.arribos and self.partidas:
            partida = self.partidas.pop()
            print(f"El vuelo {partida} despego con éxito.")
        elif self.arribos:
            despegue = self.arribos.pop()
            print(f"El vuelo {despegue} aterrizó con éxito.")
        else:
            print("No hay vuelos en espera.")


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()