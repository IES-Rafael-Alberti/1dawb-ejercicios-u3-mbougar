"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Terminar")


def agregar_factura(base_datos: dict):
    num_factura = input("Ingrese el número de factura: ")
    coste_factura = input("Ingrese el coste de la factura: ")

    base_datos[num_factura] = coste_factura

    print(f"Factura número {num_factura} añadida correctamente.")


def eliminar_factura(base_datos: dict):
    num_factura = input("Ingrese el número de la factura que desea pagar: ")

    if num_factura in base_datos:
        base_datos.pop(num_factura)
        print(f"Factura número {num_factura} pagada correctamente.")
    else:
        print(f"No se encontró una factura con número {num_factura} en la base de datos.")


def main():
    base_datos_facturas = {}

    terminar_programa = False

    while not terminar_programa:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            agregar_factura(base_datos_facturas)
        elif opcion == '2':
            eliminar_factura(base_datos_facturas)
        elif opcion == '3':
            print("Programa terminado.")
            terminar_programa = True
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")


if __name__ == "__main__":
        main()