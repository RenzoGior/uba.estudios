"""ayuda profe"""
"desarrollo guiado por pruebas  // test driven development"

# * Escribir un programa que reciba como entrada un entero representando un
# año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
# romanos.
"""
def a_romano(año):
    return "I" * año




assert a_romano(1) == "I"
assert a_romano(2) == "II"
assert a_romano(3) == "III"
"""

"""-------------------------------"""

"""copiar los ejercicios de la teorica, apuntes"""

# def split_integer(integer: int) -> int:
#   """Divide un entero en una lista de dígitos.
#   Args:
#     integer: El entero a dividir.
#   Returns:
#     Una lista de dígitos.
#   """
#   # Convierte el entero a una cadena.
#   integer_str = str(integer)
#   # Divide la cadena en una lista de caracteres.
#   digits = list(integer_str)
#   # Convierte los caracteres en enteros.
#   digits = [int(digit) for digit in digits]
#   # Devuelve la lista de dígitos.
#   return digits

# def a_romano(año: int) -> str:
#     separar_numero = split_integer(año)
#     for i in separar_numero:
#         if 3 >= i >= 1:
#             print ("I" * i, end="")
#         # if i == 4:
#         #     return "IV"
#         # if i == 5:
#         #     return "V"
#         # if 6 >= i >= 8:
#         #     return "V" "I" * 3

# a_romano(1991)

# # assert a_romano(1) == "I"
# # assert a_romano(2) == "II"
# # assert a_romano(3) == "III"
# # assert a_romano(4) == "IV"
# # assert a_romano(5) == "V"
# # assert a_romano(6) == "VI"
# # assert a_romano(7) == "VII"
# # assert a_romano(8) == "VIII"
# # assert a_romano(9) == "IX"
# # assert a_romano(10) == "X"
# # assert a_romano(50) == "L"
# # assert a_romano(100) == "C"
# # assert a_romano(500) == "D"
# # assert a_romano(1000) == "M"




# blackblox hecho con diccionario, no aprendido hasta el momento.
def int_to_roman(num: int) -> str:
  """Converts an integer to a Roman numeral.
  Args:
    num: The integer to convert.
  Returns:
    The Roman numeral representation of the integer.
  """
  # Define the Roman numeral symbols.
  roman_numerals = {
      1000: 'M',
      900: 'CM',
      500: 'D',
      400: 'CD',
      100: 'C',
      90: 'XC',
      50: 'L',
      40: 'XL',
      10: 'X',
      9: 'IX',
      5: 'V',
      4: 'IV',
      1: 'I'
  }
  # Initialize the Roman numeral string.
  roman_numeral = ''
  # Iterate over the Roman numeral symbols in descending order.
  for value, symbol in roman_numerals.items():
    # While the number is greater than or equal to the current value,
    # add the current symbol to the Roman numeral string and subtract
    # the current value from the number.
    while num >= value:
      roman_numeral += symbol
      num -= value
  # Return the Roman numeral string.
  return roman_numeral        

print(int_to_roman(1991))

