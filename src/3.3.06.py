"""
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
"""

VOCALES = {'a', 'e', 'i', 'o', 'u'}


def main():
    consonantes = set(map(chr, range(97, 123))) - VOCALES
    print(consonantes)
    letras_comunes = consonantes | VOCALES
    print(letras_comunes)
    


if __name__ == "__main__":
    main()