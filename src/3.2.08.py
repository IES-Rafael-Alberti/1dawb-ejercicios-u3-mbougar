"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

def comprobar_palabra(palabra: list[str]) -> list:
    todo_ok = False
    while not todo_ok:
        try:
            if len(palabra) != 2:
                raise Exception
            else:
                palabra[0] = palabra[0].strip().lower()
                palabra[1] = palabra[1].strip().lower()
                todo_ok = True
        except Exception:
            print("Error. Por favor introduce solo 2 palabras separadas por 2 puntos.")

    return palabra


def traducir_frase(diccionario_traducciones: dict, frase: list[str]):
    frase_traducida = ""
        
    for i in range(0, len(frase)):
        palabra_traducida = diccionario_traducciones.get(frase[i].lower())

        if palabra_traducida:
            if i == 0:
                frase_traducida += palabra_traducida.capitalize()
            else:
                frase_traducida += palabra_traducida
        else:
            frase_traducida += frase[i]

        if i != len(frase) - 1:
            frase_traducida += " "

    print(frase_traducida)


def main():
    diccionario_traducciones = {}
    todo_ok = False
    print("Introduce una palabra en español y su traduccion serapada por dos puntos (Ej: Hola:Hello). Introduce x para dejar de introducir palabras:")
    while not todo_ok:
        palabra = input("Introduce las palabras: ")
        palabra = palabra.split(":")
        if palabra [0] == "x" or palabra [0] == "X":
            todo_ok = True
        else:
            palabra = comprobar_palabra(palabra)
            diccionario_traducciones[palabra[0]] = palabra[1]

    frase = input("Introduce una frase en español: ").split(" ")
    traducir_frase(diccionario_traducciones, frase)

    




if __name__ == "__main__":
    main()