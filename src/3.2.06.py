""" 
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
import os
def clear_console():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def pedir_opcion():
    todo_ok = False
    while not todo_ok:
        try:
            opcion = input("Quiere introducir datos? s/n: ")
            if opcion.lower() not in {"s", "n"}:
                raise Exception
            todo_ok = True
        except Exception:
            print("Error, por favor introduzca s/n.")

    return opcion.lower()


def crear_diccionario_datos():
    diccionario_datos = {}
    todo_ok = False
    while not todo_ok:
        if pedir_opcion() == "s":
            nombre_dato = input("Introduce un tipo de dato: ")
            diccionario_datos[nombre_dato] = input("Introduce un dato: ")            
            mostrar_diccionario(diccionario_datos)
        else:
            todo_ok = True


def mostrar_diccionario(diccionario_datos: dict):
    datos_str = "El diccionario contiene: "
    for clave, dato in diccionario_datos.items():
        datos_str += "(" + clave + ": " + dato + ") "
    print(datos_str)


def main():
    crear_diccionario_datos()


if __name__ == "__main__":
    main()
