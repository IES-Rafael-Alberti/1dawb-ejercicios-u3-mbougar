"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
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
    

def pedir_numero(asignatura: str):
    loop = True
    while loop:
        try:
            numero = int(input(f"Introduce la nota de {asignatura}: "))
            if 0 <= numero <= 10:
                return numero
            else:
                raise ValueError
        except ValueError:
            print("Error, no has introducido un valor correcto.")
    

def clear_list(lista_asignaturas: list):
    contador = 0
    while contador < len(lista_asignaturas):
        if lista_asignaturas[contador][1] >= 5:
            lista_asignaturas.pop(contador)
        else:
            contador += 1
    return lista_asignaturas
    

def pedir_nota(lista_asignaturas: list) ->list:
    for i in range(len(lista_asignaturas)):
        nota = pedir_numero(lista_asignaturas[i][0])
        lista_asignaturas[i].append(nota)
    return lista_asignaturas


def mostrar_asignaturas(lista_asignaturas: list):
    print("El usuario tiene que repetir las siguientes asignaturas:\n")
    for asignatura in range(len(lista_asignaturas)):
        print(lista_asignaturas[asignatura][0], end="")
        if asignatura != len(lista_asignaturas) - 2 and asignatura != len(lista_asignaturas) - 1:
            print(", ", end="")
        elif asignatura != len(lista_asignaturas) - 1:
            print(" y ", end="")
        else:
            print(".")


def main():
    lista_asignaturas = [["Matematicas"], ["Física"], ["Química"], ["Historia"], ["Lengua"]]
    clear_console()
    lista_asignaturas = pedir_nota(lista_asignaturas)
    lista_asignaturas = clear_list(lista_asignaturas)
    mostrar_asignaturas(lista_asignaturas)


if __name__ == "__main__":
    main()












def main():
    value = 1


if __name__ == "__main__":
    main()