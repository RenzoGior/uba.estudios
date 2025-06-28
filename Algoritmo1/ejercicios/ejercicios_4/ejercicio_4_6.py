# Suponiendo que el primer día del año fue lunes, escribir una función que reciba
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
# si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

"""testeando blackbox"""

def get_day_of_week(day_of_year: int) -> str:
  """Devuelve el día de la semana correspondiente a un día del año.
  Args:
    day_of_year: Un entero entre 1 y 366.
  Returns:
    Un string con el día de la semana.
  """
  # Comprueba si el día del año es válido.
  if day_of_year < 1 or day_of_year > 366:
    raise ValueError("El día del año debe estar entre 1 y 366.")
  # Calcula el día de la semana.
  day_of_week = (day_of_year + 6) % 7
  # Devuelve el día de la semana.
  return ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"][day_of_week]


def main():
    print(get_day_of_week(9))


main()