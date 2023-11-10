def algoritmo_Burbuja(list:list) -> list:
    """Ordena de menor a mayor todos los números de una lista.

    Args:
        list (list): una lista con los números que se van a ordenar de menor a mayor.
    
    Returns: 
        newList (list): lista con los números ordenados de menor a mayor.
    """
    for i in range(0, len(list) - 1):
        for j in range(0, len(list)-1 -i):
            if list[j] > list[j+1]:
                holder = list[j]
                list[j] = list[j+1]
                list[j+1] = holder
    newList = list
    return newList


def pedir_Numero() -> int:
    """Pide un número entero al usuario y comprueba si el valor introducido es un número entero entre 0 y 10.
    
    Returns:
        numero: valor introducido si es entero entre 0 y 10.
    """
    loop = False
    while not loop:
        try:
            numero = int(input("Introduzca un número entero entre 0 y 99: "))
            if numero >= 0 and numero <= 99:
                loop =  True
            else:
                raise ValueError
        except ValueError:
            print("La entrada no es correcta.")
    return numero


def main():
    listaNumeros = []
    for i in range(0,5):
        numero = pedir_Numero()
        listaNumeros.append(numero)
    newList = algoritmo_Burbuja(listaNumeros)
    print("Los números ganadores de la primitiva son: ", end="")
    for i in range(0, len(newList)):
        if newList[i] < 10:
            print("0" + str(newList[i]), end="")
        else:
            print(newList[i], end="")
        if i != len(newList) - 1:
            print(" ", end="")
    

if __name__ == "__main__":
    main()