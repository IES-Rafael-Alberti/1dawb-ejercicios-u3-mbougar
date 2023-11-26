"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

def obtener_nombre_mes(diccionario_meses: dict, numero_mes: int) -> str:
    lista_nombres = list(diccionario_meses.keys())
    lista_numeros = list(diccionario_meses.values())
    return lista_nombres[lista_numeros.index(int(numero_mes))]


def main():
    diccionario_meses = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre":12}
    todo_ok = False

    while not todo_ok:
        try:
            fecha = input("Introduzca una fecha en formato dd/mm/aaaa: ").split("/")
            if 0 > int(fecha[0]) or 31 < int(fecha[0]) or int(fecha[2]) < 0:
                raise ValueError
            todo_ok = True
        except ValueError:
            fecha = input("Error, la fecha introducida no es valida. Introduzca una fecha en formato dd/mm/aaaa: ").split("/")
        except IndexError:
            fecha = input("Error, la fecha introducida no es valida. Introduzca una fecha en formato dd/mm/aaaa: ").split("/")

    try:
        print(f"{fecha[0]} de {obtener_nombre_mes(diccionario_meses, fecha[1])} de {fecha[2]}")
    except ValueError:
        print(f"El mes {fecha[1]} no existe...")



if __name__ == "__main__":
    main()