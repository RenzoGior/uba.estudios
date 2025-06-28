

def imprimir_fichas_domino(n=6):
    ''' Imprime las fichas de un juego de dominó con números entre el 0 y n. '''
    for i in range(n+1):
        for j in range(i,n+1):
            print(i, "/", j, end=" | ")
        print()
        
def main():
    imprimir_fichas_domino(8)

main()