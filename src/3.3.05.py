"""
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""


NUMEROS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def main():
    pares = set()
    multiplos_de_tres = set()
    for numero in NUMEROS:
        if numero % 2 == 0:
            pares.add(numero)
        if numero % 3 == 0:
            multiplos_de_tres.add(numero)
            
    print(pares)
    print(multiplos_de_tres)

    pares_y_multiplos_de_tres = pares & multiplos_de_tres
    print(pares_y_multiplos_de_tres)


if __name__ == "__main__":
    main()