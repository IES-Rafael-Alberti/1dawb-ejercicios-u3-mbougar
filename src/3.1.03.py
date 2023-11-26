def introducirValor() -> str:
    """Pide un valor de texto.

    Returns:
        valor: string introducida por el usuario.
    """
    loop = False
    while not loop:
        print(f"Introduzca una asignatura: ", end="")
        try:
            valor = input()
        except Exception:
            print(f"Error introduciendo la asignatura, vuelva a intentarlo: ", end="")
        else:
            loop = True
    return valor


def introducirOpcion() -> str:
    """Pide un valor opcion.

    Returns:
        opcion: string introducida por el usuario.
    """
    loop = False
    while not loop:
        try:
            opcion = input()
            if opcion == "s" or opcion == "n":
                return opcion
            else:
                raise Exception
        except Exception:
            print("Error introduciendo la opcion, vuelva a intentarlo: ", end="")


def pedir_Nota() -> int:
    """Pide un número entero al usuario y comprueba si el valor introducido es un número entero entre 0 y 10.
    
    Returns:
        numero: valor introducido si es entero entre 0 y 10.
    """
    loop = False
    while not loop:
        try:
            numero = int(input("Introduzca un número entero: "))
            if numero >= 0 and numero <= 10:
                loop =  True
            else:
                raise ValueError
        except ValueError:
            print("La entrada no es correcta.")
    return numero


def main():
    listaAsignaturas = []
    listaNotas = []
    loop = False
    while not loop:
        print("¿Quiere introducir una asignatura? s/n: ", end="")
        opcion = introducirOpcion()
        if opcion == "s": 
            asignatura = introducirValor()
            listaAsignaturas.append(asignatura)
            nota = pedir_Nota()
            listaNotas.append(nota)
        else:
            loop = True
    for i in range(0, len(listaAsignaturas)):
        print(f"En {listaAsignaturas[i]} has sacado {listaNotas[i]}")


if __name__ == "__main__":
    main()