""" 
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

def mostrar_menor_y_mayor(lista_num: list):
    lista_num.sort
    print(f"El menor número de la lista es {lista_num[-1]} y el mayor es {lista_num[0]}.")


def main():
    lista_num = [50, 75, 46, 22, 80, 65, 8]
    mostrar_menor_y_mayor(lista_num)


if __name__ == "__main__":
    main()