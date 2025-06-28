

def imprimir_fichas_domino():
    ''' Imprime las fichas del dominó. '''
    for i in range(7):
        for j in range(i,7):
            print(i, "/" , j, end=" | ")
        print()
        
def main():
    imprimir_fichas_domino()

main()