def absoluto (n)-> int:
    "calcula el valor absoluto de un numero"
    if n >= 0:
        return n
    else:
        return -1 * n
    
def main():
    print(absoluto(-10))

main()