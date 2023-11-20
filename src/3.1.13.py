""" 
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""
def crear_lista_num() -> list:
    todo_ok = False

    while not todo_ok:
        str_num = input("Introduzca una muestra de números, separados por comas: ")
        lista_num = str_num.split(",")
        if convertir_nums_int(lista_num) == None:
            print("Error, introduce solo números separados por comas.")
        else:
            todo_ok = True
    
    return lista_num


def convertir_nums_int(lista_num: list) -> list:
    for numero in range(len(lista_num)):
        try:
            lista_num[numero] = int(lista_num[numero])
        except ValueError:
            return None
    
    return lista_num


def calcular_media(lista_num: list):
    total = 0

    for numero in range(len(lista_num)):
        total += lista_num[numero]
    media = total / len(lista_num)

    return media


def calcular_varianza(media: int, lista_num: list) -> int:
    total = 0

    for numero in range(len(lista_num)):
        total += (lista_num[numero] - media) ** 2
    varianza = total / len(lista_num)

    return varianza


def calcular_desviacion_tipica(lista_num: list, media: int):
    varianza = calcular_varianza(media, lista_num)
    desviacion = varianza ** 0.5

    return desviacion


def main():
    lista_num = crear_lista_num()
    media = calcular_media(lista_num)
    desviacion = calcular_desviacion_tipica(lista_num, media)
    print(f"La media de la lista de números {lista_num} es {media} y su desviación típica es {desviacion}")


if __name__ == "__main__":
    main()