"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
VOCALES = ('a', 'e', 'i', 'o', 'u')


def contar_letra(letra: str, palabra: str) -> int:
    numero_veces = palabra.count(letra)
    return numero_veces
    


def main():
    palabra = input("Introduce una palabra: ")
    for letra in VOCALES:
        print(f"La letra {letra} aparece {contar_letra(letra, palabra.lower())} veces en la palabra {palabra.lower()}.")


if __name__ == "__main__":
    main()