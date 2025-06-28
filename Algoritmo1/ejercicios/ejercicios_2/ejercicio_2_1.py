def inversion (capital_inicial, tasa_de_interés, años):
    formula = capital_inicial * (1 + (tasa_de_interés/100))** años
    return formula

#inversion (1000, 8, 10)