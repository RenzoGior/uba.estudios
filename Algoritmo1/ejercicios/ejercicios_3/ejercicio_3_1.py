

def hora_minutos_a_segundos(h, m, s):
    "dado un intervalo de horas, minutos y segundos, devuelve su duracion en segundos"
    return (h * 3600) + (m * 60) + s


hora_minutos_a_segundos(1, 1, 0)

def minutos_segundos_a_horas(s):
    "dado segundos, devuelve su duracion en horas, minutos y segundos"
    horas = s // 3600
    minutos = (s % 3600) // 60
    segundos =  (s % 3600) % 60
    return  horas, minutos, segundos

minutos_segundos_a_horas(2600)