""" 
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def main():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    try:
        divisa_pregunta = input("Introduzca el nombre de una divisa: ")

        print(f"El simbolo de su divisa es: {divisas[divisa_pregunta.title()]}")
    except Exception:
        print("Esa divisa no esta en nuestro diccionario.")


if __name__ == "__main__":
    main()