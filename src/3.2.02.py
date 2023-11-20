""" 
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
def crear_diccionario_datos() -> dict:
    diccionario_datos = {"nombre": None, "edad": None, "direccion": None, "telefono": None}
    for dato in diccionario_datos.keys():
        diccionario_datos[dato] = input(f"Introduzca su {dato}: ")

    return diccionario_datos


def main():
    diccionario_datos = crear_diccionario_datos()
    print(f"{diccionario_datos["nombre"]} tiene {diccionario_datos["edad"]} años, vive en {diccionario_datos["direccion"]} y su número de teléfono es {diccionario_datos["telefono"]}.")


if __name__ == "__main__":
    main()
