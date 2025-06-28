def mayor_producto(x, y, z, n): 
    """Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de ellos.(printea para verificar) debe haber una mejor manera
        pero con el conocimiento que tengo por ahora es lo mejor que se me ocurrio    
    """
    producto1 = x * y
    producto2 = x * z 
    producto3 = x * n 
    producto4 = y * z
    producto5 = y * n
    producto6 = z * n
    if producto1 > producto2 and producto1 > producto3 and producto1 > producto4 and producto1 > producto5 and producto1 > producto6:
        print( producto1)
    elif producto2 > producto1 and producto2 > producto3 and producto2 > producto4 and producto2 > producto5 and producto2 > producto6:
        print (producto2)
    elif producto3 > producto1 and producto3 > producto2 and producto3 > producto4 and producto3 > producto5 and producto3 > producto6:
        print (producto3)
    elif producto4 > producto1 and producto4 > producto2 and producto4 > producto3 and producto4 > producto5 and producto4 > producto6:
        print (producto4)
    elif producto5 > producto1 and producto5 > producto2 and producto5 > producto3 and producto5 > producto4 and producto3 > producto6:
        print (producto5)
    elif producto6 > producto1 and producto6 > producto2 and producto6 > producto3 and producto6 > producto4 and producto3 > producto5:
        print (producto6)
    


mayor_producto(1, 5, -2, -4)

# def mayor_producto(x, y, z, n):
#     conjuto_numero = [x, y, z, n]
#     conjuto_numero_alrevez = [n, y, z, n]
#     for j in conjuto_numero:
#         if j != conjuto_numero_alrevez:
#             producto = j * conjuto_numero_alrevez
            
        
        


# mayor_producto(1, 5, -2, -4)