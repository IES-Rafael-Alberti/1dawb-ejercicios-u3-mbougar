""" 
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
import os


def clear_console():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")
    

def clear_list(list_char: list):
    length = len(list_char) -1
    contador = 0
    while contador < length:
        if contador % 3 == 0:
            list_char.pop(contador)
            length -= 1
               
        contador += 1
    return list_char
    

def main():
    clear_console()
    list_characters = list(map(chr, range(97, 123)))
    lista = clear_list(list_characters)
    print(lista)



if __name__ == "__main__":
    main()