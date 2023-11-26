"""
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""
import os

MATRIZ_A = ((1, 2), (3, 4), (5, 6))
MATRIZ_B = ((-1, 0), (0, 1), (1, 1))


def clear_console():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def crear_tuple_resultado(filas: int = 3, columnas: int = 2) -> tuple:
    tuple_matriz = tuple(crear_fila(columnas) for _ in range(filas))
    return tuple_matriz
    

def crear_fila(columnas: int) -> list:
    list_fila = list(0 for _ in range(columnas))
    return list_fila


def calcular_matriz_producto(tuple_matriz: tuple):
    for fila in range(3):
        for columna in range(2):
            tuple_matriz[fila][columna] = MATRIZ_A[fila][columna] * MATRIZ_B[fila][columna]


def mostrar_matriz(tuple_matriz: tuple):
    clear_console()
    print("La matriz resutado de la multiplicación de las matrices A y B es:\n")
    for fila in range(len(tuple_matriz)):
        print(tuple_matriz[fila])


def main():
    tuple_matriz = crear_tuple_resultado()
    calcular_matriz_producto(tuple_matriz)
    mostrar_matriz(tuple_matriz)


if __name__ == "__main__":
    main()