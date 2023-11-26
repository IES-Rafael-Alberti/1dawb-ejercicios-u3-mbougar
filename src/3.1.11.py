""" 
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""
def calcular_producto_escalar(vector_1: list, vector_2: list) -> int:
    producto_escalar = 0

    for numero in range(len(vector_1)):
        producto_escalar += vector_1[numero] * vector_2[numero]

    return producto_escalar


def mostrar_producto_escalar(producto_escalar: int, vector_1: list, vector_2: list):
    print(f"El producto escalar de los vectores {vector_1} y {vector_2} es {producto_escalar}.")


def main():
    v1 = [1, 2, 3]
    v2 = [-1, 0, 2]
    producto_escalar = calcular_producto_escalar(v1, v2)
    mostrar_producto_escalar(producto_escalar, v1, v2)


if __name__ == "__main__":
    main()