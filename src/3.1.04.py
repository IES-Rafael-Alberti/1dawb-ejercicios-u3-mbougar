import os

def borrar_consola():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def pedir_numero() -> list:
    """Pide 6 números entre 1 y 49 y los almacena en una lista

    Raises:
        ValueError: Error de valor por incorrecta introducción de número, puede darse 
        por introducir un número fuera de rango o por introducir caracteres no numericos

    Returns:
        list_num: lista que almacena los números introducidos.
    """
    list_num = []

    for i in range(1, 7):
        loop = True
        while loop:
            try:
                numero = int(input(f"({i})=> "))
                if list_num.count(numero) == 1:
                    raise ValueError
                if 0 < numero < 49:
                    list_num.append(numero)
                    loop = False
                else:
                    raise ValueError
            except ValueError:
                print("Error, vuelva a introducir el número.")

    return list_num


def pedir_reintegro() -> int:
    """Pide un número entre 1 y 9

    Raises:
        ValueError: Error de valor por incorrecta introducción de número, puede darse 
        por introducir un número fuera de rango o por introducir caracteres no numericos

    Returns:
        int: número introducido por el usuario
    """
    loop = True

    while loop:
        try:
            numero = int(input("(Reintegro)=> "))
            if 0 < numero < 10:
                loop = False
            else:
                raise ValueError
        except ValueError:
            print("Error, vuelva a introducir el número.")

    return numero


def imprimir_numeros(list_num: list) -> str:
    """Crea una cadena de caracteres con todos los número de la lotería y el reintegro

    Args:
        list_num (list): lista con los 6 números de la loteria y el reintegro

    Returns:
        str: cadena de caracteres con todos los número de la lotería y el reintegro
    """
    nums_str = "Los números de la loteria son: "

    for i in range(0, 6):
        nums_str += f"{list_num[i]:02d}"
        if i != 5:
            nums_str += ", "
        else:
            nums_str += ". "
    nums_str += "El reintegro es " + str(list_num[6]) + "."

    return nums_str


def main():
    borrar_consola()
    print("Introduzca los números de la lotería y el reintegro.")
    list_num = pedir_numero()
    list_num.sort()
    list_num.append(pedir_reintegro())
    print(imprimir_numeros(list_num))
    
    

if __name__ == "__main__":
    main()