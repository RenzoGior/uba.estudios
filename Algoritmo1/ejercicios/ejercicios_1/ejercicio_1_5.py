def factorial(n):
	multiplicacion_factoriales = n
	for fac in range(n-1, 0, -1):
		multiplicacion_factoriales *= fac
	return multiplicacion_factoriales

		

print(factorial(5))


	    

