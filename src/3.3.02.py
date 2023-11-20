""" 
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
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


def crear_conjunto_nombres() -> set:
    conjunto_nombres = set()
    todo_ok = False
    
    while not todo_ok:
        nombre = input("Introduzca el nombre de un alumno: ")
        if nombre.lower() != "x":
            conjunto_nombres.add(nombre.capitalize())
        else:
            todo_ok = True
    
    return conjunto_nombres


def main():
    clear_console()
    print("Introduzca los nombres de los alumnos de primaria.")
    nombres_primaria = crear_conjunto_nombres()
    print("Introduzca los nombres de los alumnos de secundaria.")
    nombres_secundaria = crear_conjunto_nombres()
    print("Estos son todos los nombres que hay entre primaria y secundaria:")
    if len(nombres_primaria | nombres_secundaria) == 0:
        print("Ninguno")
    else:
        print(nombres_primaria | nombres_secundaria)
    print("Estos son todos los nombres que se repiten entre primaria y secundaria:")
    if len(nombres_primaria & nombres_secundaria) == 0:
        print("Ninguno")
    else:
        print(nombres_primaria & nombres_secundaria)
    print("Estos son todos los nombres de primaria que no se repiten en los de secundaria:")
    if len(nombres_primaria - nombres_secundaria) == 0:
        print("Ninguno")
    else:
        print(nombres_primaria - nombres_secundaria)
    print("Todos los nombres de primaria están incluidos en secundaria:")
    if len(nombres_primaria - nombres_secundaria) == 0:
        print("Si")
    else:
        print("No")


if __name__ == "__main__":
    main()