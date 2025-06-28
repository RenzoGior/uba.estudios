def factorial(n) -> int:
	multiplicacion_factoriales = n
	for fac in range(n-1, 0, -1):
		multiplicacion_factoriales *= fac
	return  int(multiplicacion_factoriales)

		

factorial(0)


	    


