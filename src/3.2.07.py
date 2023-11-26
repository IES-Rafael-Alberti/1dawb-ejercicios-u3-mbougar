"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

def pedir_coste(contador_numero: int) -> int:
    todo_ok = False
    while not todo_ok:
        try:
            coste = int(input(f"Precio Articulo {contador_numero}: "))
            todo_ok = True
        except ValueError:
            print("Error, pro favor introduce un número.")

    return coste


def main():
    contador_articulo = 1
    todo_ok = False
    diccionario_compra = {}
    print("Introduce el nombre y precio de los ariculos. Introduce x cuando queiras dejar de introducir articulos.")
    while not todo_ok:
        nombre_articulo = input(f"Articulo {contador_articulo}: ")
        if nombre_articulo != "x" and nombre_articulo != "X":
            precio_articulo = pedir_coste(contador_articulo)
            diccionario_compra[nombre_articulo] = precio_articulo
        else:
            todo_ok = True
            total = 0
            for articulo in diccionario_compra.items():
                print(f"{str(articulo[0]).capitalize()}: precio {articulo[1]}€")
                total += articulo[1]
            print(f"Total: {total}€")


if __name__ == "__main__":
    main()